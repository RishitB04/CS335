# Generated from turtparse/tlang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,249,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,1,5,1,63,8,1,10,1,12,1,66,9,1,
        1,2,4,2,69,8,2,11,2,12,2,70,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,83,8,3,1,4,1,4,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,
        5,1,5,1,5,1,6,1,6,1,6,3,6,101,8,6,1,6,1,6,1,7,1,7,1,7,5,7,108,8,
        7,10,7,12,7,111,9,7,1,8,1,8,3,8,115,8,8,1,9,1,9,1,9,1,9,1,9,1,9,
        5,9,123,8,9,10,9,12,9,126,9,9,1,9,3,9,129,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,180,8,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,190,8,19,10,19,12,19,193,9,19,1,20,1,20,
        5,20,197,8,20,10,20,12,20,200,9,20,1,20,1,20,1,20,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,3,22,212,8,22,1,22,1,22,1,23,1,23,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        232,8,25,1,25,1,25,1,25,1,25,5,25,238,8,25,10,25,12,25,241,9,25,
        1,26,1,26,1,27,1,27,1,28,1,28,1,28,0,2,38,50,29,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        0,8,1,0,41,42,1,0,15,18,1,0,19,20,1,0,28,29,1,0,26,27,1,0,31,36,
        1,0,37,38,1,0,40,42,250,0,58,1,0,0,0,2,64,1,0,0,0,4,68,1,0,0,0,6,
        82,1,0,0,0,8,84,1,0,0,0,10,86,1,0,0,0,12,97,1,0,0,0,14,104,1,0,0,
        0,16,112,1,0,0,0,18,116,1,0,0,0,20,130,1,0,0,0,22,136,1,0,0,0,24,
        141,1,0,0,0,26,147,1,0,0,0,28,154,1,0,0,0,30,158,1,0,0,0,32,161,
        1,0,0,0,34,163,1,0,0,0,36,165,1,0,0,0,38,179,1,0,0,0,40,194,1,0,
        0,0,42,204,1,0,0,0,44,207,1,0,0,0,46,215,1,0,0,0,48,217,1,0,0,0,
        50,231,1,0,0,0,52,242,1,0,0,0,54,244,1,0,0,0,56,246,1,0,0,0,58,59,
        3,2,1,0,59,60,5,0,0,1,60,1,1,0,0,0,61,63,3,6,3,0,62,61,1,0,0,0,63,
        66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,64,1,0,0,
        0,67,69,3,6,3,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,5,1,0,0,0,72,83,3,28,14,0,73,83,3,18,9,0,74,83,3,24,12,
        0,75,83,3,30,15,0,76,83,3,34,17,0,77,83,3,26,13,0,78,83,3,36,18,
        0,79,83,3,10,5,0,80,83,3,12,6,0,81,83,3,16,8,0,82,72,1,0,0,0,82,
        73,1,0,0,0,82,74,1,0,0,0,82,75,1,0,0,0,82,76,1,0,0,0,82,77,1,0,0,
        0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,7,1,
        0,0,0,84,85,7,0,0,0,85,9,1,0,0,0,86,87,5,1,0,0,87,91,5,42,0,0,88,
        90,5,41,0,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,
        0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,95,3,4,2,0,95,96,5,2,0,0,96,11,
        1,0,0,0,97,98,3,8,4,0,98,100,5,3,0,0,99,101,3,14,7,0,100,99,1,0,
        0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,103,5,4,0,0,103,13,1,0,0,
        0,104,109,3,38,19,0,105,106,5,5,0,0,106,108,3,38,19,0,107,105,1,
        0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,15,1,0,
        0,0,111,109,1,0,0,0,112,114,5,6,0,0,113,115,3,38,19,0,114,113,1,
        0,0,0,114,115,1,0,0,0,115,17,1,0,0,0,116,117,5,7,0,0,117,118,3,50,
        25,0,118,119,5,8,0,0,119,120,3,4,2,0,120,124,5,9,0,0,121,123,3,20,
        10,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,
        0,0,125,128,1,0,0,0,126,124,1,0,0,0,127,129,3,22,11,0,128,127,1,
        0,0,0,128,129,1,0,0,0,129,19,1,0,0,0,130,131,5,10,0,0,131,132,3,
        50,25,0,132,133,5,8,0,0,133,134,3,4,2,0,134,135,5,9,0,0,135,21,1,
        0,0,0,136,137,5,11,0,0,137,138,5,8,0,0,138,139,3,4,2,0,139,140,5,
        9,0,0,140,23,1,0,0,0,141,142,5,12,0,0,142,143,3,56,28,0,143,144,
        5,8,0,0,144,145,3,4,2,0,145,146,5,9,0,0,146,25,1,0,0,0,147,148,5,
        13,0,0,148,149,5,3,0,0,149,150,3,38,19,0,150,151,5,5,0,0,151,152,
        3,38,19,0,152,153,5,4,0,0,153,27,1,0,0,0,154,155,5,41,0,0,155,156,
        5,14,0,0,156,157,3,38,19,0,157,29,1,0,0,0,158,159,3,32,16,0,159,
        160,3,38,19,0,160,31,1,0,0,0,161,162,7,1,0,0,162,33,1,0,0,0,163,
        164,7,2,0,0,164,35,1,0,0,0,165,166,5,21,0,0,166,37,1,0,0,0,167,168,
        6,19,-1,0,168,169,5,27,0,0,169,180,3,38,19,9,170,180,3,12,6,0,171,
        180,3,40,20,0,172,180,3,42,21,0,173,180,3,44,22,0,174,180,3,56,28,
        0,175,176,5,3,0,0,176,177,3,38,19,0,177,178,5,4,0,0,178,180,1,0,
        0,0,179,167,1,0,0,0,179,170,1,0,0,0,179,171,1,0,0,0,179,172,1,0,
        0,0,179,173,1,0,0,0,179,174,1,0,0,0,179,175,1,0,0,0,180,191,1,0,
        0,0,181,182,10,8,0,0,182,183,3,46,23,0,183,184,3,38,19,9,184,190,
        1,0,0,0,185,186,10,7,0,0,186,187,3,48,24,0,187,188,3,38,19,8,188,
        190,1,0,0,0,189,181,1,0,0,0,189,185,1,0,0,0,190,193,1,0,0,0,191,
        189,1,0,0,0,191,192,1,0,0,0,192,39,1,0,0,0,193,191,1,0,0,0,194,198,
        5,22,0,0,195,197,5,41,0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,
        1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,
        5,23,0,0,202,203,3,38,19,0,203,41,1,0,0,0,204,205,5,24,0,0,205,206,
        3,38,19,0,206,43,1,0,0,0,207,208,5,8,0,0,208,209,3,38,19,0,209,211,
        5,25,0,0,210,212,3,38,19,0,211,210,1,0,0,0,211,212,1,0,0,0,212,213,
        1,0,0,0,213,214,5,9,0,0,214,45,1,0,0,0,215,216,7,3,0,0,216,47,1,
        0,0,0,217,218,7,4,0,0,218,49,1,0,0,0,219,220,6,25,-1,0,220,221,5,
        39,0,0,221,232,3,50,25,5,222,223,3,38,19,0,223,224,3,52,26,0,224,
        225,3,38,19,0,225,232,1,0,0,0,226,232,5,30,0,0,227,228,5,3,0,0,228,
        229,3,50,25,0,229,230,5,4,0,0,230,232,1,0,0,0,231,219,1,0,0,0,231,
        222,1,0,0,0,231,226,1,0,0,0,231,227,1,0,0,0,232,239,1,0,0,0,233,
        234,10,3,0,0,234,235,3,54,27,0,235,236,3,50,25,4,236,238,1,0,0,0,
        237,233,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,
        240,51,1,0,0,0,241,239,1,0,0,0,242,243,7,5,0,0,243,53,1,0,0,0,244,
        245,7,6,0,0,245,55,1,0,0,0,246,247,7,7,0,0,247,57,1,0,0,0,16,64,
        70,82,91,100,109,114,124,128,179,189,191,198,211,231,239
    ]

class tlangParser ( Parser ):

    grammarFileName = "tlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'to'", "'end'", "'('", "')'", "','", 
                     "'return'", "'if'", "'['", "']'", "'elif'", "'else'", 
                     "'repeat'", "'goto'", "'='", "'forward'", "'backward'", 
                     "'left'", "'right'", "'penup'", "'pendown'", "'pause'", 
                     "'lambda'", "'=>'", "'lazy'", "'..'", "'+'", "'-'", 
                     "'*'", "'/'", "'pendown?'", "'<'", "'>'", "'=='", "'!='", 
                     "'<='", "'>='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PLUS", "MINUS", "MUL", 
                      "DIV", "PENCOND", "LT", "GT", "EQ", "NEQ", "LTE", 
                      "GTE", "AND", "OR", "NOT", "NUM", "VAR", "NAME", "Whitespace" ]

    RULE_start = 0
    RULE_instruction_list = 1
    RULE_strict_ilist = 2
    RULE_instruction = 3
    RULE_call = 4
    RULE_functionDeclaration = 5
    RULE_functionCall = 6
    RULE_argumentList = 7
    RULE_returnInstruction = 8
    RULE_ifConditional = 9
    RULE_elifConditional = 10
    RULE_elseConditional = 11
    RULE_loop = 12
    RULE_gotoCommand = 13
    RULE_assignment = 14
    RULE_moveCommand = 15
    RULE_moveOp = 16
    RULE_penCommand = 17
    RULE_pauseCommand = 18
    RULE_expression = 19
    RULE_lambdaExpr = 20
    RULE_lazyExpr = 21
    RULE_rangeExpr = 22
    RULE_multiplicative = 23
    RULE_additive = 24
    RULE_condition = 25
    RULE_binCondOp = 26
    RULE_logicOp = 27
    RULE_value = 28

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "call", "functionDeclaration", "functionCall", "argumentList", 
                   "returnInstruction", "ifConditional", "elifConditional", 
                   "elseConditional", "loop", "gotoCommand", "assignment", 
                   "moveCommand", "moveOp", "penCommand", "pauseCommand", 
                   "expression", "lambdaExpr", "lazyExpr", "rangeExpr", 
                   "multiplicative", "additive", "condition", "binCondOp", 
                   "logicOp", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    PLUS=26
    MINUS=27
    MUL=28
    DIV=29
    PENCOND=30
    LT=31
    GT=32
    EQ=33
    NEQ=34
    LTE=35
    GTE=36
    AND=37
    OR=38
    NOT=39
    NUM=40
    VAR=41
    NAME=42
    Whitespace=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction_list(self):
            return self.getTypedRuleContext(tlangParser.Instruction_listContext,0)


        def EOF(self):
            return self.getToken(tlangParser.EOF, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = tlangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.instruction_list()
            self.state = 59
            self.match(tlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instruction_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(tlangParser.InstructionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_list" ):
                return visitor.visitInstruction_list(self)
            else:
                return visitor.visitChildren(self)




    def instruction_list(self):

        localctx = tlangParser.Instruction_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6597073940674) != 0):
                self.state = 61
                self.instruction()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Strict_ilistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(tlangParser.InstructionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_strict_ilist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrict_ilist" ):
                return visitor.visitStrict_ilist(self)
            else:
                return visitor.visitChildren(self)




    def strict_ilist(self):

        localctx = tlangParser.Strict_ilistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_strict_ilist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.instruction()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6597073940674) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(tlangParser.AssignmentContext,0)


        def ifConditional(self):
            return self.getTypedRuleContext(tlangParser.IfConditionalContext,0)


        def loop(self):
            return self.getTypedRuleContext(tlangParser.LoopContext,0)


        def moveCommand(self):
            return self.getTypedRuleContext(tlangParser.MoveCommandContext,0)


        def penCommand(self):
            return self.getTypedRuleContext(tlangParser.PenCommandContext,0)


        def gotoCommand(self):
            return self.getTypedRuleContext(tlangParser.GotoCommandContext,0)


        def pauseCommand(self):
            return self.getTypedRuleContext(tlangParser.PauseCommandContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(tlangParser.FunctionDeclarationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(tlangParser.FunctionCallContext,0)


        def returnInstruction(self):
            return self.getTypedRuleContext(tlangParser.ReturnInstructionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tlangParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.ifConditional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.moveCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.penCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.gotoCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.pauseCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 80
                self.functionCall()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 81
                self.returnInstruction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = tlangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.VAR)
            else:
                return self.getToken(tlangParser.VAR, i)

        def getRuleIndex(self):
            return tlangParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = tlangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(tlangParser.T__0)
            self.state = 87
            self.match(tlangParser.NAME)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.match(tlangParser.VAR) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 94
            self.strict_ilist()
            self.state = 95
            self.match(tlangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(tlangParser.CallContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(tlangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = tlangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.call()
            self.state = 98
            self.match(tlangParser.T__2)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696736583944) != 0):
                self.state = 99
                self.argumentList()


            self.state = 102
            self.match(tlangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = tlangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.expression(0)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 105
                self.match(tlangParser.T__4)
                self.state = 106
                self.expression(0)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_returnInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnInstruction" ):
                return visitor.visitReturnInstruction(self)
            else:
                return visitor.visitChildren(self)




    def returnInstruction(self):

        localctx = tlangParser.ReturnInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_returnInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(tlangParser.T__5)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 113
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def elifConditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ElifConditionalContext)
            else:
                return self.getTypedRuleContext(tlangParser.ElifConditionalContext,i)


        def elseConditional(self):
            return self.getTypedRuleContext(tlangParser.ElseConditionalContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_ifConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConditional" ):
                return visitor.visitIfConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifConditional(self):

        localctx = tlangParser.IfConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifConditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(tlangParser.T__6)
            self.state = 117
            self.condition(0)
            self.state = 118
            self.match(tlangParser.T__7)
            self.state = 119
            self.strict_ilist()
            self.state = 120
            self.match(tlangParser.T__8)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 121
                self.elifConditional()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 127
                self.elseConditional()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_elifConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifConditional" ):
                return visitor.visitElifConditional(self)
            else:
                return visitor.visitChildren(self)




    def elifConditional(self):

        localctx = tlangParser.ElifConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elifConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(tlangParser.T__9)
            self.state = 131
            self.condition(0)
            self.state = 132
            self.match(tlangParser.T__7)
            self.state = 133
            self.strict_ilist()
            self.state = 134
            self.match(tlangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_elseConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseConditional" ):
                return visitor.visitElseConditional(self)
            else:
                return visitor.visitChildren(self)




    def elseConditional(self):

        localctx = tlangParser.ElseConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elseConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(tlangParser.T__10)
            self.state = 137
            self.match(tlangParser.T__7)
            self.state = 138
            self.strict_ilist()
            self.state = 139
            self.match(tlangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(tlangParser.ValueContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = tlangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(tlangParser.T__11)
            self.state = 142
            self.value()
            self.state = 143
            self.match(tlangParser.T__7)
            self.state = 144
            self.strict_ilist()
            self.state = 145
            self.match(tlangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_gotoCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoCommand" ):
                return visitor.visitGotoCommand(self)
            else:
                return visitor.visitChildren(self)




    def gotoCommand(self):

        localctx = tlangParser.GotoCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_gotoCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(tlangParser.T__12)
            self.state = 148
            self.match(tlangParser.T__2)
            self.state = 149
            self.expression(0)
            self.state = 150
            self.match(tlangParser.T__4)
            self.state = 151
            self.expression(0)
            self.state = 152
            self.match(tlangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = tlangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(tlangParser.VAR)
            self.state = 155
            self.match(tlangParser.T__13)
            self.state = 156
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveOp(self):
            return self.getTypedRuleContext(tlangParser.MoveOpContext,0)


        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_moveCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveCommand" ):
                return visitor.visitMoveCommand(self)
            else:
                return visitor.visitChildren(self)




    def moveCommand(self):

        localctx = tlangParser.MoveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_moveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.moveOp()
            self.state = 159
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_moveOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveOp" ):
                return visitor.visitMoveOp(self)
            else:
                return visitor.visitChildren(self)




    def moveOp(self):

        localctx = tlangParser.MoveOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_moveOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PenCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_penCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCommand" ):
                return visitor.visitPenCommand(self)
            else:
                return visitor.visitChildren(self)




    def penCommand(self):

        localctx = tlangParser.PenCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_penCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauseCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_pauseCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPauseCommand" ):
                return visitor.visitPauseCommand(self)
            else:
                return visitor.visitChildren(self)




    def pauseCommand(self):

        localctx = tlangParser.PauseCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pauseCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(tlangParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LambdaExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambdaExpr(self):
            return self.getTypedRuleContext(tlangParser.LambdaExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpression" ):
                return visitor.visitLambdaExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(tlangParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(tlangParser.FunctionCallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncExpr" ):
                return visitor.visitFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class ValueExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(tlangParser.ValueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpr" ):
                return visitor.visitValueExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)

        def additive(self):
            return self.getTypedRuleContext(tlangParser.AdditiveContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)

        def multiplicative(self):
            return self.getTypedRuleContext(tlangParser.MultiplicativeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class LazyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lazyExpr(self):
            return self.getTypedRuleContext(tlangParser.LazyExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLazyExpression" ):
                return visitor.visitLazyExpression(self)
            else:
                return visitor.visitChildren(self)


    class RangeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rangeExpr(self):
            return self.getTypedRuleContext(tlangParser.RangeExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeExpression" ):
                return visitor.visitRangeExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tlangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = tlangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 168
                self.match(tlangParser.MINUS)
                self.state = 169
                self.expression(9)
                pass

            elif la_ == 2:
                localctx = tlangParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = tlangParser.LambdaExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                self.lambdaExpr()
                pass

            elif la_ == 4:
                localctx = tlangParser.LazyExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 172
                self.lazyExpr()
                pass

            elif la_ == 5:
                localctx = tlangParser.RangeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.rangeExpr()
                pass

            elif la_ == 6:
                localctx = tlangParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.value()
                pass

            elif la_ == 7:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(tlangParser.T__2)
                self.state = 176
                self.expression(0)
                self.state = 177
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 189
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = tlangParser.MulExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 182
                        self.multiplicative()
                        self.state = 183
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = tlangParser.AddExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 186
                        self.additive()
                        self.state = 187
                        self.expression(8)
                        pass

             
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.VAR)
            else:
                return self.getToken(tlangParser.VAR, i)

        def getRuleIndex(self):
            return tlangParser.RULE_lambdaExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpr" ):
                return visitor.visitLambdaExpr(self)
            else:
                return visitor.visitChildren(self)




    def lambdaExpr(self):

        localctx = tlangParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lambdaExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(tlangParser.T__21)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 195
                self.match(tlangParser.VAR)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(tlangParser.T__22)
            self.state = 202
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LazyExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_lazyExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLazyExpr" ):
                return visitor.visitLazyExpr(self)
            else:
                return visitor.visitChildren(self)




    def lazyExpr(self):

        localctx = tlangParser.LazyExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lazyExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(tlangParser.T__23)
            self.state = 205
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_rangeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeExpr" ):
                return visitor.visitRangeExpr(self)
            else:
                return visitor.visitChildren(self)




    def rangeExpr(self):

        localctx = tlangParser.RangeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_rangeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(tlangParser.T__7)
            self.state = 208
            self.expression(0)
            self.state = 209
            self.match(tlangParser.T__24)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696736583944) != 0):
                self.state = 210
                self.expression(0)


            self.state = 213
            self.match(tlangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(tlangParser.MUL, 0)

        def DIV(self):
            return self.getToken(tlangParser.DIV, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_multiplicative

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = tlangParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(tlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(tlangParser.MINUS, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_additive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = tlangParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(tlangParser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ConditionContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def binCondOp(self):
            return self.getTypedRuleContext(tlangParser.BinCondOpContext,0)


        def PENCOND(self):
            return self.getToken(tlangParser.PENCOND, 0)

        def logicOp(self):
            return self.getTypedRuleContext(tlangParser.LogicOpContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tlangParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(tlangParser.NOT)
                self.state = 221
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 222
                self.expression(0)
                self.state = 223
                self.binCondOp()
                self.state = 224
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 226
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 4:
                self.state = 227
                self.match(tlangParser.T__2)
                self.state = 228
                self.condition(0)
                self.state = 229
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 233
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 234
                    self.logicOp()
                    self.state = 235
                    self.condition(4) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinCondOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(tlangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(tlangParser.NEQ, 0)

        def LT(self):
            return self.getToken(tlangParser.LT, 0)

        def GT(self):
            return self.getToken(tlangParser.GT, 0)

        def LTE(self):
            return self.getToken(tlangParser.LTE, 0)

        def GTE(self):
            return self.getToken(tlangParser.GTE, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_binCondOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinCondOp" ):
                return visitor.visitBinCondOp(self)
            else:
                return visitor.visitChildren(self)




    def binCondOp(self):

        localctx = tlangParser.BinCondOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_binCondOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(tlangParser.AND, 0)

        def OR(self):
            return self.getToken(tlangParser.OR, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_logicOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOp" ):
                return visitor.visitLogicOp(self)
            else:
                return visitor.visitChildren(self)




    def logicOp(self):

        localctx = tlangParser.LogicOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_logicOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not(_la==37 or _la==38):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(tlangParser.NUM, 0)

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = tlangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expression_sempred
        self._predicates[25] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




