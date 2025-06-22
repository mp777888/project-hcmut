"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Union




class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.function : List[FuncDecl] = []
        self.method : List[MethodDecl] = []
        self.struct: List[StructType] = []
        self.interface: List[InterfaceType] = []
        self.global_envi = [
            [
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
            Symbol("putFloat", MType([FloatType()], VoidType())),
            Symbol("putFloatLn", MType([FloatType()], VoidType())),
            Symbol("getBool", MType([], BoolType())),
            Symbol("putBool", MType([BoolType()], VoidType())),
            Symbol("putBoolLn", MType([BoolType()], VoidType())),
            Symbol("getString", MType([], StringType())),
            Symbol("putString", MType([StringType()], VoidType())),
            Symbol("putStringLn", MType([StringType()], VoidType())),
            Symbol("putLn", MType([], VoidType()))
            ]
        ]
        self.function_current: FuncDecl = None
        self.struct_current: StructType = None
        self.param_current: List[ParamDecl] = None
        self.in_loop = False  # Flag để kiểm tra break/continue trong vòng lặp

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast, c):
        c = [[]]  # Global scope

        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.function.append(decl)
            elif isinstance(decl, StructType):
                self.struct.append(decl)
            elif isinstance(decl, InterfaceType):
                self.interface.append(decl)
            elif isinstance(decl, MethodDecl):
                self.method.append(decl)
        
        for global_decl in self.global_envi[0]:
            self.function.append(global_decl)
            c[0].append(global_decl)
        
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                self.visit(decl, c)
        
        for decl in ast.decl:
            if decl is None:
                continue

            if isinstance(decl, MethodDecl):
                continue

            if isinstance(decl, List):  # Xử lý trường hợp một khai báo trả về nhiều symbol
                for sym in decl:
                    c[0].append(self.visit(sym, c))
            else:
                symbol = self.visit(decl, c)
                if symbol:  # Chỉ thêm vào nếu không phải None
                    if isinstance(symbol, List):
                        c[0].extend(symbol)
                    else:
                        c[0].append(symbol)
        return c

    def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) -> Symbol:
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if res is not None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitVarDecl(self, ast, c):
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)
            
        # Kiểm tra trong global environment (các hàm built-in)
        res = self.lookup(ast.varName, self.global_envi[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)
        
        # Kiểm tra và xác định kiểu dữ liệu
        if ast.varInit:
            # Kiểm tra nếu varInit là Id, cần kiểm tra xem Id đã được khai báo chưa
            if isinstance(ast.varInit, Id):
                found = False
                for scope in c:
                    res = self.lookup(ast.varInit.name, scope, lambda x: x.name)
                    if res is not None:
                        found = True
                        initType = res.mtype
                        break
                if not found:
                    raise Undeclared(Identifier(), ast.varInit.name)
            else:
                initType = self.visit(ast.varInit, c)
            
            if ast.varType is None:
                ast.varType = initType
            elif not self.isTypeCompatible(initType, ast.varType):
                raise TypeMismatch(ast)

        return Symbol(ast.varName, ast.varType, None)

    def visitConstDecl(self, ast, c):
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)
            
        # Kiểm tra trong global environment (các hàm built-in)
        res = self.lookup(ast.conName, self.global_envi[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)
        
        if ast.iniExpr:
            # Kiểm tra nếu varInit là Id, cần kiểm tra xem Id đã được khai báo chưa
            if isinstance(ast.iniExpr, Id):
                found = False
                for scope in c:
                    res = self.lookup(ast.iniExpr.name, scope, lambda x: x.name)
                    if res is not None:
                        found = True
                        initType = res.mtype
                        break
                if not found:
                    raise Undeclared(Identifier(), ast.iniExpr.name)
            else:
                # Kiểm tra biểu thức khởi tạo hợp lệ
                initType = self.visit(ast.iniExpr, c)
                
            if ast.conType is None:
                ast.conType = initType
            elif not self.isTypeCompatible(initType, ast.conType):
                raise TypeMismatch(ast)
        
        return Symbol(ast.conName, ast.conType, None)

    def visitFuncDecl(self,ast, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Function(), ast.name)

        res = self.lookup(ast.name, self.global_envi[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Function(), ast.name)

        self.function.append(ast)
        param_types = [param.parType for param in ast.params]
        func_symbol = Symbol(ast.name, MType(param_types, ast.retType))

        # Lưu trữ hàm hiện tại để kiểm tra return
        prev_func = self.function_current
        self.function_current = ast
        
        # Lưu trữ tham số hiện tại để kiểm tra shadowing
        prev_params = self.param_current
        self.param_current = [Symbol(p.parName, p.parType) for p in ast.params]
        
        # Tạo môi trường cho tham số (scope riêng)
        param_env = [[]] + c
        for param in ast.params:
            param_symbol = self.visit(param, param_env[0])
            param_env[0].append(param_symbol)
        
        # Tạo môi trường cho body (scope riêng bên trong scope tham số)
        body_env = [[]] + param_env
        self.visit(ast.body, body_env)
        
        # Khôi phục trạng thái
        self.function_current = prev_func
        self.param_current = prev_params
        
        return func_symbol

    def visitMethodDecl(self, ast, c):
        # Method chỉ xem xét trùng tên trong struct mà method đó được add vào
        # Tìm struct tương ứng cho receiver
        struct_found = None
        found = False
        for struct in self.struct:
            if struct.name == ast.recType.name:
                struct_found = struct
                found = True
                break
                
        if struct_found:
            # Kiểm tra method có trùng tên với field trong struct không
            for field_name, _ in struct_found.elements:
                if field_name == ast.fun.name:
                    raise Redeclared(Method(), ast.fun.name)
                    
            # Kiểm tra method có trùng tên với method khác trong struct không
            for method in struct_found.methods:
                if method.fun.name == ast.fun.name:
                    raise Redeclared(Method(), ast.fun.name)
            struct_found.methods.append(ast)
        # if found is False:
        #     # Nếu không tìm thấy struct, báo lỗi
        #     raise Undeclared(Type(), ast.recType.name)


        # Xử lý như một function bình thường
        param_types = [param.parType for param in ast.fun.params]
        method_symbol = Symbol(ast.fun.name, MType(param_types, ast.fun.retType))
        
        # Lưu trữ hàm hiện tại để kiểm tra return
        prev_func = self.function_current
        self.function_current = ast.fun
        
        # Lưu trữ tham số hiện tại để kiểm tra shadowing
        prev_params = self.param_current
        # Thêm cả receiver vào danh sách tham số
        self.param_current = [Symbol(ast.receiver, ast.recType)] + [Symbol(p.parName, p.parType) for p in ast.fun.params]
        
        # Tạo môi trường cho receiver (scope riêng)
        receiver_env = [[]] + c
        receiver_env[0].append(Symbol(ast.receiver, ast.recType, None))
        
        # Tạo môi trường cho tham số (scope riêng bên trong scope receiver)
        param_env = [[]] + receiver_env
        for param in ast.fun.params:
            param_symbol = self.visit(param, param_env[0])
            param_env[0].append(param_symbol)
        
        # Tạo môi trường cho body (scope riêng bên trong scope tham số)
        body_env = [[]] + param_env
        self.visit(ast.fun.body, body_env)
        
        # Khôi phục trạng thái
        self.function_current = prev_func
        self.param_current = prev_params
        
        return method_symbol

    def visitStructType(self, ast: StructType, c: List[List[Symbol]]) -> Symbol:
        # Kiểm tra khai báo trùng
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Type(), ast.name)

        # Kiểm tra các trường có bị trùng không
        field_names = set()
        for field_name, field_type in ast.elements:
            if field_name in field_names:
                raise Redeclared(Field(), field_name)
            field_names.add(field_name)

        # Thêm struct vào danh sách
        self.struct.append(ast)
        
        # Lưu struct hiện tại
        prev_struct = self.struct_current
        self.struct_current = ast
        
        # TODO: Kiểm tra các phương thức
        
        # Khôi phục struct hiện tại
        self.struct_current = prev_struct
        
        return Symbol(ast.name, ast, None)

    def visitInterfaceType(self, ast: InterfaceType, c: List[List[Symbol]]) -> Symbol:
        # Kiểm tra khai báo trùng
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Type(), ast.name)
        
        # Kiểm tra các prototype có bị trùng không
        proto_names = set()
        for proto in ast.methods:
            if proto.name in proto_names:
                raise Redeclared(Prototype(), proto.name)
            proto_names.add(proto.name)
        
        # Thêm interface vào danh sách
        self.interface.append(ast)
        
        return Symbol(ast.name, ast, None)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        # Create a new scope for the block
        local_env = [[]] + c

        for stmt in ast.member:
            if isinstance(stmt, VarDecl):
                # Check for redeclaration in ALL relevant scopes
                for i, scope in enumerate(local_env):
                    if i > 1:  # Only check current scope and the immediate parent (for loop scope)
                        break
                    res = self.lookup(stmt.varName, scope, lambda x: x.name)
                    if res is not None:
                        raise Redeclared(Variable(), stmt.varName)
                
                symbol = self.visit(stmt, local_env)
                local_env[0].append(symbol)
            elif isinstance(stmt, ConstDecl):
                # Check for redeclaration in ALL relevant scopes
                for i, scope in enumerate(local_env):
                    if i > 1:  # Only check current scope and the immediate parent (for loop scope)
                        break
                    res = self.lookup(stmt.conName, scope, lambda x: x.name)
                    if res is not None:
                        raise Redeclared(Constant(), stmt.conName)
                        
                symbol = self.visit(stmt, local_env)
                local_env[0].append(symbol)
            else:
                self.visit(stmt, local_env)

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]):
        # Kiểm tra variable đã được khai báo chưa
        found = not isinstance(ast.lhs, Id)

        if not found:
            for scope in c:
                res = self.lookup(ast.lhs.name, scope, lambda x: x.name)
                if res is not None:
                    found = True
                    break

        # Kiểm tra kiểu của RHS
        rhs_type = self.visit(ast.rhs, c)


        # Kiểm tra kiểu của LHS
        if found:
            lhs_type = self.visit(ast.lhs, c)
            # Kiểm tra LHS có phải là void không
            if isinstance(lhs_type, VoidType):
                raise TypeMismatch(ast)

            # Kiểm tra tính tương thích kiểu
            if not self.isTypeCompatible(rhs_type, lhs_type):
                raise TypeMismatch(ast)


        # Nếu LHS chưa khai báo thì nó được khai báo ngầm định với kiểu của RHS
        if not found:
            # Thêm vào trong scope của block
            c[0].append(Symbol(ast.lhs.name, rhs_type, None))





    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None:
        # Kiểm tra kiểu của điều kiện
        cond_type = self.visit(ast.expr, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        
        # Duyệt phần then
        self.visit(ast.thenStmt, c)
        
        # Duyệt phần else nếu có
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        # Kiểm tra kiểu của điều kiện
        cond_type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        
        # Đánh dấu đang ở trong vòng lặp
        prev_in_loop = self.in_loop
        self.in_loop = True
        
        # Duyệt thân vòng lặp
        self.visit(ast.loop, c)
        
        # Khôi phục trạng thái
        self.in_loop = prev_in_loop

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        # Tạo môi trường cục bộ mới cho toàn bộ vòng lặp for
        loop_env = [[]] + c
        
        # Xử lý phần khởi tạo (init)
        # Nếu init là VarDecl, thêm biến vào scope của vòng lặp
        if isinstance(ast.init, VarDecl):
            symbol = self.visit(ast.init, loop_env)
            loop_env[0].append(symbol)
        else:  # Nếu init là Assign
            self.visit(ast.init, loop_env)
        
        # Kiểm tra điều kiện
        cond_type = self.visit(ast.cond, loop_env)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        
        # Kiểm tra cập nhật
        self.visit(ast.upda, loop_env)
        
        # Đánh dấu đang ở trong vòng lặp
        prev_in_loop = self.in_loop
        self.in_loop = True
        
        # Duyệt thân vòng lặp
        self.visit(ast.loop, loop_env)
        
        # Khôi phục trạng thái
        self.in_loop = prev_in_loop

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        # Kiểm tra mảng - chỉ cần kiểm tra có phải ArrayType không
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)
        
        # Tạo môi trường cục bộ mới cho vòng lặp
        local_env = [[]] + c
        # Kiểm tra idx và value đã được khai báo chưa
        idx_found = None
        value_found = None
        
        if ast.idx.name != '_':
            for scope in c:
                idx_found = self.lookup(ast.idx.name, scope, lambda x: x.name)
                if idx_found is not None:
                    break
            if idx_found is None:
                raise Undeclared(Identifier(), ast.idx.name)
        
        for scope in c:
            value_found = self.lookup(ast.value.name, scope, lambda x: x.name)
            if value_found is not None:
                break
        if value_found is None:
            raise Undeclared(Identifier(), ast.value.name)
        
        
        # Thêm biến idx và value vào môi trường cục bộ
        # idx luôn là kiểu int
        local_env[0].append(Symbol(ast.idx.name, IntType(), None))
        # value có kiểu là element type của array
        local_env[0].append(Symbol(ast.value.name, arr_type.eleType, None))
        
        # Đánh dấu đang ở trong vòng lặp
        prev_in_loop = self.in_loop
        self.in_loop = True
        
        # Duyệt thân vòng lặp
        self.visit(ast.loop, local_env)
        
        # Khôi phục trạng thái
        self.in_loop = prev_in_loop

    def visitBreak(self, ast: Break, c: List[List[Symbol]]) -> None:
        # Kiểm tra có đang ở trong vòng lặp không
        return None

    def visitContinue(self, ast: Continue, c: List[List[Symbol]]) -> None:
        # Kiểm tra có đang ở trong vòng lặp không
        return None

    def visitReturn(self, ast: Return, c: List[List[Symbol]]) -> None:
        # Kiểm tra có đang ở trong hàm không
        if not self.function_current:
            raise TypeMismatch(ast)
        
        # Lấy kiểu trả về của hàm hiện tại
        func_ret_type = self.function_current.retType
        
        # Kiểm tra return có biểu thức không
        if ast.expr:
            # Nếu hàm trả về void nhưng return có biểu thức
            if isinstance(func_ret_type, VoidType):
                raise TypeMismatch(ast)
            
            # Kiểm tra kiểu của biểu thức
            expr_type = self.visit(ast.expr, c)
            
            # Kiểm tra tính tương thích kiểu
            if not self.isTypeCompatible(expr_type, func_ret_type):
                raise TypeMismatch(ast)
        else:
            # Nếu hàm không trả về void nhưng return không có biểu thức
            if not isinstance(func_ret_type, VoidType):
                raise TypeMismatch(ast)

    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]) -> Type:
        # Lấy kiểu của toán hạng trái và phải
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        
        # Xử lý các toán tử số học
        if ast.op in ['+', '-', '*', '/', '%']:
            # Special case for string concatenation with '+'
            if ast.op == '+' and isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            
            # Các toán tử số học cần toán hạng là số
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                # Nếu một trong hai là float, kết quả là float
                if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                    return FloatType()
                # Nếu cả hai là int, kết quả là int
                else:
                    return IntType()
            else:
                raise TypeMismatch(ast)
        
        # Xử lý các toán tử so sánh
        elif ast.op in ['==', '!=', '<', '<=', '>', '>=']:
            # Toán tử == và != có thể áp dụng cho mọi kiểu dữ liệu (trừ void)
            if ast.op in ['==', '!=']:
                if (isinstance(left_type, VoidType) or isinstance(right_type, VoidType) or 
                    not self.isTypeCompatible(left_type, right_type)):
                    raise TypeMismatch(ast)
            # Các toán tử so sánh khác chỉ áp dụng cho số
            else:
                if not (isinstance(left_type, (IntType, FloatType)) and 
                        isinstance(right_type, (IntType, FloatType))):
                    raise TypeMismatch(ast)
            return BoolType()
        
        # Xử lý các toán tử logic
        elif ast.op in ['&&', '||']:
            # Các toán tử logic cần toán hạng là boolean
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)
        
        # Trường hợp không xác định
        else:
            raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]) -> Type:
        # Lấy kiểu của toán hạng
        body_type = self.visit(ast.body, c)
        
        # Xử lý toán tử phủ định logic
        if ast.op == '!':
            if isinstance(body_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)
        
        # Xử lý toán tử âm
        elif ast.op == '-':
            if isinstance(body_type, (IntType, FloatType)):
                return body_type
            else:
                raise TypeMismatch(ast)
        
        # Trường hợp không xác định
        else:
            raise TypeMismatch(ast)

    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        # Tìm hàm trong tất cả các scope của môi trường
        found = False
        res = None
        
        for scope in c:
            res = self.lookup(ast.funName, scope, lambda x: x.name)
            if res is not None:
                found = True
                break

        if not found and self.function:
            for func in self.function:
                if func.name == ast.funName:
                    param_types = [param.parType for param in func.params]
                    res = Symbol(func.name, MType(param_types, func.retType))
                    found = True
                    break

        # Nếu không tìm thấy trong các scope, kiểm tra trong môi trường toàn cục
        if not found:
            res = self.lookup(ast.funName, self.global_envi[0], lambda x: x.name)
            
        # Nếu vẫn không tìm thấy, báo lỗi
        if res is None:
            raise Undeclared(Function(), ast.funName)
        
        # Kiểm tra res có phải là hàm không
        if not isinstance(res.mtype, MType):
            raise TypeMismatch(ast)
        
        # Kiểm tra số lượng đối số
        if len(ast.args) != len(res.mtype.partype):
            raise TypeMismatch(ast)
        
        # Kiểm tra kiểu của các đối số
        for i, arg in enumerate(ast.args):
            arg_type = self.visit(arg, c)
            param_type = res.mtype.partype[i]
            
            
            # Special case for interface parameters - struct cannot be directly passed
            if isinstance(param_type, Id):
                # Check if param_type is an interface
                for interface in self.interface:
                    if interface.name == param_type.name:
                        # Direct struct types can't be passed as interfaces without explicit conversion
                        if isinstance(arg_type, StructType) or (
                            isinstance(arg_type, Id) and 
                            any(s.name == arg_type.name for s in self.struct)
                        ):
                            raise TypeMismatch(ast)
            
            if not self.isTypeCompatible(arg_type, param_type):
                raise TypeMismatch(ast)
        
        # Trả về kiểu trả về của hàm
        return res.mtype.rettype
    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        # Get receiver type
        receiver_type = self.visit(ast.receiver, c)
        

        if isinstance(receiver_type, Id):
            struct_found = False
            for struct in self.struct:
                if struct.name == receiver_type.name:
                    receiver_type = struct
                    struct_found = True
                    break
            
            if not struct_found:
                for interface in self.interface:
                    if interface.name == receiver_type.name:
                        receiver_type = interface
                        break
        

        if not isinstance(receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)
        
        # Find method in struct or interface
        method = None
        if isinstance(receiver_type, StructType):
            for method_decl in receiver_type.methods:
                if method_decl.fun.name == ast.metName:
                    method = method_decl
                    break
        else:  # Interface
            for proto in receiver_type.methods:
                if proto.name == ast.metName:
                    method = proto
                    break
    
        
        if method is None:
            raise Undeclared(Method(), ast.metName)
        
        
        
        # Kiểm tra kiểu của receiver
        # 
        if isinstance(receiver_type, InterfaceType):
            # For interface prototypes
            if len(ast.args) != len(method.params):
                raise TypeMismatch(ast)
                
            for i, arg in enumerate(ast.args):
                arg_type = self.visit(arg, c)
                if not self.isTypeCompatible(arg_type, method.params[i]):
                    raise TypeMismatch(ast)
                    
            return method.retType
        else:  # MethodDecl in struct
            if len(ast.args) != len(method.fun.params):
                raise TypeMismatch(ast)
                
            for i, arg in enumerate(ast.args):
                arg_type = self.visit(arg, c)
                param_type = method.fun.params[i].parType
                if not self.isTypeCompatible(arg_type, param_type):
                    raise TypeMismatch(ast)
                    
            return method.fun.retType

    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]) -> Type:
        # Lấy kiểu của mảng
        arr_type = self.visit(ast.arr, c)
        
        # Kiểm tra có phải là mảng không
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)
        
        # Kiểm tra số lượng chỉ số
        if len(ast.idx) != len(arr_type.dimens):
            raise TypeMismatch(ast)
        
        # Kiểm tra kiểu của các chỉ số
        for idx in ast.idx:
            idx_type = self.visit(idx, c)
            if not isinstance(idx_type, IntType):
                raise TypeMismatch(ast)
        
        # Trả về kiểu phần tử của mảng
        return arr_type.eleType

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        receiver_type = self.visit(ast.receiver, c)



        # Kiểm tra receiver có phải là struct không
        type_rec = False
        for struct in self.struct:
            if struct.name == receiver_type.name:
                type_rec = struct
                break
        if not type_rec:
            raise TypeMismatch(ast)


        # Tìm trường trong struct
        field_found = False
        for field_name, field_type in type_rec.elements:
            if field_name == ast.field:
                field_found = True
                return field_type
        
        # Không tìm thấy trường
        if not field_found:
            raise Undeclared(Field(), ast.field)

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitNilLiteral(self, ast, c):
        return VoidType()

    def visitArrayLiteral(self, ast: ArrayLiteral, c: List[List[Symbol]]) -> Type:
        # Visit each element in the array literal to determine its type
        element_types = [self.visit(element, c) for element in ast.value]

        # Ensure all elements have the same type
        if len(set(map(str, element_types))) > 1:
            raise TypeMismatch(ast)

        # Return the array type with dimensions and element type
        return ArrayType(ast.dimens, element_types[0])

    def visitStructLiteral(self, ast: StructLiteral, c: List[List[Symbol]]) -> Type:
        # Tìm struct type từ danh sách struct đã khai báo
        struct_found = None
        for struct in self.struct:
            if struct.name == ast.name:
                struct_found = struct
                break
                
        # if struct_found is None:
        #     raise Undeclared(Type(), ast.name)
            
        # Nếu struct literal rỗng, trả về type struct
        if len(ast.elements) == 0:
            return struct_found
            
        # Kiểm tra các field trong struct literal
        struct_fields = {field_name: field_type for field_name, field_type in struct_found.elements}
        
        # Lưu các field đã kiểm tra để phát hiện trùng lặp
        checked_fields = set()
        
        # Kiểm tra từng field trong struct literal
        for field_name, expr in ast.elements:
            # Kiểm tra field có tồn tại trong struct không
            if field_name not in struct_fields:
                raise Undeclared(Field(), field_name)
                
            # Kiểm tra field có bị trùng lặp không
            if field_name in checked_fields:
                raise Redeclared(Field(), field_name)
                
            # Thêm field vào danh sách đã kiểm tra
            checked_fields.add(field_name)
            
            # Kiểm tra kiểu của field
            expr_type = self.visit(expr, c)
            field_type = struct_fields[field_name]
            
            # Kiểm tra tính tương thích kiểu
            if not self.isTypeCompatible(expr_type, field_type):
                raise TypeMismatch(ast)
                
        # Trả về kiểu của struct
        return struct_found

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast, c):
        return ast
        
    def visitId(self, ast, c):
        # Tìm kiếm biến trong tất cả các phạm vi
        for scope in c:
            res = self.lookup(ast.name, scope, lambda x: x.name)
            if res is not None:
                return res.mtype
        
        # Không tìm thấy biến
        raise Undeclared(Identifier(), ast.name)
        
    # Hàm hỗ trợ kiểm tra tính tương thích của kiểu
    def isTypeCompatible(self, srcType, destType):
        if isinstance(srcType, VoidType):
            if isinstance(destType, (Id, StructType, InterfaceType, ArrayType)):
                return True
        
        if isinstance(destType, Id):
            dest_real_type = None
            for struct in self.struct:
                if struct.name == destType.name:
                    dest_real_type = struct
                    break
            if dest_real_type is None:
                for interface in self.interface:
                    if interface.name == destType.name:
                        dest_real_type = interface
                        break
            if dest_real_type is not None:
                return self.isTypeCompatible(srcType, dest_real_type)

        if isinstance(srcType, Id):
            src_real_type = None
            for struct in self.struct:
                if struct.name == srcType.name:
                    src_real_type = struct
                    break
            if src_real_type is None:
                for interface in self.interface:
                    if interface.name == srcType.name:
                        src_real_type = interface
                        break
            if src_real_type is not None:
                return self.isTypeCompatible(src_real_type, destType)
        
        # Xử lý trường hợp đặc biệt: srcType là StructLiteral và destType liên quan đến struct
        if isinstance(srcType, StructType) and srcType.name and (
            isinstance(destType, StructType) or
            (isinstance(destType, Id) and destType.name == srcType.name)
        ):
            return True

        if type(srcType) == type(destType):
            if isinstance(srcType, StructType) and isinstance(destType, StructType):
                if srcType.name == destType.name:
                    return True

                if len(srcType.elements) != len(destType.elements):
                    return False

                for i in range(len(srcType.elements)):
                    src_field_name, src_field_type = srcType.elements[i]
                    dest_field_name, dest_field_type = destType.elements[i]

                    if src_field_name != dest_field_name or not self.isTypeCompatible(src_field_type, dest_field_type):
                        return False
                return True

            return True
        
        # Int có thể gán cho Float
        if isinstance(srcType, IntType) and isinstance(destType, FloatType):
            return True
        # Kiểm tra tương thích giữa mảng
        if isinstance(srcType, ArrayType) and isinstance(destType, ArrayType):
            # Kích thước mảng phải giống nhau
            if len(srcType.dimens) != len(destType.dimens):
                return False
            
            # Kiểm tra từng kích thước
            for i in range(len(srcType.dimens)):
                if srcType.dimens[i] != destType.dimens[i]:
                    return False
            
            # Kiểm tra kiểu phần tử
            return self.isTypeCompatible(srcType.eleType, destType.eleType)
        
        # Kiểm tra struct có implements interface không
        if isinstance(srcType, StructType) and isinstance(destType, InterfaceType):
            # Kiểm tra tất cả prototype trong interface có trong struct không
            for proto in destType.methods:
                # Tìm phương thức tương ứng trong struct
                method_found = False
                for method in srcType.methods:
                    if method.fun.name == proto.name:
                        # Kiểm tra kiểu trả về
                        if not self.isTypeCompatible(method.fun.retType, proto.retType):
                            return False
                        # Kiểm tra số lượng tham số
                        if len(method.fun.params) != len(proto.params):
                            return False
                        # Kiểm tra kiểu của từng tham số
                        for i in range(len(method.fun.params)):
                            if not self.isTypeCompatible(method.fun.params[i].parType, proto.params[i]):
                                return False
                        method_found = True
                        break
                if not method_found:
                    return False
            return True
        return False