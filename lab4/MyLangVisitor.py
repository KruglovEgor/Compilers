# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#statement.
    def visitStatement(self, ctx:MyLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignment.
    def visitAssignment(self, ctx:MyLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ifStatement.
    def visitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileLoop.
    def visitWhileLoop(self, ctx:MyLangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#printStmt.
    def visitPrintStmt(self, ctx:MyLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#inputStmt.
    def visitInputStmt(self, ctx:MyLangParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#LogicalNot.
    def visitLogicalNot(self, ctx:MyLangParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#MulDivMod.
    def visitMulDivMod(self, ctx:MyLangParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#Variable.
    def visitVariable(self, ctx:MyLangParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#Number.
    def visitNumber(self, ctx:MyLangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AddSub.
    def visitAddSub(self, ctx:MyLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#Parens.
    def visitParens(self, ctx:MyLangParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#Compare.
    def visitCompare(self, ctx:MyLangParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#String.
    def visitString(self, ctx:MyLangParser.StringContext):
        return self.visitChildren(ctx)



del MyLangParser