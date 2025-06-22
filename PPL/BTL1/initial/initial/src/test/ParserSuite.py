import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = 1;","successful", 201))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = true;","successful", 202))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [5][0]string{1, \"string\"};","successful", 203))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", 204))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = Person{name: \"Alice\", age: 30};","successful", 205))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", 206))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", 207))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = ca.foo(132) + b.c[2];","successful", 208))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = a.a.foo();","successful", 209))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.checkParser("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", 210))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.checkParser("""
            const VoTien = a.b() + 2;
        ""","successful", 211))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.checkParser("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", 212))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", 213))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", 214))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {}                                                                       
        ""","Error on line 2 col 32: }", 215))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","Error on line 11 col 35: }", 216))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", 217))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", 218))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", 219))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", 220))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", 221))

    def test_021(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 0b11;                         
        ""","successful", 222))

    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 1.;                         
        ""","successful", 223))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN 1;                         
        ""","Error on line 2 col 25: 1", 224))

    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int{1};                         
        ""","Error on line 2 col 27: int", 225))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 28: true", 226))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 28: ]", 227))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 28: ]", 228))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1;                         
        ""","Error on line 2 col 35: ;", 229))

    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1,3,4;                         
        ""","Error on line 2 col 39: ;", 230))

    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 34: }", 231))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {};                         
        ""","successful", 232))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", 233))

    def test_033(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int {};                         
        ""","Error on line 2 col 27: int", 234))

    def test_034(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID + 3;                         
        ""","successful", 235))

    def test_035(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: };                         
        ""","Error on line 2 col 34: }", 236))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", 237))

    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", 238))

    def test_038(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a + b - [2]int{2} + c - z;                         
        ""","successful", 239))

    def test_039(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a * b / d % e * 2;                         
        ""","successful", 240))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        ""","successful", 241))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", 242))

    def test_042(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 30: ,", 243))

    def test_043(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[];                         
        ""","Error on line 2 col 29: ]", 244))

    def test_044(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo();                         
        ""","successful", 245))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        ""","successful", 246))

    def test_046(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        ""","successful", 247))

    def test_047(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1,);                         
        ""","Error on line 2 col 47: )", 248))

    def test_048(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;                         
        ""","successful", 249))

    def test_049(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
        ""","successful", 250))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo().a[2].goo();                         
        ""","successful", 251))

    def test_051(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = [2]int{1}[3][4].foo();                         
        ""","successful", 252))

    def test_052(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
        ""","successful", 253))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", 254))

    def test_054(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = foo() + foo(a{a:2}) + foo(2, 3,4);                         
        ""","successful", 255))

    def test_055(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  int;                         
        ""","Error on line 2 col 23: int", 256))

    def test_056(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  (1, 2);                         
        ""","Error on line 2 col 25: ,", 257))

    def test_057(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a VOTIEN = 2 + 3 / 4;
        ""","successful", 258))

    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", 259))

    def test_059(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [][3]int = 2 + 3 / 4;
        ""","Error on line 2 col 19: ]", 260))

    def test_060(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = a.foo()[2];
        ""","successful", 261))

    def test_061(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = ;
        ""","Error on line 2 col 20: ;", 262))

    def test_062(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a 1;
        ""","Error on line 2 col 18: 1", 263))

    def test_063(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]int;
        ""","successful", 264))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]ID
        ""","successful", 265))

    def test_065(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a;
        ""","Error on line 2 col 19: ;", 266))

    def test_066(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a := 1 + foo.a[2];
        ""","Error on line 2 col 20: :=", 267))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a =;
        ""","Error on line 2 col 21: ;", 268))

    def test_068(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            
            var a int; var d = 2;
                                        
            var d = 2;
                                        
            const a = 2; var d int = 3;
                                        
            
            var d = 2;""","successful", 269))

    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", 270))

    def test_070(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() [2]id {return ;}
""","successful", 271))

    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a) [2]id {return ;}
""","Error on line 2 col 22: )", 272))

    def test_072(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(int a) int {return ;}
""","Error on line 2 col 21: int", 273))

    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() {return ;}
""","successful", 274))

    def test_074(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a int, ) {}
""","Error on line 2 col 28: )", 275))

    def test_075(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int}
""","Error on line 2 col 45: }", 276))

    def test_076(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int;}
""","successful", 277))

    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", 278))

    def test_078(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 22: a", 279))

    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 22: =", 280))

    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", 281))

    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 46: }", 282))

    def test_082(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()
        }
""","successful", 283))

    def test_083(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}
""","successful", 284))

    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", 285))

    def test_085(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID){}
        }
""","Error on line 3 col 33: {", 286))

    def test_086(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();} type Person struct{value int;}
""","Error on line 2 col 49: type", 287))

    def test_087(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}; type Person struct{value int;}
""","successful", 288))

    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y int) int  {return ;};
""","successful", 289))

    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) Add(x int) int {return ;}
""","successful", 290))

    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 20: int", 291))

    def test_090(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;}
""","successful", 292))

    def test_091(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x, c int) {return ;}
""","successful", 293))

    def test_092(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c [2]c) Add(x int) {return ;}
""","Error on line 2 col 20: [", 294))

    def test_093(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (int c) Add(x int) {return ;}
""","Error on line 2 col 18: int", 295))

    def test_094(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;};
""","successful", 296))

    def test_095(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            func (c c) Add(x int) {return ;}
                                        
            func Add(x int) {return ;}; var c int;
                                        
            var c int; type Calculator struct{c int;}; type Calculator struct{c int;} var c int;
""","Error on line 7 col 86: var", 297))

    def test_096(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            var c int func (c c) Add(x int) {return ;}
""","Error on line 3 col 22: func", 298))

    def test_097(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const a = 2 func (c c) Add(x int) {return ;}
""","Error on line 3 col 24: func", 299))

    def test_098(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const MaxSize = 100 + 50; func (c c) Add() {return ;}
""","successful", 300))

    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""

""","Error on line 3 col 0: <EOF>", 301))

    def test_100(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
            func Add() {
                                        }
""","successful", 302))

    def test_101(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int = 2;      
                                    };""","successful", 303))

    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int;      
                                    };""","successful", 304))

    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""","successful", 305))

    def test_104(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         const a = a[2].b;      
                                    };""","successful", 306))

    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    };""","successful", 307))

    def test_106(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b var a = "s";           
                                    };""","Error on line 4 col 55: var", 308))

    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""","successful", 309))


    def test_108(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2].b := 2;       
                                    };""","successful", 310))


    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""","successful", 311))

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""","Error on line 3 col 48: +=", 312))

    def test_111(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        2 + 2 += 2;       
                                    };""","Error on line 3 col 40: 2", 313))

    def test_112(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       ID {id:2}.c += 2;       
                                    };""","Error on line 3 col 42: {", 314))

    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""","successful", 315))

    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""","successful", 316))

    def test_115(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){return;}
                                        } 
                                    };""","Error on line 4 col 48: )", 317))

    def test_116(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };""","successful", 318))

    def test_117(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return
                                        } else if(){
                                        }
                                    };""","Error on line 4 col 50: )", 319))

    def test_118(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return; 
                                        } else if(1){return; 
                                        }else if(1){return; 
                                        }else if(2){return
                                        }else {return; 
                                        }
                                    };""","successful", 320))

    def test_119(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true {return; }
                                    };""","successful", 321))

    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", 322))

    def test_121(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", 323))

    def test_122(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", 324))

    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", 325))

    def test_124(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", 326))

    def test_125(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 44: const", 327))

    def test_126(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: [", 328))

    def test_127(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return; 
                                        }
                                    };""","Error on line 3 col 76: {", 329))

    def test_128(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); var i [2]int = 0 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 75: var", 330))

    def test_129(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","successful", 331))

    def test_130(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 52: ,", 332))

    def test_131(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index.ab, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 52: ,", 333))

    def test_132(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value[2] := range arr {
                                        // index: 0, 1, 2
                                        return; 
                                        }
                                    };""","Error on line 3 col 56: [", 334))

    def test_133(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr[2] {return
                                        }
                                    };""","successful", 335))

    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""","successful", 336))

    def test_135(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {
                                            for index, value := range 23 {return; }
                                        }
                                    };""","successful", 337))

    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", 338))

    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", 339))

    def test_138(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return return 2 + a[2].b()
                    
                                    };""","Error on line 3 col 47: return", 340))

    def test_139(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break continue
                    
                                    };""","Error on line 3 col 46: continue", 341))

    def test_140(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo();
                                        foo()
                                    };""","successful", 342))

    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", 343))

    def test_142(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""","Error on line 3 col 40: (", 344))

    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", 345))

    def test_144(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {break;}
                                    };""","Error on line 3 col 40: {", 346))

    def test_145(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                        break;
                                    func Add() {
                                    };""","Error on line 2 col 40: break", 347))

    def test_146(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    };""","Error on line 4 col 50: c", 348))

    def test_147(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3)[b]
                                        return -1.c[c]
                                    };""","Error on line 4 col 50: c", 349))

    def test_148(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return struct;}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    };""","Error on line 3 col 55: struct", 350))

    def test_149(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}
                                    };""","Error on line 3 col 75: string", 351))

    def test_150(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}else  {return struct;}
                                    };""","Error on line 3 col 75: string", 352))

    def test_151(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{1+1}                    
""","Error on line 1 col 18: +", 353))

    def test_152(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", 354))

    def test_153(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{}                    
""","Error on line 1 col 17: }", 355))

    def test_154(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", 356))

    def test_155(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
""","successful", 357))

    def test_156(self):
        self.assertTrue(TestParser.checkParser("""
        func Add(x, y int, b float) {return ;}           
""","successful", 358))

    def test_157(self):
        self.assertTrue(TestParser.checkParser("""
        func (c c) Add(x, y int, b float) {return ;}           
""","successful", 359))

    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }      
""","successful", 360))

    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            c int  c int;                                                    
        }      
""","Error on line 3 col 19: c", 361))

    def test_159(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""","Error on line 10 col 27: ;", 362))

    def test_160(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };  
""","Error on line 4 col 16: else", 363))

    def test_161(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else if (1) {}
            };  
""","successful", 364))

    def test_162(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else {}
            };  
""","successful", 365))

    def test_163(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {}
            };  
""","successful", 366))

    def test_164(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i < 10 {
// loop body
}
            };  
""","successful", 367))

    def test_165(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0; i < 10; i += 1 {
// loop body
}
            };  
""","successful", 368))

    def test_166(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                    for index, value := range STRUCT{} {
    // loop body                                   
    };
            };  
""","successful", 369))

    def test_167(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.2; 
""","Error on line 2 col 20: 2", 370))

    def test_168(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.b.c().d().e[2].k()[2]; 
""","successful", 371))

    def test_169(self):
        self.assertTrue(TestParser.checkParser("""
        const a = [1]int{1, 2 
""","Error on line 2 col 30: ;", 372))

    def test_170(self):
        self.assertTrue(TestParser.checkParser("""
        const a = foo(1, 2
""","Error on line 2 col 26: ;", 373))

    def test_171(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i.b := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: .", 374))

    def test_172(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[2].c += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: [", 375))

    def test_173(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 49: :=", 376))

    def test_374(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 51: :=", 377))

    def test_375(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 51: :=", 378))

    def test_376(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            };                                                 
        }      
""","Error on line 3 col 12: func", 379))

    def test_377(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b; foo().a.b(); i := 1 {
                                            return; 
                                        }
                              3      };""","Error on line 3 col 49: ;", 380))

    def test_378(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b int; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 53: ;", 381))

    def test_379(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", 382))

    def test_380(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{{{1}}, ID, a, {b}}                              
                                        ""","successful", 383))

    def test_381(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a;
                                        ""","Error on line 2 col 49: ;", 384))
    def test_382(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", 385))

    def test_383(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", 386))

    def test_384(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {
                                            return;
                                        }
                                    };""","Error on line 3 col 40: {", 387))

    def test_385(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{a, b, {c}}                              
                                        ""","successful", 388))

    def test_386(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                            return;
                                    };""","successful", 389))