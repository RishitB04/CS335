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
        4,1,48,287,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,5,1,71,8,1,10,1,12,1,74,9,1,1,2,4,2,77,8,2,11,2,12,2,
        78,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,91,8,3,1,4,1,4,1,
        5,1,5,1,5,5,5,98,8,5,10,5,12,5,101,9,5,1,5,1,5,1,5,1,6,1,6,1,6,3,
        6,109,8,6,1,6,1,6,1,7,1,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,8,
        1,8,3,8,123,8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,131,8,9,10,9,12,9,134,
        9,9,1,9,3,9,137,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,3,19,189,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,5,19,204,8,19,10,19,12,19,207,9,19,5,19,
        209,8,19,10,19,12,19,212,9,19,1,20,1,20,5,20,216,8,20,10,20,12,20,
        219,9,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,
        231,8,22,1,22,1,22,1,23,1,23,1,23,1,23,4,23,239,8,23,11,23,12,23,
        240,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,27,
        1,27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,3,29,270,8,29,1,29,1,29,1,29,1,29,5,29,276,8,29,10,29,
        12,29,279,9,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,0,2,38,58,33,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,0,9,1,0,46,47,1,0,15,18,1,0,19,20,2,0,
        30,30,45,46,1,0,33,34,1,0,31,32,1,0,36,41,1,0,42,43,1,0,45,47,288,
        0,66,1,0,0,0,2,72,1,0,0,0,4,76,1,0,0,0,6,90,1,0,0,0,8,92,1,0,0,0,
        10,94,1,0,0,0,12,105,1,0,0,0,14,112,1,0,0,0,16,120,1,0,0,0,18,124,
        1,0,0,0,20,138,1,0,0,0,22,144,1,0,0,0,24,149,1,0,0,0,26,155,1,0,
        0,0,28,162,1,0,0,0,30,166,1,0,0,0,32,169,1,0,0,0,34,171,1,0,0,0,
        36,173,1,0,0,0,38,188,1,0,0,0,40,213,1,0,0,0,42,223,1,0,0,0,44,226,
        1,0,0,0,46,234,1,0,0,0,48,242,1,0,0,0,50,247,1,0,0,0,52,249,1,0,
        0,0,54,253,1,0,0,0,56,255,1,0,0,0,58,269,1,0,0,0,60,280,1,0,0,0,
        62,282,1,0,0,0,64,284,1,0,0,0,66,67,3,2,1,0,67,68,5,0,0,1,68,1,1,
        0,0,0,69,71,3,6,3,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,
        73,1,0,0,0,73,3,1,0,0,0,74,72,1,0,0,0,75,77,3,6,3,0,76,75,1,0,0,
        0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,5,1,0,0,0,80,91,3,
        28,14,0,81,91,3,18,9,0,82,91,3,24,12,0,83,91,3,30,15,0,84,91,3,34,
        17,0,85,91,3,26,13,0,86,91,3,36,18,0,87,91,3,10,5,0,88,91,3,12,6,
        0,89,91,3,16,8,0,90,80,1,0,0,0,90,81,1,0,0,0,90,82,1,0,0,0,90,83,
        1,0,0,0,90,84,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,90,87,1,0,0,0,
        90,88,1,0,0,0,90,89,1,0,0,0,91,7,1,0,0,0,92,93,7,0,0,0,93,9,1,0,
        0,0,94,95,5,1,0,0,95,99,5,47,0,0,96,98,5,46,0,0,97,96,1,0,0,0,98,
        101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,
        1,0,0,0,102,103,3,4,2,0,103,104,5,2,0,0,104,11,1,0,0,0,105,106,3,
        8,4,0,106,108,5,3,0,0,107,109,3,14,7,0,108,107,1,0,0,0,108,109,1,
        0,0,0,109,110,1,0,0,0,110,111,5,4,0,0,111,13,1,0,0,0,112,117,3,38,
        19,0,113,114,5,5,0,0,114,116,3,38,19,0,115,113,1,0,0,0,116,119,1,
        0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,15,1,0,0,0,119,117,1,0,
        0,0,120,122,5,6,0,0,121,123,3,38,19,0,122,121,1,0,0,0,122,123,1,
        0,0,0,123,17,1,0,0,0,124,125,5,7,0,0,125,126,3,58,29,0,126,127,5,
        8,0,0,127,128,3,4,2,0,128,132,5,9,0,0,129,131,3,20,10,0,130,129,
        1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,136,
        1,0,0,0,134,132,1,0,0,0,135,137,3,22,11,0,136,135,1,0,0,0,136,137,
        1,0,0,0,137,19,1,0,0,0,138,139,5,10,0,0,139,140,3,58,29,0,140,141,
        5,8,0,0,141,142,3,4,2,0,142,143,5,9,0,0,143,21,1,0,0,0,144,145,5,
        11,0,0,145,146,5,8,0,0,146,147,3,4,2,0,147,148,5,9,0,0,148,23,1,
        0,0,0,149,150,5,12,0,0,150,151,3,64,32,0,151,152,5,8,0,0,152,153,
        3,4,2,0,153,154,5,9,0,0,154,25,1,0,0,0,155,156,5,13,0,0,156,157,
        5,3,0,0,157,158,3,38,19,0,158,159,5,5,0,0,159,160,3,38,19,0,160,
        161,5,4,0,0,161,27,1,0,0,0,162,163,5,46,0,0,163,164,5,14,0,0,164,
        165,3,38,19,0,165,29,1,0,0,0,166,167,3,32,16,0,167,168,3,38,19,0,
        168,31,1,0,0,0,169,170,7,1,0,0,170,33,1,0,0,0,171,172,7,2,0,0,172,
        35,1,0,0,0,173,174,5,21,0,0,174,37,1,0,0,0,175,176,6,19,-1,0,176,
        177,5,32,0,0,177,189,3,38,19,11,178,189,3,12,6,0,179,189,3,40,20,
        0,180,189,3,42,21,0,181,189,3,44,22,0,182,189,3,46,23,0,183,189,
        3,64,32,0,184,185,5,3,0,0,185,186,3,38,19,0,186,187,5,4,0,0,187,
        189,1,0,0,0,188,175,1,0,0,0,188,178,1,0,0,0,188,179,1,0,0,0,188,
        180,1,0,0,0,188,181,1,0,0,0,188,182,1,0,0,0,188,183,1,0,0,0,188,
        184,1,0,0,0,189,210,1,0,0,0,190,191,10,10,0,0,191,192,3,54,27,0,
        192,193,3,38,19,11,193,209,1,0,0,0,194,195,10,9,0,0,195,196,3,56,
        28,0,196,197,3,38,19,10,197,209,1,0,0,0,198,199,10,8,0,0,199,200,
        5,22,0,0,200,205,3,52,26,0,201,202,5,5,0,0,202,204,3,52,26,0,203,
        201,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,
        209,1,0,0,0,207,205,1,0,0,0,208,190,1,0,0,0,208,194,1,0,0,0,208,
        198,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,
        39,1,0,0,0,212,210,1,0,0,0,213,217,5,23,0,0,214,216,5,46,0,0,215,
        214,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,
        220,1,0,0,0,219,217,1,0,0,0,220,221,5,24,0,0,221,222,3,38,19,0,222,
        41,1,0,0,0,223,224,5,25,0,0,224,225,3,38,19,0,225,43,1,0,0,0,226,
        227,5,8,0,0,227,228,3,38,19,0,228,230,5,26,0,0,229,231,3,38,19,0,
        230,229,1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,233,5,9,0,0,
        233,45,1,0,0,0,234,235,5,27,0,0,235,236,3,38,19,0,236,238,5,28,0,
        0,237,239,3,48,24,0,238,237,1,0,0,0,239,240,1,0,0,0,240,238,1,0,
        0,0,240,241,1,0,0,0,241,47,1,0,0,0,242,243,5,29,0,0,243,244,3,50,
        25,0,244,245,5,24,0,0,245,246,3,38,19,0,246,49,1,0,0,0,247,248,7,
        3,0,0,248,51,1,0,0,0,249,250,5,46,0,0,250,251,5,14,0,0,251,252,3,
        38,19,0,252,53,1,0,0,0,253,254,7,4,0,0,254,55,1,0,0,0,255,256,7,
        5,0,0,256,57,1,0,0,0,257,258,6,29,-1,0,258,259,5,44,0,0,259,270,
        3,58,29,5,260,261,3,38,19,0,261,262,3,60,30,0,262,263,3,38,19,0,
        263,270,1,0,0,0,264,270,5,35,0,0,265,266,5,3,0,0,266,267,3,58,29,
        0,267,268,5,4,0,0,268,270,1,0,0,0,269,257,1,0,0,0,269,260,1,0,0,
        0,269,264,1,0,0,0,269,265,1,0,0,0,270,277,1,0,0,0,271,272,10,3,0,
        0,272,273,3,62,31,0,273,274,3,58,29,4,274,276,1,0,0,0,275,271,1,
        0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,59,1,0,
        0,0,279,277,1,0,0,0,280,281,7,6,0,0,281,61,1,0,0,0,282,283,7,7,0,
        0,283,63,1,0,0,0,284,285,7,8,0,0,285,65,1,0,0,0,18,72,78,90,99,108,
        117,122,132,136,188,205,208,210,217,230,240,269,277
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
                     "'where'", "'lambda'", "'=>'", "'lazy'", "'..'", "'match'", 
                     "'with'", "'|'", "'_'", "'+'", "'-'", "'*'", "'/'", 
                     "'pendown?'", "'<'", "'>'", "'=='", "'!='", "'<='", 
                     "'>='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "MUL", "DIV", "PENCOND", "LT", "GT", "EQ", "NEQ", 
                      "LTE", "GTE", "AND", "OR", "NOT", "NUM", "VAR", "NAME", 
                      "Whitespace" ]

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
    RULE_whereBinding = 26
    RULE_multiplicative = 27
    RULE_additive = 28
    RULE_condition = 29
    RULE_binCondOp = 30
    RULE_logicOp = 31
    RULE_value = 32

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "call", "functionDeclaration", "functionCall", "argumentList", 
                   "returnInstruction", "ifConditional", "elifConditional", 
                   "elseConditional", "loop", "gotoCommand", "assignment", 
                   "moveCommand", "moveOp", "penCommand", "pauseCommand", 
                   "expression", "lambdaExpr", "lazyExpr", "rangeExpr", 
                   "matchExpr", "matchCase", "pattern", "whereBinding", 
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
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    PLUS=31
    MINUS=32
    MUL=33
    DIV=34
    PENCOND=35
    LT=36
    GT=37
    EQ=38
    NEQ=39
    LTE=40
    GTE=41
    AND=42
    OR=43
    NOT=44
    NUM=45
    VAR=46
    NAME=47
    Whitespace=48

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
            self.state = 66
            self.instruction_list()
            self.state = 67
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
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 211106236707010) != 0):
                self.state = 69
                self.instruction()
                self.state = 74
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
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.instruction()
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 211106236707010) != 0)):
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
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.ifConditional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.moveCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.penCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.gotoCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 86
                self.pauseCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 87
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 88
                self.functionCall()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 89
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
            self.state = 92
            _la = self._input.LA(1)
            if not(_la==46 or _la==47):
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
            self.state = 94
            self.match(tlangParser.T__0)
            self.state = 95
            self.match(tlangParser.NAME)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96
                    self.match(tlangParser.VAR) 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 102
            self.strict_ilist()
            self.state = 103
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
            self.state = 105
            self.call()
            self.state = 106
            self.match(tlangParser.T__2)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 246295075750152) != 0):
                self.state = 107
                self.argumentList()


            self.state = 110
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
            self.state = 112
            self.expression(0)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 113
                self.match(tlangParser.T__4)
                self.state = 114
                self.expression(0)
                self.state = 119
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
            self.state = 120
            self.match(tlangParser.T__5)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 121
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
            self.state = 124
            self.match(tlangParser.T__6)
            self.state = 125
            self.condition(0)
            self.state = 126
            self.match(tlangParser.T__7)
            self.state = 127
            self.strict_ilist()
            self.state = 128
            self.match(tlangParser.T__8)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 129
                self.elifConditional()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 135
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
            self.state = 138
            self.match(tlangParser.T__9)
            self.state = 139
            self.condition(0)
            self.state = 140
            self.match(tlangParser.T__7)
            self.state = 141
            self.strict_ilist()
            self.state = 142
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
            self.state = 144
            self.match(tlangParser.T__10)
            self.state = 145
            self.match(tlangParser.T__7)
            self.state = 146
            self.strict_ilist()
            self.state = 147
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
            self.state = 149
            self.match(tlangParser.T__11)
            self.state = 150
            self.value()
            self.state = 151
            self.match(tlangParser.T__7)
            self.state = 152
            self.strict_ilist()
            self.state = 153
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
            self.state = 155
            self.match(tlangParser.T__12)
            self.state = 156
            self.match(tlangParser.T__2)
            self.state = 157
            self.expression(0)
            self.state = 158
            self.match(tlangParser.T__4)
            self.state = 159
            self.expression(0)
            self.state = 160
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
            self.state = 162
            self.match(tlangParser.VAR)
            self.state = 163
            self.match(tlangParser.T__13)
            self.state = 164
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
            self.state = 166
            self.moveOp()
            self.state = 167
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
            self.state = 169
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
            self.state = 171
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
            self.state = 173
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


    class WhereExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)

        def whereBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.WhereBindingContext)
            else:
                return self.getTypedRuleContext(tlangParser.WhereBindingContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereExpression" ):
                return visitor.visitWhereExpression(self)
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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = tlangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 176
                self.match(tlangParser.MINUS)
                self.state = 177
                self.expression(11)
                pass

            elif la_ == 2:
                localctx = tlangParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = tlangParser.LambdaExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.lambdaExpr()
                pass

            elif la_ == 4:
                localctx = tlangParser.LazyExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                self.lazyExpr()
                pass

            elif la_ == 5:
                localctx = tlangParser.RangeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 181
                self.rangeExpr()
                pass

            elif la_ == 6:
                localctx = tlangParser.MatchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.matchExpr()
                pass

            elif la_ == 7:
                localctx = tlangParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.value()
                pass

            elif la_ == 8:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 184
                self.match(tlangParser.T__2)
                self.state = 185
                self.expression(0)
                self.state = 186
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = tlangParser.MulExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 190
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 191
                        self.multiplicative()
                        self.state = 192
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = tlangParser.AddExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 195
                        self.additive()
                        self.state = 196
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = tlangParser.WhereExpressionContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 199
                        self.match(tlangParser.T__21)
                        self.state = 200
                        self.whereBinding()
                        self.state = 205
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 201
                                self.match(tlangParser.T__4)
                                self.state = 202
                                self.whereBinding() 
                            self.state = 207
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self.state = 213
            self.match(tlangParser.T__22)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 214
                self.match(tlangParser.VAR)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(tlangParser.T__23)
            self.state = 221
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
            self.state = 223
            self.match(tlangParser.T__24)
            self.state = 224
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
            self.state = 226
            self.match(tlangParser.T__7)
            self.state = 227
            self.expression(0)
            self.state = 228
            self.match(tlangParser.T__25)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 246295075750152) != 0):
                self.state = 229
                self.expression(0)


            self.state = 232
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
            self.state = 234
            self.match(tlangParser.T__26)
            self.state = 235
            self.expression(0)
            self.state = 236
            self.match(tlangParser.T__27)
            self.state = 238 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 237
                    self.matchCase()

                else:
                    raise NoViableAltException(self)
                self.state = 240 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 242
            self.match(tlangParser.T__28)
            self.state = 243
            self.pattern()
            self.state = 244
            self.match(tlangParser.T__23)
            self.state = 245
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
            self.state = 247
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 105554190008320) != 0)):
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


    class WhereBindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_whereBinding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereBinding" ):
                return visitor.visitWhereBinding(self)
            else:
                return visitor.visitChildren(self)




    def whereBinding(self):

        localctx = tlangParser.WhereBindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whereBinding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(tlangParser.VAR)
            self.state = 250
            self.match(tlangParser.T__13)
            self.state = 251
            self.expression(0)
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
        self.enterRule(localctx, 54, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
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
        self.enterRule(localctx, 56, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(tlangParser.NOT)
                self.state = 259
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 260
                self.expression(0)
                self.state = 261
                self.binCondOp()
                self.state = 262
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 264
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 4:
                self.state = 265
                self.match(tlangParser.T__2)
                self.state = 266
                self.condition(0)
                self.state = 267
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 271
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 272
                    self.logicOp()
                    self.state = 273
                    self.condition(4) 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_binCondOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
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
        self.enterRule(localctx, 62, self.RULE_logicOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
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
        self.enterRule(localctx, 64, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0)):
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
        self._predicates[29] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




