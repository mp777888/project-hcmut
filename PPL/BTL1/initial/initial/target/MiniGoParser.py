# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u02f6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4")
        buf.write("\u00dd\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00e5\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u00f1\n\7\3\b\3")
        buf.write("\b\3\b\5\b\u00f6\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00ff")
        buf.write("\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u0109\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0111\n\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u0120\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u0130\n\23\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u013d")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0148\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\5\33\u0157\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\5\35\u0160\n\35\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\5\37\u0168\n\37\3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\5#\u0181\n#\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\5")
        buf.write("&\u0190\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u019a\n(\3)")
        buf.write("\3)\3)\3)\5)\u01a0\n)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5")
        buf.write("*\u01ac\n*\3+\3+\3+\3+\3+\3,\3,\3,\5,\u01b6\n,\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01ca")
        buf.write("\n/\3\60\3\60\3\60\5\60\u01cf\n\60\3\61\3\61\3\61\5\61")
        buf.write("\u01d4\n\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63\u01dd")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u01f9\n\66\3\67\3\67\3")
        buf.write("\67\3\67\38\38\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3<")
        buf.write("\3<\5<\u020f\n<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\5@\u021c")
        buf.write("\n@\3A\3A\3A\3B\3B\3B\3B\3B\5B\u0226\nB\3C\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\5D\u0230\nD\3E\3E\3E\3F\3F\3F\3F\3F\5F\u023a")
        buf.write("\nF\3G\3G\3H\3H\3H\3I\3I\3I\3I\3I\5I\u0246\nI\3J\3J\3")
        buf.write("K\3K\3K\3L\3L\3L\3L\3L\5L\u0252\nL\3M\3M\3N\3N\3N\3N\5")
        buf.write("N\u025a\nN\3O\3O\3P\3P\3P\3Q\3Q\3Q\3Q\5Q\u0265\nQ\3R\3")
        buf.write("R\3R\3R\3R\3R\5R\u026d\nR\3S\3S\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\5S\u027c\nS\3T\3T\3T\3T\3T\3U\3U\3U\3V\3V\3")
        buf.write("V\3V\3V\5V\u028b\nV\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\5")
        buf.write("W\u0298\nW\3X\3X\5X\u029c\nX\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3")
        buf.write("Z\3Z\5Z\u02a8\nZ\3[\3[\3[\3[\3[\3[\5[\u02b0\n[\3\\\3\\")
        buf.write("\3\\\3]\3]\3]\3]\3]\3]\3]\3^\3^\3^\5^\u02bf\n^\3_\3_\5")
        buf.write("_\u02c3\n_\3`\3`\3`\3a\3a\3a\3a\3a\5a\u02cd\na\3b\3b\3")
        buf.write("b\3b\3b\3c\3c\3c\3d\3d\3d\3d\3e\3e\5e\u02dd\ne\3f\3f\3")
        buf.write("f\3f\5f\u02e3\nf\3g\3g\3g\3g\3g\3h\3h\3h\3h\3h\3h\5h\u02f0")
        buf.write("\nh\3i\3i\3i\3i\3i\2\2j\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write("\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0")
        buf.write("\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2")
        buf.write("\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\2\n\3\2\21")
        buf.write("\24\3\2\66\67\4\2\34\34<<\3\2.\63\3\2%*\3\2 !\3\2\"$\4")
        buf.write("\2!!--\2\u02dd\2\u00d2\3\2\2\2\4\u00d5\3\2\2\2\6\u00dc")
        buf.write("\3\2\2\2\b\u00e4\3\2\2\2\n\u00e6\3\2\2\2\f\u00f0\3\2\2")
        buf.write("\2\16\u00f5\3\2\2\2\20\u00f7\3\2\2\2\22\u00fe\3\2\2\2")
        buf.write("\24\u0100\3\2\2\2\26\u0108\3\2\2\2\30\u0110\3\2\2\2\32")
        buf.write("\u0112\3\2\2\2\34\u0114\3\2\2\2\36\u011f\3\2\2\2 \u0121")
        buf.write("\3\2\2\2\"\u0127\3\2\2\2$\u012f\3\2\2\2&\u0131\3\2\2\2")
        buf.write("(\u0133\3\2\2\2*\u013c\3\2\2\2,\u013e\3\2\2\2.\u0147\3")
        buf.write("\2\2\2\60\u0149\3\2\2\2\62\u014d\3\2\2\2\64\u0156\3\2")
        buf.write("\2\2\66\u0158\3\2\2\28\u015f\3\2\2\2:\u0161\3\2\2\2<\u0167")
        buf.write("\3\2\2\2>\u0169\3\2\2\2@\u016b\3\2\2\2B\u0175\3\2\2\2")
        buf.write("D\u0180\3\2\2\2F\u0182\3\2\2\2H\u0187\3\2\2\2J\u018f\3")
        buf.write("\2\2\2L\u0191\3\2\2\2N\u0199\3\2\2\2P\u019f\3\2\2\2R\u01ab")
        buf.write("\3\2\2\2T\u01ad\3\2\2\2V\u01b5\3\2\2\2X\u01b7\3\2\2\2")
        buf.write("Z\u01b9\3\2\2\2\\\u01c9\3\2\2\2^\u01ce\3\2\2\2`\u01d3")
        buf.write("\3\2\2\2b\u01d5\3\2\2\2d\u01dc\3\2\2\2f\u01de\3\2\2\2")
        buf.write("h\u01e7\3\2\2\2j\u01f8\3\2\2\2l\u01fa\3\2\2\2n\u01fe\3")
        buf.write("\2\2\2p\u0200\3\2\2\2r\u0204\3\2\2\2t\u0208\3\2\2\2v\u020e")
        buf.write("\3\2\2\2x\u0210\3\2\2\2z\u0213\3\2\2\2|\u0216\3\2\2\2")
        buf.write("~\u021b\3\2\2\2\u0080\u021d\3\2\2\2\u0082\u0225\3\2\2")
        buf.write("\2\u0084\u0227\3\2\2\2\u0086\u022f\3\2\2\2\u0088\u0231")
        buf.write("\3\2\2\2\u008a\u0239\3\2\2\2\u008c\u023b\3\2\2\2\u008e")
        buf.write("\u023d\3\2\2\2\u0090\u0245\3\2\2\2\u0092\u0247\3\2\2\2")
        buf.write("\u0094\u0249\3\2\2\2\u0096\u0251\3\2\2\2\u0098\u0253\3")
        buf.write("\2\2\2\u009a\u0259\3\2\2\2\u009c\u025b\3\2\2\2\u009e\u025d")
        buf.write("\3\2\2\2\u00a0\u0264\3\2\2\2\u00a2\u026c\3\2\2\2\u00a4")
        buf.write("\u027b\3\2\2\2\u00a6\u027d\3\2\2\2\u00a8\u0282\3\2\2\2")
        buf.write("\u00aa\u028a\3\2\2\2\u00ac\u0297\3\2\2\2\u00ae\u029b\3")
        buf.write("\2\2\2\u00b0\u029d\3\2\2\2\u00b2\u02a7\3\2\2\2\u00b4\u02af")
        buf.write("\3\2\2\2\u00b6\u02b1\3\2\2\2\u00b8\u02b4\3\2\2\2\u00ba")
        buf.write("\u02be\3\2\2\2\u00bc\u02c2\3\2\2\2\u00be\u02c4\3\2\2\2")
        buf.write("\u00c0\u02cc\3\2\2\2\u00c2\u02ce\3\2\2\2\u00c4\u02d3\3")
        buf.write("\2\2\2\u00c6\u02d6\3\2\2\2\u00c8\u02dc\3\2\2\2\u00ca\u02e2")
        buf.write("\3\2\2\2\u00cc\u02e4\3\2\2\2\u00ce\u02ef\3\2\2\2\u00d0")
        buf.write("\u02f1\3\2\2\2\u00d2\u00d3\5\4\3\2\u00d3\u00d4\7\2\2\3")
        buf.write("\u00d4\3\3\2\2\2\u00d5\u00d6\5\b\5\2\u00d6\u00d7\5\6\4")
        buf.write("\2\u00d7\5\3\2\2\2\u00d8\u00d9\5\b\5\2\u00d9\u00da\5\6")
        buf.write("\4\2\u00da\u00dd\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00d8")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\7\3\2\2\2\u00de\u00e5")
        buf.write("\5B\"\2\u00df\u00e5\5@!\2\u00e0\u00e5\5\n\6\2\u00e1\u00e5")
        buf.write("\5\34\17\2\u00e2\u00e5\5\66\34\2\u00e3\u00e5\7<\2\2\u00e4")
        buf.write("\u00de\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4\u00e0\3\2\2\2")
        buf.write("\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3")
        buf.write("\2\2\2\u00e5\t\3\2\2\2\u00e6\u00e7\7\3\2\2\u00e7\u00e8")
        buf.write("\5\20\t\2\u00e8\u00e9\5\f\7\2\u00e9\u00ea\5> \2\u00ea")
        buf.write("\13\3\2\2\2\u00eb\u00ec\5\30\r\2\u00ec\u00ed\5\16\b\2")
        buf.write("\u00ed\u00f1\3\2\2\2\u00ee\u00ef\7\37\2\2\u00ef\u00f1")
        buf.write("\5\24\13\2\u00f0\u00eb\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1")
        buf.write("\r\3\2\2\2\u00f2\u00f3\7\37\2\2\u00f3\u00f6\5\24\13\2")
        buf.write("\u00f4\u00f6\3\2\2\2\u00f5\u00f2\3\2\2\2\u00f5\u00f4\3")
        buf.write("\2\2\2\u00f6\17\3\2\2\2\u00f7\u00f8\7\66\2\2\u00f8\u00f9")
        buf.write("\5\22\n\2\u00f9\21\3\2\2\2\u00fa\u00fb\7\33\2\2\u00fb")
        buf.write("\u00fc\7\66\2\2\u00fc\u00ff\5\22\n\2\u00fd\u00ff\3\2\2")
        buf.write("\2\u00fe\u00fa\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\23\3")
        buf.write("\2\2\2\u0100\u0101\5\u0080A\2\u0101\u0102\5\26\f\2\u0102")
        buf.write("\25\3\2\2\2\u0103\u0104\7\33\2\2\u0104\u0105\5\u0080A")
        buf.write("\2\u0105\u0106\5\26\f\2\u0106\u0109\3\2\2\2\u0107\u0109")
        buf.write("\3\2\2\2\u0108\u0103\3\2\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\27\3\2\2\2\u010a\u0111\7\21\2\2\u010b\u0111\7\22\2\2")
        buf.write("\u010c\u0111\7\24\2\2\u010d\u0111\7\23\2\2\u010e\u0111")
        buf.write("\5 \21\2\u010f\u0111\5&\24\2\u0110\u010a\3\2\2\2\u0110")
        buf.write("\u010b\3\2\2\2\u0110\u010c\3\2\2\2\u0110\u010d\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\31\3\2")
        buf.write("\2\2\u0112\u0113\t\2\2\2\u0113\33\3\2\2\2\u0114\u0115")
        buf.write("\7\4\2\2\u0115\u0116\5\20\t\2\u0116\u0117\5\36\20\2\u0117")
        buf.write("\u0118\5> \2\u0118\35\3\2\2\2\u0119\u011a\5\30\r\2\u011a")
        buf.write("\u011b\7\37\2\2\u011b\u011c\5\24\13\2\u011c\u0120\3\2")
        buf.write("\2\2\u011d\u011e\7\37\2\2\u011e\u0120\5\24\13\2\u011f")
        buf.write("\u0119\3\2\2\2\u011f\u011d\3\2\2\2\u0120\37\3\2\2\2\u0121")
        buf.write("\u0122\7\31\2\2\u0122\u0123\5\"\22\2\u0123\u0124\7\32")
        buf.write("\2\2\u0124\u0125\5$\23\2\u0125\u0126\5\30\r\2\u0126!\3")
        buf.write("\2\2\2\u0127\u0128\t\3\2\2\u0128#\3\2\2\2\u0129\u012a")
        buf.write("\7\31\2\2\u012a\u012b\5\"\22\2\u012b\u012c\7\32\2\2\u012c")
        buf.write("\u012d\5$\23\2\u012d\u0130\3\2\2\2\u012e\u0130\3\2\2\2")
        buf.write("\u012f\u0129\3\2\2\2\u012f\u012e\3\2\2\2\u0130%\3\2\2")
        buf.write("\2\u0131\u0132\7\66\2\2\u0132\'\3\2\2\2\u0133\u0134\7")
        buf.write("\5\2\2\u0134\u0135\7\27\2\2\u0135\u0136\5*\26\2\u0136")
        buf.write("\u0137\7\30\2\2\u0137)\3\2\2\2\u0138\u0139\5\60\31\2\u0139")
        buf.write("\u013a\5*\26\2\u013a\u013d\3\2\2\2\u013b\u013d\5\60\31")
        buf.write("\2\u013c\u0138\3\2\2\2\u013c\u013b\3\2\2\2\u013d+\3\2")
        buf.write("\2\2\u013e\u013f\7\6\2\2\u013f\u0140\7\27\2\2\u0140\u0141")
        buf.write("\5.\30\2\u0141\u0142\7\30\2\2\u0142-\3\2\2\2\u0143\u0144")
        buf.write("\5\62\32\2\u0144\u0145\5.\30\2\u0145\u0148\3\2\2\2\u0146")
        buf.write("\u0148\5\62\32\2\u0147\u0143\3\2\2\2\u0147\u0146\3\2\2")
        buf.write("\2\u0148/\3\2\2\2\u0149\u014a\7\66\2\2\u014a\u014b\5\30")
        buf.write("\r\2\u014b\u014c\5> \2\u014c\61\3\2\2\2\u014d\u014e\7")
        buf.write("\66\2\2\u014e\u014f\7\25\2\2\u014f\u0150\5D#\2\u0150\u0151")
        buf.write("\7\26\2\2\u0151\u0152\5\64\33\2\u0152\u0153\5> \2\u0153")
        buf.write("\63\3\2\2\2\u0154\u0157\5\30\r\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157\65\3\2\2\2\u0158")
        buf.write("\u0159\7\7\2\2\u0159\u015a\7\66\2\2\u015a\u015b\58\35")
        buf.write("\2\u015b\u015c\5> \2\u015c\67\3\2\2\2\u015d\u0160\5(\25")
        buf.write("\2\u015e\u0160\5,\27\2\u015f\u015d\3\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u01609\3\2\2\2\u0161\u0162\7<\2\2\u0162\u0163")
        buf.write("\5<\37\2\u0163;\3\2\2\2\u0164\u0165\7<\2\2\u0165\u0168")
        buf.write("\5<\37\2\u0166\u0168\3\2\2\2\u0167\u0164\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168=\3\2\2\2\u0169\u016a\t\4\2\2\u016a")
        buf.write("?\3\2\2\2\u016b\u016c\7\b\2\2\u016c\u016d\5F$\2\u016d")
        buf.write("\u016e\7\66\2\2\u016e\u016f\7\25\2\2\u016f\u0170\5D#\2")
        buf.write("\u0170\u0171\7\26\2\2\u0171\u0172\5\64\33\2\u0172\u0173")
        buf.write("\5r:\2\u0173\u0174\5> \2\u0174A\3\2\2\2\u0175\u0176\7")
        buf.write("\b\2\2\u0176\u0177\7\66\2\2\u0177\u0178\7\25\2\2\u0178")
        buf.write("\u0179\5D#\2\u0179\u017a\7\26\2\2\u017a\u017b\5\64\33")
        buf.write("\2\u017b\u017c\5r:\2\u017c\u017d\5> \2\u017dC\3\2\2\2")
        buf.write("\u017e\u0181\5H%\2\u017f\u0181\3\2\2\2\u0180\u017e\3\2")
        buf.write("\2\2\u0180\u017f\3\2\2\2\u0181E\3\2\2\2\u0182\u0183\7")
        buf.write("\25\2\2\u0183\u0184\7\66\2\2\u0184\u0185\7\66\2\2\u0185")
        buf.write("\u0186\7\26\2\2\u0186G\3\2\2\2\u0187\u0188\5L\'\2\u0188")
        buf.write("\u0189\5J&\2\u0189I\3\2\2\2\u018a\u018b\7\33\2\2\u018b")
        buf.write("\u018c\5L\'\2\u018c\u018d\5J&\2\u018d\u0190\3\2\2\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u018a\3\2\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190K\3\2\2\2\u0191\u0192\7\66\2\2\u0192\u0193\5N(\2")
        buf.write("\u0193\u0194\5\30\r\2\u0194M\3\2\2\2\u0195\u0196\7\33")
        buf.write("\2\2\u0196\u0197\7\66\2\2\u0197\u019a\5N(\2\u0198\u019a")
        buf.write("\3\2\2\2\u0199\u0195\3\2\2\2\u0199\u0198\3\2\2\2\u019a")
        buf.write("O\3\2\2\2\u019b\u019c\5R*\2\u019c\u019d\5P)\2\u019d\u01a0")
        buf.write("\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019b\3\2\2\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0Q\3\2\2\2\u01a1\u01ac\5\n\6\2\u01a2")
        buf.write("\u01ac\5\34\17\2\u01a3\u01ac\5T+\2\u01a4\u01ac\5Z.\2\u01a5")
        buf.write("\u01ac\5`\61\2\u01a6\u01ac\5t;\2\u01a7\u01ac\5x=\2\u01a8")
        buf.write("\u01ac\5z>\2\u01a9\u01ac\5|?\2\u01aa\u01ac\7<\2\2\u01ab")
        buf.write("\u01a1\3\2\2\2\u01ab\u01a2\3\2\2\2\u01ab\u01a3\3\2\2\2")
        buf.write("\u01ab\u01a4\3\2\2\2\u01ab\u01a5\3\2\2\2\u01ab\u01a6\3")
        buf.write("\2\2\2\u01ab\u01a7\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01aa\3\2\2\2\u01acS\3\2\2\2\u01ad\u01ae")
        buf.write("\5V,\2\u01ae\u01af\5X-\2\u01af\u01b0\5\u0080A\2\u01b0")
        buf.write("\u01b1\5> \2\u01b1U\3\2\2\2\u01b2\u01b6\7\66\2\2\u01b3")
        buf.write("\u01b6\5\u00c4c\2\u01b4\u01b6\5\u00c6d\2\u01b5\u01b2\3")
        buf.write("\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6W")
        buf.write("\3\2\2\2\u01b7\u01b8\t\5\2\2\u01b8Y\3\2\2\2\u01b9\u01ba")
        buf.write("\7\t\2\2\u01ba\u01bb\7\25\2\2\u01bb\u01bc\5\u0080A\2\u01bc")
        buf.write("\u01bd\7\26\2\2\u01bd\u01be\5r:\2\u01be\u01bf\5\\/\2\u01bf")
        buf.write("\u01c0\5^\60\2\u01c0[\3\2\2\2\u01c1\u01c2\7\n\2\2\u01c2")
        buf.write("\u01c3\7\25\2\2\u01c3\u01c4\5\u0080A\2\u01c4\u01c5\7\26")
        buf.write("\2\2\u01c5\u01c6\5r:\2\u01c6\u01c7\5\\/\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c1\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca]\3\2\2\2\u01cb\u01cc\7\13\2\2\u01cc")
        buf.write("\u01cf\5r:\2\u01cd\u01cf\3\2\2\2\u01ce\u01cb\3\2\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf_\3\2\2\2\u01d0\u01d4\5b\62\2\u01d1")
        buf.write("\u01d4\5f\64\2\u01d2\u01d4\5h\65\2\u01d3\u01d0\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4a\3\2\2")
        buf.write("\2\u01d5\u01d6\7\f\2\2\u01d6\u01d7\5n8\2\u01d7\u01d8\5")
        buf.write("r:\2\u01d8\u01d9\5d\63\2\u01d9c\3\2\2\2\u01da\u01dd\5")
        buf.write("> \2\u01db\u01dd\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dde\3\2\2\2\u01de\u01df\7\f\2\2\u01df\u01e0")
        buf.write("\5j\66\2\u01e0\u01e1\7\34\2\2\u01e1\u01e2\5n8\2\u01e2")
        buf.write("\u01e3\7\34\2\2\u01e3\u01e4\5p9\2\u01e4\u01e5\5r:\2\u01e5")
        buf.write("\u01e6\5d\63\2\u01e6g\3\2\2\2\u01e7\u01e8\7\f\2\2\u01e8")
        buf.write("\u01e9\7\66\2\2\u01e9\u01ea\7\33\2\2\u01ea\u01eb\7\66")
        buf.write("\2\2\u01eb\u01ec\7.\2\2\u01ec\u01ed\7\r\2\2\u01ed\u01ee")
        buf.write("\5\u0080A\2\u01ee\u01ef\5r:\2\u01ef\u01f0\5d\63\2\u01f0")
        buf.write("i\3\2\2\2\u01f1\u01f2\7\66\2\2\u01f2\u01f3\5X-\2\u01f3")
        buf.write("\u01f4\5\u0080A\2\u01f4\u01f9\3\2\2\2\u01f5\u01f6\7\3")
        buf.write("\2\2\u01f6\u01f7\7\66\2\2\u01f7\u01f9\5l\67\2\u01f8\u01f1")
        buf.write("\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f9k\3\2\2\2\u01fa\u01fb")
        buf.write("\5\64\33\2\u01fb\u01fc\7\37\2\2\u01fc\u01fd\5\u0080A\2")
        buf.write("\u01fdm\3\2\2\2\u01fe\u01ff\5\u0080A\2\u01ffo\3\2\2\2")
        buf.write("\u0200\u0201\7\66\2\2\u0201\u0202\5X-\2\u0202\u0203\5")
        buf.write("\u0080A\2\u0203q\3\2\2\2\u0204\u0205\7\27\2\2\u0205\u0206")
        buf.write("\5P)\2\u0206\u0207\7\30\2\2\u0207s\3\2\2\2\u0208\u0209")
        buf.write("\7\16\2\2\u0209\u020a\5v<\2\u020a\u020b\5> \2\u020bu\3")
        buf.write("\2\2\2\u020c\u020f\5\u0080A\2\u020d\u020f\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020fw\3\2\2\2\u0210")
        buf.write("\u0211\7\17\2\2\u0211\u0212\5> \2\u0212y\3\2\2\2\u0213")
        buf.write("\u0214\7\20\2\2\u0214\u0215\5> \2\u0215{\3\2\2\2\u0216")
        buf.write("\u0217\5~@\2\u0217\u0218\5> \2\u0218}\3\2\2\2\u0219\u021c")
        buf.write("\5\u00b8]\2\u021a\u021c\5\u00c2b\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021a\3\2\2\2\u021c\177\3\2\2\2\u021d\u021e\5\u0084")
        buf.write("C\2\u021e\u021f\5\u0082B\2\u021f\u0081\3\2\2\2\u0220\u0221")
        buf.write("\7,\2\2\u0221\u0222\5\u0084C\2\u0222\u0223\5\u0082B\2")
        buf.write("\u0223\u0226\3\2\2\2\u0224\u0226\3\2\2\2\u0225\u0220\3")
        buf.write("\2\2\2\u0225\u0224\3\2\2\2\u0226\u0083\3\2\2\2\u0227\u0228")
        buf.write("\5\u0088E\2\u0228\u0229\5\u0086D\2\u0229\u0085\3\2\2\2")
        buf.write("\u022a\u022b\7+\2\2\u022b\u022c\5\u0088E\2\u022c\u022d")
        buf.write("\5\u0086D\2\u022d\u0230\3\2\2\2\u022e\u0230\3\2\2\2\u022f")
        buf.write("\u022a\3\2\2\2\u022f\u022e\3\2\2\2\u0230\u0087\3\2\2\2")
        buf.write("\u0231\u0232\5\u008eH\2\u0232\u0233\5\u008aF\2\u0233\u0089")
        buf.write("\3\2\2\2\u0234\u0235\5\u008cG\2\u0235\u0236\5\u008eH\2")
        buf.write("\u0236\u0237\5\u008aF\2\u0237\u023a\3\2\2\2\u0238\u023a")
        buf.write("\3\2\2\2\u0239\u0234\3\2\2\2\u0239\u0238\3\2\2\2\u023a")
        buf.write("\u008b\3\2\2\2\u023b\u023c\t\6\2\2\u023c\u008d\3\2\2\2")
        buf.write("\u023d\u023e\5\u0094K\2\u023e\u023f\5\u0090I\2\u023f\u008f")
        buf.write("\3\2\2\2\u0240\u0241\5\u0092J\2\u0241\u0242\5\u0094K\2")
        buf.write("\u0242\u0243\5\u0090I\2\u0243\u0246\3\2\2\2\u0244\u0246")
        buf.write("\3\2\2\2\u0245\u0240\3\2\2\2\u0245\u0244\3\2\2\2\u0246")
        buf.write("\u0091\3\2\2\2\u0247\u0248\t\7\2\2\u0248\u0093\3\2\2\2")
        buf.write("\u0249\u024a\5\u009aN\2\u024a\u024b\5\u0096L\2\u024b\u0095")
        buf.write("\3\2\2\2\u024c\u024d\5\u0098M\2\u024d\u024e\5\u009aN\2")
        buf.write("\u024e\u024f\5\u0096L\2\u024f\u0252\3\2\2\2\u0250\u0252")
        buf.write("\3\2\2\2\u0251\u024c\3\2\2\2\u0251\u0250\3\2\2\2\u0252")
        buf.write("\u0097\3\2\2\2\u0253\u0254\t\b\2\2\u0254\u0099\3\2\2\2")
        buf.write("\u0255\u0256\5\u009cO\2\u0256\u0257\5\u009aN\2\u0257\u025a")
        buf.write("\3\2\2\2\u0258\u025a\5\u009eP\2\u0259\u0255\3\2\2\2\u0259")
        buf.write("\u0258\3\2\2\2\u025a\u009b\3\2\2\2\u025b\u025c\t\t\2\2")
        buf.write("\u025c\u009d\3\2\2\2\u025d\u025e\5\u00a4S\2\u025e\u025f")
        buf.write("\5\u00a0Q\2\u025f\u009f\3\2\2\2\u0260\u0261\5\u00a2R\2")
        buf.write("\u0261\u0262\5\u00a0Q\2\u0262\u0265\3\2\2\2\u0263\u0265")
        buf.write("\3\2\2\2\u0264\u0260\3\2\2\2\u0264\u0263\3\2\2\2\u0265")
        buf.write("\u00a1\3\2\2\2\u0266\u0267\7\36\2\2\u0267\u026d\5\u00a4")
        buf.write("S\2\u0268\u0269\7\31\2\2\u0269\u026a\5\u0080A\2\u026a")
        buf.write("\u026b\7\32\2\2\u026b\u026d\3\2\2\2\u026c\u0266\3\2\2")
        buf.write("\2\u026c\u0268\3\2\2\2\u026d\u00a3\3\2\2\2\u026e\u026f")
        buf.write("\7\25\2\2\u026f\u0270\5\u0080A\2\u0270\u0271\7\26\2\2")
        buf.write("\u0271\u027c\3\2\2\2\u0272\u027c\7\67\2\2\u0273\u027c")
        buf.write("\78\2\2\u0274\u027c\79\2\2\u0275\u027c\7\64\2\2\u0276")
        buf.write("\u027c\7\65\2\2\u0277\u027c\7\66\2\2\u0278\u027c\5\u00c2")
        buf.write("b\2\u0279\u027c\5\u00a6T\2\u027a\u027c\5\u00b0Y\2\u027b")
        buf.write("\u026e\3\2\2\2\u027b\u0272\3\2\2\2\u027b\u0273\3\2\2\2")
        buf.write("\u027b\u0274\3\2\2\2\u027b\u0275\3\2\2\2\u027b\u0276\3")
        buf.write("\2\2\2\u027b\u0277\3\2\2\2\u027b\u0278\3\2\2\2\u027b\u0279")
        buf.write("\3\2\2\2\u027b\u027a\3\2\2\2\u027c\u00a5\3\2\2\2\u027d")
        buf.write("\u027e\5 \21\2\u027e\u027f\7\27\2\2\u027f\u0280\5\u00a8")
        buf.write("U\2\u0280\u0281\7\30\2\2\u0281\u00a7\3\2\2\2\u0282\u0283")
        buf.write("\5\u00acW\2\u0283\u0284\5\u00aaV\2\u0284\u00a9\3\2\2\2")
        buf.write("\u0285\u0286\7\33\2\2\u0286\u0287\5\u00acW\2\u0287\u0288")
        buf.write("\5\u00aaV\2\u0288\u028b\3\2\2\2\u0289\u028b\3\2\2\2\u028a")
        buf.write("\u0285\3\2\2\2\u028a\u0289\3\2\2\2\u028b\u00ab\3\2\2\2")
        buf.write("\u028c\u028d\7\27\2\2\u028d\u028e\5\u00aeX\2\u028e\u028f")
        buf.write("\7\30\2\2\u028f\u0298\3\2\2\2\u0290\u0298\7\66\2\2\u0291")
        buf.write("\u0298\7\67\2\2\u0292\u0298\78\2\2\u0293\u0298\7\64\2")
        buf.write("\2\u0294\u0298\79\2\2\u0295\u0298\7\65\2\2\u0296\u0298")
        buf.write("\5\u00b0Y\2\u0297\u028c\3\2\2\2\u0297\u0290\3\2\2\2\u0297")
        buf.write("\u0291\3\2\2\2\u0297\u0292\3\2\2\2\u0297\u0293\3\2\2\2")
        buf.write("\u0297\u0294\3\2\2\2\u0297\u0295\3\2\2\2\u0297\u0296\3")
        buf.write("\2\2\2\u0298\u00ad\3\2\2\2\u0299\u029c\5\u00a8U\2\u029a")
        buf.write("\u029c\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029a\3\2\2\2")
        buf.write("\u029c\u00af\3\2\2\2\u029d\u029e\7\66\2\2\u029e\u029f")
        buf.write("\7\27\2\2\u029f\u02a0\5\u00b2Z\2\u02a0\u02a1\7\30\2\2")
        buf.write("\u02a1\u00b1\3\2\2\2\u02a2\u02a3\5\u00b6\\\2\u02a3\u02a4")
        buf.write("\5\u0080A\2\u02a4\u02a5\5\u00b4[\2\u02a5\u02a8\3\2\2\2")
        buf.write("\u02a6\u02a8\3\2\2\2\u02a7\u02a2\3\2\2\2\u02a7\u02a6\3")
        buf.write("\2\2\2\u02a8\u00b3\3\2\2\2\u02a9\u02aa\7\33\2\2\u02aa")
        buf.write("\u02ab\5\u00b6\\\2\u02ab\u02ac\5\u0080A\2\u02ac\u02ad")
        buf.write("\5\u00b4[\2\u02ad\u02b0\3\2\2\2\u02ae\u02b0\3\2\2\2\u02af")
        buf.write("\u02a9\3\2\2\2\u02af\u02ae\3\2\2\2\u02b0\u00b5\3\2\2\2")
        buf.write("\u02b1\u02b2\7\66\2\2\u02b2\u02b3\7\35\2\2\u02b3\u00b7")
        buf.write("\3\2\2\2\u02b4\u02b5\5\u00ba^\2\u02b5\u02b6\7\36\2\2\u02b6")
        buf.write("\u02b7\7\66\2\2\u02b7\u02b8\7\25\2\2\u02b8\u02b9\5\u00bc")
        buf.write("_\2\u02b9\u02ba\7\26\2\2\u02ba\u00b9\3\2\2\2\u02bb\u02bf")
        buf.write("\7\66\2\2\u02bc\u02bf\5\u00c4c\2\u02bd\u02bf\5\u00c6d")
        buf.write("\2\u02be\u02bb\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bd")
        buf.write("\3\2\2\2\u02bf\u00bb\3\2\2\2\u02c0\u02c3\5\u00be`\2\u02c1")
        buf.write("\u02c3\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c1\3\2\2\2")
        buf.write("\u02c3\u00bd\3\2\2\2\u02c4\u02c5\5\u0080A\2\u02c5\u02c6")
        buf.write("\5\u00c0a\2\u02c6\u00bf\3\2\2\2\u02c7\u02c8\7\33\2\2\u02c8")
        buf.write("\u02c9\5\u0080A\2\u02c9\u02ca\5\u00c0a\2\u02ca\u02cd\3")
        buf.write("\2\2\2\u02cb\u02cd\3\2\2\2\u02cc\u02c7\3\2\2\2\u02cc\u02cb")
        buf.write("\3\2\2\2\u02cd\u00c1\3\2\2\2\u02ce\u02cf\7\66\2\2\u02cf")
        buf.write("\u02d0\7\25\2\2\u02d0\u02d1\5\u00bc_\2\u02d1\u02d2\7\26")
        buf.write("\2\2\u02d2\u00c3\3\2\2\2\u02d3\u02d4\7\66\2\2\u02d4\u02d5")
        buf.write("\5\u00ccg\2\u02d5\u00c5\3\2\2\2\u02d6\u02d7\7\66\2\2\u02d7")
        buf.write("\u02d8\5\u00c8e\2\u02d8\u02d9\5\u00caf\2\u02d9\u00c7\3")
        buf.write("\2\2\2\u02da\u02dd\5\u00ccg\2\u02db\u02dd\3\2\2\2\u02dc")
        buf.write("\u02da\3\2\2\2\u02dc\u02db\3\2\2\2\u02dd\u00c9\3\2\2\2")
        buf.write("\u02de\u02df\5\u00d0i\2\u02df\u02e0\5\u00caf\2\u02e0\u02e3")
        buf.write("\3\2\2\2\u02e1\u02e3\3\2\2\2\u02e2\u02de\3\2\2\2\u02e2")
        buf.write("\u02e1\3\2\2\2\u02e3\u00cb\3\2\2\2\u02e4\u02e5\7\31\2")
        buf.write("\2\u02e5\u02e6\5\u0080A\2\u02e6\u02e7\7\32\2\2\u02e7\u02e8")
        buf.write("\5\u00ceh\2\u02e8\u00cd\3\2\2\2\u02e9\u02ea\7\31\2\2\u02ea")
        buf.write("\u02eb\5\u0080A\2\u02eb\u02ec\7\32\2\2\u02ec\u02ed\5\u00ce")
        buf.write("h\2\u02ed\u02f0\3\2\2\2\u02ee\u02f0\3\2\2\2\u02ef\u02e9")
        buf.write("\3\2\2\2\u02ef\u02ee\3\2\2\2\u02f0\u00cf\3\2\2\2\u02f1")
        buf.write("\u02f2\7\36\2\2\u02f2\u02f3\7\66\2\2\u02f3\u02f4\5\u00c8")
        buf.write("e\2\u02f4\u00d1\3\2\2\2\61\u00dc\u00e4\u00f0\u00f5\u00fe")
        buf.write("\u0108\u0110\u011f\u012f\u013c\u0147\u0156\u015f\u0167")
        buf.write("\u0180\u018f\u0199\u019f\u01ab\u01b5\u01c9\u01ce\u01d3")
        buf.write("\u01dc\u01f8\u020e\u021b\u0225\u022f\u0239\u0245\u0251")
        buf.write("\u0259\u0264\u026c\u027b\u028a\u0297\u029b\u02a7\u02af")
        buf.write("\u02be\u02c2\u02cc\u02dc\u02e2\u02ef")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'const'", "'struct'", "'interface'", 
                     "'type'", "'func'", "'if'", "'else if'", "'else'", 
                     "'for'", "'range'", "'return'", "'break'", "'continue'", 
                     "'int'", "'float'", "'boolean'", "'string'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'", 
                     "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "VAR", "CONST", "STRUCT", "INTERFACE", 
                      "TYPE", "FUNC", "IF", "ELSEIF", "ELSE", "FOR", "RANGE", 
                      "RETURN", "BREAK", "CONTINUE", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "COMMA", "SEMI", "COLON", "DOT", 
                      "EQUAL", "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQ", 
                      "NEQ", "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", 
                      "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "BOOLLIT", "NILLIT", "ID", 
                      "INTLIT", "FLOATLIT", "STRINGLIT", "COMMENT", "MULTILINE_COMMENT", 
                      "NEWLINE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl_tail = 2
    RULE_decl = 3
    RULE_vardecl = 4
    RULE_var_init = 5
    RULE_var_init_extra = 6
    RULE_idlist = 7
    RULE_id_tail = 8
    RULE_exprlist = 9
    RULE_expr_tail = 10
    RULE_vartype = 11
    RULE_scalartype = 12
    RULE_constdecl = 13
    RULE_const_init = 14
    RULE_arraytype = 15
    RULE_array_size = 16
    RULE_array_type_tail = 17
    RULE_structtype = 18
    RULE_structdecl = 19
    RULE_element_list = 20
    RULE_interfacedecl = 21
    RULE_method_list = 22
    RULE_elements = 23
    RULE_methodbody = 24
    RULE_vartype_opt = 25
    RULE_typedecl = 26
    RULE_type_body = 27
    RULE_multiple_newline = 28
    RULE_multiple_newline_tail = 29
    RULE_endline = 30
    RULE_methoddecl = 31
    RULE_funcdecl = 32
    RULE_paramlist_opt = 33
    RULE_recevier = 34
    RULE_paramlist = 35
    RULE_param_tail = 36
    RULE_param = 37
    RULE_id_param_tail = 38
    RULE_stmt_list = 39
    RULE_stmt = 40
    RULE_assignstmt = 41
    RULE_lhs = 42
    RULE_assign_op = 43
    RULE_ifstmt = 44
    RULE_elseif_list = 45
    RULE_else_part = 46
    RULE_forstmt = 47
    RULE_forbasic = 48
    RULE_endline_opt = 49
    RULE_forstep = 50
    RULE_foreach = 51
    RULE_forinit = 52
    RULE_forinit_var = 53
    RULE_forcondition = 54
    RULE_forupdate = 55
    RULE_block = 56
    RULE_returnstmt = 57
    RULE_expr_opt = 58
    RULE_breakstmt = 59
    RULE_continuestmt = 60
    RULE_callstmt = 61
    RULE_call_expr = 62
    RULE_expr = 63
    RULE_expr_or = 64
    RULE_exp1 = 65
    RULE_exp1_and = 66
    RULE_exp2 = 67
    RULE_exp2_rel = 68
    RULE_rel_op = 69
    RULE_exp3 = 70
    RULE_exp3_add = 71
    RULE_add_op = 72
    RULE_exp4 = 73
    RULE_exp4_mul = 74
    RULE_mul_op = 75
    RULE_exp5 = 76
    RULE_unary_op = 77
    RULE_exp6 = 78
    RULE_exp6_access = 79
    RULE_access_part = 80
    RULE_exp7 = 81
    RULE_arraylit = 82
    RULE_lit_list = 83
    RULE_lit_tail = 84
    RULE_lit = 85
    RULE_lit_list_opt = 86
    RULE_structlit = 87
    RULE_structlit_items_opt = 88
    RULE_structlit_items_tail = 89
    RULE_astribute = 90
    RULE_methodcall = 91
    RULE_method_receiver = 92
    RULE_arg_list_opt = 93
    RULE_arg_list = 94
    RULE_arg_tail = 95
    RULE_funcall = 96
    RULE_arrayaccess = 97
    RULE_structaccess = 98
    RULE_access_opt = 99
    RULE_asaccess_list = 100
    RULE_access = 101
    RULE_access_tail = 102
    RULE_asaccess = 103

    ruleNames =  [ "program", "decl_list", "decl_tail", "decl", "vardecl", 
                   "var_init", "var_init_extra", "idlist", "id_tail", "exprlist", 
                   "expr_tail", "vartype", "scalartype", "constdecl", "const_init", 
                   "arraytype", "array_size", "array_type_tail", "structtype", 
                   "structdecl", "element_list", "interfacedecl", "method_list", 
                   "elements", "methodbody", "vartype_opt", "typedecl", 
                   "type_body", "multiple_newline", "multiple_newline_tail", 
                   "endline", "methoddecl", "funcdecl", "paramlist_opt", 
                   "recevier", "paramlist", "param_tail", "param", "id_param_tail", 
                   "stmt_list", "stmt", "assignstmt", "lhs", "assign_op", 
                   "ifstmt", "elseif_list", "else_part", "forstmt", "forbasic", 
                   "endline_opt", "forstep", "foreach", "forinit", "forinit_var", 
                   "forcondition", "forupdate", "block", "returnstmt", "expr_opt", 
                   "breakstmt", "continuestmt", "callstmt", "call_expr", 
                   "expr", "expr_or", "exp1", "exp1_and", "exp2", "exp2_rel", 
                   "rel_op", "exp3", "exp3_add", "add_op", "exp4", "exp4_mul", 
                   "mul_op", "exp5", "unary_op", "exp6", "exp6_access", 
                   "access_part", "exp7", "arraylit", "lit_list", "lit_tail", 
                   "lit", "lit_list_opt", "structlit", "structlit_items_opt", 
                   "structlit_items_tail", "astribute", "methodcall", "method_receiver", 
                   "arg_list_opt", "arg_list", "arg_tail", "funcall", "arrayaccess", 
                   "structaccess", "access_opt", "asaccess_list", "access", 
                   "access_tail", "asaccess" ]

    EOF = Token.EOF
    VAR=1
    CONST=2
    STRUCT=3
    INTERFACE=4
    TYPE=5
    FUNC=6
    IF=7
    ELSEIF=8
    ELSE=9
    FOR=10
    RANGE=11
    RETURN=12
    BREAK=13
    CONTINUE=14
    INT=15
    FLOAT=16
    BOOLEAN=17
    STRING=18
    LPAREN=19
    RPAREN=20
    LBRACE=21
    RBRACE=22
    LBRACK=23
    RBRACK=24
    COMMA=25
    SEMI=26
    COLON=27
    DOT=28
    EQUAL=29
    PLUS=30
    MINUS=31
    MULT=32
    DIV=33
    MOD=34
    EQ=35
    NEQ=36
    LT=37
    LTE=38
    GT=39
    GTE=40
    AND=41
    OR=42
    NOT=43
    ASSIGN=44
    PLUS_ASSIGN=45
    MINUS_ASSIGN=46
    MULT_ASSIGN=47
    DIV_ASSIGN=48
    MOD_ASSIGN=49
    BOOLLIT=50
    NILLIT=51
    ID=52
    INTLIT=53
    FLOATLIT=54
    STRINGLIT=55
    COMMENT=56
    MULTILINE_COMMENT=57
    NEWLINE=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.decl_list()
            self.state = 209
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decl_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = MiniGoParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.decl()
            self.state = 212
            self.decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decl_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_tail" ):
                return visitor.visitDecl_tail(self)
            else:
                return visitor.visitChildren(self)




    def decl_tail(self):

        localctx = MiniGoParser.Decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_tail)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR, MiniGoParser.CONST, MiniGoParser.TYPE, MiniGoParser.FUNC, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.decl()
                self.state = 215
                self.decl_tail()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethoddeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.vardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.typedecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                self.match(MiniGoParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def var_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_initContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MiniGoParser.VAR)
            self.state = 229
            self.idlist()
            self.state = 230
            self.var_init()
            self.state = 231
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def var_init_extra(self):
            return self.getTypedRuleContext(MiniGoParser.Var_init_extraContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = MiniGoParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_init)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.STRING, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.vartype()
                self.state = 234
                self.var_init_extra()
                pass
            elif token in [MiniGoParser.EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(MiniGoParser.EQUAL)
                self.state = 237
                self.exprlist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_init_extraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_init_extra

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init_extra" ):
                return visitor.visitVar_init_extra(self)
            else:
                return visitor.visitChildren(self)




    def var_init_extra(self):

        localctx = MiniGoParser.Var_init_extraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_init_extra)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(MiniGoParser.EQUAL)
                self.state = 241
                self.exprlist()
                pass
            elif token in [MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def id_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Id_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MiniGoParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MiniGoParser.ID)
            self.state = 246
            self.id_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def id_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Id_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_tail" ):
                return visitor.visitId_tail(self)
            else:
                return visitor.visitChildren(self)




    def id_tail(self):

        localctx = MiniGoParser.Id_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id_tail)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(MiniGoParser.COMMA)
                self.state = 249
                self.match(MiniGoParser.ID)
                self.state = 250
                self.id_tail()
                pass
            elif token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.STRING, MiniGoParser.LBRACK, MiniGoParser.EQUAL, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MiniGoParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exprlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expr()
            self.state = 255
            self.expr_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_tail" ):
                return visitor.visitExpr_tail(self)
            else:
                return visitor.visitChildren(self)




    def expr_tail(self):

        localctx = MiniGoParser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_tail)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(MiniGoParser.COMMA)
                self.state = 258
                self.expr()
                self.state = 259
                self.expr_tail()
                pass
            elif token in [MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def structtype(self):
            return self.getTypedRuleContext(MiniGoParser.StructtypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MiniGoParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vartype)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 268
                self.arraytype()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 269
                self.structtype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_scalartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalartype" ):
                return visitor.visitScalartype(self)
            else:
                return visitor.visitChildren(self)




    def scalartype(self):

        localctx = MiniGoParser.ScalartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scalartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def const_init(self):
            return self.getTypedRuleContext(MiniGoParser.Const_initContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MiniGoParser.CONST)
            self.state = 275
            self.idlist()
            self.state = 276
            self.const_init()
            self.state = 277
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_init" ):
                return visitor.visitConst_init(self)
            else:
                return visitor.visitChildren(self)




    def const_init(self):

        localctx = MiniGoParser.Const_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_const_init)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.STRING, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.vartype()
                self.state = 280
                self.match(MiniGoParser.EQUAL)
                self.state = 281
                self.exprlist()
                pass
            elif token in [MiniGoParser.EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(MiniGoParser.EQUAL)
                self.state = 284
                self.exprlist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def array_size(self):
            return self.getTypedRuleContext(MiniGoParser.Array_sizeContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def array_type_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_tailContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MiniGoParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MiniGoParser.LBRACK)
            self.state = 288
            self.array_size()
            self.state = 289
            self.match(MiniGoParser.RBRACK)
            self.state = 290
            self.array_type_tail()
            self.state = 291
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = MiniGoParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def array_size(self):
            return self.getTypedRuleContext(MiniGoParser.Array_sizeContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def array_type_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_tail" ):
                return visitor.visitArray_type_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_type_tail(self):

        localctx = MiniGoParser.Array_type_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_type_tail)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(MiniGoParser.LBRACK)
                self.state = 296
                self.array_size()
                self.state = 297
                self.match(MiniGoParser.RBRACK)
                self.state = 298
                self.array_type_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructtype" ):
                return visitor.visitStructtype(self)
            else:
                return visitor.visitChildren(self)




    def structtype(self):

        localctx = MiniGoParser.StructtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_structtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.STRUCT)
            self.state = 306
            self.match(MiniGoParser.LBRACE)
            self.state = 307
            self.element_list()
            self.state = 308
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MiniGoParser.ElementsContext,0)


        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = MiniGoParser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_element_list)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.elements()
                self.state = 311
                self.element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_interfacedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.INTERFACE)
            self.state = 317
            self.match(MiniGoParser.LBRACE)
            self.state = 318
            self.method_list()
            self.state = 319
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodbody(self):
            return self.getTypedRuleContext(MiniGoParser.MethodbodyContext,0)


        def method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_list" ):
                return visitor.visitMethod_list(self)
            else:
                return visitor.visitChildren(self)




    def method_list(self):

        localctx = MiniGoParser.Method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_list)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.methodbody()
                self.state = 322
                self.method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.methodbody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = MiniGoParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MiniGoParser.ID)
            self.state = 328
            self.vartype()
            self.state = 329
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramlist_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist_optContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def vartype_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Vartype_optContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodbody" ):
                return visitor.visitMethodbody(self)
            else:
                return visitor.visitChildren(self)




    def methodbody(self):

        localctx = MiniGoParser.MethodbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_methodbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.ID)
            self.state = 332
            self.match(MiniGoParser.LPAREN)
            self.state = 333
            self.paramlist_opt()
            self.state = 334
            self.match(MiniGoParser.RPAREN)
            self.state = 335
            self.vartype_opt()
            self.state = 336
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vartype_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vartype_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype_opt" ):
                return visitor.visitVartype_opt(self)
            else:
                return visitor.visitChildren(self)




    def vartype_opt(self):

        localctx = MiniGoParser.Vartype_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_vartype_opt)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.STRING, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.vartype()
                pass
            elif token in [MiniGoParser.LBRACE, MiniGoParser.SEMI, MiniGoParser.EQUAL, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_body(self):
            return self.getTypedRuleContext(MiniGoParser.Type_bodyContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MiniGoParser.TYPE)
            self.state = 343
            self.match(MiniGoParser.ID)
            self.state = 344
            self.type_body()
            self.state = 345
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_body" ):
                return visitor.visitType_body(self)
            else:
                return visitor.visitChildren(self)




    def type_body(self):

        localctx = MiniGoParser.Type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_type_body)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.structdecl()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.interfacedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def multiple_newline_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_newline_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiple_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_newline" ):
                return visitor.visitMultiple_newline(self)
            else:
                return visitor.visitChildren(self)




    def multiple_newline(self):

        localctx = MiniGoParser.Multiple_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_multiple_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MiniGoParser.NEWLINE)
            self.state = 352
            self.multiple_newline_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_newline_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def multiple_newline_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_newline_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiple_newline_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_newline_tail" ):
                return visitor.visitMultiple_newline_tail(self)
            else:
                return visitor.visitChildren(self)




    def multiple_newline_tail(self):

        localctx = MiniGoParser.Multiple_newline_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_multiple_newline_tail)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(MiniGoParser.NEWLINE)
                self.state = 355
                self.multiple_newline_tail()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndline" ):
                return visitor.visitEndline(self)
            else:
                return visitor.visitChildren(self)




    def endline(self):

        localctx = MiniGoParser.EndlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_endline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def recevier(self):
            return self.getTypedRuleContext(MiniGoParser.RecevierContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramlist_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist_optContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def vartype_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Vartype_optContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MiniGoParser.FUNC)
            self.state = 362
            self.recevier()
            self.state = 363
            self.match(MiniGoParser.ID)
            self.state = 364
            self.match(MiniGoParser.LPAREN)
            self.state = 365
            self.paramlist_opt()
            self.state = 366
            self.match(MiniGoParser.RPAREN)
            self.state = 367
            self.vartype_opt()
            self.state = 368
            self.block()
            self.state = 369
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramlist_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist_optContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def vartype_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Vartype_optContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(MiniGoParser.FUNC)
            self.state = 372
            self.match(MiniGoParser.ID)
            self.state = 373
            self.match(MiniGoParser.LPAREN)
            self.state = 374
            self.paramlist_opt()
            self.state = 375
            self.match(MiniGoParser.RPAREN)
            self.state = 376
            self.vartype_opt()
            self.state = 377
            self.block()
            self.state = 378
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramlist_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist_opt" ):
                return visitor.visitParamlist_opt(self)
            else:
                return visitor.visitChildren(self)




    def paramlist_opt(self):

        localctx = MiniGoParser.Paramlist_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramlist_opt)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.paramlist()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecevierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_recevier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecevier" ):
                return visitor.visitRecevier(self)
            else:
                return visitor.visitChildren(self)




    def recevier(self):

        localctx = MiniGoParser.RecevierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_recevier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.LPAREN)
            self.state = 385
            self.match(MiniGoParser.ID)
            self.state = 386
            self.match(MiniGoParser.ID)
            self.state = 387
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def param_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Param_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_paramlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.param()
            self.state = 390
            self.param_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def param_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Param_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_tail" ):
                return visitor.visitParam_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_tail(self):

        localctx = MiniGoParser.Param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_param_tail)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(MiniGoParser.COMMA)
                self.state = 393
                self.param()
                self.state = 394
                self.param_tail()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def id_param_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Id_param_tailContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MiniGoParser.ID)
            self.state = 400
            self.id_param_tail()
            self.state = 401
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_param_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def id_param_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Id_param_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_param_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_param_tail" ):
                return visitor.visitId_param_tail(self)
            else:
                return visitor.visitChildren(self)




    def id_param_tail(self):

        localctx = MiniGoParser.Id_param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_id_param_tail)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(MiniGoParser.COMMA)
                self.state = 404
                self.match(MiniGoParser.ID)
                self.state = 405
                self.id_param_tail()
                pass
            elif token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.STRING, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_list)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR, MiniGoParser.CONST, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.BREAK, MiniGoParser.CONTINUE, MiniGoParser.ID, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.stmt()
                self.state = 410
                self.stmt_list()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallstmtContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 418
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 419
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 420
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 421
                self.breakstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 422
                self.continuestmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 423
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 424
                self.match(MiniGoParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.lhs()
            self.state = 428
            self.assign_op()
            self.state = 429
            self.expr()
            self.state = 430
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def structaccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructaccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_lhs)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.arrayaccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
                self.structaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(MiniGoParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def elseif_list(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_listContext,0)


        def else_part(self):
            return self.getTypedRuleContext(MiniGoParser.Else_partContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(MiniGoParser.IF)
            self.state = 440
            self.match(MiniGoParser.LPAREN)
            self.state = 441
            self.expr()
            self.state = 442
            self.match(MiniGoParser.RPAREN)
            self.state = 443
            self.block()
            self.state = 444
            self.elseif_list()
            self.state = 445
            self.else_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(MiniGoParser.ELSEIF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def elseif_list(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list" ):
                return visitor.visitElseif_list(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list(self):

        localctx = MiniGoParser.Elseif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_elseif_list)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(MiniGoParser.ELSEIF)
                self.state = 448
                self.match(MiniGoParser.LPAREN)
                self.state = 449
                self.expr()
                self.state = 450
                self.match(MiniGoParser.RPAREN)
                self.state = 451
                self.block()
                self.state = 452
                self.elseif_list()
                pass
            elif token in [MiniGoParser.VAR, MiniGoParser.CONST, MiniGoParser.IF, MiniGoParser.ELSE, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.BREAK, MiniGoParser.CONTINUE, MiniGoParser.RBRACE, MiniGoParser.ID, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = MiniGoParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_else_part)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(MiniGoParser.ELSE)
                self.state = 458
                self.block()
                pass
            elif token in [MiniGoParser.VAR, MiniGoParser.CONST, MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.BREAK, MiniGoParser.CONTINUE, MiniGoParser.RBRACE, MiniGoParser.ID, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forbasic(self):
            return self.getTypedRuleContext(MiniGoParser.ForbasicContext,0)


        def forstep(self):
            return self.getTypedRuleContext(MiniGoParser.ForstepContext,0)


        def foreach(self):
            return self.getTypedRuleContext(MiniGoParser.ForeachContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_forstmt)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.forbasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.forstep()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.foreach()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForbasicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def forcondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForconditionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Endline_optContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forbasic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForbasic" ):
                return visitor.visitForbasic(self)
            else:
                return visitor.visitChildren(self)




    def forbasic(self):

        localctx = MiniGoParser.ForbasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_forbasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.FOR)
            self.state = 468
            self.forcondition()
            self.state = 469
            self.block()
            self.state = 470
            self.endline_opt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Endline_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_endline_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndline_opt" ):
                return visitor.visitEndline_opt(self)
            else:
                return visitor.visitChildren(self)




    def endline_opt(self):

        localctx = MiniGoParser.Endline_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_endline_opt)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.endline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def forinit(self):
            return self.getTypedRuleContext(MiniGoParser.ForinitContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def forcondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForconditionContext,0)


        def forupdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForupdateContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Endline_optContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstep" ):
                return visitor.visitForstep(self)
            else:
                return visitor.visitChildren(self)




    def forstep(self):

        localctx = MiniGoParser.ForstepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forstep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MiniGoParser.FOR)
            self.state = 477
            self.forinit()
            self.state = 478
            self.match(MiniGoParser.SEMI)
            self.state = 479
            self.forcondition()
            self.state = 480
            self.match(MiniGoParser.SEMI)
            self.state = 481
            self.forupdate()
            self.state = 482
            self.block()
            self.state = 483
            self.endline_opt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Endline_optContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_foreach

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach" ):
                return visitor.visitForeach(self)
            else:
                return visitor.visitChildren(self)




    def foreach(self):

        localctx = MiniGoParser.ForeachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_foreach)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MiniGoParser.FOR)
            self.state = 486
            self.match(MiniGoParser.ID)
            self.state = 487
            self.match(MiniGoParser.COMMA)
            self.state = 488
            self.match(MiniGoParser.ID)
            self.state = 489
            self.match(MiniGoParser.ASSIGN)
            self.state = 490
            self.match(MiniGoParser.RANGE)
            self.state = 491
            self.expr()
            self.state = 492
            self.block()
            self.state = 493
            self.endline_opt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def forinit_var(self):
            return self.getTypedRuleContext(MiniGoParser.Forinit_varContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinit" ):
                return visitor.visitForinit(self)
            else:
                return visitor.visitChildren(self)




    def forinit(self):

        localctx = MiniGoParser.ForinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_forinit)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(MiniGoParser.ID)
                self.state = 496
                self.assign_op()
                self.state = 497
                self.expr()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.match(MiniGoParser.VAR)
                self.state = 500
                self.match(MiniGoParser.ID)
                self.state = 501
                self.forinit_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forinit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Vartype_optContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forinit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinit_var" ):
                return visitor.visitForinit_var(self)
            else:
                return visitor.visitChildren(self)




    def forinit_var(self):

        localctx = MiniGoParser.Forinit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_forinit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.vartype_opt()
            self.state = 505
            self.match(MiniGoParser.EQUAL)
            self.state = 506
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forcondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForcondition" ):
                return visitor.visitForcondition(self)
            else:
                return visitor.visitChildren(self)




    def forcondition(self):

        localctx = MiniGoParser.ForconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_forcondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForupdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forupdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForupdate" ):
                return visitor.visitForupdate(self)
            else:
                return visitor.visitChildren(self)




    def forupdate(self):

        localctx = MiniGoParser.ForupdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_forupdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MiniGoParser.ID)
            self.state = 511
            self.assign_op()
            self.state = 512
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.LBRACE)
            self.state = 515
            self.stmt_list()
            self.state = 516
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_optContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(MiniGoParser.RETURN)
            self.state = 519
            self.expr_opt()
            self.state = 520
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_opt" ):
                return visitor.visitExpr_opt(self)
            else:
                return visitor.visitChildren(self)




    def expr_opt(self):

        localctx = MiniGoParser.Expr_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr_opt)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.BOOLLIT, MiniGoParser.NILLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.expr()
                pass
            elif token in [MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(MiniGoParser.BREAK)
            self.state = 527
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(MiniGoParser.CONTINUE)
            self.state = 530
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Call_exprContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MiniGoParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.call_expr()
            self.state = 533
            self.endline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = MiniGoParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_call_expr)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.methodcall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.funcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MiniGoParser.Exp1Context,0)


        def expr_or(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_orContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.exp1()
            self.state = 540
            self.expr_or()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def exp1(self):
            return self.getTypedRuleContext(MiniGoParser.Exp1Context,0)


        def expr_or(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_orContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or" ):
                return visitor.visitExpr_or(self)
            else:
                return visitor.visitChildren(self)




    def expr_or(self):

        localctx = MiniGoParser.Expr_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expr_or)
        try:
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.OR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(MiniGoParser.OR)
                self.state = 543
                self.exp1()
                self.state = 544
                self.expr_or()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACK, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(MiniGoParser.Exp2Context,0)


        def exp1_and(self):
            return self.getTypedRuleContext(MiniGoParser.Exp1_andContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = MiniGoParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_exp1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.exp2()
            self.state = 550
            self.exp1_and()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def exp2(self):
            return self.getTypedRuleContext(MiniGoParser.Exp2Context,0)


        def exp1_and(self):
            return self.getTypedRuleContext(MiniGoParser.Exp1_andContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp1_and

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1_and" ):
                return visitor.visitExp1_and(self)
            else:
                return visitor.visitChildren(self)




    def exp1_and(self):

        localctx = MiniGoParser.Exp1_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_exp1_and)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.AND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.match(MiniGoParser.AND)
                self.state = 553
                self.exp2()
                self.state = 554
                self.exp1_and()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACK, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.OR, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MiniGoParser.Exp3Context,0)


        def exp2_rel(self):
            return self.getTypedRuleContext(MiniGoParser.Exp2_relContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = MiniGoParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_exp2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.exp3()
            self.state = 560
            self.exp2_rel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2_relContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_op(self):
            return self.getTypedRuleContext(MiniGoParser.Rel_opContext,0)


        def exp3(self):
            return self.getTypedRuleContext(MiniGoParser.Exp3Context,0)


        def exp2_rel(self):
            return self.getTypedRuleContext(MiniGoParser.Exp2_relContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp2_rel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2_rel" ):
                return visitor.visitExp2_rel(self)
            else:
                return visitor.visitChildren(self)




    def exp2_rel(self):

        localctx = MiniGoParser.Exp2_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_exp2_rel)
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EQ, MiniGoParser.NEQ, MiniGoParser.LT, MiniGoParser.LTE, MiniGoParser.GT, MiniGoParser.GTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.rel_op()
                self.state = 563
                self.exp3()
                self.state = 564
                self.exp2_rel()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACK, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.AND, MiniGoParser.OR, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = MiniGoParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(MiniGoParser.Exp4Context,0)


        def exp3_add(self):
            return self.getTypedRuleContext(MiniGoParser.Exp3_addContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MiniGoParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_exp3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.exp4()
            self.state = 572
            self.exp3_add()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_op(self):
            return self.getTypedRuleContext(MiniGoParser.Add_opContext,0)


        def exp4(self):
            return self.getTypedRuleContext(MiniGoParser.Exp4Context,0)


        def exp3_add(self):
            return self.getTypedRuleContext(MiniGoParser.Exp3_addContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp3_add

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3_add" ):
                return visitor.visitExp3_add(self)
            else:
                return visitor.visitChildren(self)




    def exp3_add(self):

        localctx = MiniGoParser.Exp3_addContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_exp3_add)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PLUS, MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.add_op()
                self.state = 575
                self.exp4()
                self.state = 576
                self.exp3_add()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACK, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.EQ, MiniGoParser.NEQ, MiniGoParser.LT, MiniGoParser.LTE, MiniGoParser.GT, MiniGoParser.GTE, MiniGoParser.AND, MiniGoParser.OR, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = MiniGoParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(MiniGoParser.Exp5Context,0)


        def exp4_mul(self):
            return self.getTypedRuleContext(MiniGoParser.Exp4_mulContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MiniGoParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_exp4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.exp5()
            self.state = 584
            self.exp4_mul()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4_mulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_op(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_opContext,0)


        def exp5(self):
            return self.getTypedRuleContext(MiniGoParser.Exp5Context,0)


        def exp4_mul(self):
            return self.getTypedRuleContext(MiniGoParser.Exp4_mulContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp4_mul

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4_mul" ):
                return visitor.visitExp4_mul(self)
            else:
                return visitor.visitChildren(self)




    def exp4_mul(self):

        localctx = MiniGoParser.Exp4_mulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_exp4_mul)
        try:
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MULT, MiniGoParser.DIV, MiniGoParser.MOD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.mul_op()
                self.state = 587
                self.exp5()
                self.state = 588
                self.exp4_mul()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACK, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.PLUS, MiniGoParser.MINUS, MiniGoParser.EQ, MiniGoParser.NEQ, MiniGoParser.LT, MiniGoParser.LTE, MiniGoParser.GT, MiniGoParser.GTE, MiniGoParser.AND, MiniGoParser.OR, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(MiniGoParser.MULT, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_op" ):
                return visitor.visitMul_op(self)
            else:
                return visitor.visitChildren(self)




    def mul_op(self):

        localctx = MiniGoParser.Mul_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_mul_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULT) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_op(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_opContext,0)


        def exp5(self):
            return self.getTypedRuleContext(MiniGoParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MiniGoParser.Exp6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = MiniGoParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_exp5)
        try:
            self.state = 599
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.unary_op()
                self.state = 596
                self.exp5()
                pass
            elif token in [MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.BOOLLIT, MiniGoParser.NILLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 598
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = MiniGoParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MiniGoParser.Exp7Context,0)


        def exp6_access(self):
            return self.getTypedRuleContext(MiniGoParser.Exp6_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = MiniGoParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_exp6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.exp7()
            self.state = 604
            self.exp6_access()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access_part(self):
            return self.getTypedRuleContext(MiniGoParser.Access_partContext,0)


        def exp6_access(self):
            return self.getTypedRuleContext(MiniGoParser.Exp6_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp6_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6_access" ):
                return visitor.visitExp6_access(self)
            else:
                return visitor.visitChildren(self)




    def exp6_access(self):

        localctx = MiniGoParser.Exp6_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_exp6_access)
        try:
            self.state = 610
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK, MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.access_part()
                self.state = 607
                self.exp6_access()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACK, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.PLUS, MiniGoParser.MINUS, MiniGoParser.MULT, MiniGoParser.DIV, MiniGoParser.MOD, MiniGoParser.EQ, MiniGoParser.NEQ, MiniGoParser.LT, MiniGoParser.LTE, MiniGoParser.GT, MiniGoParser.GTE, MiniGoParser.AND, MiniGoParser.OR, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def exp7(self):
            return self.getTypedRuleContext(MiniGoParser.Exp7Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_access_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_part" ):
                return visitor.visitAccess_part(self)
            else:
                return visitor.visitChildren(self)




    def access_part(self):

        localctx = MiniGoParser.Access_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_access_part)
        try:
            self.state = 618
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.match(MiniGoParser.DOT)
                self.state = 613
                self.exp7()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 614
                self.match(MiniGoParser.LBRACK)
                self.state = 615
                self.expr()
                self.state = 616
                self.match(MiniGoParser.RBRACK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def NILLIT(self):
            return self.getToken(MiniGoParser.NILLIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(MiniGoParser.ArraylitContext,0)


        def structlit(self):
            return self.getTypedRuleContext(MiniGoParser.StructlitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = MiniGoParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_exp7)
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.match(MiniGoParser.LPAREN)
                self.state = 621
                self.expr()
                self.state = 622
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 625
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 626
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 627
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 628
                self.match(MiniGoParser.NILLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 629
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 630
                self.funcall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 631
                self.arraylit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 632
                self.structlit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def lit_list(self):
            return self.getTypedRuleContext(MiniGoParser.Lit_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = MiniGoParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.arraytype()
            self.state = 636
            self.match(MiniGoParser.LBRACE)
            self.state = 637
            self.lit_list()
            self.state = 638
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(MiniGoParser.LitContext,0)


        def lit_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Lit_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lit_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_list" ):
                return visitor.visitLit_list(self)
            else:
                return visitor.visitChildren(self)




    def lit_list(self):

        localctx = MiniGoParser.Lit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_lit_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.lit()
            self.state = 641
            self.lit_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def lit(self):
            return self.getTypedRuleContext(MiniGoParser.LitContext,0)


        def lit_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Lit_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lit_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_tail" ):
                return visitor.visitLit_tail(self)
            else:
                return visitor.visitChildren(self)




    def lit_tail(self):

        localctx = MiniGoParser.Lit_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_lit_tail)
        try:
            self.state = 648
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 643
                self.match(MiniGoParser.COMMA)
                self.state = 644
                self.lit()
                self.state = 645
                self.lit_tail()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def lit_list_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Lit_list_optContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def NILLIT(self):
            return self.getToken(MiniGoParser.NILLIT, 0)

        def structlit(self):
            return self.getTypedRuleContext(MiniGoParser.StructlitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = MiniGoParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_lit)
        try:
            self.state = 661
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 650
                self.match(MiniGoParser.LBRACE)
                self.state = 651
                self.lit_list_opt()
                self.state = 652
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 654
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 655
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 656
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 657
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 658
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 659
                self.match(MiniGoParser.NILLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 660
                self.structlit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_list_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit_list(self):
            return self.getTypedRuleContext(MiniGoParser.Lit_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lit_list_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_list_opt" ):
                return visitor.visitLit_list_opt(self)
            else:
                return visitor.visitChildren(self)




    def lit_list_opt(self):

        localctx = MiniGoParser.Lit_list_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_lit_list_opt)
        try:
            self.state = 665
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE, MiniGoParser.BOOLLIT, MiniGoParser.NILLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.lit_list()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def structlit_items_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Structlit_items_optContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructlit" ):
                return visitor.visitStructlit(self)
            else:
                return visitor.visitChildren(self)




    def structlit(self):

        localctx = MiniGoParser.StructlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_structlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(MiniGoParser.ID)
            self.state = 668
            self.match(MiniGoParser.LBRACE)
            self.state = 669
            self.structlit_items_opt()
            self.state = 670
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structlit_items_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def astribute(self):
            return self.getTypedRuleContext(MiniGoParser.AstributeContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def structlit_items_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Structlit_items_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structlit_items_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructlit_items_opt" ):
                return visitor.visitStructlit_items_opt(self)
            else:
                return visitor.visitChildren(self)




    def structlit_items_opt(self):

        localctx = MiniGoParser.Structlit_items_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_structlit_items_opt)
        try:
            self.state = 677
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 672
                self.astribute()
                self.state = 673
                self.expr()
                self.state = 674
                self.structlit_items_tail()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structlit_items_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def astribute(self):
            return self.getTypedRuleContext(MiniGoParser.AstributeContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def structlit_items_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Structlit_items_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structlit_items_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructlit_items_tail" ):
                return visitor.visitStructlit_items_tail(self)
            else:
                return visitor.visitChildren(self)




    def structlit_items_tail(self):

        localctx = MiniGoParser.Structlit_items_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_structlit_items_tail)
        try:
            self.state = 685
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                self.match(MiniGoParser.COMMA)
                self.state = 680
                self.astribute()
                self.state = 681
                self.expr()
                self.state = 682
                self.structlit_items_tail()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AstributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_astribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAstribute" ):
                return visitor.visitAstribute(self)
            else:
                return visitor.visitChildren(self)




    def astribute(self):

        localctx = MiniGoParser.AstributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_astribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.match(MiniGoParser.ID)
            self.state = 688
            self.match(MiniGoParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_receiver(self):
            return self.getTypedRuleContext(MiniGoParser.Method_receiverContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def arg_list_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_list_optContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)




    def methodcall(self):

        localctx = MiniGoParser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_methodcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
            self.method_receiver()
            self.state = 691
            self.match(MiniGoParser.DOT)
            self.state = 692
            self.match(MiniGoParser.ID)
            self.state = 693
            self.match(MiniGoParser.LPAREN)
            self.state = 694
            self.arg_list_opt()
            self.state = 695
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_receiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def structaccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructaccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_receiver" ):
                return visitor.visitMethod_receiver(self)
            else:
                return visitor.visitChildren(self)




    def method_receiver(self):

        localctx = MiniGoParser.Method_receiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_method_receiver)
        try:
            self.state = 700
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 697
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 698
                self.arrayaccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 699
                self.structaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_list_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arg_list_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list_opt" ):
                return visitor.visitArg_list_opt(self)
            else:
                return visitor.visitChildren(self)




    def arg_list_opt(self):

        localctx = MiniGoParser.Arg_list_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_arg_list_opt)
        try:
            self.state = 704
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.BOOLLIT, MiniGoParser.NILLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 702
                self.arg_list()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arg_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = MiniGoParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_arg_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.expr()
            self.state = 707
            self.arg_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arg_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arg_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_tail" ):
                return visitor.visitArg_tail(self)
            else:
                return visitor.visitChildren(self)




    def arg_tail(self):

        localctx = MiniGoParser.Arg_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_arg_tail)
        try:
            self.state = 714
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 709
                self.match(MiniGoParser.COMMA)
                self.state = 710
                self.expr()
                self.state = 711
                self.arg_tail()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def arg_list_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_list_optContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MiniGoParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_funcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(MiniGoParser.ID)
            self.state = 717
            self.match(MiniGoParser.LPAREN)
            self.state = 718
            self.arg_list_opt()
            self.state = 719
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def access(self):
            return self.getTypedRuleContext(MiniGoParser.AccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayaccess" ):
                return visitor.visitArrayaccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayaccess(self):

        localctx = MiniGoParser.ArrayaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_arrayaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.match(MiniGoParser.ID)
            self.state = 722
            self.access()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def access_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Access_optContext,0)


        def asaccess_list(self):
            return self.getTypedRuleContext(MiniGoParser.Asaccess_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructaccess" ):
                return visitor.visitStructaccess(self)
            else:
                return visitor.visitChildren(self)




    def structaccess(self):

        localctx = MiniGoParser.StructaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_structaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(MiniGoParser.ID)
            self.state = 725
            self.access_opt()
            self.state = 726
            self.asaccess_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access(self):
            return self.getTypedRuleContext(MiniGoParser.AccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access_opt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_opt" ):
                return visitor.visitAccess_opt(self)
            else:
                return visitor.visitChildren(self)




    def access_opt(self):

        localctx = MiniGoParser.Access_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_access_opt)
        try:
            self.state = 730
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 728
                self.access()
                pass
            elif token in [MiniGoParser.DOT, MiniGoParser.ASSIGN, MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MULT_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asaccess_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asaccess(self):
            return self.getTypedRuleContext(MiniGoParser.AsaccessContext,0)


        def asaccess_list(self):
            return self.getTypedRuleContext(MiniGoParser.Asaccess_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asaccess_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsaccess_list" ):
                return visitor.visitAsaccess_list(self)
            else:
                return visitor.visitChildren(self)




    def asaccess_list(self):

        localctx = MiniGoParser.Asaccess_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_asaccess_list)
        try:
            self.state = 736
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                self.asaccess()
                self.state = 733
                self.asaccess_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Access_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess" ):
                return visitor.visitAccess(self)
            else:
                return visitor.visitChildren(self)




    def access(self):

        localctx = MiniGoParser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
            self.match(MiniGoParser.LBRACK)
            self.state = 739
            self.expr()
            self.state = 740
            self.match(MiniGoParser.RBRACK)
            self.state = 741
            self.access_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Access_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_tail" ):
                return visitor.visitAccess_tail(self)
            else:
                return visitor.visitChildren(self)




    def access_tail(self):

        localctx = MiniGoParser.Access_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_access_tail)
        try:
            self.state = 749
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 743
                self.match(MiniGoParser.LBRACK)
                self.state = 744
                self.expr()
                self.state = 745
                self.match(MiniGoParser.RBRACK)
                self.state = 746
                self.access_tail()
                pass
            elif token in [MiniGoParser.DOT, MiniGoParser.ASSIGN, MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MULT_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def access_opt(self):
            return self.getTypedRuleContext(MiniGoParser.Access_optContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsaccess" ):
                return visitor.visitAsaccess(self)
            else:
                return visitor.visitChildren(self)




    def asaccess(self):

        localctx = MiniGoParser.AsaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_asaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self.match(MiniGoParser.DOT)
            self.state = 752
            self.match(MiniGoParser.ID)
            self.state = 753
            self.access_opt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





