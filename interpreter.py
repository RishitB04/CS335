
from ChironAST import ChironAST
from ChironHooks import Chironhooks
import turtle

Release="Chiron v5.3"

# -- Lazy Evaluation Support --

class Thunk:
    """A deferred computation. Stores the expression and the scope snapshot.
    Evaluated only when forceValue() is called. Result is cached (memoized)."""
    def __init__(self, expr, scope_snapshot):
        self.expr = expr
        self.scope_snapshot = scope_snapshot
        self.evaluated = False
        self.cached_value = None
    
    def __str__(self):
        if self.evaluated:
            return f"Thunk(cached={self.cached_value})"
        return f"Thunk(unevaluated={self.expr})"

class InfiniteRange:
    """Represents a lazy infinite range [start..]. Elements are generated on demand."""
    def __init__(self, start):
        self.start = start
        self.generated = []
    
    def get(self, index):
        while len(self.generated) <= index:
            self.generated.append(self.start + len(self.generated))
        return self.generated[index]
    
    def take_n(self, n):
        return [self.get(i) for i in range(n)]
    
    def __str__(self):
        if self.generated:
            return f"[{self.start}.. (generated {len(self.generated)} elements)]"
        return f"[{self.start}..]"

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

    def handleAssignment(self, stmt):
        raise NotImplementedError('Assignments are not handled!')

    def handleCondition(self, stmt, tgt):
        raise NotImplementedError('Conditions are not handled!')

    def handleMove(self, stmt):
        raise NotImplementedError('Moves are not handled!')

    def handlePen(self, stmt):
        raise NotImplementedError('Pens are not handled!')

    def handleGotoCommand(self, stmt):
        raise NotImplementedError('Gotos are not handled!')

    def handleNoOpCommand(self,  tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def handlePauseCommand(self):
        raise NotImplementedError('No-Ops are not handled!')

    def sanityCheck(self, irInstr):
        stmt, tgt = irInstr
        # if not a condition command, rel. jump can't be anything but 1
        if not (isinstance(stmt, ChironAST.ConditionCommand) or isinstance(stmt, ChironAST.FunctionDefCommand) or isinstance(stmt, ChironAST.NoOpCommand)):
            if tgt != 1:
                raise ValueError("Improper relative jump ", str(stmt), tgt)
    
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
        self.lambda_counter = 0;
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
            case ChironAST.NoOpCommand(): return self.handleNoOpCommand(tgt)
            case ChironAST.PauseCommand(): return self.handlePauseCommand()
            case ChironAST.FunctionCallCommand(): return self.handleFunctionCallCommand(stmt)
            case ChironAST.FunctionDefCommand(): return self.handleFunctionDefCommand(stmt,tgt)
            case ChironAST.ReturnCommand(): return tgt
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
            case ChironAST.NameVal(): return expr.val
            case ChironAST.UMinus():
                val = self.forceValue(self.expressionEvaluation(expr.expr))
                if isinstance(val, str):
                    raise Exception(f"Unary minus cannot be applied to str value: {val}.")
                return -val
            case ChironAST.Sum():
                lval = self.forceValue(self.expressionEvaluation(expr.lexpr))
                rval = self.forceValue(self.expressionEvaluation(expr.rexpr))
                if isinstance(lval, str) or isinstance(rval, str):
                    raise Exception(f"Sum operator cannot be applied to str values: {lval}, {rval}.")
                return lval + rval
            case ChironAST.Diff():
                lval = self.forceValue(self.expressionEvaluation(expr.lexpr))
                rval = self.forceValue(self.expressionEvaluation(expr.rexpr))
                if isinstance(lval, str) or isinstance(rval, str):
                    raise Exception(f"Subtraction operator cannot be applied to str values: {lval}, {rval}.")
                return lval - rval
            case ChironAST.Mult():
                lval = self.forceValue(self.expressionEvaluation(expr.lexpr))
                rval = self.forceValue(self.expressionEvaluation(expr.rexpr))
                if isinstance(lval, str) or isinstance(rval, str):
                    raise Exception(f"Multiplication operator cannot be applied to str values: {lval}, {rval}.")
                return lval * rval
            case ChironAST.Div():
                lval = self.forceValue(self.expressionEvaluation(expr.lexpr))
                rval = self.forceValue(self.expressionEvaluation(expr.rexpr))
                if isinstance(lval, str) or isinstance(rval, str):
                    raise Exception(f"Division operator cannot be applied to str values: {lval}, {rval}.")
                return lval / rval
            case ChironAST.FunctionExpr(): return self.executeFunction(expr.callname, expr.args)
            case ChironAST.LambdaExpr(): return self.handleLambdaExpr(expr)
            case ChironAST.LazyExpr(): return self.handleLazyExpr(expr)
            case ChironAST.RangeExpr(): return self.handleRangeExpr(expr)
            case ChironAST.MatchExpr(): return self.handleMatchExpr(expr)
            case _ : raise Exception(f"Unknown expression: {type(expr)}, {expr}.")

    def conditionEvaluation(self, cond):
        match cond:
            case ChironAST.NOT(): return not self.conditionEvaluation(cond.expr)
            case ChironAST.PenStatus(): return self.trtl.isdown()
            case ChironAST.BoolTrue(): return True
            case ChironAST.BoolFalse(): return False
            case ChironAST.AND(): return self.conditionEvaluation(cond.lexpr) and self.conditionEvaluation(cond.rexpr)
            case ChironAST.OR(): return self.conditionEvaluation(cond.lexpr) or self.conditionEvaluation(cond.rexpr)
        lval = self.forceValue(self.expressionEvaluation(cond.lexpr))
        rval = self.forceValue(self.expressionEvaluation(cond.rexpr))
        match cond:
            case ChironAST.LT(): return lval < rval
            case ChironAST.LTE(): return lval <= rval
            case ChironAST.GT(): return lval > rval
            case ChironAST.GTE(): return lval >= rval
            case ChironAST.EQ(): return lval == rval
            case ChironAST.NEQ(): return lval != rval
            case _ : raise Exception(f"Unknown condition: {type(cond)}, {cond}.")

    def executeFunction(self, callname, args):
        if len(self.call_stack) > 100:
            raise Exception("Maximum call stack depth exceeded.")
        
        if isinstance(callname, ChironAST.Var):
            function_name = self.variableCheck(callname.varname)
        elif isinstance(callname, ChironAST.NameVal):
            function_name = callname.val
        else: raise Exception(f"Invalid function name: {callname}.")

        if function_name not in self.function_def:
            # Check built-in functions first
            builtin_result = self.tryBuiltinFunction(function_name, args)
            if builtin_result is not None:
                return builtin_result
            raise Exception(f"Undefined function: {function_name}.")
        
        func_entry = self.function_def[function_name]
        
        # Check if this is a lambda function
        if isinstance(func_entry, dict) and func_entry.get('type') == 'lambda':
            return self.executeLambda(func_entry, args)
        
        arguments , start_pc = func_entry
        if len(arguments) != len(args):
            raise Exception(f"Argument count mismatch for function {function_name}.")
        
        eval_args = [self.expressionEvaluation(arg) for arg in args]

        local_scope = dict(zip(arguments, eval_args))
        self.stack.append(local_scope)
        self.call_stack.append(self.pc)

        self.pc = start_pc
        ret_value = None

        while self.pc < len(self.ir):
            curr_stmt, curr_tgt = self.ir[self.pc]
            if isinstance(curr_stmt, ChironAST.ReturnCommand):
                ret_value = self.expressionEvaluation(curr_stmt.rexpr) if curr_stmt.rexpr else None
                break
            ntgt = self.executeInstruction(curr_stmt, curr_tgt)
            self.pc += ntgt
        
        self.stack.pop()
        self.pc = self.call_stack.pop()
        return ret_value

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
        dist = self.forceValue(self.expressionEvaluation(stmt.expr))
        if stmt.direction == "forward": self.trtl.forward(dist)
        elif stmt.direction == "backward": self.trtl.backward(dist)
        elif stmt.direction == "left": self.trtl.left(dist)
        elif stmt.direction == "right": self.trtl.right(dist)
        else: raise Exception(f"Unknown move direction: {stmt.direction}.")
        return 1

    def handleNoOpCommand(self, tgt):
        print("  No-Op Command")
        return tgt

    def handlePen(self, stmt):
        print("  PenCommand")
        if stmt.status == "penup": self.trtl.penup()
        elif stmt.status == "pendown": self.trtl.pendown()
        else: raise Exception(f"Unknown pen status: {stmt.status}.")
        return 1

    def handleGotoCommand(self, stmt):
        print(" GotoCommand")
        xcor = self.forceValue(self.expressionEvaluation(stmt.xcor))
        ycor = self.forceValue(self.expressionEvaluation(stmt.ycor))
        self.trtl.goto(xcor, ycor)
        return 1
    
    def handlePauseCommand(self):
        print(" PauseCommand")
        return 1
    
    def handleFunctionCallCommand(self,stmt):
        print(" FunctionCallCommand")
        self.executeFunction(stmt.callname, stmt.args)
        return 1
    
    def handleFunctionDefCommand(self, stmt, tgt):
        print(" FunctionDefCommand")
        self.function_def[stmt.funcname] = (stmt.params, self.pc + 1)
        return tgt

    def handleLambdaExpr(self, expr):
        self.lambda_counter += 1
        lambda_name = f"__lambda_{self.lambda_counter}"
        
        captured_scope = {}
        for scope in self.stack:
            captured_scope.update(scope)
        
        self.function_def[lambda_name] = {
            'type': 'lambda',
            'params': expr.params,
            'body': expr.body_expr,
            'closure': captured_scope
        }
        
        return lambda_name
    
    def executeLambda(self, lambda_def, args):
        params = lambda_def['params']
        body = lambda_def['body']
        closure = lambda_def['closure']
        
        if len(params) != len(args):
            raise Exception(f"Lambda argument count mismatch: expected {len(params)}, got {len(args)}.")
        
        eval_args = [self.expressionEvaluation(arg) for arg in args]
        
        local_scope = dict(closure)
        local_scope.update(dict(zip(params, eval_args)))
        
        self.stack.append(local_scope)
        ret_value = self.expressionEvaluation(body)
        self.stack.pop()
        
        return ret_value

    # -- Lazy Evaluation Methods --

    def forceValue(self, val):
        """Force a thunk to evaluate. If already a concrete value, return as-is.
        Called transparently whenever a concrete value is needed."""
        if isinstance(val, Thunk):
            if not val.evaluated:
                old_stack = self.stack
                self.stack = val.scope_snapshot + [{}]
                val.cached_value = self.forceValue(self.expressionEvaluation(val.expr))
                self.stack = old_stack
                val.evaluated = True
            return val.cached_value
        return val
    
    def handleLazyExpr(self, expr):
        """Create a thunk — a deferred computation that captures the current scope."""
        scope_snapshot = [dict(scope) for scope in self.stack]
        return Thunk(expr.expr, scope_snapshot)
    
    def handleRangeExpr(self, expr):
        """Handle range expressions: [1..10] for finite, [1..] for infinite."""
        start = int(self.forceValue(self.expressionEvaluation(expr.start_expr)))
        if expr.end_expr is not None:
            end = int(self.forceValue(self.expressionEvaluation(expr.end_expr)))
            return list(range(start, end + 1))
        else:
            return InfiniteRange(start)
    
    # -- Pattern Matching --

    def handleMatchExpr(self, expr):
        """
        Pattern matching: match :x with | 0 => expr1 | :y => expr2 | _ => expr3
        Evaluates subject, then tries each case in order.
        - Numeric pattern (Num): exact value match
        - Variable pattern (Var): binds the value to the variable, always matches
        - Wildcard pattern (_): always matches (default case)
        """
        subject_val = self.forceValue(self.expressionEvaluation(expr.subject))
        
        for pattern, result_expr in expr.cases:
            if isinstance(pattern, ChironAST.NameVal) and pattern.val == "_":
                # Wildcard: always matches
                return self.expressionEvaluation(result_expr)
            elif isinstance(pattern, ChironAST.Num):
                # Numeric literal: exact value match
                if subject_val == pattern.val:
                    return self.expressionEvaluation(result_expr)
            elif isinstance(pattern, ChironAST.Var):
                # Variable pattern: bind the matched value and evaluate
                self.stack.append({pattern.varname: subject_val})
                result = self.expressionEvaluation(result_expr)
                self.stack.pop()
                return result
        
        raise Exception(f"Non-exhaustive pattern match for value: {subject_val}")
    
    def callFunctionByName(self, func_name, arg_values):
        """Helper: call a function by name with already-evaluated argument values."""
        temp_args = []
        temp_scope = {}
        for i, val in enumerate(arg_values):
            temp_var = f":__arg_{i}"
            temp_scope[temp_var] = val
            temp_args.append(ChironAST.Var(temp_var))
        
        self.stack.append(temp_scope)
        result = self.executeFunction(ChironAST.NameVal(func_name), temp_args)
        self.stack.pop()
        return result

    def tryBuiltinFunction(self, function_name, args):
        """Handle built-in functions. Returns None if not a built-in."""
        
        if function_name == "force":
            if len(args) != 1:
                raise Exception("force requires exactly 1 argument")
            val = self.expressionEvaluation(args[0])
            return self.forceValue(val)
        
        elif function_name == "take":
            if len(args) != 2:
                raise Exception("take requires exactly 2 arguments: take(n, list)")
            n = int(self.forceValue(self.expressionEvaluation(args[0])))
            lst = self.expressionEvaluation(args[1])
            if isinstance(lst, InfiniteRange):
                return lst.take_n(n)
            if isinstance(lst, list):
                return lst[:n]
            raise Exception(f"take second argument must be a list or range, got: {type(lst)}")
        
        elif function_name == "head":
            if len(args) != 1:
                raise Exception("head requires exactly 1 argument")
            lst = self.expressionEvaluation(args[0])
            if isinstance(lst, InfiniteRange):
                return lst.get(0)
            if not isinstance(lst, list) or len(lst) == 0:
                raise Exception("head called on empty or non-list")
            return lst[0]
        
        elif function_name == "tail":
            if len(args) != 1:
                raise Exception("tail requires exactly 1 argument")
            lst = self.expressionEvaluation(args[0])
            if isinstance(lst, InfiniteRange):
                return InfiniteRange(lst.start + 1)
            if not isinstance(lst, list) or len(lst) == 0:
                raise Exception("tail called on empty or non-list")
            return lst[1:]
        
        elif function_name == "length":
            if len(args) != 1:
                raise Exception("length requires exactly 1 argument")
            lst = self.expressionEvaluation(args[0])
            if isinstance(lst, InfiniteRange):
                raise Exception("Cannot take length of infinite range")
            if not isinstance(lst, list):
                raise Exception("length called on non-list")
            return len(lst)
        
        elif function_name == "nth":
            if len(args) != 2:
                raise Exception("nth requires exactly 2 arguments: nth(list, index)")
            lst = self.expressionEvaluation(args[0])
            idx = int(self.forceValue(self.expressionEvaluation(args[1])))
            if isinstance(lst, InfiniteRange):
                return lst.get(idx)
            if not isinstance(lst, list):
                raise Exception("nth first argument must be a list")
            if idx < 0 or idx >= len(lst):
                raise Exception(f"nth index {idx} out of bounds for list of length {len(lst)}")
            return lst[idx]
        
        elif function_name == "cons":
            if len(args) != 2:
                raise Exception("cons requires exactly 2 arguments: cons(elem, list)")
            elem = self.expressionEvaluation(args[0])
            lst = self.expressionEvaluation(args[1])
            if not isinstance(lst, list):
                raise Exception("cons second argument must be a list")
            return [elem] + lst
        
        elif function_name == "zipWith":
            if len(args) != 3:
                raise Exception("zipWith requires exactly 3 arguments: zipWith(func, list1, list2)")
            func_name_val = self.expressionEvaluation(args[0])
            lst1 = self.expressionEvaluation(args[1])
            lst2 = self.expressionEvaluation(args[2])
            if isinstance(lst1, InfiniteRange) and isinstance(lst2, InfiniteRange):
                raise Exception("zipWith cannot operate on two infinite ranges. Use take() on at least one.")
            if isinstance(lst1, InfiniteRange):
                lst1 = lst1.take_n(len(lst2))
            if isinstance(lst2, InfiniteRange):
                lst2 = lst2.take_n(len(lst1))
            if not isinstance(lst1, list) or not isinstance(lst2, list):
                raise Exception("zipWith arguments must be lists")
            min_len = min(len(lst1), len(lst2))
            return [self.callFunctionByName(func_name_val, [lst1[i], lst2[i]]) for i in range(min_len)]
        
        elif function_name == "map":
            if len(args) != 2:
                raise Exception("map requires exactly 2 arguments: map(func, list)")
            fn = self.expressionEvaluation(args[0])
            lst = self.expressionEvaluation(args[1])
            if not isinstance(lst, list):
                raise Exception(f"map second argument must be a list, got: {type(lst)}")
            return [self.callFunctionByName(fn, [elem]) for elem in lst]
        
        elif function_name == "filter":
            if len(args) != 2:
                raise Exception("filter requires exactly 2 arguments: filter(func, list)")
            fn = self.expressionEvaluation(args[0])
            lst = self.expressionEvaluation(args[1])
            if not isinstance(lst, list):
                raise Exception(f"filter second argument must be a list, got: {type(lst)}")
            return [elem for elem in lst if self.callFunctionByName(fn, [elem])]
        
        elif function_name == "fold":
            if len(args) != 3:
                raise Exception("fold requires exactly 3 arguments: fold(func, initial, list)")
            fn = self.expressionEvaluation(args[0])
            accumulator = self.expressionEvaluation(args[1])
            lst = self.expressionEvaluation(args[2])
            if not isinstance(lst, list):
                raise Exception(f"fold third argument must be a list, got: {type(lst)}")
            for elem in lst:
                accumulator = self.callFunctionByName(fn, [accumulator, elem])
            return accumulator
        
        return None
