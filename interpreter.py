
from ChironAST import ChironAST
from ChironHooks import Chironhooks
import turtle

Release="Chiron v5.3"

class Interpreter:
    # Turtle program should not contain variable with names "ir", "pc", "t_screen"
    ir = None
    pc = None
    t_screen = None
    trtl = None

    def __init__(self, irHandler, params):
        self.ir = irHandler.ir
        self.cfg = irHandler.cfg
        self.pc = 0
        self.t_screen = turtle.getscreen()
        self.trtl = turtle.Turtle()
        self.trtl.shape("turtle")
        self.trtl.color("blue", "yellow")
        self.trtl.fillcolor("green")
        self.trtl.begin_fill()
        self.trtl.pensize(4)
        self.trtl.speed(1) # TODO: Make it user friendly

        if params is not None:
            self.args = params
        else:
            self.args = None

        turtle.title(Release)
        turtle.bgcolor("white")
        turtle.hideturtle()

    def handleAssignment(self, stmt,tgt):
        raise NotImplementedError('Assignments are not handled!')

    def handleCondition(self, stmt, tgt):
        raise NotImplementedError('Conditions are not handled!')

    def handleMove(self, stmt, tgt):
        raise NotImplementedError('Moves are not handled!')

    def handlePen(self, stmt, tgt):
        raise NotImplementedError('Pens are not handled!')

    def handleGotoCommand(self, stmt, tgt):
        raise NotImplementedError('Gotos are not handled!')

    def handleNoOpCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def handlePauseCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def sanityCheck(self, irInstr):
        stmt, tgt = irInstr
        # if not a condition command, rel. jump can't be anything but 1
        if not isinstance(stmt, ChironAST.ConditionCommand):
            if tgt != 1:
                raise ValueError("Improper relative jump for non-conditional instruction", str(stmt), tgt)
    
    def interpret(self):
        pass

    def initProgramContext(self, params):
        pass


# TODO: move to a different file
class ConcreteInterpreter(Interpreter):
    # Ref: https://realpython.com/beginners-guide-python-turtle
    cond_eval = None # used as a temporary variable within the embedded program interpreter
    prg = None

    def __init__(self, irHandler, params):
        super().__init__(irHandler, params)
        self.stack=[{}];
        self.call_stack=[];
        self.function_def={};
        # Hooks Object:
        if self.args is not None and self.args.hooks:
            self.chironhook = Chironhooks.ConcreteChironHooks()
        self.pc = 0

    def executeInstruction(self, stmt, tgt):
        match stmt:
            case ChironAST.AssignmentCommand(): return self.handleAssignment(stmt)
            case ChironAST.ConditionCommand(): return self.handleCondition(stmt, tgt)
            case ChironAST.MoveCommand(): return self.handleMove(stmt)
            case ChironAST.PenCommand(): return self.handlePen(stmt)
            case ChironAST.GotoCommand(): return self.handleGotoCommand(stmt)
            case ChironAST.NoOpCommand(): return self.handleNoOpCommand()
            case ChironAST.PauseCommand(): return self.handlePauseCommand()
            case _ : raise Exception(f"Unknown instruction: {type(stmt)}, {stmt}.")

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print(stmt, stmt.__class__.__name__, tgt)

        self.sanityCheck(self.ir[self.pc])

        ntgt = self.executeInstruction(stmt, tgt)

        # TODO: handle statement
        self.pc += ntgt

        if self.pc >= len(self.ir):
            # This is the ending of the interpreter.
            self.trtl.write("End, Press ESC", font=("Arial", 15, "bold"))
            if self.args is not None and self.args.hooks:
                self.chironhook.ChironEndHook(self)
            return True
        else:
            return False
    
    def initProgramContext(self, params):
        # This is the starting of the interpreter at setup stage.
        if self.args is not None and self.args.hooks:
            self.chironhook.ChironStartHook(self)
        self.trtl.write("Start", font=("Arial", 15, "bold"))
        for key,val in params.items():
            self.stack[0][key]=val
    
    def variableCheck(self, varname):
        for scope in reversed(self.stack):
            if varname in scope:
                return scope[varname]
        raise Exception(varname + " not defined")
    
    def expressionEvaluation(self, expr):
        match expr:
            case ChironAST.Num(): return expr.val
            case ChironAST.Var(): return self.variableCheck(expr.varname)
            case ChironAST.UMinus(): return -self.expressionEvaluation(expr.expr)
            case ChironAST.Sum(): return self.expressionEvaluation(expr.lexpr) + self.expressionEvaluation(expr.rexpr)
            case ChironAST.Diff(): return self.expressionEvaluation(expr.lexpr) - self.expressionEvaluation(expr.rexpr)
            case ChironAST.Mult(): return self.expressionEvaluation(expr.lexpr) * self.expressionEvaluation(expr.rexpr)
            case ChironAST.Div(): return self.expressionEvaluation(expr.lexpr) / self.expressionEvaluation(expr.rexpr)
            case _ : raise Exception(f"Unknown expression: {type(expr)}, {expr}.")

    def conditionEvaluation(self, cond):
        match cond:
            case ChironAST.LT(): return self.expressionEvaluation(cond.lexpr) < self.expressionEvaluation(cond.rexpr)
            case ChironAST.LTE(): return self.expressionEvaluation(cond.lexpr) <= self.expressionEvaluation(cond.rexpr)
            case ChironAST.GT(): return self.expressionEvaluation(cond.lexpr) > self.expressionEvaluation(cond.rexpr)
            case ChironAST.GTE(): return self.expressionEvaluation(cond.lexpr) >= self.expressionEvaluation(cond.rexpr)
            case ChironAST.AND(): return self.conditionEvaluation(cond.lexpr) and self.conditionEvaluation(cond.rexpr)
            case ChironAST.OR(): return self.conditionEvaluation(cond.lexpr) or self.conditionEvaluation(cond.rexpr)
            case ChironAST.EQ(): return self.expressionEvaluation(cond.lexpr) == self.expressionEvaluation(cond.rexpr)
            case ChironAST.NEQ(): return self.expressionEvaluation(cond.lexpr) != self.expressionEvaluation(cond.rexpr)
            case ChironAST.NOT(): return not self.conditionEvaluation(cond.expr)
            case ChironAST.PenStatus(): return self.trtl.isdown()
            case ChironAST.BoolTrue(): return True
            case ChironAST.BoolFalse(): return False
            case _ : raise Exception(f"Unknown condition: {type(cond)}, {cond}.")

    def handleAssignment(self, stmt):
        print("  Assignment Statement")
        self.stack[-1][stmt.lvar.varname] = self.expressionEvaluation(stmt.rexpr)
        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        cond_val= self.conditionEvaluation(stmt.cond)
        return 1 if cond_val else tgt

    def handleMove(self, stmt):
        print("  MoveCommand")
        dist = self.expressionEvaluation(stmt.expr)
        if stmt.direction == "forward": self.trtl.forward(dist)
        elif stmt.direction == "backward": self.trtl.backward(dist)
        elif stmt.direction == "left": self.trtl.left(dist)
        elif stmt.direction == "right": self.trtl.right(dist)
        else: raise Exception(f"Unknown move direction: {stmt.direction}.")
        return 1

    def handleNoOpCommand(self):
        print("  No-Op Command")
        return 1

    def handlePen(self, stmt):
        print("  PenCommand")
        if stmt.status == "penup": self.trtl.penup()
        elif stmt.status == "pendown": self.trtl.pendown()
        else: raise Exception(f"Unknown pen status: {stmt.status}.")
        return 1

    def handleGotoCommand(self, stmt):
        print(" GotoCommand")
        xcor = self.expressionEvaluation(stmt.xcor)
        ycor = self.expressionEvaluation(stmt.ycor)
        self.trtl.goto(xcor, ycor)
        return 1
    
    def handlePauseCommand(self):
        print(" PauseCommand")
        return 1
