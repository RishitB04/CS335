# Generated from tlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .tlangParser import tlangParser
else:
    from tlangParser import tlangParser

# This class defines a complete listener for a parse tree produced by tlangParser.
class tlangListener(ParseTreeListener):

    # Enter a parse tree produced by tlangParser#start.
    def enterStart(self, ctx:tlangParser.StartContext):
        pass

    # Exit a parse tree produced by tlangParser#start.
    def exitStart(self, ctx:tlangParser.StartContext):
        pass


    # Enter a parse tree produced by tlangParser#instruction_list.
    def enterInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        pass

    # Exit a parse tree produced by tlangParser#instruction_list.
    def exitInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        pass


    # Enter a parse tree produced by tlangParser#strict_ilist.
    def enterStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
        pass

    # Exit a parse tree produced by tlangParser#strict_ilist.
    def exitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
        pass


    # Enter a parse tree produced by tlangParser#listLiteral.
    def enterListLiteral(self, ctx:tlangParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by tlangParser#listLiteral.
    def exitListLiteral(self, ctx:tlangParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by tlangParser#instruction.
    def enterInstruction(self, ctx:tlangParser.InstructionContext):
        pass

    # Exit a parse tree produced by tlangParser#instruction.
    def exitInstruction(self, ctx:tlangParser.InstructionContext):
        pass


    # Enter a parse tree produced by tlangParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:tlangParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by tlangParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:tlangParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by tlangParser#functionCall.
    def enterFunctionCall(self, ctx:tlangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by tlangParser#functionCall.
    def exitFunctionCall(self, ctx:tlangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by tlangParser#argumentList.
    def enterArgumentList(self, ctx:tlangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by tlangParser#argumentList.
    def exitArgumentList(self, ctx:tlangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by tlangParser#returnInstruction.
    def enterReturnInstruction(self, ctx:tlangParser.ReturnInstructionContext):
        pass

    # Exit a parse tree produced by tlangParser#returnInstruction.
    def exitReturnInstruction(self, ctx:tlangParser.ReturnInstructionContext):
        pass


    # Enter a parse tree produced by tlangParser#ifConditional.
    def enterIfConditional(self, ctx:tlangParser.IfConditionalContext):
        pass

    # Exit a parse tree produced by tlangParser#ifConditional.
    def exitIfConditional(self, ctx:tlangParser.IfConditionalContext):
        pass


    # Enter a parse tree produced by tlangParser#elifConditional.
    def enterElifConditional(self, ctx:tlangParser.ElifConditionalContext):
        pass

    # Exit a parse tree produced by tlangParser#elifConditional.
    def exitElifConditional(self, ctx:tlangParser.ElifConditionalContext):
        pass


    # Enter a parse tree produced by tlangParser#elseConditional.
    def enterElseConditional(self, ctx:tlangParser.ElseConditionalContext):
        pass

    # Exit a parse tree produced by tlangParser#elseConditional.
    def exitElseConditional(self, ctx:tlangParser.ElseConditionalContext):
        pass


    # Enter a parse tree produced by tlangParser#loop.
    def enterLoop(self, ctx:tlangParser.LoopContext):
        pass

    # Exit a parse tree produced by tlangParser#loop.
    def exitLoop(self, ctx:tlangParser.LoopContext):
        pass


    # Enter a parse tree produced by tlangParser#gotoCommand.
    def enterGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        pass

    # Exit a parse tree produced by tlangParser#gotoCommand.
    def exitGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        pass


    # Enter a parse tree produced by tlangParser#assignment.
    def enterAssignment(self, ctx:tlangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by tlangParser#assignment.
    def exitAssignment(self, ctx:tlangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by tlangParser#moveCommand.
    def enterMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        pass

    # Exit a parse tree produced by tlangParser#moveCommand.
    def exitMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        pass


    # Enter a parse tree produced by tlangParser#moveOp.
    def enterMoveOp(self, ctx:tlangParser.MoveOpContext):
        pass

    # Exit a parse tree produced by tlangParser#moveOp.
    def exitMoveOp(self, ctx:tlangParser.MoveOpContext):
        pass


    # Enter a parse tree produced by tlangParser#penCommand.
    def enterPenCommand(self, ctx:tlangParser.PenCommandContext):
        pass

    # Exit a parse tree produced by tlangParser#penCommand.
    def exitPenCommand(self, ctx:tlangParser.PenCommandContext):
        pass


    # Enter a parse tree produced by tlangParser#pauseCommand.
    def enterPauseCommand(self, ctx:tlangParser.PauseCommandContext):
        pass

    # Exit a parse tree produced by tlangParser#pauseCommand.
    def exitPauseCommand(self, ctx:tlangParser.PauseCommandContext):
        pass


    # Enter a parse tree produced by tlangParser#matchExpression.
    def enterMatchExpression(self, ctx:tlangParser.MatchExpressionContext):
        pass

    # Exit a parse tree produced by tlangParser#matchExpression.
    def exitMatchExpression(self, ctx:tlangParser.MatchExpressionContext):
        pass


    # Enter a parse tree produced by tlangParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:tlangParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by tlangParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:tlangParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by tlangParser#whereExpression.
    def enterWhereExpression(self, ctx:tlangParser.WhereExpressionContext):
        pass

    # Exit a parse tree produced by tlangParser#whereExpression.
    def exitWhereExpression(self, ctx:tlangParser.WhereExpressionContext):
        pass


    # Enter a parse tree produced by tlangParser#unaryExpr.
    def enterUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by tlangParser#unaryExpr.
    def exitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by tlangParser#funcExpr.
    def enterFuncExpr(self, ctx:tlangParser.FuncExprContext):
        pass

    # Exit a parse tree produced by tlangParser#funcExpr.
    def exitFuncExpr(self, ctx:tlangParser.FuncExprContext):
        pass


    # Enter a parse tree produced by tlangParser#valueExpr.
    def enterValueExpr(self, ctx:tlangParser.ValueExprContext):
        pass

    # Exit a parse tree produced by tlangParser#valueExpr.
    def exitValueExpr(self, ctx:tlangParser.ValueExprContext):
        pass


    # Enter a parse tree produced by tlangParser#addExpr.
    def enterAddExpr(self, ctx:tlangParser.AddExprContext):
        pass

    # Exit a parse tree produced by tlangParser#addExpr.
    def exitAddExpr(self, ctx:tlangParser.AddExprContext):
        pass


    # Enter a parse tree produced by tlangParser#listLiteralExpr.
    def enterListLiteralExpr(self, ctx:tlangParser.ListLiteralExprContext):
        pass

    # Exit a parse tree produced by tlangParser#listLiteralExpr.
    def exitListLiteralExpr(self, ctx:tlangParser.ListLiteralExprContext):
        pass


    # Enter a parse tree produced by tlangParser#mulExpr.
    def enterMulExpr(self, ctx:tlangParser.MulExprContext):
        pass

    # Exit a parse tree produced by tlangParser#mulExpr.
    def exitMulExpr(self, ctx:tlangParser.MulExprContext):
        pass


    # Enter a parse tree produced by tlangParser#lazyExpression.
    def enterLazyExpression(self, ctx:tlangParser.LazyExpressionContext):
        pass

    # Exit a parse tree produced by tlangParser#lazyExpression.
    def exitLazyExpression(self, ctx:tlangParser.LazyExpressionContext):
        pass


    # Enter a parse tree produced by tlangParser#rangeExpression.
    def enterRangeExpression(self, ctx:tlangParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by tlangParser#rangeExpression.
    def exitRangeExpression(self, ctx:tlangParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by tlangParser#parenExpr.
    def enterParenExpr(self, ctx:tlangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by tlangParser#parenExpr.
    def exitParenExpr(self, ctx:tlangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by tlangParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:tlangParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by tlangParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:tlangParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by tlangParser#lazyExpr.
    def enterLazyExpr(self, ctx:tlangParser.LazyExprContext):
        pass

    # Exit a parse tree produced by tlangParser#lazyExpr.
    def exitLazyExpr(self, ctx:tlangParser.LazyExprContext):
        pass


    # Enter a parse tree produced by tlangParser#rangeExpr.
    def enterRangeExpr(self, ctx:tlangParser.RangeExprContext):
        pass

    # Exit a parse tree produced by tlangParser#rangeExpr.
    def exitRangeExpr(self, ctx:tlangParser.RangeExprContext):
        pass


    # Enter a parse tree produced by tlangParser#matchExpr.
    def enterMatchExpr(self, ctx:tlangParser.MatchExprContext):
        pass

    # Exit a parse tree produced by tlangParser#matchExpr.
    def exitMatchExpr(self, ctx:tlangParser.MatchExprContext):
        pass


    # Enter a parse tree produced by tlangParser#matchCase.
    def enterMatchCase(self, ctx:tlangParser.MatchCaseContext):
        pass

    # Exit a parse tree produced by tlangParser#matchCase.
    def exitMatchCase(self, ctx:tlangParser.MatchCaseContext):
        pass


    # Enter a parse tree produced by tlangParser#pattern.
    def enterPattern(self, ctx:tlangParser.PatternContext):
        pass

    # Exit a parse tree produced by tlangParser#pattern.
    def exitPattern(self, ctx:tlangParser.PatternContext):
        pass


    # Enter a parse tree produced by tlangParser#whereBinding.
    def enterWhereBinding(self, ctx:tlangParser.WhereBindingContext):
        pass

    # Exit a parse tree produced by tlangParser#whereBinding.
    def exitWhereBinding(self, ctx:tlangParser.WhereBindingContext):
        pass


    # Enter a parse tree produced by tlangParser#multiplicative.
    def enterMultiplicative(self, ctx:tlangParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by tlangParser#multiplicative.
    def exitMultiplicative(self, ctx:tlangParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by tlangParser#additive.
    def enterAdditive(self, ctx:tlangParser.AdditiveContext):
        pass

    # Exit a parse tree produced by tlangParser#additive.
    def exitAdditive(self, ctx:tlangParser.AdditiveContext):
        pass


    # Enter a parse tree produced by tlangParser#condition.
    def enterCondition(self, ctx:tlangParser.ConditionContext):
        pass

    # Exit a parse tree produced by tlangParser#condition.
    def exitCondition(self, ctx:tlangParser.ConditionContext):
        pass


    # Enter a parse tree produced by tlangParser#binCondOp.
    def enterBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        pass

    # Exit a parse tree produced by tlangParser#binCondOp.
    def exitBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        pass


    # Enter a parse tree produced by tlangParser#logicOp.
    def enterLogicOp(self, ctx:tlangParser.LogicOpContext):
        pass

    # Exit a parse tree produced by tlangParser#logicOp.
    def exitLogicOp(self, ctx:tlangParser.LogicOpContext):
        pass


    # Enter a parse tree produced by tlangParser#value.
    def enterValue(self, ctx:tlangParser.ValueContext):
        pass

    # Exit a parse tree produced by tlangParser#value.
    def exitValue(self, ctx:tlangParser.ValueContext):
        pass



del tlangParser