import unittest
from TestUtils import TestAST
from AST import *




class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """func main() {};"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),300))

    def test_2(self):
        input = """var x int ;"""
        expect = Program([VarDecl("x",IntType(),None)])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),301))

    def test_3(self):
        input = """func main () {}; var x int ;"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),302))

    def test_4(self):
        input = """const year = 0x3456ABCE; """
        expect = Program([ConstDecl("year", None, IntLiteral("0x3456ABCE"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))

    def test_5(self):
        input = """const b = 0b11; """
        expect = Program([ConstDecl("b", None, IntLiteral("0b11"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 304))

    def test_6(self):
        input = """const hexa = 0Xa1; """
        expect = Program([ConstDecl("hexa", None, IntLiteral("0Xa1"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 305))

    def test_7(self):
        input = """const realnum = 05.e-1; """
        expect = Program([ConstDecl("realnum", None, FloatLiteral(0.5))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 306))

    def test_8(self):
        input = """const hcmut = true; """
        expect = Program([ConstDecl("hcmut", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 307))

    def test_9(self):
        input = """const arrlit = [ID] int {3.5}; """
        expect = Program([ConstDecl("arrlit", None, ArrayLiteral([Id("ID")],IntType(),[FloatLiteral(3.5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 308))

    def test_10(self):
        input = """const hcmut = (2024 + 2025) * 2; """
        expect = Program([ConstDecl("hcmut", None, BinaryOp("*", BinaryOp("+", IntLiteral(2024), IntLiteral(2025)), IntLiteral(2)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 309))


    def test_11(self):
        input = """var num int = a.b.c; """
        expect = Program([VarDecl("num", IntType(), FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 310))

    def test_12(self):
        input = """var num int = a.b().c(); """
        expect = Program([VarDecl("num", IntType(), MethCall(MethCall(Id("a"),"b",[]),"c",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 311))

    def test_13(self):
        input = """var num = a.b[1].c.d(); """
        expect = Program([VarDecl("num", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(1)]),"c"),"d",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 312))

    def test_14(self):
        input = """var num = a.b.c[2].d(); """
        expect = Program([VarDecl("num", None, MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"), "b"), "c"), [IntLiteral(2)]), "d", []))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 313))

    def test_15(self):
        input = """
            type ID struct {
                a int;
                b float;
                c string;
            }
        """
        expect = Program([StructType("ID",[
            ("a",IntType()),
            ("b",FloatType()),
            ("c",StringType())],[])
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 314))

    def test_16(self):
        input = """
            func foo () {}
            func foo () int {}
            func foo () float{}
        """
        expect = Program([FuncDecl("foo",[],VoidType(),Block([])),
                          FuncDecl("foo",[],IntType(),Block([])),
                          FuncDecl("foo",[],FloatType(),Block([]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 315))

    def test_17(self):
        input = """
            func foo () {var a int;}
            func foo () int {var b float;}
            func foo () float {var c string;}
        """
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),None)])),
                          FuncDecl("foo",[],IntType(),Block([VarDecl("b",FloatType(),None)])),
                          FuncDecl("foo",[],FloatType(),Block([VarDecl("c",StringType(),None)]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 316))


    def test_18(self):
        input = """
            func foo (x int) {var a int;}
            func foo (y float) int {var b float;}
            func foo (z string) float {var c string;}
        """
        expect = Program([FuncDecl("foo",[ParamDecl("x",IntType())],VoidType(),Block([VarDecl("a",IntType(),None)])),
                          FuncDecl("foo",[ParamDecl("y",FloatType())],IntType(),Block([VarDecl("b",FloatType(),None)])),
                          FuncDecl("foo",[ParamDecl("z",StringType())],FloatType(),Block([VarDecl("c",StringType(),None)]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 317))

    def test_19(self):
        input = """
            func foo (x,x1 int) {var a int;}
            func foo (y,y1 float) int {var b float;}
            func foo (z,z1 string) float {var c string;}
        """
        expect = Program([
            FuncDecl("foo", [ParamDecl("x", IntType()), ParamDecl("x1", IntType())], VoidType(), Block([VarDecl("a", IntType(), None)])),
            FuncDecl("foo", [ParamDecl("y", FloatType()), ParamDecl("y1", FloatType())], IntType(), Block([VarDecl("b", FloatType(), None)])),
            FuncDecl("foo", [ParamDecl("z", StringType()), ParamDecl("z1", StringType())], FloatType(), Block([VarDecl("c", StringType(), None)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 318))

    def test_20(self):
        input = """
        type INTERFACE interface {
            foo();
        }
        """
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType())
            ])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 319))

    def test_21(self):
        input = """
        type INTERFACE interface {
            foo();
            foo(a int);
            foo(b float) int;
            foo(c string) float;   
        }
        """
        expect = Program([
            InterfaceType("INTERFACE", [
                Prototype("foo", [], VoidType()),
                Prototype("foo", [IntType()], VoidType()),
                Prototype("foo", [FloatType()], IntType()),
                Prototype("foo", [StringType()], FloatType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 320))

    def test_22(self):
        input = """
        type Calculator interface {                 
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()             
                SayHello(name string);            
            }
        """
        expect = Program([
                InterfaceType("Calculator", [
                Prototype("Add", [IntType(), IntType()], IntType()),
                Prototype("Subtract", [FloatType(), FloatType(), IntType()], ArrayType([IntLiteral(3)], Id("ID"))),
                Prototype("Reset", [], VoidType()),
                Prototype("SayHello", [StringType()], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 321))


    def test_23(self):
        input = """
    func (Calculator c) Add(x, y int) int {
        return x + y;
    } 
"""
        expect = Program([MethodDecl("Calculator", Id("c"), FuncDecl("Add",[ParamDecl("x",IntType()),ParamDecl("y", IntType())], IntType(), Block([
                Return(BinaryOp("+", Id("x"), Id("y")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 322))

    def test_24(self):
        input = """
    func (Calculator c) Add(x, y int) int {
        return x + y;
    }
    func (Calculator c) Subtract(a, b float, c int) [3]ID {
        return ;
    } 
"""
        expect = Program([
            MethodDecl("Calculator", Id("c"), FuncDecl("Add", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], IntType(), Block([
                Return(BinaryOp("+", Id("x"), Id("y")))
            ]))),
            MethodDecl("Calculator", Id("c"), FuncDecl("Subtract", [ParamDecl("a", FloatType()), ParamDecl("b", FloatType()), ParamDecl("c", IntType())], ArrayType([IntLiteral(3)], Id("ID")), Block([
                Return(None)
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 323))


    def test_25(self):
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 324))


    def test_26(self):
        input = """
        func foo () {
            if (a){
                return;
            } else{
                return;
            }   
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), Block([Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 325))

    def test_27(self):
        input = """
        func foo () {
            if (a){
                return;
            }else if(b){
                return;
            }else if(c){
                return;
            }else{
                return;
            }   
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                If(Id("a"), Block([Return(None)]),
                   If(Id("b"), Block([Return(None)]),
                      If(Id("c"), Block([Return(None)]),
                         Block([Return(None)]))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 326))

    def test_28(self):
        input = """
        func foo () {
            if (a == 1){
                return 1;
            }else if(b == 5){
                return 5;
            }else if(c == 10){
                return 10;
            }else{
                return 0;
            }   
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                If(BinaryOp("==", Id("a"), IntLiteral(1)), Block([Return(IntLiteral(1))]),
                   If(BinaryOp("==", Id("b"), IntLiteral(5)), Block([Return(IntLiteral(5))]),
                      If(BinaryOp("==", Id("c"), IntLiteral(10)), Block([Return(IntLiteral(10))]),
                         Block([Return(IntLiteral(0))])))
                   )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 327))

    def test_29(self):
        input = """
        func foo () {
            if (a == 1){
                if (x) {return;}  
                return 1;
            }else if(b == 5){
                if(y) {return;} 
                return 5;
            }else if(c == 10){
                if(z) {return;} 
                return 10;
            }else{
                return 0;
            }   
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                If(BinaryOp("==", Id("a"), IntLiteral(1)), Block([
                    If(Id("x"), Block([Return(None)]), None),
                    Return(IntLiteral(1))
                ]),
                   If(BinaryOp("==", Id("b"), IntLiteral(5)), Block([
                       If(Id("y"), Block([Return(None)]), None),
                       Return(IntLiteral(5))
                   ]),
                      If(BinaryOp("==", Id("c"), IntLiteral(10)), Block([
                          If(Id("z"), Block([Return(None)]), None),
                          Return(IntLiteral(10))
                      ]),
                         Block([Return(IntLiteral(0))])))
                   )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 328))


    def test_30(self):
        input = """
        func foo () {
            if (a == 1){
                if (x) {
                    return;
                }else{
                    if(y){
                        return;
                    } 
                }    
                return 1;
            }
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                If(BinaryOp("==", Id("a"), IntLiteral(1)), Block([
                    If(Id("x"), Block([Return(None)]), Block([
                        If(Id("y"), Block([Return(None)]), None)
                    ])),
                    Return(IntLiteral(1))
                ]), None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 329))

    def test_31(self):
        input = """
        func foo () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),
            ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))


    def test_32(self):
        input = """
        func foo () {
            for var a = 5; a < 10; a += 1 {return;}
            for a := 1; a < 10; a += 1 {return;}
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                ForStep(VarDecl("a", None, IntLiteral(5)), BinaryOp("<", Id("a"), IntLiteral(10)), Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))), Block([Return(None)])),
                ForStep(Assign(Id("a"), IntLiteral(1)), BinaryOp("<", Id("a"), IntLiteral(10)), Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))), Block([Return(None)]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))


    def test_33(self):
        input = """
        func foo () {
            arr := [3]int{10, 20, 30}
            for index, value := range arr {
            // index: 0, 1, 2
            // value: 10, 20, 30
            }
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                Assign(Id("arr"), ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(10), IntLiteral(20), IntLiteral(30)])),
                ForEach(Id("index"), Id("value"), Id("arr"), Block([]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 332))


    def test_34(self):
        input = """
        func foo () {
            arr := [3]int{10, 20, 30}
            for _, value := range arr {
            // value: 10, 20, 30
            }
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                Assign(Id("arr"), ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(10), IntLiteral(20), IntLiteral(30)])),
                ForEach(Id("_"), Id("value"), Id("arr"), Block([]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 333))

    def test_35(self):
        input = """
        func foo () {
            for i < 10 {
            // loop body
            }
        }
"""
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)), Block([]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))

    def test_36(self):
        input = """
        func foo () {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 335))

    def test_37(self):
        input = """
        func foo () {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 336))

    def test_38(self):
        input = """
        func foo () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))


    def test_39(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
                          FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))


    def test_40(self):
        input = """
            type Hello struct {
                a int;
                b float;
                c string;  
            }
"""
        expect = Program([StructType("Hello",[
            ("a",IntType()),("b",FloatType()),("c",StringType())],[]
                                     )])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339))

    def test_41(self):
        input = """
        type Point struct {
            x float;
            y float;
        }
"""
        expect = Program([StructType("Point", [
            ("x", FloatType()), ("y", FloatType())], [])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))

    def test_42(self):
        input = """
        type Person struct {
            name string;
            age int;
            active boolean;
        }
"""
        expect = Program([StructType("Person", [("name", StringType()), ("age", IntType()), ("active", BoolType())], [])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))

    def test_43(self):
        input = """
        type Rectangle struct {
            width int;
            height int;
        }
"""
        expect = Program([StructType("Rectangle", [("width", IntType()), ("height", IntType())], [])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))

    def test_44(self):
        input = """
        type Config struct {
            id int;
            enabled boolean;
            path string;
            version float;
        }
"""
        expect = Program([StructType("Config", [("id", IntType()), ("enabled", BoolType()), ("path", StringType()), ("version", FloatType())], [])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))

    def test_45(self):
        input = """
        type Node struct {
            value string;
        }
"""
        expect = Program([StructType("Node", [("value", StringType())], [])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))

    def test_46(self):
        input = """
            type Hello interface {
                Add(x, y int) int;
            }
"""
        expect = Program([InterfaceType("Hello",[Prototype("Add",[IntType(),IntType()],IntType())])
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))

    def test_47(self):
        input = """
        type Math interface {
            Multiply(a, b float) float;
        }
"""
        expect = Program([InterfaceType("Math", [Prototype("Multiply", [FloatType(), FloatType()], FloatType())])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))

    def test_48(self):
        input = """
        type Printer interface {
            Print(message string);
        }
"""
        expect = Program([InterfaceType("Printer", [Prototype("Print", [StringType()], VoidType())])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))

    def test_49(self):
        input = """
        type Counter interface {
            Increment() int;
            Reset();
        }
"""
        expect = Program([InterfaceType("Counter", [Prototype("Increment", [], IntType()), Prototype("Reset", [], VoidType())])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 348))

    def test_50(self):
        input = """
        type Shape interface {
            Area() float;
            Perimeter() float;
        }
"""
        expect = Program([InterfaceType("Shape", [Prototype("Area", [], FloatType()), Prototype("Perimeter", [], FloatType())])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 349))

    def test_51(self):
        input = """
        type Logger interface {
            Log(level int, msg string) boolean;
        }
"""
        expect = Program([InterfaceType("Logger", [Prototype("Log", [IntType(), StringType()], BoolType())])])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 350))

    def test_52(self):
        input = """
            func foo() {
                a += 1;
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 351))

    def test_53(self):
        input = """
        func bar() {
            x -= 2;
        }
"""
        expect = Program([FuncDecl("bar", [], VoidType(), Block([Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 352))

    def test_54(self):
        input = """
        func baz() {
            count *= 3;
        }
"""
        expect = Program([FuncDecl("baz", [], VoidType(), Block([Assign(Id("count"), BinaryOp("*", Id("count"), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 353))

    def test_55(self):
        input = """
        func qux() {
            value /= 4;
        }
"""
        expect = Program([FuncDecl("qux", [], VoidType(), Block([Assign(Id("value"), BinaryOp("/", Id("value"), IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 354))

    def test_56(self):
        input = """
        func zap() {
            total += 5;
        }
"""
        expect = Program([FuncDecl("zap", [], VoidType(), Block([Assign(Id("total"), BinaryOp("+", Id("total"), IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 355))

    def test_57(self):
        input = """
        func fizz() {
            num %= 6;
        }
"""
        expect = Program([FuncDecl("fizz", [], VoidType(), Block([Assign(Id("num"), BinaryOp("%", Id("num"), IntLiteral(6)))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 356))

    def test_58(self):
        input = """
            func foo() {
                foo(1, 2);
                a[2].foo(1,3);
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 357))

    def test_59(self):
        input = """
        func bar() {
            bar(5);
            x[0].bar(2);
        }
"""
        expect = Program([FuncDecl("bar", [], VoidType(), Block([FuncCall("bar", [IntLiteral(5)]), MethCall(ArrayCell(Id("x"), [IntLiteral(0)]), "bar", [IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 358))

    def test_60(self):
        input = """
        func baz() {
            baz("hello");
            data[1].baz(3, 4);
        }
"""
        expect = Program([FuncDecl("baz", [], VoidType(), Block([FuncCall("baz", [StringLiteral("\"hello\"")]), MethCall(ArrayCell(Id("data"), [IntLiteral(1)]), "baz", [IntLiteral(3), IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 359))

    def test_61(self):
        input = """
        func qux() {
            qux(1.5);
            obj[3].qux();
        }
"""
        expect = Program([FuncDecl("qux", [], VoidType(), Block([FuncCall("qux", [FloatLiteral(1.5)]), MethCall(ArrayCell(Id("obj"), [IntLiteral(3)]), "qux", [])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 360))

    def test_62(self):
        input = """
        func zap() {
            zap(true, false);
            list[2].zap(10);
        }
"""
        expect = Program([FuncDecl("zap", [], VoidType(), Block([FuncCall("zap", [BooleanLiteral(True), BooleanLiteral(False)]), MethCall(ArrayCell(Id("list"), [IntLiteral(2)]), "zap", [IntLiteral(10)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 361))

    def test_63(self):
        input = """
        func fizz() {
            fizz();
            arr[4].fizz(5, "text");
        }
"""
        expect = Program([FuncDecl("fizz", [], VoidType(), Block([FuncCall("fizz", []), MethCall(ArrayCell(Id("arr"), [IntLiteral(4)]), "fizz", [IntLiteral(5), StringLiteral("\"text\"")])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 362))

    def test_64(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {foo();}
            func foo(){return;}
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([VarDecl("a", None,IntLiteral(1)),
                          ConstDecl("b",None,IntLiteral(2)),
                          StructType("a",[("a",FloatType())],[]),
                          InterfaceType("b",[Prototype("foo",[],VoidType())]),
                          FuncDecl("foo",[],VoidType(),Block([Return(None)])),
                          MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 363))

    def test_65(self):
        input = """
        var x = 3.14;
        const y = "hello";
        type Point struct {x int;}
        type Shape interface {area() float;}
        func bar() {print(1);}
        func (Dog d) bark() string {return "woof";}
"""
        expect = Program([
            VarDecl("x", None, FloatLiteral(3.14)),
            ConstDecl("y", None, StringLiteral("\"hello\"")),
            StructType("Point", [("x", IntType())], []),
            InterfaceType("Shape", [Prototype("area", [], FloatType())]),
            FuncDecl("bar", [], VoidType(), Block([FuncCall("print", [IntLiteral(1)])])),
            MethodDecl("Dog", Id("d"), FuncDecl("bark", [], StringType(), Block([Return(StringLiteral("\"woof\""))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 364))

    def test_66(self):
        input = """
        var flag = true;
        const pi = 3.14159;
        type Circle struct {radius float;}
        type Measurable interface {length() int;}
        func baz() {return;}
        func (Rect r) width() int {return 5;}
"""
        expect = Program([
            VarDecl("flag", None, BooleanLiteral(True)),
            ConstDecl("pi", None, FloatLiteral(3.14159)),
            StructType("Circle", [("radius", FloatType())], []),
            InterfaceType("Measurable", [Prototype("length", [], IntType())]),
            FuncDecl("baz", [], VoidType(), Block([Return(None)])),
            MethodDecl("Rect", Id("r"), FuncDecl("width", [], IntType(), Block([Return(IntLiteral(5))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 365))

    def test_67(self):
        input = """
        var count = 10;
        const name = "test";
        type Box struct {width int; height int;}
        type Printable interface {print();}
        func qux() {x := 1;}
        func (Bird b) fly() boolean {return true;}
"""
        expect = Program([
            VarDecl("count", None, IntLiteral(10)),
            ConstDecl("name", None, StringLiteral("\"test\"")),
            StructType("Box", [("width", IntType()), ("height", IntType())], []),
            InterfaceType("Printable", [Prototype("print", [], VoidType())]),
            FuncDecl("qux", [], VoidType(), Block([Assign(Id("x"), IntLiteral(1))])),
            MethodDecl("Bird", Id("b"), FuncDecl("fly", [], BoolType(), Block([Return(BooleanLiteral(True))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 366))

    def test_68(self):
        input = """
        var value = "data";
        const max = 100;
        type Node struct {val string; next int;}
        type Iterator interface {next() string;}
        func zap() {return "done";}
        func (List l) size() int {return 0;}
"""
        expect = Program([
            VarDecl("value", None, StringLiteral("\"data\"")),
            ConstDecl("max", None, IntLiteral(100)),
            StructType("Node", [("val", StringType()), ("next", IntType())], []),
            InterfaceType("Iterator", [Prototype("next", [], StringType())]),
            FuncDecl("zap", [], VoidType(), Block([Return(StringLiteral("\"done\""))])),
            MethodDecl("List", Id("l"), FuncDecl("size", [], IntType(), Block([Return(IntLiteral(0))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 367))

    def test_69(self):
        input = """
        var temp = 2.5;
        const limit = 50;
        type Vector struct {x float; y float;}
        type Movable interface {move(x int);}
        func fizz() {a += 1;}
        func (Car c) stop() {return;}
"""
        expect = Program([
            VarDecl("temp", None, FloatLiteral(2.5)),
            ConstDecl("limit", None, IntLiteral(50)),
            StructType("Vector", [("x", FloatType()), ("y", FloatType())], []),
            InterfaceType("Movable", [Prototype("move", [IntType()], VoidType())]),
            FuncDecl("fizz", [], VoidType(), Block([Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))])),
            MethodDecl("Car", Id("c"), FuncDecl("stop", [], VoidType(), Block([Return(None)])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 368))

    def test_70(self):
        input = """
        var active = false;
        const version = 1.0;
        type User struct {id int; name string;}
        type Auth interface {login() boolean;}
        func buzz() {print("buzz");}
        func (Admin a) logout() string {return "out";}
"""
        expect = Program([
            VarDecl("active", None, BooleanLiteral(False)),
            ConstDecl("version", None, FloatLiteral(1.0)),
            StructType("User", [("id", IntType()), ("name", StringType())], []),
            InterfaceType("Auth", [Prototype("login", [], BoolType())]),
            FuncDecl("buzz", [], VoidType(), Block([FuncCall("print", [StringLiteral("\"buzz\"")])])),
            MethodDecl("Admin", Id("a"), FuncDecl("logout", [], StringType(), Block([Return(StringLiteral("\"out\""))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 369))

    def test_71(self):
        input = """
        var num = 42;
        const key = "secret";
        type Key struct {value string;}
        type Encryptor interface {encrypt() string;}
        func hello() {return 1;}
        func (Lock l) unlock() boolean {return false;}
"""
        expect = Program([
            VarDecl("num", None, IntLiteral(42)),
            ConstDecl("key", None, StringLiteral("\"secret\"")),
            StructType("Key", [("value", StringType())], []),
            InterfaceType("Encryptor", [Prototype("encrypt", [], StringType())]),
            FuncDecl("hello", [], VoidType(), Block([Return(IntLiteral(1))])),
            MethodDecl("Lock", Id("l"), FuncDecl("unlock", [], BoolType(), Block([Return(BooleanLiteral(False))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 370))

    def test_72(self):
        input = """
        var rate = 0.5;
        const size = 1000;
        type Buffer struct {data int; full boolean;}
        type Reader interface {read() int;}
        func process() {x := 2;}
        func (File f) close() {return;}
"""
        expect = Program([
            VarDecl("rate", None, FloatLiteral(0.5)),
            ConstDecl("size", None, IntLiteral(1000)),
            StructType("Buffer", [("data", IntType()), ("full", BoolType())], []),
            InterfaceType("Reader", [Prototype("read", [], IntType())]),
            FuncDecl("process", [], VoidType(), Block([Assign(Id("x"), IntLiteral(2))])),
            MethodDecl("File", Id("f"), FuncDecl("close", [], VoidType(), Block([Return(None)])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 371))

    def test_73(self):
        input = """
        var id = 123;
        const code = "abc";
        type Item struct {price float; qty int;}
        type Seller interface {sell() float;}
        func start() {return "start";}
        func (Store s) open() boolean {return true;}
"""
        expect = Program([
            VarDecl("id", None, IntLiteral(123)),
            ConstDecl("code", None, StringLiteral("\"abc\"")),
            StructType("Item", [("price", FloatType()), ("qty", IntType())], []),
            InterfaceType("Seller", [Prototype("sell", [], FloatType())]),
            FuncDecl("start", [], VoidType(), Block([Return(StringLiteral("\"start\""))])),
            MethodDecl("Store", Id("s"), FuncDecl("open", [], BoolType(), Block([Return(BooleanLiteral(True))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 372))

    def test_74(self):
        input = """
        var status = "ok";
        const threshold = 10;
        type Signal struct {level int;}
        type Controller interface {adjust() int;}
        func end() {print(0);}
        func (Switch s) toggle() [1]string {return;}
"""
        expect = Program([
            VarDecl("status", None, StringLiteral("\"ok\"")),
            ConstDecl("threshold", None, IntLiteral(10)),
            StructType("Signal", [("level", IntType())], []),
            InterfaceType("Controller", [Prototype("adjust", [], IntType())]),
            FuncDecl("end", [], VoidType(), Block([FuncCall("print", [IntLiteral(0)])])),
            MethodDecl("Switch", Id("s"), FuncDecl("toggle", [], ArrayType([IntLiteral(1)], StringType()), Block([Return(None)])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 373))

    def test_75(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block(
            [FuncCall("foo",[]),FuncCall("foo",
                                         [FuncCall("foo",[]),IntLiteral(2)]),
             MethCall(Id("a"),"foo",[]),
             MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",
                      [FuncCall("foo",[]),IntLiteral(2)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 374))

    def test_76(self):
        input = """
        func bar() {
            bar();
            bar(3);
            x.bar();
            x[1].y.bar(5);
        }
"""
        expect = Program([FuncDecl("bar", [], VoidType(), Block(
            [FuncCall("bar", []), FuncCall("bar", [IntLiteral(3)]),
             MethCall(Id("x"), "bar", []),
             MethCall(FieldAccess(ArrayCell(Id("x"), [IntLiteral(1)]), "y"), "bar", [IntLiteral(5)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 375))


    def test_77(self):
        input = """
        func baz() {
            baz("test");
            baz(baz(), 1.5);
            data.baz();
            data[0].info.baz("info");
        }
"""
        expect = Program([FuncDecl("baz", [], VoidType(), Block(
            [FuncCall("baz", [StringLiteral("\"test\"")]), FuncCall("baz", [FuncCall("baz", []), FloatLiteral(1.5)]),
             MethCall(Id("data"), "baz", []),
             MethCall(FieldAccess(ArrayCell(Id("data"), [IntLiteral(0)]), "info"), "baz", [StringLiteral("\"info\"")])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 376))

    def test_78(self):
        input = """
        func qux() {
            qux();
            qux(true);
            obj.qux();
            obj[3].val.qux(qux());
        }
"""
        expect = Program([FuncDecl("qux", [], VoidType(), Block(
            [FuncCall("qux", []), FuncCall("qux", [BooleanLiteral(True)]),
             MethCall(Id("obj"), "qux", []),
             MethCall(FieldAccess(ArrayCell(Id("obj"), [IntLiteral(3)]), "val"), "qux", [FuncCall("qux", [])])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 377))

    def test_79(self):
        input = """
        func zap() {
            zap(4, 5);
            zap(zap(), "end");
            list.zap();
            list[2].node.zap(10, false);
        }
"""
        expect = Program([FuncDecl("zap", [], VoidType(), Block(
            [FuncCall("zap", [IntLiteral(4), IntLiteral(5)]), FuncCall("zap", [FuncCall("zap", []), StringLiteral("\"end\"")]),
             MethCall(Id("list"), "zap", []),
             MethCall(FieldAccess(ArrayCell(Id("list"), [IntLiteral(2)]), "node"), "zap", [IntLiteral(10), BooleanLiteral(False)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 378))


    def test_80(self):
        input = """
        func fizz() {
            fizz();
            fizz(fizz());
            arr.fizz();
            arr[4].data.fizz(2.5);
        }
"""
        expect = Program([FuncDecl("fizz", [], VoidType(), Block(
            [FuncCall("fizz", []), FuncCall("fizz", [FuncCall("fizz", [])]),
             MethCall(Id("arr"), "fizz", []),
             MethCall(FieldAccess(ArrayCell(Id("arr"), [IntLiteral(4)]), "data"), "fizz", [FloatLiteral(2.5)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 379))

    def test_81(self):
        input = """
        func buzz() {
            buzz(1);
            buzz(buzz(), "start");
            node.buzz();
            node[0].child.buzz(true, 3);
        }
"""
        expect = Program([FuncDecl("buzz", [], VoidType(), Block(
            [FuncCall("buzz", [IntLiteral(1)]), FuncCall("buzz", [FuncCall("buzz", []), StringLiteral("\"start\"")]),
             MethCall(Id("node"), "buzz", []),
             MethCall(FieldAccess(ArrayCell(Id("node"), [IntLiteral(0)]), "child"), "buzz", [BooleanLiteral(True), IntLiteral(3)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 380))

    def test_82(self):
        input = """
        func hello() {
            hello();
            hello(hello(), hello());
            user.hello();
            user[5].profile.hello("hi");
        }
"""
        expect = Program([FuncDecl("hello", [], VoidType(), Block(
            [FuncCall("hello", []), FuncCall("hello", [FuncCall("hello", []), FuncCall("hello", [])]),
             MethCall(Id("user"), "hello", []),
             MethCall(FieldAccess(ArrayCell(Id("user"), [IntLiteral(5)]), "profile"), "hello", [StringLiteral("\"hi\"")])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 381))

    def test_83(self):
        input = """
        func process() {
            process(6);
            process(process());
            queue.process();
            queue[1].task.process(7, 8);
        }
"""
        expect = Program([FuncDecl("process", [], VoidType(), Block(
            [FuncCall("process", [IntLiteral(6)]), FuncCall("process", [FuncCall("process", [])]),
             MethCall(Id("queue"), "process", []),
             MethCall(FieldAccess(ArrayCell(Id("queue"), [IntLiteral(1)]), "task"), "process", [IntLiteral(7), IntLiteral(8)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 382))

    def test_84(self):
        input = """
        func end() {
            end("done");
            end(end(), 9);
            signal.end();
            signal[3].state.end(false);
        }
"""
        expect = Program([FuncDecl("end", [], VoidType(), Block(
            [FuncCall("end", [StringLiteral("\"done\"")]), FuncCall("end", [FuncCall("end", []), IntLiteral(9)]),
             MethCall(Id("signal"), "end", []),
             MethCall(FieldAccess(ArrayCell(Id("signal"), [IntLiteral(3)]), "state"), "end", [BooleanLiteral(False)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 383))


    def test_85(self):
        input = """
        func start() {
            start();
            start(1.0, start());
            config.start();
            config[2].option.start("go", 4);
        }
"""
        expect = Program([FuncDecl("start", [], VoidType(), Block(
            [FuncCall("start", []), FuncCall("start", [FloatLiteral(1.0), FuncCall("start", [])]),
             MethCall(Id("config"), "start", []),
             MethCall(FieldAccess(ArrayCell(Id("config"), [IntLiteral(2)]), "option"), "start", [StringLiteral("\"go\""), IntLiteral(4)])
             ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 384))

    def test_86(self):
        input = """
            func foo(){
                a["s"][foo()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[StringLiteral("\"s\""),FuncCall("foo",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),
            Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 385))

    def test_87(self):
        input = """
        func bar() {
            x[1] := x[2];
            x[bar()] := x[3];
            y.z[0] := y.z[1];
            y.z[2][3] := y.z[2][4];
        }
"""
        expect = Program([FuncDecl("bar", [], VoidType(), Block([
            Assign(ArrayCell(Id("x"), [IntLiteral(1)]), ArrayCell(Id("x"), [IntLiteral(2)])),
            Assign(ArrayCell(Id("x"), [FuncCall("bar", [])]), ArrayCell(Id("x"), [IntLiteral(3)])),
            Assign(ArrayCell(FieldAccess(Id("y"), "z"), [IntLiteral(0)]), ArrayCell(FieldAccess(Id("y"), "z"), [IntLiteral(1)])),
            Assign(ArrayCell(FieldAccess(Id("y"), "z"), [IntLiteral(2), IntLiteral(3)]), ArrayCell(FieldAccess(Id("y"), "z"), [IntLiteral(2), IntLiteral(4)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 386))

    def test_88(self):
        input = """
        func baz() {
            data["key"] := data[0];
            data[1][2] := data[baz()];
            obj.prop[3] := obj.prop[4];
            obj.prop[5][6] := obj.prop[5][7];
        }
"""
        expect = Program([FuncDecl("baz", [], VoidType(), Block([
            Assign(ArrayCell(Id("data"), [StringLiteral("\"key\"")]), ArrayCell(Id("data"), [IntLiteral(0)])),
            Assign(ArrayCell(Id("data"), [IntLiteral(1), IntLiteral(2)]), ArrayCell(Id("data"), [FuncCall("baz", [])])),
            Assign(ArrayCell(FieldAccess(Id("obj"), "prop"), [IntLiteral(3)]), ArrayCell(FieldAccess(Id("obj"), "prop"), [IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(Id("obj"), "prop"), [IntLiteral(5), IntLiteral(6)]), ArrayCell(FieldAccess(Id("obj"), "prop"), [IntLiteral(5), IntLiteral(7)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 387))

    def test_89(self):
        input = """
        func qux() {
            list[0][qux()] := list[1][2];
            list[3] := list[4];
            node.child[5] := node.child[6];
            node.child[7][8] := node.child[7][9];
        }
"""
        expect = Program([FuncDecl("qux", [], VoidType(), Block([
            Assign(ArrayCell(Id("list"), [IntLiteral(0), FuncCall("qux", [])]), ArrayCell(Id("list"), [IntLiteral(1), IntLiteral(2)])),
            Assign(ArrayCell(Id("list"), [IntLiteral(3)]), ArrayCell(Id("list"), [IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(Id("node"), "child"), [IntLiteral(5)]), ArrayCell(FieldAccess(Id("node"), "child"), [IntLiteral(6)])),
            Assign(ArrayCell(FieldAccess(Id("node"), "child"), [IntLiteral(7), IntLiteral(8)]), ArrayCell(FieldAccess(Id("node"), "child"), [IntLiteral(7), IntLiteral(9)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 388))

    def test_90(self):
        input = """
        func zap() {
            arr[true] := arr[false];
            arr[2][3] := arr[zap()];
            info.data[4] := info.data[5];
            info.data[6][7] := info.data[6][8];
        }
"""
        expect = Program([FuncDecl("zap", [], VoidType(), Block([
            Assign(ArrayCell(Id("arr"), [BooleanLiteral(True)]), ArrayCell(Id("arr"), [BooleanLiteral(False)])),
            Assign(ArrayCell(Id("arr"), [IntLiteral(2), IntLiteral(3)]), ArrayCell(Id("arr"), [FuncCall("zap", [])])),
            Assign(ArrayCell(FieldAccess(Id("info"), "data"), [IntLiteral(4)]), ArrayCell(FieldAccess(Id("info"), "data"), [IntLiteral(5)])),
            Assign(ArrayCell(FieldAccess(Id("info"), "data"), [IntLiteral(6), IntLiteral(7)]), ArrayCell(FieldAccess(Id("info"), "data"), [IntLiteral(6), IntLiteral(8)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 389))

    def test_91(self):
        input = """
        func fizz() {
            x["a"][1] := x[2][3];
            x[4] := x[fizz()];
            y.z.w[5] := y.z.w[6];
            y.z.w[7][8] := y.z.w[7][9];
        }
"""
        expect = Program([FuncDecl("fizz", [], VoidType(), Block([
            Assign(ArrayCell(Id("x"), [StringLiteral("\"a\""), IntLiteral(1)]), ArrayCell(Id("x"), [IntLiteral(2), IntLiteral(3)])),
            Assign(ArrayCell(Id("x"), [IntLiteral(4)]), ArrayCell(Id("x"), [FuncCall("fizz", [])])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "w"), [IntLiteral(5)]), ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "w"), [IntLiteral(6)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "w"), [IntLiteral(7), IntLiteral(8)]), ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "w"), [IntLiteral(7), IntLiteral(9)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 390))

    def test_92(self):
        input = """
        func buzz() {
            a[0][buzz()] := a[1][2];
            a[3] := a[4];
            b.c.d[5] := b.c.d[6];
            b.c.d[7][8] := b.c.d[7][9];
        }
"""
        expect = Program([FuncDecl("buzz", [], VoidType(), Block([
            Assign(ArrayCell(Id("a"), [IntLiteral(0), FuncCall("buzz", [])]), ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)])),
            Assign(ArrayCell(Id("a"), [IntLiteral(3)]), ArrayCell(Id("a"), [IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"), "c"), "d"), [IntLiteral(5)]), ArrayCell(FieldAccess(FieldAccess(Id("b"), "c"), "d"), [IntLiteral(6)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"), "c"), "d"), [IntLiteral(7), IntLiteral(8)]), ArrayCell(FieldAccess(FieldAccess(Id("b"), "c"), "d"), [IntLiteral(7), IntLiteral(9)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 391))

    def test_93(self):
        input = """
        func hello() {
            list["key"] := list[0];
            list[1][2] := list[hello()];
            node.data[3] := node.data[4];
            node.data[5][6] := node.data[5][7];
        }
"""
        expect = Program([FuncDecl("hello", [], VoidType(), Block([
            Assign(ArrayCell(Id("list"), [StringLiteral("\"key\"")]), ArrayCell(Id("list"), [IntLiteral(0)])),
            Assign(ArrayCell(Id("list"), [IntLiteral(1), IntLiteral(2)]), ArrayCell(Id("list"), [FuncCall("hello", [])])),
            Assign(ArrayCell(FieldAccess(Id("node"), "data"), [IntLiteral(3)]), ArrayCell(FieldAccess(Id("node"), "data"), [IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(Id("node"), "data"), [IntLiteral(5), IntLiteral(6)]), ArrayCell(FieldAccess(Id("node"), "data"), [IntLiteral(5), IntLiteral(7)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 392))

    def test_94(self):
        input = """
        func process() {
            arr[process()] := arr[1];
            arr[2][3] := arr[4];
            info.x[5] := info.x[6];
            info.x[7][8] := info.x[7][9];
        }
"""
        expect = Program([FuncDecl("process", [], VoidType(), Block([
            Assign(ArrayCell(Id("arr"), [FuncCall("process", [])]), ArrayCell(Id("arr"), [IntLiteral(1)])),
            Assign(ArrayCell(Id("arr"), [IntLiteral(2), IntLiteral(3)]), ArrayCell(Id("arr"), [IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(Id("info"), "x"), [IntLiteral(5)]), ArrayCell(FieldAccess(Id("info"), "x"), [IntLiteral(6)])),
            Assign(ArrayCell(FieldAccess(Id("info"), "x"), [IntLiteral(7), IntLiteral(8)]), ArrayCell(FieldAccess(Id("info"), "x"), [IntLiteral(7), IntLiteral(9)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 393))

    def test_95(self):
        input = """
        func end() {
            x[0][1] := x[end()];
            x[2] := x[3];
            y.z.a[4] := y.z.a[5];
            y.z.a[6][7] := y.z.a[6][8];
        }
"""
        expect = Program([FuncDecl("end", [], VoidType(), Block([
            Assign(ArrayCell(Id("x"), [IntLiteral(0), IntLiteral(1)]), ArrayCell(Id("x"), [FuncCall("end", [])])),
            Assign(ArrayCell(Id("x"), [IntLiteral(2)]), ArrayCell(Id("x"), [IntLiteral(3)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "a"), [IntLiteral(4)]), ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "a"), [IntLiteral(5)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "a"), [IntLiteral(6), IntLiteral(7)]), ArrayCell(FieldAccess(FieldAccess(Id("y"), "z"), "a"), [IntLiteral(6), IntLiteral(8)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 394))

    def test_96(self):
        input = """
        func start() {
            data[true][start()] := data[0][1];
            data[2] := data[3];
            obj.info[4] := obj.info[5];
            obj.info[6][7] := obj.info[6][8];
        }
"""
        expect = Program([FuncDecl("start", [], VoidType(), Block([
            Assign(ArrayCell(Id("data"), [BooleanLiteral(True), FuncCall("start", [])]), ArrayCell(Id("data"), [IntLiteral(0), IntLiteral(1)])),
            Assign(ArrayCell(Id("data"), [IntLiteral(2)]), ArrayCell(Id("data"), [IntLiteral(3)])),
            Assign(ArrayCell(FieldAccess(Id("obj"), "info"), [IntLiteral(4)]), ArrayCell(FieldAccess(Id("obj"), "info"), [IntLiteral(5)])),
            Assign(ArrayCell(FieldAccess(Id("obj"), "info"), [IntLiteral(6), IntLiteral(7)]), ArrayCell(FieldAccess(Id("obj"), "info"), [IntLiteral(6), IntLiteral(8)]))
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 395))


    def test_97(self):
        input = """
            func foo() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
            };
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("\"2\"")],[NilLiteral()],[StructLiteral("struc",[])]]))]))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 396))

    def test_98(self):
        input = """
        func bar() {
            return [3] Point { {5}, {"x"}, {true} };
        };
"""
        expect = Program([FuncDecl("bar", [], VoidType(), Block([Return(ArrayLiteral([IntLiteral(3)], Id("Point"), [[IntLiteral(5)], [StringLiteral("\"x\"")], [BooleanLiteral(True)]]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 397))

    def test_99(self):
        input = """
        func baz() {
            return [1] Node { {"data"} };
        };
"""
        expect = Program([FuncDecl("baz", [], VoidType(), Block([Return(ArrayLiteral([IntLiteral(1)], Id("Node"), [[StringLiteral("\"data\"")]]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 398))

    def test_100(self):
        input = """
        func qux() {
            return [4] Box { {nil}, {3.14}, {abc} };
        };
"""
        expect = Program([FuncDecl("qux", [], VoidType(), Block([Return(ArrayLiteral([IntLiteral(4)], Id("Box"), [[NilLiteral()], [FloatLiteral(3.14)], [Id("abc")]]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 399))