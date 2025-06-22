import unittest
from TestUtils import TestChecker
from AST import *
import inspect



class CheckSuite(unittest.TestCase):
    def test_001(self):
        """
var a = 1; 
var a = 2;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a\n", inspect.stack()[0].function))

    def test_002(self):
        """
var a = 1; 
const a = 2;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", inspect.stack()[0].function))

    def test_003(self):
        """
const a = 1; 
var a = 2;
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),VarDecl("a", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a\n", inspect.stack()[0].function))

    def test_004(self):
        """
const a = 1; 
func a () {return;}
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("a",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: a\n", inspect.stack()[0].function))

    def test_005(self):
        """ 
func foo () {return;}
var foo = 1;
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),VarDecl("foo", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: foo\n", inspect.stack()[0].function))

    def test_006(self):
        """ 
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt\n", inspect.stack()[0].function))

    def test_007(self):
        """ 
type foo struct {
    foo int;
}
type a struct {
    str string;
    v int;
    v float;
}
        """
        input = Program([StructType("foo",[("foo",IntType())],[]),StructType("a",[("str",StringType()),("v",IntType()),("v",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: v\n", inspect.stack()[0].function))

    def test_008(self):
        """ 
func (v A) putIntLn () {return;}
func (v A) getInt () {return;}
func (v A) getInt () {return;}
type A struct {
    v int;
}
        """ 
        input = Program([MethodDecl("v",Id("A"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("A"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("A"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),StructType("A",[("v",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", inspect.stack()[0].function))

    def test_009(self):
        """ 
    type Calculator interface {
        add ();
        add (x float, y float);
    }
        """
        input = Program([InterfaceType("Calculator",[Prototype("add",[],VoidType()),Prototype("add",[FloatType(),FloatType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: add\n", inspect.stack()[0].function))

    def test_010(self):
        """ 
    func calculate (x, x float) {return;}
        """
        input = Program([FuncDecl("calculate",[ParamDecl("x",FloatType()),ParamDecl("x",FloatType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: x\n", inspect.stack()[0].function))

    def test_011(self):
        """ 
    func calculate (x float) {
        var y = 3.0;
        var z = 5.0;
        const z = 10.0;
    }
        """
        input = Program([FuncDecl("calculate",[ParamDecl("x",FloatType())],VoidType(),Block([VarDecl("y", None,FloatLiteral(3.0)),VarDecl("z", None,FloatLiteral(5.0)),ConstDecl("z",None,FloatLiteral(10.0))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: z\n", inspect.stack()[0].function))

    def test_012(self):
        """ 
    func calculate (x float) {
        for var i = 0; i < 10; i += 2 {
            const i = 100;
        }
    }
        """
        input = Program([FuncDecl("calculate",[ParamDecl("x",FloatType())],VoidType(),Block([ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(2))),Block([ConstDecl("i",None,IntLiteral(100))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: i\n", inspect.stack()[0].function))

    def test_013(self):
        """ 
    var x = 100;
    var y = x;
    var z = unknown;
        """
        input = Program([VarDecl("x", None,IntLiteral(100)),VarDecl("y", None,Id("x")),VarDecl("z", None,Id("unknown"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: unknown\n", inspect.stack()[0].function))

    def test_014(self):
        """ 
    func square (x int) int {return x * x;}

    func main () {
        var result = square(5);
        nonexistent_function();
        return;
    }
        """
        input = Program([FuncDecl("square",[ParamDecl("x",IntType())],IntType(),Block([Return(BinaryOp("*", Id("x"), Id("x")))])),FuncDecl("main",[],VoidType(),Block([VarDecl("result", None,FuncCall("square",[IntLiteral(5)])),FuncCall("nonexistent_function",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: nonexistent_function\n", inspect.stack()[0].function))

    def test_015(self): #test_015
        """ 
    type Person struct {
        name string;
        age int;
    }

    func (p Person) display () {
        const n = p.name;
        var a = p.salary;
    }
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("p",Id("Person"),FuncDecl("display",[],VoidType(),Block([ConstDecl("n",None,FieldAccess(Id("p"),"name")),VarDecl("a", None,FieldAccess(Id("p"),"salary"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: salary\n", inspect.stack()[0].function))

    def test_016(self):
        """ 
    type Person struct {
        name string;
        age int;
    }

    func (p Person) display () {
        p.display();
        p.calculate();
    }
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("p",Id("Person"),FuncDecl("display",[],VoidType(),Block([MethCall(Id("p"),"display",[]),MethCall(Id("p"),"calculate",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: calculate\n", inspect.stack()[0].function))

    def test_017(self):
        """  
    type Student struct {name string;}
    type Student struct {id int;}
        """
        input = Program([StructType("Student",[("name",StringType())],[]),StructType("Student",[("id",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: Student\n", inspect.stack()[0].function))

    def test_018(self): #test_044
        """
    type Rectangle struct {
        width float;
        height float;
    }
    func (r Rectangle) area (scale float) {return;}
    func area () {return;}"""
        input = Program([StructType("Rectangle",[("width",FloatType()),("height",FloatType())],[]),MethodDecl("r",Id("Rectangle"),FuncDecl("area",[ParamDecl("scale",FloatType())],VoidType(),Block([Return(None)]))),FuncDecl("area",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    def test_019(self): #test_050
        '''
    func (s Shape) perimeter (a, b float) {
        const s = 3.14;
        const a = 2.0;
    }

    type Shape struct {
        radius float;
    }

    func (c Circle) perimeter () {
        const a = 3.14;
    }

    type Circle struct {
        radius float;
    }

    func (c Circle) perimeter (a, b float) {
        const a = 2.0;
    }
        '''
        input = Program([MethodDecl("s",Id("Shape"),FuncDecl("perimeter",[ParamDecl("a",FloatType()),ParamDecl("b",FloatType())],VoidType(),Block([ConstDecl("s",None,FloatLiteral(3.14)),ConstDecl("a",None,FloatLiteral(2.0))]))),StructType("Shape",[("radius",FloatType())],[]),MethodDecl("c",Id("Circle"),FuncDecl("perimeter",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral(3.14))]))),StructType("Circle",[("radius",FloatType())],[]),MethodDecl("c",Id("Circle"),FuncDecl("perimeter",[ParamDecl("a",FloatType()),ParamDecl("b",FloatType())],VoidType(),Block([ConstDecl("a",None,FloatLiteral(2.0))])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: perimeter\n", inspect.stack()[0].function))
    
    
    def test_020(self): #test_019
        """
    func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString\n", inspect.stack()[0].function))
    
    def test_021(self): #test_190
        input =  """
const v = 3;
const a = v + v;
var b [a * 2 + a] int;
var c [18] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 

    def test_022(self): # test_181
        input =  """
        func foo(a [2] float) {
            foo([2] float {1.0,2.0})
            foo([2] int {1,2})
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)])])\n""", inspect.stack()[0].function)) 

    
    
    
    def test_023(self): # test_176
        input =  """
    type A interface {foo();}
    const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: A\n""", inspect.stack()[0].function)) 



    def test_024(self): # test_061
        input = """
var a = foo();
func foo () int {
    var a =  koo();
    var c = getInt();
    putInt(c);
    putIntLn(c);
    return 1;
}
var d = foo();
func koo () int {
    var a =  foo ();
    return 1;
}
        """
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))


    def test_025(self): # 53
        """
func foo () {
    var a = 1;
    var b = 1;
    for a, b := range [3]int {1, 2, 3} {
        var b = 1;
    }
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))


    def test_026(self): # test_071
        input =  """  
var v TIEN;      
type TIEN struct {
    a int;
} 
type VO interface {
    foo() int;
}

func (v TIEN) foo() int {return 1;}
func (b TIEN) koo() {b.koo();}
func foo() {
    var x VO;  
    const b = x.foo(); 
    x.koo(); 
}
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo\n", inspect.stack()[0].function))


    def test_027(self): # test_068
            input =  """  
var v TIEN;
const b = v.foo();        
type TIEN struct {
    a int;
} 
func (v TIEN) foo() int {return 1;}

func (v TIEN) koo() int {return 1;}
const c = v.koo();  
const d = v.zoo();
            """
            input = Program([VarDecl("v",Id("TIEN"), None),ConstDecl("b",None,MethCall(Id("v"),"foo",[])),StructType("TIEN",[("a",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("v",Id("TIEN"),FuncDecl("koo",[],IntType(),Block([Return(IntLiteral(1))]))),ConstDecl("c",None,MethCall(Id("v"),"koo",[])),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))])
            self.assertTrue(TestChecker.test(input, "Undeclared Method: zoo\n", inspect.stack()[0].function))


    def test_028(self): # test_051
            input =  """  
const a = 2;
func foo () {
    const a = 1;
    for var a = 1; a < 1; b := 2 {
        const b = 1;
    }
}
            """
            input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
            self.assertTrue(TestChecker.test(input, "Redeclared Constant: b\n", inspect.stack()[0].function))


    def test_029(self): # test_008
            input =  """  
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    Votien int;
}  
            """
            input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType())],[])])
            self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", inspect.stack()[0].function))

    def test_030(self): # 216
        """
func (v TIEN) VO () {return ;}
func (v TIEN) Tien () {return ;}
type TIEN struct {
    Votien int;
    Tien int;
}
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Tien\n""", inspect.stack()[0].function))

        
    def test_031(self): # 210
        """
var v TIEN;
func (v TIEN) foo (v int) int {
    return v;
}

type TIEN struct {
    Votien int;
}
        """
        input = Program([VarDecl("v",Id("TIEN"), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))

    def test_032(self):
        """
        var a int;
        
        func (x A) a(){
            
        }
        """	
        input = Program([VarDecl("a",IntType(),None),MethodDecl("x",Id("A"),FuncDecl("a",[],VoidType(),Block([])))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
        


    def test_033(self): # 202
        """
func foo() {
    a := 1;
    var a = 1;
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a\n""", inspect.stack()[0].function)) 
    def test_034(self): # 190
        input =  """
const v = 3;
const a = v + v;
var b [a * 2 + a] int;
var c [18] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 


    def test_035(self): # 181
        input =  """
func foo(a [2] float) {
    foo([2] float {1.0,2.0})
    foo([2] int {1,2})
}
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)])])\n""", inspect.stack()[0].function)) 

    def test_036(self): # 176
        input =  """
    type A interface {foo();}
    const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: A\n""", inspect.stack()[0].function)) 


        
    def test_037(self): # 228
        input = """
func foo() int {
    const foo = 1;
    return foo()
}
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", inspect.stack()[0].function))
        
    def test_038(self): # 72
        input = """  
var v int = 1.02;
        """
        input = Program([VarDecl("v",IntType(),FloatLiteral(1.02))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.02))\n""", inspect.stack()[0].function))
        
    def test_039(self): # 73
        input = """  
var v float = 1;
        """
        input = Program([VarDecl("v",FloatType(),IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
        
    def test_040(self): # 74
        input = """  
var v string = true;
        """
        input = Program([VarDecl("v",StringType(),BooleanLiteral(True))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(v,StringType,BooleanLiteral(true))\n""", inspect.stack()[0].function))
        
    def test_041(self): # 76 
        input = """  
type S1 struct {votien int;}
type S2 struct {votien int;}

var v S1;
const x = v;
var z S1 = x;
var k S2 = x;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(k,Id(S2),Id(x))\n""", inspect.stack()[0].function))
    def test_042(self): # 77
        input = """  
type I1 interface {votien();}
type I2 interface {votien();}


var v I1;
const x = v;
var z I1 = x;
var k I2 = x;
        """
        input = Program([InterfaceType("I1",[Prototype("votien",[],VoidType())]),InterfaceType("I2",[Prototype("votien",[],VoidType())]),VarDecl("v",Id("I1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("I1"),Id("x")),VarDecl("k",Id("I2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(k,Id(I2),Id(x))\n""", inspect.stack()[0].function))
        
    def test_043(self): # 78
        input = """  
type S1 struct {votien int;}
type S2 struct {votien int;}
type I1 interface {votien1();}
type I2 interface {votien1();}

func (s S1) votien1() {return;}

var a S1;
var b S2;
var c I1 = a;
var d I2 = b;"""
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[],VoidType())]),InterfaceType("I2",[Prototype("votien1",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,Id(I2),Id(b))\n""", inspect.stack()[0].function))
    def test_044(self): # 182
        input =  """
type S1 struct {votien int;}
type I1 interface {votien();}

func (s S1) votien() {return;}

var b [2] S1;
var a [2] I1 = b;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))\n""", inspect.stack()[0].function)) 

    def test_045(self): # 184
        input =  """
var a [1 + 9] int;
var b [10] int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 

    def test_046(self): # 174
        input =  """
var A = 1;
type A struct {a int;}
        """
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Type: A\n""", inspect.stack()[0].function)) 

    def test_047(self): # 143
        input =  """
var a TIEN;
func foo() TIEN {
    return a;
    return TIEN;
}

type TIEN struct {tien int;}
        """
        input = Program([VarDecl("a",Id("TIEN"), None),FuncDecl("foo",[],Id("TIEN"),Block([Return(Id("a")),Return(Id("TIEN"))])),StructType("TIEN",[("tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: TIEN\n""", inspect.stack()[0].function))


    def test_048(self): # 086
        input =  """  
func foo(){
    if (true) {
         var a float = 1.02;

    } else {
        var a int = 1.02;
    }
}

        """
        input = Program([
            FuncDecl("foo",[],VoidType(),
                Block([If(BooleanLiteral(True), 
                    Block([VarDecl("a",FloatType(),FloatLiteral(1.02))]), 
                Block([VarDecl("a",IntType(),FloatLiteral(1.02))]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.02))\n""", inspect.stack()[0].function))
    
    def test_049(self): # 090
        input =  """  
type TIEN struct {v int;}
var v TIEN;
func foo(){
    for 1 {
         var a int = 1.02;
    }
}

        """
        input = Program([
            StructType("TIEN",[("v",IntType())],[]),
            VarDecl("v",Id("TIEN"), None),
            FuncDecl("foo",[],VoidType(),
                Block([ForBasic(IntLiteral(1),
                    Block([VarDecl("a",IntType(),FloatLiteral(1.02))]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.02))]))\n""", inspect.stack()[0].function))


    def test_050(self): # 092
        input =  """  

func foo(){
    return
}
func foo1() int{
    return 1.5
}
func foo2() float{
    return 2
}

        """
        input = Program([
            FuncDecl("foo",[],VoidType(),Block([Return(None)])),
            FuncDecl("foo1",[],IntType(),Block([Return(FloatLiteral(1.5))])),
            FuncDecl("foo2",[],FloatType(),Block([Return(IntLiteral(2))]))])
        
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(FloatLiteral(1.5))\n", inspect.stack()[0].function))


    def test_051(self): # 038
        input =  """  
const a = 1;
func foo() {
    var a = 1;
}
        """
        input = Program([
            ConstDecl("a",None,IntLiteral(1)),
            FuncDecl("foo",[],VoidType(),
                Block([VarDecl("a", None,IntLiteral(1))]))])
        
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_052(self): # 052
        input =  """  
const a = 2;
func foo () {
    const a = 1;
    for a < 1 {
        const a = 1;
        for a < 1 {
            const a = 1;
            const b = 1;
        }
        const b = 1;
        var a = 1;
    }
}
        """
        input = Program([
            ConstDecl("a",None,IntLiteral(2)),
            FuncDecl("foo",[],VoidType(),
                Block([ConstDecl("a",None,IntLiteral(1)),
                ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([
                    ConstDecl("a",None,IntLiteral(1)),
                    ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))])),
                    ConstDecl("b",None,IntLiteral(1)),
                    VarDecl("a", None,IntLiteral(1))]))]))])
        
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a\n""", inspect.stack()[0].function))

    def test_053(self): # 075
        input =  """  
var v string = "1";
const x = v;
var k string = x;
var y boolean = x;
        """
        input = Program([
            VarDecl("v",StringType(),StringLiteral("1")),
            ConstDecl("x",None,Id("v")),
            VarDecl("k",StringType(),Id("x")),
            VarDecl("y",BoolType(),Id("x"))])
        
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(y,BoolType,Id(x))\n""", inspect.stack()[0].function))

    def test_054(self): # 079
        input =  """  
type S1 struct {votien int;} # struct S1
type S2 struct {votien int;} # struct S2
type I1 interface {votien1();} # interface I1
type I2 interface {votien1() int;} # interface I2

func (s S1) votien1() {return;} # method S1.votien1

var a S1; # a is instace of struct S1
var b S2; # b is instance of struct S2
var c I2 = a; # c is instance of interface I2, but a is instance of struct S1
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[],VoidType())]),InterfaceType("I2",[Prototype("votien1",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I2"),Id("a"))])
        
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(c,Id(I2),Id(a))\n""", inspect.stack()[0].function))


    def test_055(self): # 080
        input =  """  
type S1 struct {votien int;} # struct type S1
type S2 struct {votien int;} # struct type S1
type I1 interface {votien1() S1;} # interface I1
type I2 interface {votien1() S2;} # interface I2

func (s S1) votien1() S1 {return s;} # method S1.votien1, return S1

var a S1; # a is instance of struct S1
var c I1 = a; # c is instance of interface I1, a is instance of struct S1
var d I2 = a; # d is instance of interface I2, a is instance of struct S1
        """
        input = Program([
            StructType("S1",[("votien",IntType())],[]),
            StructType("S2",[("votien",IntType())],[]),
            InterfaceType("I1",[Prototype("votien1",[],Id("S1"))]),
            InterfaceType("I2",[Prototype("votien1",[],Id("S2"))]),
            MethodDecl("s",Id("S1"),FuncDecl("votien1",[],Id("S1"),Block([Return(Id("s"))]))),
            VarDecl("a",Id("S1"), None),
            VarDecl("c",Id("I1"),Id("a")),
            VarDecl("d",Id("I2"),Id("a"))])

        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,Id(I2),Id(a))\n""", inspect.stack()[0].function))

    def test_056(self): # 081
        input =  """  
type S1 struct {votien int;}
type S2 struct {votien int;}
type I1 interface {votien1(e, e int) S1;}
type I2 interface {votien1(a int) S1;}

func (s S1) votien1(a, b int) S1 {return s;}

var a S1;
var c I1 = a;
var d I2 = a;
        """
        input = Program([
            StructType("S1",[("votien",IntType())],[]),
            StructType("S2",[("votien",IntType())],[]),
            InterfaceType("I1",[Prototype("votien1",[IntType(),IntType()],Id("S1"))]),
            InterfaceType("I2",[Prototype("votien1",[IntType()],Id("S1"))]),
            MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),
                Block([Return(Id("s"))]))),
            VarDecl("a",Id("S1"), None),
            VarDecl("c",Id("I1"),Id("a")),
            VarDecl("d",Id("I2"),Id("a"))])

        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,Id(I2),Id(a))\n""", inspect.stack()[0].function))

    def test_057(self): # 082
        input =  """  
type S1 struct {votien int;}
type S2 struct {votien int;}
type I1 interface {votien1(e, e int) S1;}
type I2 interface {votien1(a int, b float) S1;}

func (s S1) votien1(a, b int) S1 {return s;}

var a S1;
var c I1 = a;
var d I2 = a;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien1",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("votien1",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("votien1",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])

        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,Id(I2),Id(a))\n""", inspect.stack()[0].function))

    def test_058(self): # 087
        input =  """  
func foo(){
    if (1) {
         var a float = 1.02;
    }
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(IntLiteral(1), Block([VarDecl("a",FloatType(),FloatLiteral(1.02))]), None)]))])

        self.assertTrue(TestChecker.test(input, """Type Mismatch: If(IntLiteral(1),Block([VarDecl(a,FloatType,FloatLiteral(1.02))]))\n""", inspect.stack()[0].function))

    def test_059(self): # 093
        input =  """  
type S1 struct {votien1 int;}
type I1 interface {votien();}

func (s S1) votien() {return;}

func foo() S1 {
    var a S1;
    return a
}

func foo1() I1 {
    var a I1;
    return a
}

func foo2() S1 {
    var b I1;
    return b
}
        """
        input = Program([StructType("S1",[("votien1",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("votien",[],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],Id("S1"),Block([VarDecl("a",Id("S1"), None),Return(Id("a"))])),FuncDecl("foo1",[],Id("I1"),Block([VarDecl("a",Id("I1"), None),Return(Id("a"))])),FuncDecl("foo2",[],Id("S1"),Block([VarDecl("b",Id("I1"), None),Return(Id("b"))]))])

        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id(b))\n""", inspect.stack()[0].function))
        
    def test_060(self): # 231
        """
func foo() {
    var a = foo
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: foo\n""", inspect.stack()[0].function))
        
    def test_061(self): # 95
        """
type S1 struct {v int;}

var a = S1 {v :  z}
        """
        input = Program([StructType("S1",[("v",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",Id("z"))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: z\n""", inspect.stack()[0].function))
    def test_062(self): # 97
        """
var a = [2] float {1, 2}
var c [3] int = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],FloatType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(c,ArrayType([IntLiteral(3)],IntType),Id(a))\n""", inspect.stack()[0].function))
    def test_063(self): # 96
        """
var a = [2] int {1, 2}
var c [2] float = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
        
    def test_064(self): # 101
        """
var a [2][3] int;
var b = a[1][2];
var c int = b;
var d [1] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",IntType(),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,ArrayType([IntLiteral(1)],StringType),Id(b))\n""", inspect.stack()[0].function))
    def test_065(self): # 102
        """
var a [2][3] int;
var b = a[1];
var c [3] int = b;
var d [3] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(3)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,ArrayType([IntLiteral(3)],StringType),Id(b))\n""", inspect.stack()[0].function))
    def test_066(self): # 107
        """"
type S1 struct {votien int;}
type I1 interface {votien();}
var a I1;
var c I1 = nil;
var d S1 = nil;
func foo(){
    c := a;
    a := nil;
}

var e int = nil;
        """
        input = Program([StructType("S1",[("votien",IntType())],[]),InterfaceType("I1",[Prototype("votien",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(e,IntType,NilLiteral())\n""", inspect.stack()[0].function)) 
    def test_067(self): # 108
        """
var a = -1;
var b = -1.02;
var c = - true;
        """
        input = Program([VarDecl("a", None,UnaryOp("-",IntLiteral(1))),VarDecl("b", None,UnaryOp("-",FloatLiteral(1.02))),VarDecl("c", None,UnaryOp("-",BooleanLiteral(True)))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: UnaryOp(-,BooleanLiteral(true))\n""", inspect.stack()[0].function))        
#     
    def test_068(self): # 111
        """
var a = 1 + 2.0;
var b = 1 + 1;
func foo() int {
    return b;
    return a;
}
        """
        input = Program([VarDecl("a", None,BinaryOp("+", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b", None,BinaryOp("+", IntLiteral(1), IntLiteral(1))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id(a))\n""", inspect.stack()[0].function))
    def test_069(self): # 115
        """
var a int = 1 % 2;
var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(b,IntType,BinaryOp(IntLiteral(1),%,FloatLiteral(2.0)))\n""", inspect.stack()[0].function))
    def test_070(self): # 116
        """
var a boolean = true && false || true;
var b boolean = true && 1;
        """
        input = Program([VarDecl("a",BoolType(),BinaryOp("||", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True))),VarDecl("b",BoolType(),BinaryOp("&&", BooleanLiteral(True), IntLiteral(1)))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(BooleanLiteral(true),&&,IntLiteral(1))\n""", inspect.stack()[0].function))
    def test_071(self): # 117
        """
var a boolean = 1 > 2;
var b boolean = 1.0 < 2.0;
var c boolean = "1" == "2";
var d boolean = 1 > 2.0;
        """
        input = Program([VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),VarDecl("c",BoolType(),BinaryOp("==", StringLiteral("1"), StringLiteral("2"))),VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    def test_072(self): # 120
        """test_120.txt
1 KB

func foo(){
    for var i int = 1; i < 10; i := 1.0 {
        return;
    }
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.0)),Block([Return(None)]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(i),FloatLiteral(1.0))\n""", inspect.stack()[0].function))
    def test_073(self): # 122
        """
func foo(){
    for var i int = 1; i; i := 1.0 {
        var a = 1;
    }
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.0)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: For(VarDecl(i,IntType,IntLiteral(1)),Id(i),Assign(Id(i),FloatLiteral(1.0)),Block([VarDecl(a,IntLiteral(1))]))\n""", inspect.stack()[0].function))
    def test_074(self): # 123
        """
func foo(){
    var arr [2][3] int;
    var a = 1;
    var b[3]int;
    for a, b := range arr {

    }
}
       """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("a", None,IntLiteral(1)),VarDecl("b",ArrayType([IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([]))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    def test_075(self): # 132
        """
        func foo(a int) int{
            var b = 1;
            var c = a + b;
            return c; 
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],IntType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("c", None,BinaryOp("+", Id("a"), Id("b"))),Return(Id("c"))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    def test_076(self): # 134
        """
        func foo() int{
            var a = 1;
            var b = 1;
            return a + b;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),Return(BinaryOp("+", Id("a"), Id("b")))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    def test_077(self): # 110
        """
        var a = "1" + "2";

        """
        input = Program([VarDecl("a", None,BinaryOp("+", StringLiteral("1"), StringLiteral("2")))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    def test_078(self): # 59
        """
        var a = 1;
        func foo () {
            const b = 1;
            for a, c := range [3]int{1, 2, 3} {
                var d = c;
            }
            var d = a;
            var a = 1;
        }
        var d = b;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("b"))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: b\n""", inspect.stack()[0].function))
    def test_079(self): # 113
        """
var a float = 1 * 2.0;
var b int = 1 / 2;
var c float = 1 / 2;
func foo() int {
    return b;
    return c;
}
        """
        input = Program([VarDecl("a",FloatType(),BinaryOp("*", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b",IntType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),VarDecl("c",FloatType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("c"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id(c))\n""", inspect.stack()[0].function))
        
    def test_080(self): # 130
        """
        func main(){
            var a = 1;
            var b = a;
            var c = b;
            var d = c;
            var e = d;
            var f = e;
            var g = f;
            var h = g;
            var i = h;
            var j = i;
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("b")),VarDecl("d", None,Id("c")),VarDecl("e", None,Id("d")),VarDecl("f", None,Id("e")),VarDecl("g", None,Id("f")),VarDecl("h", None,Id("g")),VarDecl("i", None,Id("h")),VarDecl("j", None,Id("i"))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    def test_081(self): # 131
        """
        func main(){
            var s = 1;
            s := "string";
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("s", None,IntLiteral(1)),Assign(Id("s"),StringLiteral("string"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(s),StringLiteral(string))\n""", inspect.stack()[0].function))
    def test_082(self): # 151
        """
type putLn struct {a int;};
        """
        input = Program([StructType("putLn",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Type: putLn\n""", inspect.stack()[0].function))
    
    def test_083(self): # 152
        """
type putLn interface {foo();};
        """
        input = Program([InterfaceType("putLn",[Prototype("foo",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, """Redeclared Type: putLn\n""", inspect.stack()[0].function))
        
    def test_084(self): # 154
        """
        func foo() {
            putFloat();
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
    def test_085(self): # 158
        """
        func foo() [2] float {
            return [2] float {1.0, 2.0};
            return [2] int {1, 2};
        }
        """
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
    def test_086(self): # 164
        """
        func foo(a int,b float) {
            var c = a;
            var d = b;
            var e = c + d;
            var f string = e;
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",FloatType())],VoidType(),Block([VarDecl("c", None,Id("a")),VarDecl("d", None,Id("b")),VarDecl("e", None,BinaryOp("+", Id("c"), Id("d"))),VarDecl("f",StringType(),Id("e"))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(f,StringType,Id(e))\n", inspect.stack()[0].function))
    def test_087(self): # 163
        """
    type TIEN struct {
        a [2]int;
    } 
    type VO interface {foo() int;}

    func (v TIEN) foo() int {return 1;}

    func foo(a VO) {
        var b = TIEN{a: [2]int{1, 2}};
        foo(b)
    }
        """
        input = Program([StructType("TIEN",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("VO"))],VoidType(),Block([VarDecl("b", None,StructLiteral("TIEN",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[Id(b)])\n""", inspect.stack()[0].function))


    def test_088(self): # 208
        """
        func foo (b int) {
            for var a = 1; c < 1; a += c {
                const c = 2;
            }
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c\n""", inspect.stack()[0].function)) 
        
    def test_089(self): # Test undeclared field in struct literal
        """
        type Person struct {
            name string;
            age int;
        }
        
        var p = Person{name: "John", salary: 1000};
        """
        input = Program([
            StructType("Person",[("name",StringType()),("age",IntType())],[]),
            VarDecl("p", None, StructLiteral("Person",[("name",StringLiteral("John")),("salary",IntLiteral(1000))]))
        ])
        self.assertTrue(TestChecker.test(input, """Undeclared Field: salary\n""", inspect.stack()[0].function))

    def test_090(self): # Test array indexing with non-integer type
        """
        var arr [5] int;
        var idx = true;
        var value = arr[idx];
        """
        input = Program([
            VarDecl("arr",ArrayType([IntLiteral(5)],IntType()), None),
            VarDecl("idx", None, BooleanLiteral(True)),
            VarDecl("value", None, ArrayCell(Id("arr"),[Id("idx")]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ArrayCell(Id(arr),[Id(idx)])\n""", inspect.stack()[0].function))

    def test_091(self): # Test passing array to function with wrong dimensions
        """
        func process(a [2][3] int) {
            return;
        }
        
        func main() {
            var arr [3][2] int;
            process(arr);
        }
        """
        input = Program([
            FuncDecl("process",[ParamDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()))],VoidType(),Block([Return(None)])),
            FuncDecl("main",[],VoidType(),Block([
                VarDecl("arr",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()), None),
                FuncCall("process",[Id("arr")])
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_092(self): # Test method call on non-struct type
        """
        var x int = 10;
        var y = x.getValue();
        """
        input = Program([
            VarDecl("x",IntType(),IntLiteral(10)),
            VarDecl("y", None, MethCall(Id("x"),"getValue",[]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),getValue,[])\n""", inspect.stack()[0].function))

    def test_093(self): # Test binary operation with incompatible types
        """
        var result = "hello" - 5;
        """
        input = Program([
            VarDecl("result", None, BinaryOp("-",StringLiteral("hello"),IntLiteral(5)))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(StringLiteral(hello),-,IntLiteral(5))\n""", inspect.stack()[0].function))

    def test_094(self): # Test if statement with non-boolean condition
        """
        func test() {
            if ("string") {
                return;
            }
        }
        """
        input = Program([
            FuncDecl("test",[],VoidType(),Block([
                If(StringLiteral("string"), Block([Return(None)]), None)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: If(StringLiteral(string),Block([Return()]))\n""", inspect.stack()[0].function))

    def test_095(self): # Test return type mismatch in function
        """
        func calculate() string {
            return 42;
        }
        """
        input = Program([
            FuncDecl("calculate",[],StringType(),Block([
                Return(IntLiteral(42))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(IntLiteral(42))\n""", inspect.stack()[0].function))

    def test_096(self): # Test interface implementation with wrong method signature
        """
        type Drawable interface {
            draw(scale float);
        }
        
        type Circle struct {
            radius float;
        }
        
        func (c Circle) draw(scale int) {
            return;
        }
        
        var shape Drawable = Circle{radius: 5.0};
        """
        input = Program([
            InterfaceType("Drawable",[Prototype("draw",[FloatType()],VoidType())]),
            StructType("Circle",[("radius",FloatType())],[]),
            MethodDecl("c",Id("Circle"),FuncDecl("draw",[ParamDecl("scale",IntType())],VoidType(),Block([Return(None)]))),
            VarDecl("shape",Id("Drawable"),StructLiteral("Circle",[("radius",FloatLiteral(5.0))]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_097(self): # Test for loop with wrong condition type
        """
        func test() {
            for var i = 0; "not_boolean"; i += 1 {
                putInt(i);
            }
        }
        """
        input = Program([
            FuncDecl("test",[],VoidType(),Block([
                ForStep(VarDecl("i", None, IntLiteral(0)), 
                    StringLiteral("not_boolean"), 
                    Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))), 
                    Block([FuncCall("putInt",[Id("i")])]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: For(VarDecl(i,IntType,IntLiteral(0)),StringLiteral(not_boolean),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([FuncCall(putInt,[Id(i)])]))\n""", inspect.stack()[0].function))

    def test_098(self): # Test redeclared variable in method
        """
        type Rectangle struct {
            width float;
            height float;
        }
        
        func (r Rectangle) area() float {
            var width = 10.0;
            var width = 20.0;
            return width * r.height;
        }
        """
        input = Program([
            StructType("Rectangle",[("width",FloatType()),("height",FloatType())],[]),
            MethodDecl("r",Id("Rectangle"),FuncDecl("area",[],FloatType(),Block([
                VarDecl("width", None, FloatLiteral(10.0)),
                VarDecl("width", None, FloatLiteral(20.0)),
                Return(BinaryOp("*", Id("width"), FieldAccess(Id("r"),"height")))
            ])))
        ])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: width\n""", inspect.stack()[0].function))

    def test_099(self): # Test function call with wrong number of arguments
        """
        func sum(a int, b int) int {
            return a + b;
        }
        
        func main() {
            var result = sum(1, 2, 3);
        }
        """
        input = Program([
            FuncDecl("sum",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])),
            FuncDecl("main",[],VoidType(),Block([
                VarDecl("result", None, FuncCall("sum",[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(sum,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])\n""", inspect.stack()[0].function))

    def test_100(self): # Test array access with wrong number of dimensions
        """
        var matrix [2][3] int;
        var value = matrix[1][2][3];
        """
        input = Program([
            VarDecl("matrix",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),
            VarDecl("value", None, ArrayCell(Id("matrix"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
        ])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ArrayCell(Id(matrix),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])\n""", inspect.stack()[0].function))