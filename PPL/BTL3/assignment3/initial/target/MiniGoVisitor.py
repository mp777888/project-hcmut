# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idlist.
    def visitIdlist(self, ctx:MiniGoParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprlist.
    def visitExprlist(self, ctx:MiniGoParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vartype.
    def visitVartype(self, ctx:MiniGoParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalartype.
    def visitScalartype(self, ctx:MiniGoParser.ScalartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraytype.
    def visitArraytype(self, ctx:MiniGoParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structtype.
    def visitStructtype(self, ctx:MiniGoParser.StructtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elements.
    def visitElements(self, ctx:MiniGoParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodbody.
    def visitMethodbody(self, ctx:MiniGoParser.MethodbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiple_newline.
    def visitMultiple_newline(self, ctx:MiniGoParser.Multiple_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#endline.
    def visitEndline(self, ctx:MiniGoParser.EndlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methoddecl.
    def visitMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#recevier.
    def visitRecevier(self, ctx:MiniGoParser.RecevierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forbasic.
    def visitForbasic(self, ctx:MiniGoParser.ForbasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstep.
    def visitForstep(self, ctx:MiniGoParser.ForstepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#foreach.
    def visitForeach(self, ctx:MiniGoParser.ForeachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forinit.
    def visitForinit(self, ctx:MiniGoParser.ForinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forcondition.
    def visitForcondition(self, ctx:MiniGoParser.ForconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forupdate.
    def visitForupdate(self, ctx:MiniGoParser.ForupdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callstmt.
    def visitCallstmt(self, ctx:MiniGoParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp1.
    def visitExp1(self, ctx:MiniGoParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp2.
    def visitExp2(self, ctx:MiniGoParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp3.
    def visitExp3(self, ctx:MiniGoParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp4.
    def visitExp4(self, ctx:MiniGoParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp5.
    def visitExp5(self, ctx:MiniGoParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp6.
    def visitExp6(self, ctx:MiniGoParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp7.
    def visitExp7(self, ctx:MiniGoParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraylit.
    def visitArraylit(self, ctx:MiniGoParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lit_list.
    def visitLit_list(self, ctx:MiniGoParser.Lit_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lit.
    def visitLit(self, ctx:MiniGoParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structlit.
    def visitStructlit(self, ctx:MiniGoParser.StructlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#astribute.
    def visitAstribute(self, ctx:MiniGoParser.AstributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcall.
    def visitFuncall(self, ctx:MiniGoParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayaccess.
    def visitArrayaccess(self, ctx:MiniGoParser.ArrayaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structaccess.
    def visitStructaccess(self, ctx:MiniGoParser.StructaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access.
    def visitAccess(self, ctx:MiniGoParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asaccess.
    def visitAsaccess(self, ctx:MiniGoParser.AsaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#intlit.
    def visitIntlit(self, ctx:MiniGoParser.IntlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#floatlit.
    def visitFloatlit(self, ctx:MiniGoParser.FloatlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stringlit.
    def visitStringlit(self, ctx:MiniGoParser.StringlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#boollit.
    def visitBoollit(self, ctx:MiniGoParser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nillit.
    def visitNillit(self, ctx:MiniGoParser.NillitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idlit.
    def visitIdlit(self, ctx:MiniGoParser.IdlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#newline.
    def visitNewline(self, ctx:MiniGoParser.NewlineContext):
        return self.visitChildren(ctx)



del MiniGoParser