from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *




class ASTGeneration(MiniGoVisitor):
    #program  : decl+ EOF ;
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])
    #decl: vardecl | constdecl | typedecl | funcdecl | methoddecl;
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        if ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        elif ctx.methoddecl():
            return self.visit(ctx.methoddecl())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl())
        elif ctx.typedecl():
            return self.visit(ctx.typedecl())
        else:
            return None


    #vartype: INT | FLOAT | STRING | BOOLEAN | arraytype | structtype ;
    def visitVartype(self, ctx: MiniGoParser.VartypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        elif ctx.structtype():
            return Id(ctx.structtype().ID().getText())
        else:
            return None

    #arraytype: (LBRACK (INTLIT | ID) RBRACK)+ vartype ;
    def visitArraytype(self, ctx: MiniGoParser.ArraytypeContext):
        dims = []
        i = 0
        while i < ctx.getChildCount():
            if ctx.getChild(i).getText() == "[":
                i += 1  # Bỏ qua '['
                if ctx.getChild(i) in ctx.INTLIT():
                    dims.append(IntLiteral(int(ctx.getChild(i).getText())))
                elif ctx.getChild(i) in ctx.ID():
                    dims.append(Id(ctx.getChild(i).getText()))
                i += 2  # Bỏ qua giá trị và ']'
            else:
                break
        eleType = self.visit(ctx.vartype())
        return ArrayType(dims, eleType)


    # methodbody: ID LPAREN paramlist? RPAREN vartype? endline;
    # chỉ lấy type đối với methodbody
    def visitParamTypes(self, ctx: MiniGoParser.ParamlistContext):
        param_types = []
        for param in ctx.param():
            ids = [id.getText() for id in param.ID()]
            # lấy kiểu của tham số
            typ = self.visit(param.vartype())
            # thêm kiểu vào danh sách, nhân lên theo số lượng ID
            param_types.extend([typ] * len(ids))
        return param_types
    def visitMethodbody(self, ctx: MiniGoParser.MethodbodyContext):
        name = ctx.ID().getText()
        params = self.visitParamTypes(ctx.paramlist()) if ctx.paramlist() else []
        retType = self.visit(ctx.vartype()) if ctx.vartype() else VoidType()
        return Prototype(name, params, retType)

    # structdecl: STRUCT LBRACE elements+ RBRACE;
    # elements: ID vartype endline;
    def visitElements(self, ctx: MiniGoParser.ElementsContext):
        #return a tuple (name, type) of each element in struct
        name = ctx.ID().getText()
        vartype = self.visit(ctx.vartype())
        return (name, vartype)

    #typedecl: TYPE ID (structdecl | interfacedecl) endline;
    def visitTypedecl(self, ctx: MiniGoParser.TypedeclContext):
        name = ctx.ID().getText()
        if ctx.interfacedecl():
            methods = [self.visitMethodbody(method) for method in ctx.interfacedecl().methodbody()]
            return InterfaceType(name, methods)
        elif ctx.structdecl():
            elements = [self.visit(element) for element in ctx.structdecl().elements()]
            methods = []
            return StructType(name,elements,methods)



    #vardecl: (VAR idlist (vartype (EQUAL exprlist)? | EQUAL exprlist) endline) ;
    def visitVardecl(self, ctx: MiniGoParser.VardeclContext):
        id_list = [id.getText() for id in ctx.idlist().ID()]
        varType = self.visit(ctx.vartype()) if ctx.vartype() else None
        varInit = self.visit(ctx.exprlist()) if ctx.exprlist() else None

        if varInit is None: return VarDecl(id_list[0], varType, None)
        return [VarDecl(varName=id, varType=varType, varInit=varInit) for id,expr in zip(id_list,varInit)] if len(id_list) > 1 else VarDecl(id_list[0], varType, varInit[0])

    #constdecl: CONST idlist vartype? EQUAL exprlist endline;
    def visitConstdecl(self, ctx: MiniGoParser.ConstdeclContext):
        id_list = [id.getText() for id in ctx.idlist().ID()]
        conType = self.visit(ctx.vartype()) if ctx.vartype() else None
        iniExpr = self.visit(ctx.exprlist())
        return [ConstDecl(conName = id,conType = conType,iniExpr = expr) for id, expr in zip(id_list, iniExpr)] if len(id_list) > 1 else ConstDecl(id_list[0], conType, iniExpr[0])

    #funcdecl: FUNC ID LPAREN paramlist? RPAREN  vartype? block endline;
    def visitFuncdecl(self, ctx: MiniGoParser.FuncdeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.paramlist()) if ctx.paramlist() else []
        retType = self.visit(ctx.vartype()) if ctx.vartype() else VoidType()
        body = self.visit(ctx.block())
        return FuncDecl(name, params, retType, body)


    #methoddecl: FUNC recevier ID LPAREN paramlist? RPAREN vartype? block endline;
    #recevier: LPAREN ID ID RPAREN;
    def visitRecevier(self, ctx: MiniGoParser.RecevierContext):
        return ctx.ID(0).getText()

    def visitMethoddecl(self, ctx: MiniGoParser.MethoddeclContext):
        receiver = self.visit(ctx.recevier())
        recType = Id(ctx.recevier().ID(1).getText())
        name = ctx.ID().getText()
        params = self.visit(ctx.paramlist()) if ctx.paramlist() else []
        varType = self.visit(ctx.vartype()) if ctx.vartype() else VoidType()
        body = self.visit(ctx.block())
        return MethodDecl(receiver,recType,FuncDecl(name,params,varType,body))

    #paramlist: param (COMMA param)*;
    def visitParamlist(self, ctx: MiniGoParser.ParamlistContext):
        params = []
        for p in ctx.param():
            result = self.visit(p)
            if isinstance(result, list):
                params.extend(result)
            else:
                params.append(result)
        return params

    #param: ID (COMMA ID)* vartype;
    def visitParam(self, ctx: MiniGoParser.ParamContext):
        ids = ctx.ID()  #danh sách các token ID
        typ = self.visit(ctx.vartype())

        return [ParamDecl(id.getText(), typ) for id in ids]

    # block: LBRACE stmt* RBRACE;
    def visitBlock(self, ctx: MiniGoParser.BlockContext):
        stmts = [self.visit(stmt) for stmt in ctx.stmt()]
        # Lọc bỏ các phần tử None
        stmts = [s for s in stmts if s is not None]
        return Block(stmts)

    # returnstmt: RETURN expr? endline ;
    def visitReturnstmt(self, ctx: MiniGoParser.ReturnstmtContext):
        return Return(self.visit(ctx.expr())) if ctx.expr() else Return(None)

    # breakstmt: BREAK endline ;
    def visitBreakstmt(self, ctx: MiniGoParser.BreakstmtContext):
        return Break()

    # continuestmt: CONTINUE endline ;
    def visitContinuestmt(self, ctx: MiniGoParser.ContinuestmtContext):
        return Continue()

    #arrayaccess: ID access ; access: (LBRACK expr RBRACK)+;
    def visitArrayaccess(self, ctx: MiniGoParser.ArrayaccessContext):
        name = ctx.ID().getText()
        access = [self.visit(expr) for expr in ctx.access().expr()]
        return ArrayCell(Id(name), access)

    # structaccess: ID access? (asaccess)+ ;
    # access: (LBRACK expr RBRACK)+;
    # asaccess: DOT ID access?;
    def visitStructaccess(self, ctx: MiniGoParser.StructaccessContext):
        receiver = Id(ctx.ID().getText())

        # Xử lý access đầu tiên (nếu có) sau ID
        if ctx.access():
            receiver = ArrayCell(receiver, [self.visit(expr) for expr in ctx.access().expr()])

        # Xử lý từng asaccess từ trái sang phải
        for i in range(len(ctx.asaccess())):
            # Nếu asaccess có access (array access)
            if ctx.asaccess(i).access():
                receiver = FieldAccess(receiver, ctx.asaccess(i).ID().getText())
                receiver = ArrayCell(receiver, [self.visit(expr) for expr in ctx.asaccess(i).access().expr()])
            else:
                # Chỉ có field access
                receiver = FieldAccess(receiver, ctx.asaccess(i).ID().getText())

        return receiver

    # assignstmt: (ID | arrayaccess | structaccess) (ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr endline;
    def visitAssignstmt(self, ctx: MiniGoParser.AssignstmtContext):
        lhs = None
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        elif ctx.arrayaccess():
            lhs = self.visit(ctx.arrayaccess())
        elif ctx.structaccess():
            lhs = self.visit(ctx.structaccess())

        op = ctx.getChild(1).getText()
        rhs = self.visit(ctx.expr())
        if op in ['+=', '-=', '*=', '/=', '%=']:
            rhs = BinaryOp(op[:-1], lhs, rhs)
        return Assign(lhs, rhs)

    # ifstmt: IF LPAREN expr RPAREN block multiple_newline?
    # (ELSEIF LPAREN expr RPAREN block )* multiple_newline?
    # (ELSE block)? ;
    def visitIfstmt(self, ctx: MiniGoParser.IfstmtContext):
        expr = self.visit(ctx.expr(0))
        thenStmt = self.visit(ctx.block(0))
        elseStmt = None
        if ctx.ELSE():
            elseStmt = self.visit(ctx.block(len(ctx.block()) - 1)) # nếu có else thì gán else cuối cùng
        for i in range(len(ctx.ELSEIF()) - 1, -1, -1):
            elseif_expr = self.visit(ctx.expr(i + 1))
            elseif_block = self.visit(ctx.block(i + 1))
            elseStmt = If(elseif_expr, elseif_block, elseStmt) # gán elseStmt ngược cho thằng trước nó
        return If(expr, thenStmt, elseStmt)

    # forstmt: forbasic | forstep | foreach;
    # forbasic: FOR forcondition block;
    # forstep: FOR forinit SEMI forcondition SEMI forupdate block;
    # foreach: FOR ID COMMA ID ASSIGN RANGE expr block;
    # forinit: ID (ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr
    #       | (VAR ID vartype? EQUAL expr) ;
    # forcondition: expr ;
    # forupdate: ID (ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr;
    def visitForinit(self, ctx: MiniGoParser.ForinitContext):
        if ctx.VAR():
            lhs = ctx.ID().getText()
            varType = self.visit(ctx.vartype()) if ctx.vartype() else None
            rhs = self.visit(ctx.expr())
            return VarDecl(lhs, varType, rhs)
        else:
            lhs = Id(ctx.ID().getText())
            op = ctx.getChild(1).getText()
            rhs = self.visit(ctx.expr())
            if op in ['+=', '-=', '*=', '/=', '%=']:
                rhs = BinaryOp(op[:-1], lhs, rhs)
            return Assign(lhs, rhs)

    def visitForupdate(self, ctx: MiniGoParser.ForupdateContext):
        lhs = Id(ctx.ID().getText())
        op = ctx.getChild(1).getText()
        rhs = self.visit(ctx.expr())
        if op in ['+=', '-=', '*=', '/=', '%=']:
            rhs = BinaryOp(op[:-1], lhs, rhs)  # Adjust the operator for compound assignments
        return Assign(lhs, rhs)

    def visitForstmt(self, ctx: MiniGoParser.ForstmtContext):
        return self.visit(ctx.getChild(0))

    def visitForbasic(self, ctx: MiniGoParser.ForbasicContext):
        cond = self.visit(ctx.forcondition())
        loop = self.visit(ctx.block())
        return ForBasic(cond, loop)

    def visitForstep(self, ctx: MiniGoParser.ForstepContext):
        init = self.visit(ctx.forinit())
        cond = self.visit(ctx.forcondition().expr())
        upda = self.visit(ctx.forupdate())
        loop = self.visit(ctx.block())
        return ForStep(init,cond,upda,loop)

    def visitForeach(self, ctx: MiniGoParser.ForeachContext):
        idx = Id(ctx.ID(0).getText())
        value = Id(ctx.ID(1).getText())
        arr = self.visit(ctx.expr())
        loop = self.visit(ctx.block())
        return ForEach(idx,value,arr,loop)

    # callstmt: (methodcall | funcall) endline ;
    def visitCallstmt(self, ctx: MiniGoParser.CallstmtContext):
        return self.visit(ctx.getChild(0))
    # funcall: ID LPAREN (expr (COMMA expr)*)? RPAREN ;
    def visitFuncall(self, ctx: MiniGoParser.FuncallContext):
        name = ctx.ID().getText()
        args = [self.visit(expr) for expr in ctx.expr()] if ctx.expr() else []
        return FuncCall(name, args)
    # methodcall: (ID | arrayaccess | structaccess ) DOT ID LPAREN (expr (COMMA expr)*)? RPAREN ;
    def visitMethodcall(self, ctx: MiniGoParser.MethodcallContext):
        receiver = self.visit(ctx.getChild(0)) if ctx.arrayaccess() or ctx.structaccess() else Id(ctx.getChild(0).getText())
        metName = ctx.getChild(2).getText()
        args = [self.visit(expr) for expr in ctx.expr()] if ctx.expr() else []
        return MethCall(receiver, metName, args)


    # NEWLINE: ('\r'? '\n'){
    # if self.InsertSemi():
    #     self.text = ';'
    # else:
    #     self.skip()
    # };
    def visitNewline(self, ctx: MiniGoParser.NewlineContext):
        return None
    # endline: SEMI | NEWLINE;
    def visitEndline(self, ctx: MiniGoParser.EndlineContext):
        return None
    # multiple_newline: NEWLINE multiple_newline| NEWLINE;
    def visitMultiple_newline(self, ctx: MiniGoParser.Multiple_newlineContext):
        return None

    # exprlist: expr (COMMA expr)*;
    def visitExprlist(self, ctx: MiniGoParser.ExprlistContext):
        return [self.visit(expr) for expr in ctx.expr()]

    # expr: exp1 ( OR exp1 )*
    def visitExpr(self, ctx: MiniGoParser.ExprContext):
        if ctx.OR():
            left = self.visit(ctx.exp1(0))
            for i in range(1, len(ctx.exp1())):
                right = self.visit(ctx.exp1(i))
                left = BinaryOp("||", left, right)
            return left
        return self.visit(ctx.exp1(0))

    # exp1: exp2 ( AND exp2 )*
    def visitExp1(self, ctx: MiniGoParser.Exp1Context):
        if ctx.AND():
            left = self.visit(ctx.exp2(0))
            for i in range(1, len(ctx.exp2())):
                right = self.visit(ctx.exp2(i))
                left = BinaryOp("&&", left, right)
            return left
        return self.visit(ctx.exp2(0))

    # exp2: exp3 ( (EQ | NEQ | LT | LTE | GT | GTE) exp3 )*
    def visitExp2(self, ctx: MiniGoParser.Exp2Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp3(0))
            for i in range(1, len(ctx.exp3())):
                op = ctx.getChild(2 * i - 1).getText()
                right = self.visit(ctx.exp3(i))
                left = BinaryOp(op, left, right)
            return left
        return self.visit(ctx.exp3(0))

    # exp3: exp4 ( (PLUS | MINUS) exp4 )*
    def visitExp3(self, ctx: MiniGoParser.Exp3Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp4(0))
            for i in range(1, len(ctx.exp4())):
                op = ctx.getChild(2 * i - 1).getText()
                right = self.visit(ctx.exp4(i))
                left = BinaryOp(op, left, right)
            return left
        return self.visit(ctx.exp4(0))

    # exp4: exp5 ( (MULT | DIV | MOD) exp5 )*
    def visitExp4(self, ctx: MiniGoParser.Exp4Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp5(0))
            for i in range(1, len(ctx.exp5())):
                op = ctx.getChild(2 * i - 1).getText()
                right = self.visit(ctx.exp5(i))
                left = BinaryOp(op, left, right)
            return left
        return self.visit(ctx.exp5(0))

    # exp5: (NOT | MINUS) exp5
    def visitExp5(self, ctx: MiniGoParser.Exp5Context):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp5())
            return UnaryOp(op, body)
        return self.visit(ctx.exp6())

    # exp6: exp7 ( (DOT exp7) | (LBRACK expr RBRACK) )* ;
    def visitExp6(self, ctx: MiniGoParser.Exp6Context):
        left = self.visit(ctx.exp7(0))
        indices = []
        exp7_index = 1

        i = 1
        while i < ctx.getChildCount():
            operator = ctx.getChild(i).getText()
            if operator == ".":
                if indices:
                    left = ArrayCell(left, indices)
                    indices = []
                if exp7_index < len(ctx.exp7()):
                    right = self.visit(ctx.exp7(exp7_index))
                    exp7_index += 1
                    if isinstance(right, Id):
                        left = FieldAccess(left, right.name)
                    elif isinstance(right, FuncCall):
                        left = MethCall(left, right.funName, right.args)
                    i += 2  # bỏ qua '.' và exp7
                else:
                    break

            elif operator == "[":
                index = self.visit(ctx.getChild(i + 1))
                indices.append(index)
                i += 3  # bỏ qua '[' , expr và ']'
            else:
                break

        if indices:
            left = ArrayCell(left, indices)

        return left


    # exp7: LPAREN expr RPAREN | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | NILLIT | ID | methodcall | funcall| arraylit| structlit ;
    def visitExp7(self, ctx: MiniGoParser.Exp7Context):
        if ctx.LPAREN():  # (expr)
            return self.visit(ctx.expr())
        elif ctx.INTLIT():
            text = ctx.INTLIT().getText()
            # if text.startswith("0b") or text.startswith("0B"):
            #     return IntLiteral(int(text[2:], 2))  # Binary
            # elif text.startswith("0o") or text.startswith("0O"):
            #     return IntLiteral(int(text[2:], 8))  # Octal
            # elif text.startswith("0x") or text.startswith("0X"):
            #     return IntLiteral(int(text[2:], 16))  # Hexadecimal
            if (text.startswith("0b") or text.startswith("0B") or text.startswith("0o")
                    or text.startswith("0O") or text.startswith("0x") or text.startswith("0X")):
                return IntLiteral(text)
            else:
                return IntLiteral(int(text))  # Decimal
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            text = ctx.STRINGLIT().getText()
            return StringLiteral(text)
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.NILLIT():
            return NilLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0))


    # intlit: INTLIT;
    def visitIntlit(self, ctx: MiniGoParser.IntlitContext):
        text = ctx.INTLIT().getText()
        if text.startswith("0b") or text.startswith("0B"):
            return IntLiteral(int(text[2:], 2))  # Binary
        elif text.startswith("0o") or text.startswith("0O"):
            return IntLiteral(int(text[2:], 8))  # Octal
        elif text.startswith("0x") or text.startswith("0X"):
            return IntLiteral(int(text[2:], 16))  # Hexadecimal
        else:
            return IntLiteral(int(text))  # Decimal

    # floatlit: FLOATLIT;
    def visitFloatlit(self, ctx: MiniGoParser.FloatlitContext):
        return FloatLiteral(float(ctx.FLOATLIT().getText()))

    # stringlit: STRINGLIT;
    def visitStringlit(self, ctx: MiniGoParser.StringlitContext):
        return StringLiteral(ctx.STRINGLIT().getText())

    # boollit: BOOLLIT;
    def visitBoollit(self, ctx: MiniGoParser.BoollitContext):
        return BooleanLiteral(ctx.BOOLLIT().getText().lower() == 'true')

    # arraylit: arraytype LBRACE lit_list RBRACE;
    # lit_list: lit (COMMA lit)*;
    # lit: LBRACE lit_list? RBRACE | ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | NILLIT | structlit;
    def visitLit(self, ctx: MiniGoParser.LitContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText().lower() == 'true')
        elif ctx.NILLIT():
            return NilLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.structlit():
            return self.visit(ctx.structlit())
        elif ctx.lit_list():  # Trường hợp giá trị mảng lồng nhau
            return [self.visit(lit) for lit in ctx.lit_list().lit()]
        else:
            return None
    def visitArraylit(self, ctx: MiniGoParser.ArraylitContext):
        dimens = []
        if ctx.arraytype().INTLIT():
            for token in ctx.arraytype().INTLIT():
                dimens.append(IntLiteral(int(token.getText())))
        if ctx.arraytype().ID():
            for token in ctx.arraytype().ID():
                dimens.append(Id(token.getText()))
        eleType = self.visit(ctx.arraytype().vartype())
        value = [self.visit(lit) for lit in ctx.lit_list().lit()]
        return ArrayLiteral(dimens,eleType,value)



    # structlit: ID LBRACE (astribute expr (COMMA astribute expr)*)? RBRACE ;
    # astribute: ID COLON;
    def visitStructlit(self, ctx: MiniGoParser.StructlitContext):
        name = ctx.ID().getText()
        elements = []
        if ctx.astribute():
            attributes = ctx.astribute()
            expressions = ctx.expr()

            for attr, expr in zip(attributes, expressions):
                attr_name = attr.ID().getText()  # Lấy tên thuộc tính
                value = self.visit(expr)         # Lấy giá trị
                elements.append((attr_name, value))

        return StructLiteral(name, elements)

    # id: ID;
    def visitId(self, ctx: MiniGoParser.IdlitContext):
        return Id(ctx.ID().getText())