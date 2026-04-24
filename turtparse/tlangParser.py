# Generated from tlang.g4 by ANTLR 4.13.1
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
        4,1,50,298,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,5,1,71,8,1,10,1,12,1,74,9,1,1,2,4,2,77,8,2,11,2,12,2,
        78,1,3,1,3,1,3,1,3,5,3,85,8,3,10,3,12,3,88,9,3,3,3,90,8,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,103,8,4,1,5,1,5,1,5,5,
        5,108,8,5,10,5,12,5,111,9,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,119,8,6,
        1,6,1,6,1,7,1,7,1,7,5,7,126,8,7,10,7,12,7,129,9,7,1,8,1,8,3,8,133,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,141,8,9,10,9,12,9,144,9,9,1,9,3,
        9,147,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,3,19,200,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,215,8,19,10,19,12,19,218,9,19,5,19,220,
        8,19,10,19,12,19,223,9,19,1,20,1,20,5,20,227,8,20,10,20,12,20,230,
        9,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,242,
        8,22,1,22,1,22,1,23,1,23,1,23,1,23,4,23,250,8,23,11,23,12,23,251,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,
        1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,3,29,281,8,29,1,29,1,29,1,29,1,29,5,29,287,8,29,10,29,12,29,
        290,9,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,0,2,38,58,33,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,0,8,1,0,17,20,1,0,21,22,2,0,32,32,47,48,1,0,
        35,36,1,0,33,34,1,0,38,43,1,0,44,45,1,0,47,48,301,0,66,1,0,0,0,2,
        72,1,0,0,0,4,76,1,0,0,0,6,80,1,0,0,0,8,102,1,0,0,0,10,104,1,0,0,
        0,12,115,1,0,0,0,14,122,1,0,0,0,16,130,1,0,0,0,18,134,1,0,0,0,20,
        148,1,0,0,0,22,154,1,0,0,0,24,159,1,0,0,0,26,165,1,0,0,0,28,172,
        1,0,0,0,30,176,1,0,0,0,32,179,1,0,0,0,34,181,1,0,0,0,36,183,1,0,
        0,0,38,199,1,0,0,0,40,224,1,0,0,0,42,234,1,0,0,0,44,237,1,0,0,0,
        46,245,1,0,0,0,48,253,1,0,0,0,50,258,1,0,0,0,52,260,1,0,0,0,54,264,
        1,0,0,0,56,266,1,0,0,0,58,280,1,0,0,0,60,291,1,0,0,0,62,293,1,0,
        0,0,64,295,1,0,0,0,66,67,3,2,1,0,67,68,5,0,0,1,68,1,1,0,0,0,69,71,
        3,8,4,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,3,1,0,0,0,74,72,1,0,0,0,75,77,3,8,4,0,76,75,1,0,0,0,77,78,1,0,
        0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,5,1,0,0,0,80,89,5,1,0,0,81,86,
        3,38,19,0,82,83,5,2,0,0,83,85,3,38,19,0,84,82,1,0,0,0,85,88,1,0,
        0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,81,
        1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,3,0,0,92,7,1,0,0,0,93,
        103,3,28,14,0,94,103,3,18,9,0,95,103,3,24,12,0,96,103,3,30,15,0,
        97,103,3,34,17,0,98,103,3,26,13,0,99,103,3,36,18,0,100,103,3,10,
        5,0,101,103,3,16,8,0,102,93,1,0,0,0,102,94,1,0,0,0,102,95,1,0,0,
        0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,99,1,0,0,0,102,
        100,1,0,0,0,102,101,1,0,0,0,103,9,1,0,0,0,104,105,5,4,0,0,105,109,
        5,49,0,0,106,108,5,48,0,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,
        1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,0,0,0,112,113,
        3,4,2,0,113,114,5,5,0,0,114,11,1,0,0,0,115,116,5,49,0,0,116,118,
        5,6,0,0,117,119,3,14,7,0,118,117,1,0,0,0,118,119,1,0,0,0,119,120,
        1,0,0,0,120,121,5,7,0,0,121,13,1,0,0,0,122,127,3,38,19,0,123,124,
        5,2,0,0,124,126,3,38,19,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,15,1,0,0,0,129,127,1,0,0,0,130,132,5,
        8,0,0,131,133,3,38,19,0,132,131,1,0,0,0,132,133,1,0,0,0,133,17,1,
        0,0,0,134,135,5,9,0,0,135,136,3,58,29,0,136,137,5,10,0,0,137,138,
        3,4,2,0,138,142,5,11,0,0,139,141,3,20,10,0,140,139,1,0,0,0,141,144,
        1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,146,1,0,0,0,144,142,
        1,0,0,0,145,147,3,22,11,0,146,145,1,0,0,0,146,147,1,0,0,0,147,19,
        1,0,0,0,148,149,5,12,0,0,149,150,3,58,29,0,150,151,5,10,0,0,151,
        152,3,4,2,0,152,153,5,11,0,0,153,21,1,0,0,0,154,155,5,13,0,0,155,
        156,5,10,0,0,156,157,3,4,2,0,157,158,5,11,0,0,158,23,1,0,0,0,159,
        160,5,14,0,0,160,161,3,64,32,0,161,162,5,10,0,0,162,163,3,4,2,0,
        163,164,5,11,0,0,164,25,1,0,0,0,165,166,5,15,0,0,166,167,5,6,0,0,
        167,168,3,38,19,0,168,169,5,2,0,0,169,170,3,38,19,0,170,171,5,7,
        0,0,171,27,1,0,0,0,172,173,5,48,0,0,173,174,5,16,0,0,174,175,3,38,
        19,0,175,29,1,0,0,0,176,177,3,32,16,0,177,178,3,38,19,0,178,31,1,
        0,0,0,179,180,7,0,0,0,180,33,1,0,0,0,181,182,7,1,0,0,182,35,1,0,
        0,0,183,184,5,23,0,0,184,37,1,0,0,0,185,186,6,19,-1,0,186,187,5,
        34,0,0,187,200,3,38,19,12,188,200,3,12,6,0,189,200,3,40,20,0,190,
        200,3,42,21,0,191,200,3,44,22,0,192,200,3,46,23,0,193,200,3,6,3,
        0,194,200,3,64,32,0,195,196,5,6,0,0,196,197,3,38,19,0,197,198,5,
        7,0,0,198,200,1,0,0,0,199,185,1,0,0,0,199,188,1,0,0,0,199,189,1,
        0,0,0,199,190,1,0,0,0,199,191,1,0,0,0,199,192,1,0,0,0,199,193,1,
        0,0,0,199,194,1,0,0,0,199,195,1,0,0,0,200,221,1,0,0,0,201,202,10,
        11,0,0,202,203,3,54,27,0,203,204,3,38,19,12,204,220,1,0,0,0,205,
        206,10,10,0,0,206,207,3,56,28,0,207,208,3,38,19,11,208,220,1,0,0,
        0,209,210,10,9,0,0,210,211,5,24,0,0,211,216,3,52,26,0,212,213,5,
        2,0,0,213,215,3,52,26,0,214,212,1,0,0,0,215,218,1,0,0,0,216,214,
        1,0,0,0,216,217,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,219,201,
        1,0,0,0,219,205,1,0,0,0,219,209,1,0,0,0,220,223,1,0,0,0,221,219,
        1,0,0,0,221,222,1,0,0,0,222,39,1,0,0,0,223,221,1,0,0,0,224,228,5,
        25,0,0,225,227,5,48,0,0,226,225,1,0,0,0,227,230,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,228,1,0,0,0,231,232,
        5,26,0,0,232,233,3,38,19,0,233,41,1,0,0,0,234,235,5,27,0,0,235,236,
        3,38,19,0,236,43,1,0,0,0,237,238,5,10,0,0,238,239,3,38,19,0,239,
        241,5,28,0,0,240,242,3,38,19,0,241,240,1,0,0,0,241,242,1,0,0,0,242,
        243,1,0,0,0,243,244,5,11,0,0,244,45,1,0,0,0,245,246,5,29,0,0,246,
        247,3,38,19,0,247,249,5,30,0,0,248,250,3,48,24,0,249,248,1,0,0,0,
        250,251,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,47,1,0,0,0,253,
        254,5,31,0,0,254,255,3,50,25,0,255,256,5,26,0,0,256,257,3,38,19,
        0,257,49,1,0,0,0,258,259,7,2,0,0,259,51,1,0,0,0,260,261,5,48,0,0,
        261,262,5,16,0,0,262,263,3,38,19,0,263,53,1,0,0,0,264,265,7,3,0,
        0,265,55,1,0,0,0,266,267,7,4,0,0,267,57,1,0,0,0,268,269,6,29,-1,
        0,269,270,5,46,0,0,270,281,3,58,29,5,271,272,3,38,19,0,272,273,3,
        60,30,0,273,274,3,38,19,0,274,281,1,0,0,0,275,281,5,37,0,0,276,277,
        5,6,0,0,277,278,3,58,29,0,278,279,5,7,0,0,279,281,1,0,0,0,280,268,
        1,0,0,0,280,271,1,0,0,0,280,275,1,0,0,0,280,276,1,0,0,0,281,288,
        1,0,0,0,282,283,10,3,0,0,283,284,3,62,31,0,284,285,3,58,29,4,285,
        287,1,0,0,0,286,282,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,
        289,1,0,0,0,289,59,1,0,0,0,290,288,1,0,0,0,291,292,7,5,0,0,292,61,
        1,0,0,0,293,294,7,6,0,0,294,63,1,0,0,0,295,296,7,7,0,0,296,65,1,
        0,0,0,20,72,78,86,89,102,109,118,127,132,142,146,199,216,219,221,
        228,241,251,280,288
    ]

class tlangParser ( Parser ):

    grammarFileName = "tlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "'to'", "'end'", 
                     "'('", "')'", "'return'", "'if'", "'['", "']'", "'elif'", 
                     "'else'", "'repeat'", "'goto'", "'='", "'forward'", 
                     "'backward'", "'left'", "'right'", "'penup'", "'pendown'", 
                     "'pause'", "'where'", "'lambda'", "'=>'", "'lazy'", 
                     "'..'", "'match'", "'with'", "'|'", "'_'", "'+'", "'-'", 
                     "'*'", "'/'", "'pendown?'", "'<'", "'>'", "'=='", "'!='", 
                     "'<='", "'>='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "PENCOND", 
                      "LT", "GT", "EQ", "NEQ", "LTE", "GTE", "AND", "OR", 
                      "NOT", "NUM", "VAR", "NAME", "Whitespace" ]

    RULE_start = 0
    RULE_instruction_list = 1
    RULE_strict_ilist = 2
    RULE_listLiteral = 3
    RULE_instruction = 4
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

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "listLiteral", 
                   "instruction", "functionDeclaration", "functionCall", 
                   "argumentList", "returnInstruction", "ifConditional", 
                   "elifConditional", "elseConditional", "loop", "gotoCommand", 
                   "assignment", "moveCommand", "moveOp", "penCommand", 
                   "pauseCommand", "expression", "lambdaExpr", "lazyExpr", 
                   "rangeExpr", "matchExpr", "matchCase", "pattern", "whereBinding", 
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
    T__30=31
    T__31=32
    PLUS=33
    MINUS=34
    MUL=35
    DIV=36
    PENCOND=37
    LT=38
    GT=39
    EQ=40
    NEQ=41
    LTE=42
    GTE=43
    AND=44
    OR=45
    NOT=46
    NUM=47
    VAR=48
    NAME=49
    Whitespace=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction_list" ):
                listener.enterInstruction_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction_list" ):
                listener.exitInstruction_list(self)

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281474993406736) != 0):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrict_ilist" ):
                listener.enterStrict_ilist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrict_ilist" ):
                listener.exitStrict_ilist(self)

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 281474993406736) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
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
            return tlangParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = tlangParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(tlangParser.T__0)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 985180303000642) != 0):
                self.state = 81
                self.expression(0)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 82
                    self.match(tlangParser.T__1)
                    self.state = 83
                    self.expression(0)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 91
            self.match(tlangParser.T__2)
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


        def returnInstruction(self):
            return self.getTypedRuleContext(tlangParser.ReturnInstructionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tlangParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruction)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.assignment()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.ifConditional()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.loop()
                pass
            elif token in [17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.moveCommand()
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.penCommand()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 98
                self.gotoCommand()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 7)
                self.state = 99
                self.pauseCommand()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 8)
                self.state = 100
                self.functionDeclaration()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 101
                self.returnInstruction()
                pass
            else:
                raise NoViableAltException(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

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
            self.state = 104
            self.match(tlangParser.T__3)
            self.state = 105
            self.match(tlangParser.NAME)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 106
                    self.match(tlangParser.VAR) 
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 112
            self.strict_ilist()
            self.state = 113
            self.match(tlangParser.T__4)
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

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def argumentList(self):
            return self.getTypedRuleContext(tlangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

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
            self.state = 115
            self.match(tlangParser.NAME)
            self.state = 116
            self.match(tlangParser.T__5)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 985180303000642) != 0):
                self.state = 117
                self.argumentList()


            self.state = 120
            self.match(tlangParser.T__6)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

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
            self.state = 122
            self.expression(0)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 123
                self.match(tlangParser.T__1)
                self.state = 124
                self.expression(0)
                self.state = 129
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnInstruction" ):
                listener.enterReturnInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnInstruction" ):
                listener.exitReturnInstruction(self)

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
            self.state = 130
            self.match(tlangParser.T__7)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 131
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfConditional" ):
                listener.enterIfConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfConditional" ):
                listener.exitIfConditional(self)

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
            self.state = 134
            self.match(tlangParser.T__8)
            self.state = 135
            self.condition(0)
            self.state = 136
            self.match(tlangParser.T__9)
            self.state = 137
            self.strict_ilist()
            self.state = 138
            self.match(tlangParser.T__10)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 139
                self.elifConditional()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 145
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifConditional" ):
                listener.enterElifConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifConditional" ):
                listener.exitElifConditional(self)

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
            self.state = 148
            self.match(tlangParser.T__11)
            self.state = 149
            self.condition(0)
            self.state = 150
            self.match(tlangParser.T__9)
            self.state = 151
            self.strict_ilist()
            self.state = 152
            self.match(tlangParser.T__10)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseConditional" ):
                listener.enterElseConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseConditional" ):
                listener.exitElseConditional(self)

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
            self.state = 154
            self.match(tlangParser.T__12)
            self.state = 155
            self.match(tlangParser.T__9)
            self.state = 156
            self.strict_ilist()
            self.state = 157
            self.match(tlangParser.T__10)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

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
            self.state = 159
            self.match(tlangParser.T__13)
            self.state = 160
            self.value()
            self.state = 161
            self.match(tlangParser.T__9)
            self.state = 162
            self.strict_ilist()
            self.state = 163
            self.match(tlangParser.T__10)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoCommand" ):
                listener.enterGotoCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoCommand" ):
                listener.exitGotoCommand(self)

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
            self.state = 165
            self.match(tlangParser.T__14)
            self.state = 166
            self.match(tlangParser.T__5)
            self.state = 167
            self.expression(0)
            self.state = 168
            self.match(tlangParser.T__1)
            self.state = 169
            self.expression(0)
            self.state = 170
            self.match(tlangParser.T__6)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

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
            self.state = 172
            self.match(tlangParser.VAR)
            self.state = 173
            self.match(tlangParser.T__15)
            self.state = 174
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveCommand" ):
                listener.enterMoveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveCommand" ):
                listener.exitMoveCommand(self)

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
            self.state = 176
            self.moveOp()
            self.state = 177
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveOp" ):
                listener.enterMoveOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveOp" ):
                listener.exitMoveOp(self)

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
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenCommand" ):
                listener.enterPenCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenCommand" ):
                listener.exitPenCommand(self)

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
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPauseCommand" ):
                listener.enterPauseCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPauseCommand" ):
                listener.exitPauseCommand(self)

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
            self.state = 183
            self.match(tlangParser.T__22)
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchExpression" ):
                listener.enterMatchExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchExpression" ):
                listener.exitMatchExpression(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpression" ):
                listener.enterLambdaExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpression" ):
                listener.exitLambdaExpression(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereExpression" ):
                listener.enterWhereExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereExpression" ):
                listener.exitWhereExpression(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncExpr" ):
                listener.enterFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncExpr" ):
                listener.exitFuncExpr(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueExpr" ):
                listener.enterValueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueExpr" ):
                listener.exitValueExpr(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListLiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listLiteral(self):
            return self.getTypedRuleContext(tlangParser.ListLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteralExpr" ):
                listener.enterListLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteralExpr" ):
                listener.exitListLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteralExpr" ):
                return visitor.visitListLiteralExpr(self)
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLazyExpression" ):
                listener.enterLazyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLazyExpression" ):
                listener.exitLazyExpression(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeExpression" ):
                listener.enterRangeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeExpression" ):
                listener.exitRangeExpression(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

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
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = tlangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 186
                self.match(tlangParser.MINUS)
                self.state = 187
                self.expression(12)
                pass
            elif token in [49]:
                localctx = tlangParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.functionCall()
                pass
            elif token in [25]:
                localctx = tlangParser.LambdaExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.lambdaExpr()
                pass
            elif token in [27]:
                localctx = tlangParser.LazyExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.lazyExpr()
                pass
            elif token in [10]:
                localctx = tlangParser.RangeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.rangeExpr()
                pass
            elif token in [29]:
                localctx = tlangParser.MatchExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.matchExpr()
                pass
            elif token in [1]:
                localctx = tlangParser.ListLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.listLiteral()
                pass
            elif token in [47, 48]:
                localctx = tlangParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                self.value()
                pass
            elif token in [6]:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                self.match(tlangParser.T__5)
                self.state = 196
                self.expression(0)
                self.state = 197
                self.match(tlangParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = tlangParser.MulExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 202
                        self.multiplicative()
                        self.state = 203
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = tlangParser.AddExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 205
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 206
                        self.additive()
                        self.state = 207
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = tlangParser.WhereExpressionContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 209
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 210
                        self.match(tlangParser.T__23)
                        self.state = 211
                        self.whereBinding()
                        self.state = 216
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 212
                                self.match(tlangParser.T__1)
                                self.state = 213
                                self.whereBinding() 
                            self.state = 218
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                        pass

             
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpr" ):
                listener.enterLambdaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpr" ):
                listener.exitLambdaExpr(self)

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
            self.state = 224
            self.match(tlangParser.T__24)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 225
                self.match(tlangParser.VAR)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(tlangParser.T__25)
            self.state = 232
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLazyExpr" ):
                listener.enterLazyExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLazyExpr" ):
                listener.exitLazyExpr(self)

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
            self.state = 234
            self.match(tlangParser.T__26)
            self.state = 235
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeExpr" ):
                listener.enterRangeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeExpr" ):
                listener.exitRangeExpr(self)

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
            self.state = 237
            self.match(tlangParser.T__9)
            self.state = 238
            self.expression(0)
            self.state = 239
            self.match(tlangParser.T__27)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 985180303000642) != 0):
                self.state = 240
                self.expression(0)


            self.state = 243
            self.match(tlangParser.T__10)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchExpr" ):
                listener.enterMatchExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchExpr" ):
                listener.exitMatchExpr(self)

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
            self.state = 245
            self.match(tlangParser.T__28)
            self.state = 246
            self.expression(0)
            self.state = 247
            self.match(tlangParser.T__29)
            self.state = 249 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 248
                    self.matchCase()

                else:
                    raise NoViableAltException(self)
                self.state = 251 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchCase" ):
                listener.enterMatchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchCase" ):
                listener.exitMatchCase(self)

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
            self.state = 253
            self.match(tlangParser.T__30)
            self.state = 254
            self.pattern()
            self.state = 255
            self.match(tlangParser.T__25)
            self.state = 256
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

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
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 422216760033280) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereBinding" ):
                listener.enterWhereBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereBinding" ):
                listener.exitWhereBinding(self)

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
            self.state = 260
            self.match(tlangParser.VAR)
            self.state = 261
            self.match(tlangParser.T__15)
            self.state = 262
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

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
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

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
            self.state = 266
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

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
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 269
                self.match(tlangParser.NOT)
                self.state = 270
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 271
                self.expression(0)
                self.state = 272
                self.binCondOp()
                self.state = 273
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 275
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 4:
                self.state = 276
                self.match(tlangParser.T__5)
                self.state = 277
                self.condition(0)
                self.state = 278
                self.match(tlangParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 282
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 283
                    self.logicOp()
                    self.state = 284
                    self.condition(4) 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinCondOp" ):
                listener.enterBinCondOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinCondOp" ):
                listener.exitBinCondOp(self)

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
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17317308137472) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOp" ):
                listener.enterLogicOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOp" ):
                listener.exitLogicOp(self)

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
            self.state = 293
            _la = self._input.LA(1)
            if not(_la==44 or _la==45):
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

        def getRuleIndex(self):
            return tlangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

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
            self.state = 295
            _la = self._input.LA(1)
            if not(_la==47 or _la==48):
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
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




