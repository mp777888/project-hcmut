# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0143")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\65\3\65\7\65\u014b\n\65\f")
        buf.write("\65\16\65\u014e\13\65\3\66\3\66\3\66\3\66\5\66\u0154\n")
        buf.write("\66\3\66\6\66\u0157\n\66\r\66\16\66\u0158\3\66\3\66\3")
        buf.write("\66\3\66\5\66\u015f\n\66\3\66\6\66\u0162\n\66\r\66\16")
        buf.write("\66\u0163\3\66\3\66\3\66\3\66\5\66\u016a\n\66\3\66\6\66")
        buf.write("\u016d\n\66\r\66\16\66\u016e\3\66\3\66\3\66\7\66\u0174")
        buf.write("\n\66\f\66\16\66\u0177\13\66\5\66\u0179\n\66\3\67\6\67")
        buf.write("\u017c\n\67\r\67\16\67\u017d\3\67\3\67\7\67\u0182\n\67")
        buf.write("\f\67\16\67\u0185\13\67\3\67\3\67\5\67\u0189\n\67\3\67")
        buf.write("\6\67\u018c\n\67\r\67\16\67\u018d\5\67\u0190\n\67\38\3")
        buf.write("8\38\78\u0195\n8\f8\168\u0198\138\38\38\39\39\39\3:\3")
        buf.write(":\3:\3:\7:\u01a3\n:\f:\16:\u01a6\13:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\7;\u01af\n;\f;\16;\u01b2\13;\3;\3;\3;\3;\3;\3<\5")
        buf.write("<\u01ba\n<\3<\3<\3<\3<\3=\6=\u01c1\n=\r=\16=\u01c2\3=")
        buf.write("\3=\3>\3>\3>\7>\u01ca\n>\f>\16>\u01cd\13>\3>\5>\u01d0")
        buf.write("\n>\3>\3>\3?\3?\3?\7?\u01d7\n?\f?\16?\u01da\13?\3?\3?")
        buf.write("\3?\3?\3@\3@\3@\3\u01b0\2A\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q\2s:u;w<y={>}?\177@\3\2\22\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62\63\3\2\629\5\2\62;CHch\3\2")
        buf.write("\62\62\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$")
        buf.write("$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2\13\13\16\17\"\"\4")
        buf.write("\2$$^^\4\3\f\f\17\17\2\u01fd\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081")
        buf.write("\3\2\2\2\5\u0085\3\2\2\2\7\u008b\3\2\2\2\t\u0092\3\2\2")
        buf.write("\2\13\u009c\3\2\2\2\r\u00a1\3\2\2\2\17\u00a6\3\2\2\2\21")
        buf.write("\u00a9\3\2\2\2\23\u00b1\3\2\2\2\25\u00b6\3\2\2\2\27\u00ba")
        buf.write("\3\2\2\2\31\u00c0\3\2\2\2\33\u00c7\3\2\2\2\35\u00cd\3")
        buf.write("\2\2\2\37\u00d6\3\2\2\2!\u00da\3\2\2\2#\u00e0\3\2\2\2")
        buf.write("%\u00e8\3\2\2\2\'\u00ef\3\2\2\2)\u00f1\3\2\2\2+\u00f3")
        buf.write("\3\2\2\2-\u00f5\3\2\2\2/\u00f7\3\2\2\2\61\u00f9\3\2\2")
        buf.write("\2\63\u00fb\3\2\2\2\65\u00fd\3\2\2\2\67\u00ff\3\2\2\2")
        buf.write("9\u0101\3\2\2\2;\u0103\3\2\2\2=\u0105\3\2\2\2?\u0107\3")
        buf.write("\2\2\2A\u0109\3\2\2\2C\u010b\3\2\2\2E\u010d\3\2\2\2G\u010f")
        buf.write("\3\2\2\2I\u0112\3\2\2\2K\u0115\3\2\2\2M\u0117\3\2\2\2")
        buf.write("O\u011a\3\2\2\2Q\u011c\3\2\2\2S\u011f\3\2\2\2U\u0122\3")
        buf.write("\2\2\2W\u0125\3\2\2\2Y\u0127\3\2\2\2[\u012a\3\2\2\2]\u012d")
        buf.write("\3\2\2\2_\u0130\3\2\2\2a\u0133\3\2\2\2c\u0136\3\2\2\2")
        buf.write("e\u0142\3\2\2\2g\u0144\3\2\2\2i\u0148\3\2\2\2k\u0178\3")
        buf.write("\2\2\2m\u017b\3\2\2\2o\u0191\3\2\2\2q\u019b\3\2\2\2s\u019e")
        buf.write("\3\2\2\2u\u01a9\3\2\2\2w\u01b9\3\2\2\2y\u01c0\3\2\2\2")
        buf.write("{\u01c6\3\2\2\2}\u01d3\3\2\2\2\177\u01df\3\2\2\2\u0081")
        buf.write("\u0082\7x\2\2\u0082\u0083\7c\2\2\u0083\u0084\7t\2\2\u0084")
        buf.write("\4\3\2\2\2\u0085\u0086\7e\2\2\u0086\u0087\7q\2\2\u0087")
        buf.write("\u0088\7p\2\2\u0088\u0089\7u\2\2\u0089\u008a\7v\2\2\u008a")
        buf.write("\6\3\2\2\2\u008b\u008c\7u\2\2\u008c\u008d\7v\2\2\u008d")
        buf.write("\u008e\7t\2\2\u008e\u008f\7w\2\2\u008f\u0090\7e\2\2\u0090")
        buf.write("\u0091\7v\2\2\u0091\b\3\2\2\2\u0092\u0093\7k\2\2\u0093")
        buf.write("\u0094\7p\2\2\u0094\u0095\7v\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\u0097\7t\2\2\u0097\u0098\7h\2\2\u0098\u0099\7c\2\2\u0099")
        buf.write("\u009a\7e\2\2\u009a\u009b\7g\2\2\u009b\n\3\2\2\2\u009c")
        buf.write("\u009d\7v\2\2\u009d\u009e\7{\2\2\u009e\u009f\7r\2\2\u009f")
        buf.write("\u00a0\7g\2\2\u00a0\f\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2")
        buf.write("\u00a3\7w\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7e\2\2\u00a5")
        buf.write("\16\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7h\2\2\u00a8")
        buf.write("\20\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7n\2\2\u00ab")
        buf.write("\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7\"\2\2\u00ae")
        buf.write("\u00af\7k\2\2\u00af\u00b0\7h\2\2\u00b0\22\3\2\2\2\u00b1")
        buf.write("\u00b2\7g\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4")
        buf.write("\u00b5\7g\2\2\u00b5\24\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7")
        buf.write("\u00b8\7q\2\2\u00b8\u00b9\7t\2\2\u00b9\26\3\2\2\2\u00ba")
        buf.write("\u00bb\7t\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7p\2\2\u00bd")
        buf.write("\u00be\7i\2\2\u00be\u00bf\7g\2\2\u00bf\30\3\2\2\2\u00c0")
        buf.write("\u00c1\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7w\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\32\3\2\2\2\u00c7\u00c8\7d\2\2\u00c8\u00c9\7t\2\2\u00c9")
        buf.write("\u00ca\7g\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7m\2\2\u00cc")
        buf.write("\34\3\2\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7q\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7p\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\36\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9 \3\2\2\2\u00da\u00db\7h\2\2\u00db")
        buf.write("\u00dc\7n\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7c\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\"\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1")
        buf.write("\u00e2\7q\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7n\2\2\u00e4")
        buf.write("\u00e5\7g\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write("$\3\2\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\u00ee\7i\2\2\u00ee&\3\2\2\2\u00ef\u00f0\7*\2\2\u00f0")
        buf.write("(\3\2\2\2\u00f1\u00f2\7+\2\2\u00f2*\3\2\2\2\u00f3\u00f4")
        buf.write("\7}\2\2\u00f4,\3\2\2\2\u00f5\u00f6\7\177\2\2\u00f6.\3")
        buf.write("\2\2\2\u00f7\u00f8\7]\2\2\u00f8\60\3\2\2\2\u00f9\u00fa")
        buf.write("\7_\2\2\u00fa\62\3\2\2\2\u00fb\u00fc\7.\2\2\u00fc\64\3")
        buf.write("\2\2\2\u00fd\u00fe\7=\2\2\u00fe\66\3\2\2\2\u00ff\u0100")
        buf.write("\7<\2\2\u01008\3\2\2\2\u0101\u0102\7\60\2\2\u0102:\3\2")
        buf.write("\2\2\u0103\u0104\7?\2\2\u0104<\3\2\2\2\u0105\u0106\7-")
        buf.write("\2\2\u0106>\3\2\2\2\u0107\u0108\7/\2\2\u0108@\3\2\2\2")
        buf.write("\u0109\u010a\7,\2\2\u010aB\3\2\2\2\u010b\u010c\7\61\2")
        buf.write("\2\u010cD\3\2\2\2\u010d\u010e\7\'\2\2\u010eF\3\2\2\2\u010f")
        buf.write("\u0110\7?\2\2\u0110\u0111\7?\2\2\u0111H\3\2\2\2\u0112")
        buf.write("\u0113\7#\2\2\u0113\u0114\7?\2\2\u0114J\3\2\2\2\u0115")
        buf.write("\u0116\7>\2\2\u0116L\3\2\2\2\u0117\u0118\7>\2\2\u0118")
        buf.write("\u0119\7?\2\2\u0119N\3\2\2\2\u011a\u011b\7@\2\2\u011b")
        buf.write("P\3\2\2\2\u011c\u011d\7@\2\2\u011d\u011e\7?\2\2\u011e")
        buf.write("R\3\2\2\2\u011f\u0120\7(\2\2\u0120\u0121\7(\2\2\u0121")
        buf.write("T\3\2\2\2\u0122\u0123\7~\2\2\u0123\u0124\7~\2\2\u0124")
        buf.write("V\3\2\2\2\u0125\u0126\7#\2\2\u0126X\3\2\2\2\u0127\u0128")
        buf.write("\7<\2\2\u0128\u0129\7?\2\2\u0129Z\3\2\2\2\u012a\u012b")
        buf.write("\7-\2\2\u012b\u012c\7?\2\2\u012c\\\3\2\2\2\u012d\u012e")
        buf.write("\7/\2\2\u012e\u012f\7?\2\2\u012f^\3\2\2\2\u0130\u0131")
        buf.write("\7,\2\2\u0131\u0132\7?\2\2\u0132`\3\2\2\2\u0133\u0134")
        buf.write("\7\61\2\2\u0134\u0135\7?\2\2\u0135b\3\2\2\2\u0136\u0137")
        buf.write("\7\'\2\2\u0137\u0138\7?\2\2\u0138d\3\2\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a\u013b\7t\2\2\u013b\u013c\7w\2\2\u013c\u0143")
        buf.write("\7g\2\2\u013d\u013e\7h\2\2\u013e\u013f\7c\2\2\u013f\u0140")
        buf.write("\7n\2\2\u0140\u0141\7u\2\2\u0141\u0143\7g\2\2\u0142\u0139")
        buf.write("\3\2\2\2\u0142\u013d\3\2\2\2\u0143f\3\2\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7k\2\2\u0146\u0147\7n\2\2\u0147h\3")
        buf.write("\2\2\2\u0148\u014c\t\2\2\2\u0149\u014b\t\3\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014dj\3\2\2\2\u014e\u014c\3\2\2\2\u014f")
        buf.write("\u0150\7\62\2\2\u0150\u0154\7d\2\2\u0151\u0152\7\62\2")
        buf.write("\2\u0152\u0154\7D\2\2\u0153\u014f\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0157\t\4\2\2\u0156")
        buf.write("\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0158\u0159\3\2\2\2\u0159\u0179\3\2\2\2\u015a\u015b\7")
        buf.write("\62\2\2\u015b\u015f\7q\2\2\u015c\u015d\7\62\2\2\u015d")
        buf.write("\u015f\7Q\2\2\u015e\u015a\3\2\2\2\u015e\u015c\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u0162\t\5\2\2\u0161\u0160\3")
        buf.write("\2\2\2\u0162\u0163\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0179\3\2\2\2\u0165\u0166\7\62\2\2\u0166")
        buf.write("\u016a\7z\2\2\u0167\u0168\7\62\2\2\u0168\u016a\7Z\2\2")
        buf.write("\u0169\u0165\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\3")
        buf.write("\2\2\2\u016b\u016d\t\6\2\2\u016c\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0179\3\2\2\2\u0170\u0179\t\7\2\2\u0171\u0175\t\b\2\2")
        buf.write("\u0172\u0174\t\t\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0179")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0153\3\2\2\2\u0178")
        buf.write("\u015e\3\2\2\2\u0178\u0169\3\2\2\2\u0178\u0170\3\2\2\2")
        buf.write("\u0178\u0171\3\2\2\2\u0179l\3\2\2\2\u017a\u017c\t\t\2")
        buf.write("\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0183\59\35\2\u0180\u0182\t\t\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184\u018f\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0188")
        buf.write("\t\n\2\2\u0187\u0189\t\13\2\2\u0188\u0187\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u018c\t\t\2\2")
        buf.write("\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3")
        buf.write("\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u0186")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190n\3\2\2\2\u0191\u0196")
        buf.write("\7$\2\2\u0192\u0195\n\f\2\2\u0193\u0195\5q9\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0199\u019a\7$\2\2\u019ap\3\2\2\2")
        buf.write("\u019b\u019c\7^\2\2\u019c\u019d\t\r\2\2\u019dr\3\2\2\2")
        buf.write("\u019e\u019f\7\61\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a4")
        buf.write("\3\2\2\2\u01a1\u01a3\n\16\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a7\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a8\b")
        buf.write(":\2\2\u01a8t\3\2\2\2\u01a9\u01aa\7\61\2\2\u01aa\u01ab")
        buf.write("\7,\2\2\u01ab\u01b0\3\2\2\2\u01ac\u01af\5u;\2\u01ad\u01af")
        buf.write("\13\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("\u01b2\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\7")
        buf.write(",\2\2\u01b4\u01b5\7\61\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7")
        buf.write("\b;\2\2\u01b7v\3\2\2\2\u01b8\u01ba\7\17\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bc\7\f\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\b<\3\2")
        buf.write("\u01bex\3\2\2\2\u01bf\u01c1\t\17\2\2\u01c0\u01bf\3\2\2")
        buf.write("\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b=\2\2\u01c5")
        buf.write("z\3\2\2\2\u01c6\u01cb\7$\2\2\u01c7\u01ca\5q9\2\u01c8\u01ca")
        buf.write("\n\20\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d0\t")
        buf.write("\21\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d2\b>\4\2\u01d2|\3\2\2\2\u01d3\u01d8\7$\2\2\u01d4")
        buf.write("\u01d7\n\20\2\2\u01d5\u01d7\5q9\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u01dc\7^\2\2\u01dc\u01dd\n\r\2\2\u01dd")
        buf.write("\u01de\b?\5\2\u01de~\3\2\2\2\u01df\u01e0\13\2\2\2\u01e0")
        buf.write("\u01e1\b@\6\2\u01e1\u0080\3\2\2\2\36\2\u0142\u014c\u0153")
        buf.write("\u0158\u015e\u0163\u0169\u016e\u0175\u0178\u017d\u0183")
        buf.write("\u0188\u018d\u018f\u0194\u0196\u01a4\u01ae\u01b0\u01b9")
        buf.write("\u01c2\u01c9\u01cb\u01cf\u01d6\u01d8\7\b\2\2\3<\2\3>\3")
        buf.write("\3?\4\3@\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    CONST = 2
    STRUCT = 3
    INTERFACE = 4
    TYPE = 5
    FUNC = 6
    IF = 7
    ELSEIF = 8
    ELSE = 9
    FOR = 10
    RANGE = 11
    RETURN = 12
    BREAK = 13
    CONTINUE = 14
    INT = 15
    FLOAT = 16
    BOOLEAN = 17
    STRING = 18
    LPAREN = 19
    RPAREN = 20
    LBRACE = 21
    RBRACE = 22
    LBRACK = 23
    RBRACK = 24
    COMMA = 25
    SEMI = 26
    COLON = 27
    DOT = 28
    EQUAL = 29
    PLUS = 30
    MINUS = 31
    MULT = 32
    DIV = 33
    MOD = 34
    EQ = 35
    NEQ = 36
    LT = 37
    LTE = 38
    GT = 39
    GTE = 40
    AND = 41
    OR = 42
    NOT = 43
    ASSIGN = 44
    PLUS_ASSIGN = 45
    MINUS_ASSIGN = 46
    MULT_ASSIGN = 47
    DIV_ASSIGN = 48
    MOD_ASSIGN = 49
    BOOLLIT = 50
    NILLIT = 51
    ID = 52
    INTLIT = 53
    FLOATLIT = 54
    STRINGLIT = 55
    COMMENT = 56
    MULTILINE_COMMENT = 57
    NEWLINE = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'const'", "'struct'", "'interface'", "'type'", "'func'", 
            "'if'", "'else if'", "'else'", "'for'", "'range'", "'return'", 
            "'break'", "'continue'", "'int'", "'float'", "'boolean'", "'string'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'", 
            "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "':='", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "CONST", "STRUCT", "INTERFACE", "TYPE", "FUNC", "IF", 
            "ELSEIF", "ELSE", "FOR", "RANGE", "RETURN", "BREAK", "CONTINUE", 
            "INT", "FLOAT", "BOOLEAN", "STRING", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", "COLON", "DOT", 
            "EQUAL", "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQ", "NEQ", 
            "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", "ASSIGN", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "BOOLLIT", 
            "NILLIT", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "COMMENT", 
            "MULTILINE_COMMENT", "NEWLINE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "VAR", "CONST", "STRUCT", "INTERFACE", "TYPE", "FUNC", 
                  "IF", "ELSEIF", "ELSE", "FOR", "RANGE", "RETURN", "BREAK", 
                  "CONTINUE", "INT", "FLOAT", "BOOLEAN", "STRING", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", 
                  "SEMI", "COLON", "DOT", "EQUAL", "PLUS", "MINUS", "MULT", 
                  "DIV", "MOD", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "AND", 
                  "OR", "NOT", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                  "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "BOOLLIT", 
                  "NILLIT", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "ESC_SEQ", 
                  "COMMENT", "MULTILINE_COMMENT", "NEWLINE", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();

    lastToken = None

    def nextToken(self):
        token = super().nextToken()
        while token.channel == Token.HIDDEN_CHANNEL:
            token = super().nextToken()
        self.lastToken = token
        return token

    def InsertSemi(self):
        ttype = self.lastToken.type if self.lastToken is not None else -1
        allowed = [
            MiniGoLexer.ID, MiniGoLexer.FLOAT, MiniGoLexer.INT, MiniGoLexer.STRING, MiniGoLexer.BOOLEAN,
            MiniGoLexer.INTLIT, MiniGoLexer.FLOATLIT, MiniGoLexer.NILLIT,
            MiniGoLexer.STRINGLIT, MiniGoLexer.BOOLLIT, MiniGoLexer.RETURN,
            MiniGoLexer.CONTINUE, MiniGoLexer.BREAK, MiniGoLexer.RBRACE,
            MiniGoLexer.RPAREN, MiniGoLexer.RBRACK
        ]
        return ttype in allowed


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.NEWLINE_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.InsertSemi():
                   self.text = ';'
                else:
                   self.skip()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                index = self.text.find('\n')
                pos_of_r = self.text.find('\r')
                if  pos_of_r <= index - 1 and pos_of_r >0:
                    raise UncloseString(self.text[:pos_of_r ])
                else:
                    if index != -1:
                        raise UncloseString(self.text[:index])
                    else:
                        raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text) ;

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text)
     


