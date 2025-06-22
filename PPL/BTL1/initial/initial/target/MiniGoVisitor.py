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


    # Visit a parse tree produced by MiniGoParser#decl_list.
    def visitDecl_list(self, ctx:MiniGoParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_tail.
    def visitDecl_tail(self, ctx:MiniGoParser.Decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_init.
    def visitVar_init(self, ctx:MiniGoParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_init_extra.
    def visitVar_init_extra(self, ctx:MiniGoParser.Var_init_extraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idlist.
    def visitIdlist(self, ctx:MiniGoParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_tail.
    def visitId_tail(self, ctx:MiniGoParser.Id_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprlist.
    def visitExprlist(self, ctx:MiniGoParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_tail.
    def visitExpr_tail(self, ctx:MiniGoParser.Expr_tailContext):
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


    # Visit a parse tree produced by MiniGoParser#const_init.
    def visitConst_init(self, ctx:MiniGoParser.Const_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraytype.
    def visitArraytype(self, ctx:MiniGoParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_size.
    def visitArray_size(self, ctx:MiniGoParser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type_tail.
    def visitArray_type_tail(self, ctx:MiniGoParser.Array_type_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structtype.
    def visitStructtype(self, ctx:MiniGoParser.StructtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element_list.
    def visitElement_list(self, ctx:MiniGoParser.Element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_list.
    def visitMethod_list(self, ctx:MiniGoParser.Method_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elements.
    def visitElements(self, ctx:MiniGoParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodbody.
    def visitMethodbody(self, ctx:MiniGoParser.MethodbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vartype_opt.
    def visitVartype_opt(self, ctx:MiniGoParser.Vartype_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_body.
    def visitType_body(self, ctx:MiniGoParser.Type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiple_newline.
    def visitMultiple_newline(self, ctx:MiniGoParser.Multiple_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiple_newline_tail.
    def visitMultiple_newline_tail(self, ctx:MiniGoParser.Multiple_newline_tailContext):
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


    # Visit a parse tree produced by MiniGoParser#paramlist_opt.
    def visitParamlist_opt(self, ctx:MiniGoParser.Paramlist_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#recevier.
    def visitRecevier(self, ctx:MiniGoParser.RecevierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_tail.
    def visitParam_tail(self, ctx:MiniGoParser.Param_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_param_tail.
    def visitId_param_tail(self, ctx:MiniGoParser.Id_param_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_list.
    def visitElseif_list(self, ctx:MiniGoParser.Elseif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_part.
    def visitElse_part(self, ctx:MiniGoParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forbasic.
    def visitForbasic(self, ctx:MiniGoParser.ForbasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#endline_opt.
    def visitEndline_opt(self, ctx:MiniGoParser.Endline_optContext):
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


    # Visit a parse tree produced by MiniGoParser#forinit_var.
    def visitForinit_var(self, ctx:MiniGoParser.Forinit_varContext):
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


    # Visit a parse tree produced by MiniGoParser#expr_opt.
    def visitExpr_opt(self, ctx:MiniGoParser.Expr_optContext):
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


    # Visit a parse tree produced by MiniGoParser#call_expr.
    def visitCall_expr(self, ctx:MiniGoParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_or.
    def visitExpr_or(self, ctx:MiniGoParser.Expr_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp1.
    def visitExp1(self, ctx:MiniGoParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp1_and.
    def visitExp1_and(self, ctx:MiniGoParser.Exp1_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp2.
    def visitExp2(self, ctx:MiniGoParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp2_rel.
    def visitExp2_rel(self, ctx:MiniGoParser.Exp2_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rel_op.
    def visitRel_op(self, ctx:MiniGoParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp3.
    def visitExp3(self, ctx:MiniGoParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp3_add.
    def visitExp3_add(self, ctx:MiniGoParser.Exp3_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_op.
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp4.
    def visitExp4(self, ctx:MiniGoParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp4_mul.
    def visitExp4_mul(self, ctx:MiniGoParser.Exp4_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_op.
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp5.
    def visitExp5(self, ctx:MiniGoParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_op.
    def visitUnary_op(self, ctx:MiniGoParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp6.
    def visitExp6(self, ctx:MiniGoParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exp6_access.
    def visitExp6_access(self, ctx:MiniGoParser.Exp6_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_part.
    def visitAccess_part(self, ctx:MiniGoParser.Access_partContext):
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


    # Visit a parse tree produced by MiniGoParser#lit_tail.
    def visitLit_tail(self, ctx:MiniGoParser.Lit_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lit.
    def visitLit(self, ctx:MiniGoParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lit_list_opt.
    def visitLit_list_opt(self, ctx:MiniGoParser.Lit_list_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structlit.
    def visitStructlit(self, ctx:MiniGoParser.StructlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structlit_items_opt.
    def visitStructlit_items_opt(self, ctx:MiniGoParser.Structlit_items_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structlit_items_tail.
    def visitStructlit_items_tail(self, ctx:MiniGoParser.Structlit_items_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#astribute.
    def visitAstribute(self, ctx:MiniGoParser.AstributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_receiver.
    def visitMethod_receiver(self, ctx:MiniGoParser.Method_receiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arg_list_opt.
    def visitArg_list_opt(self, ctx:MiniGoParser.Arg_list_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arg_list.
    def visitArg_list(self, ctx:MiniGoParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arg_tail.
    def visitArg_tail(self, ctx:MiniGoParser.Arg_tailContext):
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


    # Visit a parse tree produced by MiniGoParser#access_opt.
    def visitAccess_opt(self, ctx:MiniGoParser.Access_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asaccess_list.
    def visitAsaccess_list(self, ctx:MiniGoParser.Asaccess_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access.
    def visitAccess(self, ctx:MiniGoParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_tail.
    def visitAccess_tail(self, ctx:MiniGoParser.Access_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asaccess.
    def visitAsaccess(self, ctx:MiniGoParser.AsaccessContext):
        return self.visitChildren(ctx)



del MiniGoParser