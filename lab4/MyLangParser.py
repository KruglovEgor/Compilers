# Generated from MyLang.g4 by ANTLR 4.13.2
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
        4,1,28,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,45,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,5,7,67,8,7,10,7,12,7,70,9,7,1,7,1,
        7,3,7,74,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        88,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,99,8,8,10,8,12,8,
        102,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,3,1,0,12,14,1,0,15,
        16,1,0,17,22,110,0,19,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,37,1,0,
        0,0,8,46,1,0,0,0,10,52,1,0,0,0,12,58,1,0,0,0,14,73,1,0,0,0,16,87,
        1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,
        21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,31,3,4,
        2,0,26,31,3,6,3,0,27,31,3,8,4,0,28,31,3,10,5,0,29,31,3,12,6,0,30,
        25,1,0,0,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,
        0,31,3,1,0,0,0,32,33,5,24,0,0,33,34,5,1,0,0,34,35,3,16,8,0,35,36,
        5,2,0,0,36,5,1,0,0,0,37,38,5,3,0,0,38,39,5,4,0,0,39,40,3,16,8,0,
        40,41,5,5,0,0,41,44,3,14,7,0,42,43,5,6,0,0,43,45,3,14,7,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,7,1,0,0,0,46,47,5,7,0,0,47,48,5,4,0,0,48,
        49,3,16,8,0,49,50,5,5,0,0,50,51,3,14,7,0,51,9,1,0,0,0,52,53,5,8,
        0,0,53,54,5,4,0,0,54,55,3,16,8,0,55,56,5,5,0,0,56,57,5,2,0,0,57,
        11,1,0,0,0,58,59,5,9,0,0,59,60,5,4,0,0,60,61,5,24,0,0,61,62,5,5,
        0,0,62,63,5,2,0,0,63,13,1,0,0,0,64,68,5,10,0,0,65,67,3,2,1,0,66,
        65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,
        0,70,68,1,0,0,0,71,74,5,11,0,0,72,74,3,2,1,0,73,64,1,0,0,0,73,72,
        1,0,0,0,74,15,1,0,0,0,75,76,6,8,-1,0,76,88,5,25,0,0,77,88,5,26,0,
        0,78,88,5,24,0,0,79,80,5,4,0,0,80,81,3,16,8,0,81,82,5,5,0,0,82,88,
        1,0,0,0,83,84,5,16,0,0,84,88,3,16,8,2,85,86,5,23,0,0,86,88,3,16,
        8,1,87,75,1,0,0,0,87,77,1,0,0,0,87,78,1,0,0,0,87,79,1,0,0,0,87,83,
        1,0,0,0,87,85,1,0,0,0,88,100,1,0,0,0,89,90,10,9,0,0,90,91,7,0,0,
        0,91,99,3,16,8,10,92,93,10,8,0,0,93,94,7,1,0,0,94,99,3,16,8,9,95,
        96,10,7,0,0,96,97,7,2,0,0,97,99,3,16,8,8,98,89,1,0,0,0,98,92,1,0,
        0,0,98,95,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,17,1,0,0,0,102,100,1,0,0,0,8,21,30,44,68,73,87,98,100
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'if'", "'('", "')'", "'else'", 
                     "'while'", "'print'", "'input'", "'{'", "'}'", "'*'", 
                     "'/'", "'%'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_ifStatement = 3
    RULE_whileLoop = 4
    RULE_printStmt = 5
    RULE_inputStmt = 6
    RULE_block = 7
    RULE_expr = 8

    ruleNames =  [ "program", "statement", "assignment", "ifStatement", 
                   "whileLoop", "printStmt", "inputStmt", "block", "expr" ]

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
    ID=24
    NUMBER=25
    STRING=26
    WS=27
    COMMENT=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16778120) != 0)):
                    break

            self.state = 23
            self.match(MyLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfStatementContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(MyLangParser.WhileLoopContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(MyLangParser.PrintStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(MyLangParser.InputStmtContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.whileLoop()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.printStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.inputStmt()
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_assignment

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

        localctx = MyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MyLangParser.ID)
            self.state = 33
            self.match(MyLangParser.T__0)
            self.state = 34
            self.expr(0)
            self.state = 35
            self.match(MyLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyLangParser.BlockContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MyLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MyLangParser.T__2)
            self.state = 38
            self.match(MyLangParser.T__3)
            self.state = 39
            self.expr(0)
            self.state = 40
            self.match(MyLangParser.T__4)
            self.state = 41
            self.block()
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 42
                self.match(MyLangParser.T__5)
                self.state = 43
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = MyLangParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MyLangParser.T__6)
            self.state = 47
            self.match(MyLangParser.T__3)
            self.state = 48
            self.expr(0)
            self.state = 49
            self.match(MyLangParser.T__4)
            self.state = 50
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = MyLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MyLangParser.T__7)
            self.state = 53
            self.match(MyLangParser.T__3)
            self.state = 54
            self.expr(0)
            self.state = 55
            self.match(MyLangParser.T__4)
            self.state = 56
            self.match(MyLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = MyLangParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_inputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MyLangParser.T__8)
            self.state = 59
            self.match(MyLangParser.T__3)
            self.state = 60
            self.match(MyLangParser.ID)
            self.state = 61
            self.match(MyLangParser.T__4)
            self.state = 62
            self.match(MyLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(MyLangParser.T__9)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16778120) != 0):
                    self.state = 65
                    self.statement()
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self.match(MyLangParser.T__10)
                pass
            elif token in [3, 7, 8, 9, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.statement()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicalNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = MyLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 76
                self.match(MyLangParser.NUMBER)
                pass
            elif token in [26]:
                localctx = MyLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(MyLangParser.STRING)
                pass
            elif token in [24]:
                localctx = MyLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(MyLangParser.ID)
                pass
            elif token in [4]:
                localctx = MyLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(MyLangParser.T__3)
                self.state = 80
                self.expr(0)
                self.state = 81
                self.match(MyLangParser.T__4)
                pass
            elif token in [16]:
                localctx = MyLangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 83
                self.match(MyLangParser.T__15)
                self.state = 84
                self.expr(2)
                pass
            elif token in [23]:
                localctx = MyLangParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(MyLangParser.T__22)
                self.state = 86
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.MulDivModContext(self, MyLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.AddSubContext(self, MyLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 93
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 94
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.CompareContext(self, MyLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 96
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 97
                        self.expr(8)
                        pass

             
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




