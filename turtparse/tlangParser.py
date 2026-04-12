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
        4,1,47,271,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,5,1,69,8,1,10,1,12,1,72,9,1,1,2,4,2,75,8,2,11,2,12,2,76,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,89,8,3,1,4,1,4,1,5,1,5,1,5,
        5,5,96,8,5,10,5,12,5,99,9,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,107,8,6,
        1,6,1,6,1,7,1,7,1,7,5,7,114,8,7,10,7,12,7,117,9,7,1,8,1,8,3,8,121,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,129,8,9,10,9,12,9,132,9,9,1,9,3,
        9,135,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        3,19,187,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,197,8,
        19,10,19,12,19,200,9,19,1,20,1,20,5,20,204,8,20,10,20,12,20,207,
        9,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,219,
        8,22,1,22,1,22,1,23,1,23,1,23,1,23,4,23,227,8,23,11,23,12,23,228,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,254,8,28,
        1,28,1,28,1,28,1,28,5,28,260,8,28,10,28,12,28,263,9,28,1,29,1,29,
        1,30,1,30,1,31,1,31,1,31,0,2,38,56,32,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,
        9,1,0,45,46,1,0,15,18,1,0,19,20,2,0,29,29,44,45,1,0,32,33,1,0,30,
        31,1,0,35,40,1,0,41,42,1,0,44,46,271,0,64,1,0,0,0,2,70,1,0,0,0,4,
        74,1,0,0,0,6,88,1,0,0,0,8,90,1,0,0,0,10,92,1,0,0,0,12,103,1,0,0,
        0,14,110,1,0,0,0,16,118,1,0,0,0,18,122,1,0,0,0,20,136,1,0,0,0,22,
        142,1,0,0,0,24,147,1,0,0,0,26,153,1,0,0,0,28,160,1,0,0,0,30,164,
        1,0,0,0,32,167,1,0,0,0,34,169,1,0,0,0,36,171,1,0,0,0,38,186,1,0,
        0,0,40,201,1,0,0,0,42,211,1,0,0,0,44,214,1,0,0,0,46,222,1,0,0,0,
        48,230,1,0,0,0,50,235,1,0,0,0,52,237,1,0,0,0,54,239,1,0,0,0,56,253,
        1,0,0,0,58,264,1,0,0,0,60,266,1,0,0,0,62,268,1,0,0,0,64,65,3,2,1,
        0,65,66,5,0,0,1,66,1,1,0,0,0,67,69,3,6,3,0,68,67,1,0,0,0,69,72,1,
        0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,3,1,0,0,0,72,70,1,0,0,0,73,
        75,3,6,3,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,
        0,77,5,1,0,0,0,78,89,3,28,14,0,79,89,3,18,9,0,80,89,3,24,12,0,81,
        89,3,30,15,0,82,89,3,34,17,0,83,89,3,26,13,0,84,89,3,36,18,0,85,
        89,3,10,5,0,86,89,3,12,6,0,87,89,3,16,8,0,88,78,1,0,0,0,88,79,1,
        0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,88,82,1,0,0,0,88,83,1,0,0,0,88,
        84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,88,87,1,0,0,0,89,7,1,0,0,
        0,90,91,7,0,0,0,91,9,1,0,0,0,92,93,5,1,0,0,93,97,5,46,0,0,94,96,
        5,45,0,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,
        98,100,1,0,0,0,99,97,1,0,0,0,100,101,3,4,2,0,101,102,5,2,0,0,102,
        11,1,0,0,0,103,104,3,8,4,0,104,106,5,3,0,0,105,107,3,14,7,0,106,
        105,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,4,0,0,109,
        13,1,0,0,0,110,115,3,38,19,0,111,112,5,5,0,0,112,114,3,38,19,0,113,
        111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
        15,1,0,0,0,117,115,1,0,0,0,118,120,5,6,0,0,119,121,3,38,19,0,120,
        119,1,0,0,0,120,121,1,0,0,0,121,17,1,0,0,0,122,123,5,7,0,0,123,124,
        3,56,28,0,124,125,5,8,0,0,125,126,3,4,2,0,126,130,5,9,0,0,127,129,
        3,20,10,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,133,135,3,22,11,0,134,133,
        1,0,0,0,134,135,1,0,0,0,135,19,1,0,0,0,136,137,5,10,0,0,137,138,
        3,56,28,0,138,139,5,8,0,0,139,140,3,4,2,0,140,141,5,9,0,0,141,21,
        1,0,0,0,142,143,5,11,0,0,143,144,5,8,0,0,144,145,3,4,2,0,145,146,
        5,9,0,0,146,23,1,0,0,0,147,148,5,12,0,0,148,149,3,62,31,0,149,150,
        5,8,0,0,150,151,3,4,2,0,151,152,5,9,0,0,152,25,1,0,0,0,153,154,5,
        13,0,0,154,155,5,3,0,0,155,156,3,38,19,0,156,157,5,5,0,0,157,158,
        3,38,19,0,158,159,5,4,0,0,159,27,1,0,0,0,160,161,5,45,0,0,161,162,
        5,14,0,0,162,163,3,38,19,0,163,29,1,0,0,0,164,165,3,32,16,0,165,
        166,3,38,19,0,166,31,1,0,0,0,167,168,7,1,0,0,168,33,1,0,0,0,169,
        170,7,2,0,0,170,35,1,0,0,0,171,172,5,21,0,0,172,37,1,0,0,0,173,174,
        6,19,-1,0,174,175,5,31,0,0,175,187,3,38,19,10,176,187,3,12,6,0,177,
        187,3,40,20,0,178,187,3,42,21,0,179,187,3,44,22,0,180,187,3,46,23,
        0,181,187,3,62,31,0,182,183,5,3,0,0,183,184,3,38,19,0,184,185,5,
        4,0,0,185,187,1,0,0,0,186,173,1,0,0,0,186,176,1,0,0,0,186,177,1,
        0,0,0,186,178,1,0,0,0,186,179,1,0,0,0,186,180,1,0,0,0,186,181,1,
        0,0,0,186,182,1,0,0,0,187,198,1,0,0,0,188,189,10,9,0,0,189,190,3,
        52,26,0,190,191,3,38,19,10,191,197,1,0,0,0,192,193,10,8,0,0,193,
        194,3,54,27,0,194,195,3,38,19,9,195,197,1,0,0,0,196,188,1,0,0,0,
        196,192,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,
        199,39,1,0,0,0,200,198,1,0,0,0,201,205,5,22,0,0,202,204,5,45,0,0,
        203,202,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,
        206,208,1,0,0,0,207,205,1,0,0,0,208,209,5,23,0,0,209,210,3,38,19,
        0,210,41,1,0,0,0,211,212,5,24,0,0,212,213,3,38,19,0,213,43,1,0,0,
        0,214,215,5,8,0,0,215,216,3,38,19,0,216,218,5,25,0,0,217,219,3,38,
        19,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,5,9,
        0,0,221,45,1,0,0,0,222,223,5,26,0,0,223,224,3,38,19,0,224,226,5,
        27,0,0,225,227,3,48,24,0,226,225,1,0,0,0,227,228,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,47,1,0,0,0,230,231,5,28,0,0,231,232,
        3,50,25,0,232,233,5,23,0,0,233,234,3,38,19,0,234,49,1,0,0,0,235,
        236,7,3,0,0,236,51,1,0,0,0,237,238,7,4,0,0,238,53,1,0,0,0,239,240,
        7,5,0,0,240,55,1,0,0,0,241,242,6,28,-1,0,242,243,5,43,0,0,243,254,
        3,56,28,5,244,245,3,38,19,0,245,246,3,58,29,0,246,247,3,38,19,0,
        247,254,1,0,0,0,248,254,5,34,0,0,249,250,5,3,0,0,250,251,3,56,28,
        0,251,252,5,4,0,0,252,254,1,0,0,0,253,241,1,0,0,0,253,244,1,0,0,
        0,253,248,1,0,0,0,253,249,1,0,0,0,254,261,1,0,0,0,255,256,10,3,0,
        0,256,257,3,60,30,0,257,258,3,56,28,4,258,260,1,0,0,0,259,255,1,
        0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,57,1,0,
        0,0,263,261,1,0,0,0,264,265,7,6,0,0,265,59,1,0,0,0,266,267,7,7,0,
        0,267,61,1,0,0,0,268,269,7,8,0,0,269,63,1,0,0,0,17,70,76,88,97,106,
        115,120,130,134,186,196,198,205,218,228,253,261
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
                     "'lambda'", "'=>'", "'lazy'", "'..'", "'match'", "'with'", 
                     "'|'", "'_'", "'+'", "'-'", "'*'", "'/'", "'pendown?'", 
                     "'<'", "'>'", "'=='", "'!='", "'<='", "'>='", "'&&'", 
                     "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_matchExpr = 23
    RULE_matchCase = 24
    RULE_pattern = 25
    RULE_multiplicative = 26
    RULE_additive = 27
    RULE_condition = 28
    RULE_binCondOp = 29
    RULE_logicOp = 30
    RULE_value = 31

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "call", "functionDeclaration", "functionCall", "argumentList", 
                   "returnInstruction", "ifConditional", "elifConditional", 
                   "elseConditional", "loop", "gotoCommand", "assignment", 
                   "moveCommand", "moveOp", "penCommand", "pauseCommand", 
                   "expression", "lambdaExpr", "lazyExpr", "rangeExpr", 
                   "matchExpr", "matchCase", "pattern", "multiplicative", 
                   "additive", "condition", "binCondOp", "logicOp", "value" ]

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
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    PLUS=30
    MINUS=31
    MUL=32
    DIV=33
    PENCOND=34
    LT=35
    GT=36
    EQ=37
    NEQ=38
    LTE=39
    GTE=40
    AND=41
    OR=42
    NOT=43
    NUM=44
    VAR=45
    NAME=46
    Whitespace=47

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
            self.state = 64
            self.instruction_list()
            self.state = 65
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
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 105553120440514) != 0):
                self.state = 67
                self.instruction()
                self.state = 72
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
            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self.instruction()
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 105553120440514) != 0)):
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.ifConditional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.moveCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.penCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.gotoCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
                self.pauseCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 85
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 86
                self.functionCall()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 87
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
            self.state = 90
            _la = self._input.LA(1)
            if not(_la==45 or _la==46):
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
            self.state = 92
            self.match(tlangParser.T__0)
            self.state = 93
            self.match(tlangParser.NAME)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.match(tlangParser.VAR) 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 100
            self.strict_ilist()
            self.state = 101
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
            self.state = 103
            self.call()
            self.state = 104
            self.match(tlangParser.T__2)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 123147537875208) != 0):
                self.state = 105
                self.argumentList()


            self.state = 108
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
            self.state = 110
            self.expression(0)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 111
                self.match(tlangParser.T__4)
                self.state = 112
                self.expression(0)
                self.state = 117
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
            self.state = 118
            self.match(tlangParser.T__5)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 119
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
            self.state = 122
            self.match(tlangParser.T__6)
            self.state = 123
            self.condition(0)
            self.state = 124
            self.match(tlangParser.T__7)
            self.state = 125
            self.strict_ilist()
            self.state = 126
            self.match(tlangParser.T__8)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 127
                self.elifConditional()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 133
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
            self.state = 136
            self.match(tlangParser.T__9)
            self.state = 137
            self.condition(0)
            self.state = 138
            self.match(tlangParser.T__7)
            self.state = 139
            self.strict_ilist()
            self.state = 140
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
            self.state = 142
            self.match(tlangParser.T__10)
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
            self.state = 147
            self.match(tlangParser.T__11)
            self.state = 148
            self.value()
            self.state = 149
            self.match(tlangParser.T__7)
            self.state = 150
            self.strict_ilist()
            self.state = 151
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
            self.state = 153
            self.match(tlangParser.T__12)
            self.state = 154
            self.match(tlangParser.T__2)
            self.state = 155
            self.expression(0)
            self.state = 156
            self.match(tlangParser.T__4)
            self.state = 157
            self.expression(0)
            self.state = 158
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
            self.state = 160
            self.match(tlangParser.VAR)
            self.state = 161
            self.match(tlangParser.T__13)
            self.state = 162
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
            self.state = 164
            self.moveOp()
            self.state = 165
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
            self.state = 167
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
            self.state = 169
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
            self.state = 171
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


    class MatchExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matchExpr(self):
            return self.getTypedRuleContext(tlangParser.MatchExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchExpression" ):
                return visitor.visitMatchExpression(self)
            else:
                return visitor.visitChildren(self)


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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = tlangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 174
                self.match(tlangParser.MINUS)
                self.state = 175
                self.expression(10)
                pass

            elif la_ == 2:
                localctx = tlangParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 176
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = tlangParser.LambdaExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.lambdaExpr()
                pass

            elif la_ == 4:
                localctx = tlangParser.LazyExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.lazyExpr()
                pass

            elif la_ == 5:
                localctx = tlangParser.RangeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.rangeExpr()
                pass

            elif la_ == 6:
                localctx = tlangParser.MatchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                self.matchExpr()
                pass

            elif la_ == 7:
                localctx = tlangParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 181
                self.value()
                pass

            elif la_ == 8:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.match(tlangParser.T__2)
                self.state = 183
                self.expression(0)
                self.state = 184
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 196
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = tlangParser.MulExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 189
                        self.multiplicative()
                        self.state = 190
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = tlangParser.AddExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 193
                        self.additive()
                        self.state = 194
                        self.expression(9)
                        pass

             
                self.state = 200
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
            self.state = 201
            self.match(tlangParser.T__21)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 202
                self.match(tlangParser.VAR)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(tlangParser.T__22)
            self.state = 209
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
            self.state = 211
            self.match(tlangParser.T__23)
            self.state = 212
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
            self.state = 214
            self.match(tlangParser.T__7)
            self.state = 215
            self.expression(0)
            self.state = 216
            self.match(tlangParser.T__24)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 123147537875208) != 0):
                self.state = 217
                self.expression(0)


            self.state = 220
            self.match(tlangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def matchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.MatchCaseContext)
            else:
                return self.getTypedRuleContext(tlangParser.MatchCaseContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_matchExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchExpr" ):
                return visitor.visitMatchExpr(self)
            else:
                return visitor.visitChildren(self)




    def matchExpr(self):

        localctx = tlangParser.MatchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_matchExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(tlangParser.T__25)
            self.state = 223
            self.expression(0)
            self.state = 224
            self.match(tlangParser.T__26)
            self.state = 226 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 225
                    self.matchCase()

                else:
                    raise NoViableAltException(self)
                self.state = 228 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(tlangParser.PatternContext,0)


        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_matchCase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCase" ):
                return visitor.visitMatchCase(self)
            else:
                return visitor.visitChildren(self)




    def matchCase(self):

        localctx = tlangParser.MatchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_matchCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(tlangParser.T__27)
            self.state = 231
            self.pattern()
            self.state = 232
            self.match(tlangParser.T__22)
            self.state = 233
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(tlangParser.NUM, 0)

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = tlangParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 52777095004160) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
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
        self.enterRule(localctx, 54, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 242
                self.match(tlangParser.NOT)
                self.state = 243
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 244
                self.expression(0)
                self.state = 245
                self.binCondOp()
                self.state = 246
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 248
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 4:
                self.state = 249
                self.match(tlangParser.T__2)
                self.state = 250
                self.condition(0)
                self.state = 251
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 255
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 256
                    self.logicOp()
                    self.state = 257
                    self.condition(4) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_binCondOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
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
        self.enterRule(localctx, 60, self.RULE_logicOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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
        self.enterRule(localctx, 62, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0)):
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
        self._predicates[28] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




