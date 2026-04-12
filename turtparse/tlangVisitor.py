# Generated from turtparse/tlang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .tlangParser import tlangParser
else:
    from tlangParser import tlangParser

# This class defines a complete generic visitor for a parse tree produced by tlangParser.

class tlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tlangParser#start.
    def visitStart(self, ctx:tlangParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction_list.
    def visitInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#strict_ilist.
    def visitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction.
    def visitInstruction(self, ctx:tlangParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#call.
    def visitCall(self, ctx:tlangParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:tlangParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#functionCall.
    def visitFunctionCall(self, ctx:tlangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#argumentList.
    def visitArgumentList(self, ctx:tlangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#returnInstruction.
    def visitReturnInstruction(self, ctx:tlangParser.ReturnInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ifConditional.
    def visitIfConditional(self, ctx:tlangParser.IfConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#elifConditional.
    def visitElifConditional(self, ctx:tlangParser.ElifConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#elseConditional.
    def visitElseConditional(self, ctx:tlangParser.ElseConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#loop.
    def visitLoop(self, ctx:tlangParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#gotoCommand.
    def visitGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#assignment.
    def visitAssignment(self, ctx:tlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#moveCommand.
    def visitMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#moveOp.
    def visitMoveOp(self, ctx:tlangParser.MoveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#penCommand.
    def visitPenCommand(self, ctx:tlangParser.PenCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#pauseCommand.
    def visitPauseCommand(self, ctx:tlangParser.PauseCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#matchExpression.
    def visitMatchExpression(self, ctx:tlangParser.MatchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:tlangParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#funcExpr.
    def visitFuncExpr(self, ctx:tlangParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#valueExpr.
    def visitValueExpr(self, ctx:tlangParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#addExpr.
    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#mulExpr.
    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#lazyExpression.
    def visitLazyExpression(self, ctx:tlangParser.LazyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#rangeExpression.
    def visitRangeExpression(self, ctx:tlangParser.RangeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:tlangParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#lazyExpr.
    def visitLazyExpr(self, ctx:tlangParser.LazyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#rangeExpr.
    def visitRangeExpr(self, ctx:tlangParser.RangeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#matchExpr.
    def visitMatchExpr(self, ctx:tlangParser.MatchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#matchCase.
    def visitMatchCase(self, ctx:tlangParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#pattern.
    def visitPattern(self, ctx:tlangParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#multiplicative.
    def visitMultiplicative(self, ctx:tlangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#additive.
    def visitAdditive(self, ctx:tlangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#condition.
    def visitCondition(self, ctx:tlangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#binCondOp.
    def visitBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#logicOp.
    def visitLogicOp(self, ctx:tlangParser.LogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#value.
    def visitValue(self, ctx:tlangParser.ValueContext):
        return self.visitChildren(ctx)



del tlangParser