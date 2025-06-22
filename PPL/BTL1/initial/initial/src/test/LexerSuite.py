import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>", 1001))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>", 1002))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>", 1003))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_VOTien","_VOTien,<EOF>", 1004))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>", 1005))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11","0x11,<EOF>", 1006))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 1007))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", 1008))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN","<EOF>", 1009))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", 1010))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 1011))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", 1012))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", 1013))
        
    #!!! 87 test yêu cầu code chấm sau
    def test_014(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", 1014))

    def test_015(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", 1015))

    def test_016(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 1016))

    def test_017(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 1017))

    def test_018(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 1018))

    def test_019(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /*
        /* a */ /* b */ 
        // 321231
        */ if /* */ /* */""", "if,<EOF>", 1019))

    def test_020(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /*
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", 1020))

    def test_021(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /* //123312
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", 1022))

    def test_022(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/*", "/,*,<EOF>", 1023))

    def test_023(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 1024))

    def test_024(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 1025))

    def test_025(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 1026))

    def test_026(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 1027))

    def test_027(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("A_2b_3", "A_2b_3,<EOF>", 1029))

    def test_028(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_a__", "_a__,<EOF>", 1030))

    def test_029(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("u_2_bB", "u_2_bB,<EOF>", 1031))

    def test_030(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0452.", "0452.,<EOF>", 1032))

    def test_031(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>", 1033))

    def test_032(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("012", "0,12,<EOF>", 1034))

    def test_033(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1_2", "1,_2,<EOF>", 1035))

    def test_034(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 1036))

    def test_035(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-12", "-,12,<EOF>", 1037))

    def test_036(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b000", "0b000,<EOF>", 1038))

    def test_037(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1e", "0b1,e,<EOF>", 1039))

    def test_038(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b12", "0b1,2,<EOF>", 1040))

    def test_039(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1101", "0b1101,<EOF>", 1041))

    def test_040(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0B111", "0B111,<EOF>", 1042))

    def test_041(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00O72", "0,0O72,<EOF>", 1043))

    def test_042(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0O72", "-,0O72,<EOF>", 1044))

    def test_043(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0o18", "0o1,8,<EOF>", 1045))

    def test_044(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0o12", "0o12,<EOF>", 1046))

    def test_045(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0Oo1", "0,Oo1,<EOF>", 1047))

    def test_046(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0x2g", "-,0x2,g,<EOF>", 1048))

    def test_047(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0X0cb", "0X0cb,<EOF>", 1049))

    def test_048(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0xae2", "0xae2,<EOF>", 1050))

    def test_049(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0Xx2", "0,Xx2,<EOF>", 1051))

    def test_050(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-020", "010.010e-020,<EOF>", 1052))

    def test_051(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2e+-2", "1.2,e,+,-,2,<EOF>", 1053))

    def test_052(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2Ee2", "1.2,Ee2,<EOF>", 1054))

    def test_053(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("09.e-002", "09.e-002,<EOF>", 1055))

    def test_054(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2", "1.e-2,<EOF>", 1056))

    def test_055(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e2", "1.e2,<EOF>", 1057))

    def test_056(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e", "1.,e,<EOF>", 1058))

    def test_057(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 1059))

    def test_058(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00.1e2", "00.1e2,<EOF>", 1060))

    def test_059(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme(".e+2", ".,e,+,2,<EOF>", 1061))

    def test_060(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 1062))

    def test_061(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "votien" """, "\"votien\",<EOF>", 1063))

    def test_062(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r" """, "\"\\r\",<EOF>", 1064))

    def test_063(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\n" """, "\"\\n\",<EOF>", 1065))

    def test_064(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\" """, "\"\\\\\",<EOF>", 1066))

    def test_065(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\"" """, "\"\\\"\",<EOF>", 1067))

    def test_066(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "a \\r a" """, "\"a \\r a\",<EOF>", 1068))

    def test_067(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", 1069))

    def test_068(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """, "\"\",<EOF>", 1070))

    def test_069(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" ^ """, "ErrorToken ^", 1072))

    def test_070(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" /* @@ * */ """, "<EOF>", 1073))

    def test_071(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" 
        /* a * */
 """, "<EOF>", 1074))

    def test_072(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" // /* */  """, "<EOF>", 1075))

    def test_073(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" // /*
                                       */""", "*,/,<EOF>", 1076))

    def test_074(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" 
        /* */ /* */ /*a // */ b""", "b,<EOF>", 1077))

    def test_075(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* a */ */ b """, "*,/,b,<EOF>", 1078))

    def test_076(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* /* */ a """, "a,<EOF>", 1079))

    def test_077(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* a /* b */ */ c /* */""", "c,<EOF>", 1080))

    def test_078(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* test */ a /* */ """, "a,<EOF>", 1081))

    def test_079(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme("""
        /* test
        */ a /* */
""", "a,;,<EOF>", 1082))

    def test_080(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" 
    // // //
 """, "<EOF>", 1083))

    def test_081(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme("""
// // // """, "<EOF>", 1084))

    def test_082(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" // // // """, "<EOF>", 1085))

    def test_083(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 1086))

    def test_084(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 1087))

    def test_085(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 1088))

    def test_086(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 1089))

    def test_087(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 1090))

    def test_088(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("#", "ErrorToken #", 1091))

    def test_089(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("\\", "ErrorToken \\", 1092))

    def test_090(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("&", "ErrorToken &", 1093))

    def test_091(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" 123" """, "123,Unclosed string: \" ", 1094))

    def test_092(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123""", "Unclosed string: \"123", 1095))

    def test_093(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123 \\n \n" """, "Unclosed string: \"123 \\n ", 1096))

    def test_094(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123
        " """, "Unclosed string: \"123", 1097))

    def test_095(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123\n" """, "Unclosed string: \"123", 1098))

    def test_096(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\" \\\\ \\q" """, "Illegal escape in string: \"\\\" \\\\ \\q", 1099))

    def test_097(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "&\\&" """, "Illegal escape in string: \"&\\&", 1100))

    def test_098(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\z" """, "Illegal escape in string: \"\\z", 1101))

    def test_099(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\0" """, "Illegal escape in string: \"\\0", 1102))

    def test_100(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\b" """, "Illegal escape in string: \"\\b", 1103))

    def test_101(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            1
""", "1,;,<EOF>", 1104))
        
    def test_102(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            0x1
""", "0x1,;,<EOF>", 1105))
        
    def test_103(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            "s"
""", "\"s\",;,<EOF>", 1106))
        
    def test_104(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            true
""", "true,;,<EOF>", 1107))
        
    def test_105(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            2.
""", "2.,;,<EOF>", 1108))

    def test_106(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            ID
""", "ID,;,<EOF>", 1109))


    def test_107(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            return
""", "return,;,<EOF>", 1110))

    def test_108(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            continue
            break
""", "continue,;,break,;,<EOF>", 1111))

    def test_109(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            if
            }
            ]
            )
""", "if,},;,],;,),;,<EOF>", 1112))

    def test_110(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1113))
        
    def test_111(self):
        self.assertTrue(TestLexer.checkLexeme("""
            1e+7
""", "1,e,+,7,;,<EOF>", 1114))
        
    def test_112(self):
        self.assertTrue(TestLexer.checkLexeme("""
           \"12\"\"
""", "\"12\",Unclosed string: \"", 1115))
        
    def test_113(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1116))
        
    def test_114(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1117))
        
    def test_115(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1118))
        
    def test_116(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1119))
        
    def test_117(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1120))
        
    def test_118(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil\n/*
*/""", "nil,;,<EOF>", 1121))
    
    def test_119(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil/*
*/\n""", "nil,;,<EOF>", 1122))
        
    def test_120(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil/*
*/""", "nil,<EOF>", 1123))
        
    def test_121(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 1124))