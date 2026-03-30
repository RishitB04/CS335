#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ChironLang Abstract Syntax Tree Builder

import os
import sys
sys.path.insert(0, os.path.join("..", "turtparse"))

from turtparse.tlangParser import tlangParser
from turtparse.tlangVisitor import tlangVisitor

from ChironAST import ChironAST


class astGenPass(tlangVisitor):

    def __init__(self):
        self.repeatInstrCount = 0 # keeps count for no of 'repeat' instructions

    def visitStart(self, ctx:tlangParser.StartContext):
        stmtList = self.visit(ctx.instruction_list())
        return stmtList

    def visitInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        instrList = []
        for instr in ctx.instruction():
            instrList.extend(self.visit(instr))

        return instrList

    def visitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
	# TODO: code refactoring. visitInstruction_list and visitStrict_ilist have same body
        instrList = []
        for instr in ctx.instruction():
            visvalue = self.visit(instr)
            instrList.extend(visvalue)

        return instrList


    def visitAssignment(self, ctx:tlangParser.AssignmentContext):
        lval = ChironAST.Var(ctx.VAR().getText())
        rval = self.visit(ctx.expression())
        return [(ChironAST.AssignmentCommand(lval, rval), 1)]

# Modified ifelse IR generation
    def visitIfConditional(self, ctx:tlangParser.IfConditionalContext):
        ifCondition = self.visit(ctx.condition())
        ifScopeIR = []
        for instr in ctx.strict_ilist().instruction():
            ifScopeIR.extend(self.visit(instr))
        
        elseScopeIR = []
        if ctx.elseConditional():
            for inst in ctx.elseConditional().strict_ilist().instruction():
                elseScopeIR.extend(self.visit(inst))
        
        elifs = []
        for elif_ctx in ctx.elifConditional():
            elifCondition = self.visit(elif_ctx.condition())
            elifScopeIR = []
            for instr in elif_ctx.strict_ilist().instruction():
                elifScopeIR.extend(self.visit(instr))
            elifs.append((elifCondition, elifScopeIR))
        
        for elifCondition, elifScopeIR in reversed(elifs):
            if elseScopeIR:
                jmp_nxt = len(elifScopeIR) + 2
                jmp_end = len(elseScopeIR) + 1
                elif_block = [(ChironAST.ConditionCommand(elifCondition), jmp_nxt)] + elifScopeIR + [(ChironAST.NoOpCommand(), jmp_end)]
            else:
                jmp_nxt = len(elifScopeIR) + 1
                elif_block = [(ChironAST.ConditionCommand(elifCondition), jmp_nxt)] + elifScopeIR
            
            elseScopeIR = elif_block + elseScopeIR
            
        if elseScopeIR:
            jmp_nxt = len(ifScopeIR) + 2
            jmp_end = len(elseScopeIR) + 1
            completeIR = [(ChironAST.ConditionCommand(ifCondition), jmp_nxt)] + ifScopeIR + [(ChironAST.NoOpCommand(), jmp_end)] + elseScopeIR
        else:
            jmp_nxt = len(ifScopeIR) + 1
            completeIR = [(ChironAST.ConditionCommand(ifCondition), jmp_nxt)] + ifScopeIR
            
        return completeIR

    def visitGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        xcor = self.visit(ctx.expression(0))
        ycor = self.visit(ctx.expression(1))
        return [(ChironAST.GotoCommand(xcor, ycor), 1)]

    # Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        expr1 = self.visit(ctx.expression())
        if ctx.MINUS():
            return ChironAST.UMinus(expr1)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#addExpr.
    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.additive().PLUS():
            return ChironAST.Sum(left, right)
        elif ctx.additive().MINUS():
            return ChironAST.Diff(left, right)


    # Visit a parse tree produced by tlangParser#mulExpr.
    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.multiplicative().MUL():
            return ChironAST.Mult(left, right)
        elif ctx.multiplicative().DIV():
            return ChironAST.Div(left, right)


    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visit(ctx.expression()) 
   

    def visitCondition(self, ctx:tlangParser.ConditionContext):
        if ctx.PENCOND():
            return ChironAST.PenStatus();

        if ctx.NOT():
            expr1 = self.visit(ctx.condition(0))
            return ChironAST.NOT(expr1)


        if ctx.logicOp():
            expr1 = self.visit(ctx.condition(0))
            expr2 = self.visit(ctx.condition(1))
            logicOpCtx = ctx.logicOp()

            if logicOpCtx.AND():
                return ChironAST.AND(expr1, expr2)
            elif logicOpCtx.OR():
                return ChironAST.OR(expr1, expr2)


        if ctx.binCondOp():
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))
            binOpCtx = ctx.binCondOp()

            if binOpCtx.LT():
                return ChironAST.LT(expr1, expr2)
            elif binOpCtx.GT():
                return ChironAST.GT(expr1, expr2)
            elif binOpCtx.EQ():
                return ChironAST.EQ(expr1, expr2)
            elif binOpCtx.NEQ():
                return ChironAST.NEQ(expr1, expr2)
            elif binOpCtx.LTE():
                return ChironAST.LTE(expr1, expr2)
            elif binOpCtx.GTE():
                return ChironAST.GTE(expr1, expr2)

        if ctx.condition():
            # condition is inside paranthesis
            return self.visit(ctx.condition(0))

        return self.visitChildren(ctx)

    def visitValue(self, ctx:tlangParser.ValueContext):
        if ctx.NUM():
            return ChironAST.Num(ctx.NUM().getText())
        elif ctx.VAR():
            return ChironAST.Var(ctx.VAR().getText())
        elif ctx.NAME():
            return ChironAST.NameVal(ctx.NAME().getText())

    def visitLoop(self, ctx:tlangParser.LoopContext):
        # insert counter variable in IR for tracking repeat count
        self.repeatInstrCount += 1
        repeatNum = self.visit(ctx.value())
        counterVar = ChironAST.Var(":__rep_counter_" + str(self.repeatInstrCount))
        counterVarInitInstr = ChironAST.AssignmentCommand(counterVar, repeatNum)
        constZero = ChironAST.Num(0)
        constOne = ChironAST.Num(1)
        loopCond = ChironAST.ConditionCommand(ChironAST.GT(counterVar, constZero))
        counterVarDecrInstr = ChironAST.AssignmentCommand(counterVar, ChironAST.Diff(counterVar, constOne))

        thenInstrList = []
        for instr in ctx.strict_ilist().instruction():
            temp = self.visit(instr)
            thenInstrList.extend(temp)

        boolFalse = ChironAST.ConditionCommand(ChironAST.BoolFalse())
        return [(counterVarInitInstr, 1), (loopCond, len(thenInstrList) + 3)] + thenInstrList +\
            [(counterVarDecrInstr, 1), (boolFalse, -len(thenInstrList) - 2)]

    def visitMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        mvcommand = ctx.moveOp().getText()
        mvexpr = self.visit(ctx.expression())
        return [(ChironAST.MoveCommand(mvcommand, mvexpr), 1)]

    def visitPenCommand(self, ctx:tlangParser.PenCommandContext):
        return [(ChironAST.PenCommand(ctx.getText()), 1)]
    
    def visitFunctionDeclaration(self, ctx:tlangParser.FunctionDeclarationContext):
        funcname = ctx.NAME().getText()
        params = [p.getText() for p in ctx.VAR()]

        self.scope = getattr(self, "scope", 0) + 1

        instructionList = []

        for inst in ctx.strict_ilist().instruction():
            instructionList.extend(self.visit(inst))

        self.scope -= 1

        declAttr = ChironAST.FunctionDefCommand(funcname, params)
        explicitReturn = ChironAST.ReturnCommand(None)
        jmpTgt = len(instructionList) + 2

        return [(declAttr, jmpTgt)] + instructionList + [(explicitReturn, 1)]
    
    def visitReturnInstruction(self, ctx:tlangParser.ReturnInstructionContext):
        if getattr(self, "scope", 0) == 0:
            raise Exception("return statement not allowed in global scope")
        
        rexpr = self.visit(ctx.expression()) if ctx.expression() else None
        return [(ChironAST.ReturnCommand(rexpr), 1)]
    
    def buildFunctionCall(self, ctx:tlangParser.FunctionCallContext):
        if ctx.call().NAME():
            callname = ChironAST.NameVal(ctx.call().NAME().getText())
        elif ctx.call().VAR():
            callname = ChironAST.Var(ctx.call().VAR().getText())
        else:
            raise Exception("Invalid function call")
        
        args = []
        if ctx.argumentList():
            for arg in ctx.argumentList().expression():
                args.append(self.visit(arg))
        
        return callname, args
    
    def visitFunctionCall(self, ctx:tlangParser.FunctionCallContext):
        callname, args = self.buildFunctionCall(ctx)
        return [(ChironAST.FunctionCallCommand(callname, args), 1)]
    
    def visitFuncExpr(self, ctx:tlangParser.FuncExprContext):
        callname, args = self.buildFunctionCall(ctx.functionCall())
        return ChironAST.FunctionExpr(callname, args)

    def visitLambdaExpression(self, ctx:tlangParser.LambdaExpressionContext):
        return self.visit(ctx.lambdaExpr())
    
    def visitLambdaExpr(self, ctx:tlangParser.LambdaExprContext):
        params = [p.getText() for p in ctx.VAR()]
        body_expr = self.visit(ctx.expression())
        return ChironAST.LambdaExpr(params, body_expr)
