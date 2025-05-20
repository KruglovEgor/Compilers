# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#statement.
    def enterStatement(self, ctx:MyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#statement.
    def exitStatement(self, ctx:MyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#assignment.
    def enterAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyLangParser#assignment.
    def exitAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyLangParser#ifStatement.
    def enterIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#ifStatement.
    def exitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#whileLoop.
    def enterWhileLoop(self, ctx:MyLangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MyLangParser#whileLoop.
    def exitWhileLoop(self, ctx:MyLangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MyLangParser#printStmt.
    def enterPrintStmt(self, ctx:MyLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#printStmt.
    def exitPrintStmt(self, ctx:MyLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#inputStmt.
    def enterInputStmt(self, ctx:MyLangParser.InputStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#inputStmt.
    def exitInputStmt(self, ctx:MyLangParser.InputStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLangParser#LogicalNot.
    def enterLogicalNot(self, ctx:MyLangParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by MyLangParser#LogicalNot.
    def exitLogicalNot(self, ctx:MyLangParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by MyLangParser#MulDivMod.
    def enterMulDivMod(self, ctx:MyLangParser.MulDivModContext):
        pass

    # Exit a parse tree produced by MyLangParser#MulDivMod.
    def exitMulDivMod(self, ctx:MyLangParser.MulDivModContext):
        pass


    # Enter a parse tree produced by MyLangParser#Variable.
    def enterVariable(self, ctx:MyLangParser.VariableContext):
        pass

    # Exit a parse tree produced by MyLangParser#Variable.
    def exitVariable(self, ctx:MyLangParser.VariableContext):
        pass


    # Enter a parse tree produced by MyLangParser#Number.
    def enterNumber(self, ctx:MyLangParser.NumberContext):
        pass

    # Exit a parse tree produced by MyLangParser#Number.
    def exitNumber(self, ctx:MyLangParser.NumberContext):
        pass


    # Enter a parse tree produced by MyLangParser#AddSub.
    def enterAddSub(self, ctx:MyLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by MyLangParser#AddSub.
    def exitAddSub(self, ctx:MyLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by MyLangParser#Parens.
    def enterParens(self, ctx:MyLangParser.ParensContext):
        pass

    # Exit a parse tree produced by MyLangParser#Parens.
    def exitParens(self, ctx:MyLangParser.ParensContext):
        pass


    # Enter a parse tree produced by MyLangParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by MyLangParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by MyLangParser#Compare.
    def enterCompare(self, ctx:MyLangParser.CompareContext):
        pass

    # Exit a parse tree produced by MyLangParser#Compare.
    def exitCompare(self, ctx:MyLangParser.CompareContext):
        pass


    # Enter a parse tree produced by MyLangParser#String.
    def enterString(self, ctx:MyLangParser.StringContext):
        pass

    # Exit a parse tree produced by MyLangParser#String.
    def exitString(self, ctx:MyLangParser.StringContext):
        pass



del MyLangParser