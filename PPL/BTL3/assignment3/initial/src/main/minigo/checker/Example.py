from functools import reduce
from AST import *
from Visitor import BaseVisitor

class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [[]]  # Khởi tạo môi trường toàn cục

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast: Program, c):
        # Khởi tạo c là danh sách các danh sách nếu chưa có
        if not c:
            c = [[]]
        # Thăm từng khai báo
        for decl in ast.decl:
            symbol = self.visit(decl, c)
            c[0].append(symbol)  # Thêm symbol vào môi trường
        return c

    def visitVarDecl(self, ast: VarDecl, c):
        # Kiểm tra xem biến đã được khai báo chưa
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res:
            raise Redeclared(ast.varName)  # Ví dụ lỗi khai báo lại
        # Trả về symbol cho biến
        return Symbol(ast.varName, ast.varType)

    def visitConstDecl(self, ast: ConstDecl, c):
        # Kiểm tra logic cho hằng số
        res = self.lookup(ast.constName, c[0], lambda x: x.name)
        if res:
            raise Redeclared(ast.constName)
        return Symbol(ast.constName, ast.constType)

    def lookup(self, name, lst, func):
        for x in lst:   
            if name == func(x):
                return x
        return None