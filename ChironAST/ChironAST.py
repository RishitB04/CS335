#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Abstract syntax tree for ChironLang

class AST(object):
    pass


# --Instruction Classes-----------------------------------------------

class Instruction(AST):
    pass


class AssignmentCommand(Instruction):
    def __init__(self, leftvars, rexpr):
        self.lvars = leftvars
        self.rexpr = rexpr

    def __str__(self):
        return ", ".join(str(v) for v in self.lvars) + " = " + self.rexpr.__str__()


class ConditionCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return self.cond.__str__()

# Not Implemented Yet.
class AssertCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return self.cond.__str__()

class MoveCommand(Instruction):
    def __init__(self, motion, expr):
        self.direction = motion
        self.expr = expr

    def __str__(self):
        return self.direction + " " + self.expr.__str__()


class PenCommand(Instruction):
    def __init__(self, penstat):
        self.status = penstat

    def __str__(self):
        return self.status

class GotoCommand(Instruction):
    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y

    def __str__(self):
        return "goto " + str(self.xcor) + " " + str(self.ycor)

class NoOpCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "NOP"

class PauseCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "pause"

class Expression(AST):
    pass


# --Arithmetic Expressions--------------------------------------------

class ArithExpr(Expression):
    pass


class BinArithOp(ArithExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + " " + self.symbol + " " + self.rexpr.__str__() + ")"


class UnaryArithOp(ArithExpr):
    def __init__(self, expr1, opsymbol):
        self.expr = expr1
        self.symbol = opsymbol

    def __str__(self):
        return self.symbol + self.expr.__str__()


class UMinus(UnaryArithOp):
    def __init__(self, lexpr):
        super().__init__(lexpr, "-")


class Sum(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "+")


class Diff(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "-")


class Mult(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "*")

class Div(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "/")


# --Boolean Expressions-----------------------------------------------

class BoolExpr(Expression):
    pass


class BinCondOp(BoolExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + ' ' + self.symbol + ' ' + self.rexpr.__str__() + ")"


class AND(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "and")

class OR(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "or")


class LT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<")


class GT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">")


class LTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<=")


class GTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">=")


class EQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "==")


class NEQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "!=")


class NOT(BoolExpr):
    def __init__(self, uexpr):
        self.expr = uexpr
        self.symbol = "not"

    def __str__(self):
        return self.symbol + self.expr.__str__()


class PenStatus(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "pendown?"


class BoolTrue(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "True"


class BoolFalse(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "False"


class Value(Expression):
    pass


class Num(Value):
    def __init__(self, v):
        self.val = int(v)

    def __str__(self):
        return str(self.val)


class Var(Value):
    def __init__(self, vname):
        self.varname = vname

    def __str__(self):
        return self.varname

# Work Done

class NameVal(Value):
    def __init__(self, fname):
        self.val = fname
    
    def __str__(self):
        return self.val

class FunctionExpr(Expression):
    def __init__(self, callname, args):
        self.callname = callname
        self.args = args
    
    def __str__(self):
        return str(self.callname)

class ReturnCommand(Instruction):
    def __init__(self, rexpr):
        self.rexpr = rexpr
    
    def __str__(self):
        return "return " + (str(self.rexpr) if self.rexpr else "")

class FunctionDefCommand(Instruction):
    def __init__ (self, funcname, params):
        self.funcname = funcname
        self.params = params
    
    def __str__(self):
        return str(self.funcname)

class FunctionCallCommand(Instruction): 
    def __init__(self, callname, args):
        self.callname = callname
        self.args = args
    
    def __str__(self):
        return str(self.callname)

class LambdaExpr(Expression):
    def __init__(self, params, body_expr):
        self.params = params
        self.body_expr = body_expr
    
    def __str__(self):
        return "lambda " + " ".join(self.params) + " => " + str(self.body_expr)
    
class LazyExpr(Expression):
    """Lazy expression: lazy expr — defers evaluation until value is needed"""
    def __init__(self, expr):
        self.expr = expr
    
    def __str__(self):
        return f"lazy {self.expr}"

class RangeExpr(Expression):
    """Range expression: [1..10] for finite, [1..] for infinite"""
    def __init__(self, start_expr, end_expr=None):
        self.start_expr = start_expr
        self.end_expr = end_expr
    
    def __str__(self):
        if self.end_expr:
            return f"[{self.start_expr}..{self.end_expr}]"
        return f"[{self.start_expr}..]"

class ListExpr(Expression):
    def __init__(self, elements):
        self.elements = elements
    def __str__(self):
        return "[" + ", ".join(str(e) for e in self.elements) + "]"

# -- Pattern Matching --

class MatchExpr(Expression):
    """Pattern matching: match :x with | 0 => expr | 1 => expr | _ => expr"""
    def __init__(self, subject, cases):
        self.subject = subject
        self.cases = cases  # list of (pattern, expression) tuples
    
    def __str__(self):
        cases_str = " ".join(f"| {p} => {e}" for p, e in self.cases)
        return f"match {self.subject} with {cases_str}"

# -- Where Clauses --

class WhereExpr(Expression):
    """Where clause: expression where :x = 10, :y = 20"""
    def __init__(self, body, bindings):
        self.body = body
        self.bindings = bindings  # list of (var_name, expression) tuples
    
    def __str__(self):
        binds = ", ".join(f"{v} = {e}" for v, e in self.bindings)
        return f"{self.body} where {binds}"

class TypeDefCommand(Instruction):
    def __init__(self, typename, variants):
        self.typename = typename
        self.variants = variants 

    def __str__(self):
        return f"type {self.typename} = " + " | ".join(
            f"{k}({', '.join(v)})" if v else k for k, v in self.variants.items()
        )

class ADTValue(Value):
    def __init__(self, label, values):
        self.label = label
        self.values = values 

    def __str__(self):
        if not self.values:
            return self.label
        return f"{self.label}({', '.join(str(v) for v in self.values)})"
    
    def __eq__(self, other):
        if isinstance(other, ADTValue):
            return self.label == other.label and self.values == other.values
        return False
    
    __repr__ = __str__
    
class ADTPattern(AST):
    """Represents an ADT shape in a match case: | Some(:x) => ..."""
    def __init__(self, label, variables):
        self.label = label
        self.variables = variables  # list of variable names (e.g., [':x'])
    
    def __str__(self):
        if not self.variables:
            return self.label
        return f"{self.label}({', '.join(self.variables)})"
    
class ListPattern(AST):
    def __init__(self, patterns):
        self.patterns = patterns 
    def __str__(self):
        return "[" + ", ".join(str(p) for p in self.patterns) + "]"
