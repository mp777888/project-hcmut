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
        buf.write("\u0263\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008e")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u0095\n\4\3\4\3\4\5\4\u0099")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\5\7\5\u00a0\n\5\f\5\16\5\u00a3")
        buf.write("\13\5\3\6\3\6\3\6\7\6\u00a8\n\6\f\6\16\6\u00ab\13\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7\u00b3\n\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\5\t\u00ba\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\6\n\u00c3")
        buf.write("\n\n\r\n\16\n\u00c4\3\n\3\n\3\13\3\13\3\f\3\f\3\f\6\f")
        buf.write("\u00ce\n\f\r\f\16\f\u00cf\3\f\3\f\3\r\3\r\3\r\6\r\u00d7")
        buf.write("\n\r\r\r\16\r\u00d8\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\5\17\u00e4\n\17\3\17\3\17\5\17\u00e8\n\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u00f0\n\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\5\21\u00f7\n\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u0100\n\23\3\23\3\23\5\23\u0104\n\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u010d\n\24\3\24")
        buf.write("\3\24\5\24\u0111\n\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\7\26\u011e\n\26\f\26\16\26\u0121")
        buf.write("\13\26\3\27\3\27\3\27\7\27\u0126\n\27\f\27\16\27\u0129")
        buf.write("\13\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0137\n\30\3\31\3\31\3\31\5\31\u013c")
        buf.write("\n\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u014d\n\32\f\32\16\32\u0150")
        buf.write("\13\32\3\32\3\32\5\32\u0154\n\32\3\33\3\33\3\33\5\33\u0159")
        buf.write("\n\33\3\34\3\34\3\34\3\34\5\34\u015f\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0169\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0174\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u017c\n\37\3\37\3\37")
        buf.write("\5\37\u0180\n\37\3 \3 \3!\3!\3!\3!\3\"\3\"\7\"\u018a\n")
        buf.write("\"\f\"\16\"\u018d\13\"\3\"\3\"\3#\3#\5#\u0193\n#\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3%\3&\3&\5&\u019f\n&\3&\3&\3\'\3\'\3")
        buf.write("\'\7\'\u01a6\n\'\f\'\16\'\u01a9\13\'\3(\3(\3(\7(\u01ae")
        buf.write("\n(\f(\16(\u01b1\13(\3)\3)\3)\7)\u01b6\n)\f)\16)\u01b9")
        buf.write("\13)\3*\3*\3*\7*\u01be\n*\f*\16*\u01c1\13*\3+\3+\3+\7")
        buf.write("+\u01c6\n+\f+\16+\u01c9\13+\3,\3,\3,\5,\u01ce\n,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\7-\u01d7\n-\f-\16-\u01da\13-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01e9\n.\3/\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\7\60\u01f3\n\60\f\60\16\60\u01f6\13")
        buf.write("\60\3\61\3\61\5\61\u01fa\n\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u0204\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\7\62\u020e\n\62\f\62\16\62\u0211\13")
        buf.write("\62\5\62\u0213\n\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\5\64\u021d\n\64\3\64\3\64\3\64\3\64\3\64\3\64\7")
        buf.write("\64\u0225\n\64\f\64\16\64\u0228\13\64\5\64\u022a\n\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\7\65\u0233\n\65\f")
        buf.write("\65\16\65\u0236\13\65\5\65\u0238\n\65\3\65\3\65\3\66\3")
        buf.write("\66\3\66\3\67\3\67\5\67\u0241\n\67\3\67\6\67\u0244\n\67")
        buf.write("\r\67\16\67\u0245\38\38\38\38\68\u024c\n8\r8\168\u024d")
        buf.write("\39\39\39\59\u0253\n9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3@\2\2A\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\2\n\3\2\21\24\3\2\66\67\4\2\34\34<<\3\2.\63\3")
        buf.write("\2%*\3\2 !\3\2\"$\4\2!!--\2\u027d\2\u0081\3\2\2\2\4\u008d")
        buf.write("\3\2\2\2\6\u008f\3\2\2\2\b\u009c\3\2\2\2\n\u00a4\3\2\2")
        buf.write("\2\f\u00b2\3\2\2\2\16\u00b4\3\2\2\2\20\u00b6\3\2\2\2\22")
        buf.write("\u00c2\3\2\2\2\24\u00c8\3\2\2\2\26\u00ca\3\2\2\2\30\u00d3")
        buf.write("\3\2\2\2\32\u00dc\3\2\2\2\34\u00e0\3\2\2\2\36\u00eb\3")
        buf.write("\2\2\2 \u00f6\3\2\2\2\"\u00f8\3\2\2\2$\u00fa\3\2\2\2&")
        buf.write("\u0108\3\2\2\2(\u0115\3\2\2\2*\u011a\3\2\2\2,\u0122\3")
        buf.write("\2\2\2.\u0136\3\2\2\2\60\u013b\3\2\2\2\62\u0141\3\2\2")
        buf.write("\2\64\u0158\3\2\2\2\66\u015a\3\2\2\28\u0160\3\2\2\2:\u016a")
        buf.write("\3\2\2\2<\u017f\3\2\2\2>\u0181\3\2\2\2@\u0183\3\2\2\2")
        buf.write("B\u0187\3\2\2\2D\u0190\3\2\2\2F\u0196\3\2\2\2H\u0199\3")
        buf.write("\2\2\2J\u019e\3\2\2\2L\u01a2\3\2\2\2N\u01aa\3\2\2\2P\u01b2")
        buf.write("\3\2\2\2R\u01ba\3\2\2\2T\u01c2\3\2\2\2V\u01cd\3\2\2\2")
        buf.write("X\u01cf\3\2\2\2Z\u01e8\3\2\2\2\\\u01ea\3\2\2\2^\u01ef")
        buf.write("\3\2\2\2`\u0203\3\2\2\2b\u0205\3\2\2\2d\u0216\3\2\2\2")
        buf.write("f\u021c\3\2\2\2h\u022d\3\2\2\2j\u023b\3\2\2\2l\u023e\3")
        buf.write("\2\2\2n\u024b\3\2\2\2p\u024f\3\2\2\2r\u0254\3\2\2\2t\u0256")
        buf.write("\3\2\2\2v\u0258\3\2\2\2x\u025a\3\2\2\2z\u025c\3\2\2\2")
        buf.write("|\u025e\3\2\2\2~\u0260\3\2\2\2\u0080\u0082\5\4\3\2\u0081")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\7")
        buf.write("\2\2\3\u0086\3\3\2\2\2\u0087\u008e\5&\24\2\u0088\u008e")
        buf.write("\5$\23\2\u0089\u008e\5\6\4\2\u008a\u008e\5\20\t\2\u008b")
        buf.write("\u008e\5\36\20\2\u008c\u008e\7<\2\2\u008d\u0087\3\2\2")
        buf.write("\2\u008d\u0088\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008a")
        buf.write("\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\5\3\2\2\2\u008f\u0090\7\3\2\2\u0090\u0098\5\b\5\2\u0091")
        buf.write("\u0094\5\f\7\2\u0092\u0093\7\37\2\2\u0093\u0095\5\n\6")
        buf.write("\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0099")
        buf.write("\3\2\2\2\u0096\u0097\7\37\2\2\u0097\u0099\5\n\6\2\u0098")
        buf.write("\u0091\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\5\"\22\2\u009b\7\3\2\2\2\u009c\u00a1\7\66")
        buf.write("\2\2\u009d\u009e\7\33\2\2\u009e\u00a0\7\66\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\t\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a9\5L\'\2\u00a5\u00a6\7\33\2\2\u00a6\u00a8\5L\'\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\13\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00b3\7\21\2\2\u00ad\u00b3\7\22\2\2\u00ae")
        buf.write("\u00b3\7\24\2\2\u00af\u00b3\7\23\2\2\u00b0\u00b3\5\22")
        buf.write("\n\2\u00b1\u00b3\5\24\13\2\u00b2\u00ac\3\2\2\2\u00b2\u00ad")
        buf.write("\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\r\3\2\2\2\u00b4")
        buf.write("\u00b5\t\2\2\2\u00b5\17\3\2\2\2\u00b6\u00b7\7\4\2\2\u00b7")
        buf.write("\u00b9\5\b\5\2\u00b8\u00ba\5\f\7\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7")
        buf.write("\37\2\2\u00bc\u00bd\5\n\6\2\u00bd\u00be\5\"\22\2\u00be")
        buf.write("\21\3\2\2\2\u00bf\u00c0\7\31\2\2\u00c0\u00c1\t\3\2\2\u00c1")
        buf.write("\u00c3\7\32\2\2\u00c2\u00bf\3\2\2\2\u00c3\u00c4\3\2\2")
        buf.write("\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00c7\5\f\7\2\u00c7\23\3\2\2\2\u00c8\u00c9")
        buf.write("\7\66\2\2\u00c9\25\3\2\2\2\u00ca\u00cb\7\5\2\2\u00cb\u00cd")
        buf.write("\7\27\2\2\u00cc\u00ce\5\32\16\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00d2\7\30\2\2\u00d2\27\3\2")
        buf.write("\2\2\u00d3\u00d4\7\6\2\2\u00d4\u00d6\7\27\2\2\u00d5\u00d7")
        buf.write("\5\34\17\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00db\7\30\2\2\u00db\31\3\2\2\2\u00dc\u00dd\7\66")
        buf.write("\2\2\u00dd\u00de\5\f\7\2\u00de\u00df\5\"\22\2\u00df\33")
        buf.write("\3\2\2\2\u00e0\u00e1\7\66\2\2\u00e1\u00e3\7\25\2\2\u00e2")
        buf.write("\u00e4\5*\26\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e7\7\26\2\2\u00e6\u00e8")
        buf.write("\5\f\7\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ea\5\"\22\2\u00ea\35\3\2\2\2\u00eb")
        buf.write("\u00ec\7\7\2\2\u00ec\u00ef\7\66\2\2\u00ed\u00f0\5\26\f")
        buf.write("\2\u00ee\u00f0\5\30\r\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\5\"\22\2\u00f2")
        buf.write("\37\3\2\2\2\u00f3\u00f4\7<\2\2\u00f4\u00f7\5 \21\2\u00f5")
        buf.write("\u00f7\7<\2\2\u00f6\u00f3\3\2\2\2\u00f6\u00f5\3\2\2\2")
        buf.write("\u00f7!\3\2\2\2\u00f8\u00f9\t\4\2\2\u00f9#\3\2\2\2\u00fa")
        buf.write("\u00fb\7\b\2\2\u00fb\u00fc\5(\25\2\u00fc\u00fd\7\66\2")
        buf.write("\2\u00fd\u00ff\7\25\2\2\u00fe\u0100\5*\26\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0103\7\26\2\2\u0102\u0104\5\f\7\2\u0103\u0102\3\2\2")
        buf.write("\2\u0103\u0104\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106")
        buf.write("\5B\"\2\u0106\u0107\5\"\22\2\u0107%\3\2\2\2\u0108\u0109")
        buf.write("\7\b\2\2\u0109\u010a\7\66\2\2\u010a\u010c\7\25\2\2\u010b")
        buf.write("\u010d\5*\26\2\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u0110\7\26\2\2\u010f\u0111")
        buf.write("\5\f\7\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u0113\5B\"\2\u0113\u0114\5\"\22\2")
        buf.write("\u0114\'\3\2\2\2\u0115\u0116\7\25\2\2\u0116\u0117\7\66")
        buf.write("\2\2\u0117\u0118\7\66\2\2\u0118\u0119\7\26\2\2\u0119)")
        buf.write("\3\2\2\2\u011a\u011f\5,\27\2\u011b\u011c\7\33\2\2\u011c")
        buf.write("\u011e\5,\27\2\u011d\u011b\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120+\3\2\2")
        buf.write("\2\u0121\u011f\3\2\2\2\u0122\u0127\7\66\2\2\u0123\u0124")
        buf.write("\7\33\2\2\u0124\u0126\7\66\2\2\u0125\u0123\3\2\2\2\u0126")
        buf.write("\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\5")
        buf.write("\f\7\2\u012b-\3\2\2\2\u012c\u0137\5\6\4\2\u012d\u0137")
        buf.write("\5\20\t\2\u012e\u0137\5\60\31\2\u012f\u0137\5\62\32\2")
        buf.write("\u0130\u0137\5\64\33\2\u0131\u0137\5D#\2\u0132\u0137\5")
        buf.write("F$\2\u0133\u0137\5H%\2\u0134\u0137\5J&\2\u0135\u0137\7")
        buf.write("<\2\2\u0136\u012c\3\2\2\2\u0136\u012d\3\2\2\2\u0136\u012e")
        buf.write("\3\2\2\2\u0136\u012f\3\2\2\2\u0136\u0130\3\2\2\2\u0136")
        buf.write("\u0131\3\2\2\2\u0136\u0132\3\2\2\2\u0136\u0133\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137/\3\2\2")
        buf.write("\2\u0138\u013c\7\66\2\2\u0139\u013c\5j\66\2\u013a\u013c")
        buf.write("\5l\67\2\u013b\u0138\3\2\2\2\u013b\u0139\3\2\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\t\5\2\2")
        buf.write("\u013e\u013f\5L\'\2\u013f\u0140\5\"\22\2\u0140\61\3\2")
        buf.write("\2\2\u0141\u0142\7\t\2\2\u0142\u0143\7\25\2\2\u0143\u0144")
        buf.write("\5L\'\2\u0144\u0145\7\26\2\2\u0145\u014e\5B\"\2\u0146")
        buf.write("\u0147\7\n\2\2\u0147\u0148\7\25\2\2\u0148\u0149\5L\'\2")
        buf.write("\u0149\u014a\7\26\2\2\u014a\u014b\5B\"\2\u014b\u014d\3")
        buf.write("\2\2\2\u014c\u0146\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0153\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0151\u0152\7\13\2\2\u0152\u0154\5B\"\2")
        buf.write("\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\63\3\2")
        buf.write("\2\2\u0155\u0159\5\66\34\2\u0156\u0159\58\35\2\u0157\u0159")
        buf.write("\5:\36\2\u0158\u0155\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\65\3\2\2\2\u015a\u015b\7\f\2\2\u015b")
        buf.write("\u015c\5> \2\u015c\u015e\5B\"\2\u015d\u015f\5\"\22\2\u015e")
        buf.write("\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f\67\3\2\2\2\u0160")
        buf.write("\u0161\7\f\2\2\u0161\u0162\5<\37\2\u0162\u0163\7\34\2")
        buf.write("\2\u0163\u0164\5> \2\u0164\u0165\7\34\2\2\u0165\u0166")
        buf.write("\5@!\2\u0166\u0168\5B\"\2\u0167\u0169\5\"\22\2\u0168\u0167")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u01699\3\2\2\2\u016a\u016b")
        buf.write("\7\f\2\2\u016b\u016c\7\66\2\2\u016c\u016d\7\33\2\2\u016d")
        buf.write("\u016e\7\66\2\2\u016e\u016f\7.\2\2\u016f\u0170\7\r\2\2")
        buf.write("\u0170\u0171\5L\'\2\u0171\u0173\5B\"\2\u0172\u0174\5\"")
        buf.write("\22\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174;\3")
        buf.write("\2\2\2\u0175\u0176\7\66\2\2\u0176\u0177\t\5\2\2\u0177")
        buf.write("\u0180\5L\'\2\u0178\u0179\7\3\2\2\u0179\u017b\7\66\2\2")
        buf.write("\u017a\u017c\5\f\7\2\u017b\u017a\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\7\37\2\2\u017e")
        buf.write("\u0180\5L\'\2\u017f\u0175\3\2\2\2\u017f\u0178\3\2\2\2")
        buf.write("\u0180=\3\2\2\2\u0181\u0182\5L\'\2\u0182?\3\2\2\2\u0183")
        buf.write("\u0184\7\66\2\2\u0184\u0185\t\5\2\2\u0185\u0186\5L\'\2")
        buf.write("\u0186A\3\2\2\2\u0187\u018b\7\27\2\2\u0188\u018a\5.\30")
        buf.write("\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\7\30\2\2\u018fC\3\2\2\2\u0190")
        buf.write("\u0192\7\16\2\2\u0191\u0193\5L\'\2\u0192\u0191\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\5")
        buf.write("\"\22\2\u0195E\3\2\2\2\u0196\u0197\7\17\2\2\u0197\u0198")
        buf.write("\5\"\22\2\u0198G\3\2\2\2\u0199\u019a\7\20\2\2\u019a\u019b")
        buf.write("\5\"\22\2\u019bI\3\2\2\2\u019c\u019f\5f\64\2\u019d\u019f")
        buf.write("\5h\65\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\5\"\22\2\u01a1K\3\2\2\2\u01a2")
        buf.write("\u01a7\5N(\2\u01a3\u01a4\7,\2\2\u01a4\u01a6\5N(\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8M\3\2\2\2\u01a9\u01a7\3\2\2")
        buf.write("\2\u01aa\u01af\5P)\2\u01ab\u01ac\7+\2\2\u01ac\u01ae\5")
        buf.write("P)\2\u01ad\u01ab\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0O\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b2\u01b7\5R*\2\u01b3\u01b4\t\6\2\2\u01b4\u01b6")
        buf.write("\5R*\2\u01b5\u01b3\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8Q\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bf\5T+\2\u01bb\u01bc\t\7\2\2\u01bc\u01be")
        buf.write("\5T+\2\u01bd\u01bb\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0S\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c2\u01c7\5V,\2\u01c3\u01c4\t\b\2\2\u01c4\u01c6")
        buf.write("\5V,\2\u01c5\u01c3\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8U\3\2\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01ca\u01cb\t\t\2\2\u01cb\u01ce\5V,\2\u01cc\u01ce")
        buf.write("\5X-\2\u01cd\u01ca\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ceW")
        buf.write("\3\2\2\2\u01cf\u01d8\5Z.\2\u01d0\u01d1\7\36\2\2\u01d1")
        buf.write("\u01d7\5Z.\2\u01d2\u01d3\7\31\2\2\u01d3\u01d4\5L\'\2\u01d4")
        buf.write("\u01d5\7\32\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d0\3\2\2")
        buf.write("\2\u01d6\u01d2\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9Y\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u01dc\7\25\2\2\u01dc\u01dd\5L\'\2\u01dd")
        buf.write("\u01de\7\26\2\2\u01de\u01e9\3\2\2\2\u01df\u01e9\7\67\2")
        buf.write("\2\u01e0\u01e9\78\2\2\u01e1\u01e9\79\2\2\u01e2\u01e9\7")
        buf.write("\64\2\2\u01e3\u01e9\7\65\2\2\u01e4\u01e9\7\66\2\2\u01e5")
        buf.write("\u01e9\5h\65\2\u01e6\u01e9\5\\/\2\u01e7\u01e9\5b\62\2")
        buf.write("\u01e8\u01db\3\2\2\2\u01e8\u01df\3\2\2\2\u01e8\u01e0\3")
        buf.write("\2\2\2\u01e8\u01e1\3\2\2\2\u01e8\u01e2\3\2\2\2\u01e8\u01e3")
        buf.write("\3\2\2\2\u01e8\u01e4\3\2\2\2\u01e8\u01e5\3\2\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9[\3\2\2\2\u01ea")
        buf.write("\u01eb\5\22\n\2\u01eb\u01ec\7\27\2\2\u01ec\u01ed\5^\60")
        buf.write("\2\u01ed\u01ee\7\30\2\2\u01ee]\3\2\2\2\u01ef\u01f4\5`")
        buf.write("\61\2\u01f0\u01f1\7\33\2\2\u01f1\u01f3\5`\61\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5_\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u01f9\7\27\2\2\u01f8\u01fa\5^\60\2\u01f9\u01f8\3\2\2")
        buf.write("\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u0204")
        buf.write("\7\30\2\2\u01fc\u0204\7\66\2\2\u01fd\u0204\7\67\2\2\u01fe")
        buf.write("\u0204\78\2\2\u01ff\u0204\7\64\2\2\u0200\u0204\79\2\2")
        buf.write("\u0201\u0204\7\65\2\2\u0202\u0204\5b\62\2\u0203\u01f7")
        buf.write("\3\2\2\2\u0203\u01fc\3\2\2\2\u0203\u01fd\3\2\2\2\u0203")
        buf.write("\u01fe\3\2\2\2\u0203\u01ff\3\2\2\2\u0203\u0200\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204a\3\2\2")
        buf.write("\2\u0205\u0206\7\66\2\2\u0206\u0212\7\27\2\2\u0207\u0208")
        buf.write("\5d\63\2\u0208\u020f\5L\'\2\u0209\u020a\7\33\2\2\u020a")
        buf.write("\u020b\5d\63\2\u020b\u020c\5L\'\2\u020c\u020e\3\2\2\2")
        buf.write("\u020d\u0209\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u020f\u0210\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0212\u0207\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0215\7\30\2\2\u0215c\3\2\2\2\u0216")
        buf.write("\u0217\7\66\2\2\u0217\u0218\7\35\2\2\u0218e\3\2\2\2\u0219")
        buf.write("\u021d\7\66\2\2\u021a\u021d\5j\66\2\u021b\u021d\5l\67")
        buf.write("\2\u021c\u0219\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021b")
        buf.write("\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021f\7\36\2\2\u021f")
        buf.write("\u0220\7\66\2\2\u0220\u0229\7\25\2\2\u0221\u0226\5L\'")
        buf.write("\2\u0222\u0223\7\33\2\2\u0223\u0225\5L\'\2\u0224\u0222")
        buf.write("\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0229\u0221\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\3")
        buf.write("\2\2\2\u022b\u022c\7\26\2\2\u022cg\3\2\2\2\u022d\u022e")
        buf.write("\7\66\2\2\u022e\u0237\7\25\2\2\u022f\u0234\5L\'\2\u0230")
        buf.write("\u0231\7\33\2\2\u0231\u0233\5L\'\2\u0232\u0230\3\2\2\2")
        buf.write("\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3")
        buf.write("\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u022f")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\3\2\2\2\u0239")
        buf.write("\u023a\7\26\2\2\u023ai\3\2\2\2\u023b\u023c\7\66\2\2\u023c")
        buf.write("\u023d\5n8\2\u023dk\3\2\2\2\u023e\u0240\7\66\2\2\u023f")
        buf.write("\u0241\5n8\2\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0243\3\2\2\2\u0242\u0244\5p9\2\u0243\u0242\3\2\2\2\u0244")
        buf.write("\u0245\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0246\3\2\2\2")
        buf.write("\u0246m\3\2\2\2\u0247\u0248\7\31\2\2\u0248\u0249\5L\'")
        buf.write("\2\u0249\u024a\7\32\2\2\u024a\u024c\3\2\2\2\u024b\u0247")
        buf.write("\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024b\3\2\2\2\u024d")
        buf.write("\u024e\3\2\2\2\u024eo\3\2\2\2\u024f\u0250\7\36\2\2\u0250")
        buf.write("\u0252\7\66\2\2\u0251\u0253\5n8\2\u0252\u0251\3\2\2\2")
        buf.write("\u0252\u0253\3\2\2\2\u0253q\3\2\2\2\u0254\u0255\7\67\2")
        buf.write("\2\u0255s\3\2\2\2\u0256\u0257\78\2\2\u0257u\3\2\2\2\u0258")
        buf.write("\u0259\79\2\2\u0259w\3\2\2\2\u025a\u025b\7\64\2\2\u025b")
        buf.write("y\3\2\2\2\u025c\u025d\7\65\2\2\u025d{\3\2\2\2\u025e\u025f")
        buf.write("\7\66\2\2\u025f}\3\2\2\2\u0260\u0261\7<\2\2\u0261\177")
        buf.write("\3\2\2\2;\u0083\u008d\u0094\u0098\u00a1\u00a9\u00b2\u00b9")
        buf.write("\u00c4\u00cf\u00d8\u00e3\u00e7\u00ef\u00f6\u00ff\u0103")
        buf.write("\u010c\u0110\u011f\u0127\u0136\u013b\u014e\u0153\u0158")
        buf.write("\u015e\u0168\u0173\u017b\u017f\u018b\u0192\u019e\u01a7")
        buf.write("\u01af\u01b7\u01bf\u01c7\u01cd\u01d6\u01d8\u01e8\u01f4")
        buf.write("\u01f9\u0203\u020f\u0212\u021c\u0226\u0229\u0234\u0237")
        buf.write("\u0240\u0245\u024d\u0252")
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
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_idlist = 3
    RULE_exprlist = 4
    RULE_vartype = 5
    RULE_scalartype = 6
    RULE_constdecl = 7
    RULE_arraytype = 8
    RULE_structtype = 9
    RULE_structdecl = 10
    RULE_interfacedecl = 11
    RULE_elements = 12
    RULE_methodbody = 13
    RULE_typedecl = 14
    RULE_multiple_newline = 15
    RULE_endline = 16
    RULE_methoddecl = 17
    RULE_funcdecl = 18
    RULE_recevier = 19
    RULE_paramlist = 20
    RULE_param = 21
    RULE_stmt = 22
    RULE_assignstmt = 23
    RULE_ifstmt = 24
    RULE_forstmt = 25
    RULE_forbasic = 26
    RULE_forstep = 27
    RULE_foreach = 28
    RULE_forinit = 29
    RULE_forcondition = 30
    RULE_forupdate = 31
    RULE_block = 32
    RULE_returnstmt = 33
    RULE_breakstmt = 34
    RULE_continuestmt = 35
    RULE_callstmt = 36
    RULE_expr = 37
    RULE_exp1 = 38
    RULE_exp2 = 39
    RULE_exp3 = 40
    RULE_exp4 = 41
    RULE_exp5 = 42
    RULE_exp6 = 43
    RULE_exp7 = 44
    RULE_arraylit = 45
    RULE_lit_list = 46
    RULE_lit = 47
    RULE_structlit = 48
    RULE_astribute = 49
    RULE_methodcall = 50
    RULE_funcall = 51
    RULE_arrayaccess = 52
    RULE_structaccess = 53
    RULE_access = 54
    RULE_asaccess = 55
    RULE_intlit = 56
    RULE_floatlit = 57
    RULE_stringlit = 58
    RULE_boollit = 59
    RULE_nillit = 60
    RULE_idlit = 61
    RULE_newline = 62

    ruleNames =  [ "program", "decl", "vardecl", "idlist", "exprlist", "vartype", 
                   "scalartype", "constdecl", "arraytype", "structtype", 
                   "structdecl", "interfacedecl", "elements", "methodbody", 
                   "typedecl", "multiple_newline", "endline", "methoddecl", 
                   "funcdecl", "recevier", "paramlist", "param", "stmt", 
                   "assignstmt", "ifstmt", "forstmt", "forbasic", "forstep", 
                   "foreach", "forinit", "forcondition", "forupdate", "block", 
                   "returnstmt", "breakstmt", "continuestmt", "callstmt", 
                   "expr", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "arraylit", "lit_list", "lit", "structlit", "astribute", 
                   "methodcall", "funcall", "arrayaccess", "structaccess", 
                   "access", "asaccess", "intlit", "floatlit", "stringlit", 
                   "boollit", "nillit", "idlit", "newline" ]

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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.decl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.NEWLINE))) != 0)):
                    break

            self.state = 131
            self.match(MiniGoParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.vardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.typedecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
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


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MiniGoParser.VAR)
            self.state = 142
            self.idlist()
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.STRING, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 143
                self.vartype()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.EQUAL:
                    self.state = 144
                    self.match(MiniGoParser.EQUAL)
                    self.state = 145
                    self.exprlist()


                pass
            elif token in [MiniGoParser.EQUAL]:
                self.state = 148
                self.match(MiniGoParser.EQUAL)
                self.state = 149
                self.exprlist()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 152
            self.endline()
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MiniGoParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(MiniGoParser.ID)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 155
                self.match(MiniGoParser.COMMA)
                self.state = 156
                self.match(MiniGoParser.ID)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MiniGoParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expr()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 163
                self.match(MiniGoParser.COMMA)
                self.state = 164
                self.expr()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 10, self.RULE_vartype)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 173
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 174
                self.arraytype()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 175
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
        self.enterRule(localctx, 12, self.RULE_scalartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MiniGoParser.CONST)
            self.state = 181
            self.idlist()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 182
                self.vartype()


            self.state = 185
            self.match(MiniGoParser.EQUAL)
            self.state = 186
            self.exprlist()
            self.state = 187
            self.endline()
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

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MiniGoParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 189
                    self.match(MiniGoParser.LBRACK)
                    self.state = 190
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTLIT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 191
                    self.match(MiniGoParser.RBRACK)

                else:
                    raise NoViableAltException(self)
                self.state = 194 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 196
            self.vartype()
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
        self.enterRule(localctx, 18, self.RULE_structtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ElementsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ElementsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MiniGoParser.STRUCT)
            self.state = 201
            self.match(MiniGoParser.LBRACE)
            self.state = 203 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 202
                self.elements()
                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 207
            self.match(MiniGoParser.RBRACE)
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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def methodbody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethodbodyContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethodbodyContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.INTERFACE)
            self.state = 210
            self.match(MiniGoParser.LBRACE)
            self.state = 212 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 211
                self.methodbody()
                self.state = 214 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 216
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 24, self.RULE_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MiniGoParser.ID)
            self.state = 219
            self.vartype()
            self.state = 220
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

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodbody" ):
                return visitor.visitMethodbody(self)
            else:
                return visitor.visitChildren(self)




    def methodbody(self):

        localctx = MiniGoParser.MethodbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methodbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.ID)
            self.state = 223
            self.match(MiniGoParser.LPAREN)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 224
                self.paramlist()


            self.state = 227
            self.match(MiniGoParser.RPAREN)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 228
                self.vartype()


            self.state = 231
            self.endline()
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

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MiniGoParser.TYPE)
            self.state = 234
            self.match(MiniGoParser.ID)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 235
                self.structdecl()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 236
                self.interfacedecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 239
            self.endline()
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

        def multiple_newline(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_newlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiple_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_newline" ):
                return visitor.visitMultiple_newline(self)
            else:
                return visitor.visitChildren(self)




    def multiple_newline(self):

        localctx = MiniGoParser.Multiple_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multiple_newline)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(MiniGoParser.NEWLINE)
                self.state = 242
                self.multiple_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(MiniGoParser.NEWLINE)
                pass


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
        self.enterRule(localctx, 32, self.RULE_endline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MiniGoParser.FUNC)
            self.state = 249
            self.recevier()
            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
            self.match(MiniGoParser.LPAREN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 252
                self.paramlist()


            self.state = 255
            self.match(MiniGoParser.RPAREN)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 256
                self.vartype()


            self.state = 259
            self.block()
            self.state = 260
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

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MiniGoParser.FUNC)
            self.state = 263
            self.match(MiniGoParser.ID)
            self.state = 264
            self.match(MiniGoParser.LPAREN)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 265
                self.paramlist()


            self.state = 268
            self.match(MiniGoParser.RPAREN)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 269
                self.vartype()


            self.state = 272
            self.block()
            self.state = 273
            self.endline()
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
        self.enterRule(localctx, 38, self.RULE_recevier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MiniGoParser.LPAREN)
            self.state = 276
            self.match(MiniGoParser.ID)
            self.state = 277
            self.match(MiniGoParser.ID)
            self.state = 278
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

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.param()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 281
                self.match(MiniGoParser.COMMA)
                self.state = 282
                self.param()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(MiniGoParser.ID)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 289
                self.match(MiniGoParser.COMMA)
                self.state = 290
                self.match(MiniGoParser.ID)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self.vartype()
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
        self.enterRule(localctx, 44, self.RULE_stmt)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 300
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 302
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 303
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 304
                self.breakstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 305
                self.continuestmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 306
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 307
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def structaccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructaccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 310
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 311
                self.arrayaccess()
                pass

            elif la_ == 3:
                self.state = 312
                self.structaccess()
                pass


            self.state = 315
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 316
            self.expr()
            self.state = 317
            self.endline()
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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSEIF)
            else:
                return self.getToken(MiniGoParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.IF)
            self.state = 320
            self.match(MiniGoParser.LPAREN)
            self.state = 321
            self.expr()
            self.state = 322
            self.match(MiniGoParser.RPAREN)
            self.state = 323
            self.block()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ELSEIF:
                self.state = 324
                self.match(MiniGoParser.ELSEIF)
                self.state = 325
                self.match(MiniGoParser.LPAREN)
                self.state = 326
                self.expr()
                self.state = 327
                self.match(MiniGoParser.RPAREN)
                self.state = 328
                self.block()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 335
                self.match(MiniGoParser.ELSE)
                self.state = 336
                self.block()


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
        self.enterRule(localctx, 50, self.RULE_forstmt)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.forbasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.forstep()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
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


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forbasic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForbasic" ):
                return visitor.visitForbasic(self)
            else:
                return visitor.visitChildren(self)




    def forbasic(self):

        localctx = MiniGoParser.ForbasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forbasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.FOR)
            self.state = 345
            self.forcondition()
            self.state = 346
            self.block()
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 347
                self.endline()


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


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstep" ):
                return visitor.visitForstep(self)
            else:
                return visitor.visitChildren(self)




    def forstep(self):

        localctx = MiniGoParser.ForstepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forstep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.FOR)
            self.state = 351
            self.forinit()
            self.state = 352
            self.match(MiniGoParser.SEMI)
            self.state = 353
            self.forcondition()
            self.state = 354
            self.match(MiniGoParser.SEMI)
            self.state = 355
            self.forupdate()
            self.state = 356
            self.block()
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 357
                self.endline()


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


        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_foreach

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach" ):
                return visitor.visitForeach(self)
            else:
                return visitor.visitChildren(self)




    def foreach(self):

        localctx = MiniGoParser.ForeachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_foreach)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.FOR)
            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 362
            self.match(MiniGoParser.COMMA)
            self.state = 363
            self.match(MiniGoParser.ID)
            self.state = 364
            self.match(MiniGoParser.ASSIGN)
            self.state = 365
            self.match(MiniGoParser.RANGE)
            self.state = 366
            self.expr()
            self.state = 367
            self.block()
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 368
                self.endline()


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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MiniGoParser.VartypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinit" ):
                return visitor.visitForinit(self)
            else:
                return visitor.visitChildren(self)




    def forinit(self):

        localctx = MiniGoParser.ForinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forinit)
        self._la = 0 # Token type
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(MiniGoParser.ID)
                self.state = 372
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 373
                self.expr()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(MiniGoParser.VAR)
                self.state = 375
                self.match(MiniGoParser.ID)
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 376
                    self.vartype()


                self.state = 379
                self.match(MiniGoParser.EQUAL)
                self.state = 380
                self.expr()
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
        self.enterRule(localctx, 60, self.RULE_forcondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
            return MiniGoParser.RULE_forupdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForupdate" ):
                return visitor.visitForupdate(self)
            else:
                return visitor.visitChildren(self)




    def forupdate(self):

        localctx = MiniGoParser.ForupdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forupdate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.ID)
            self.state = 386
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 387
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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.LBRACE)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 390
                self.stmt()
                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 396
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

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(MiniGoParser.RETURN)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 399
                self.expr()


            self.state = 402
            self.endline()
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
        self.enterRule(localctx, 68, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(MiniGoParser.BREAK)
            self.state = 405
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
        self.enterRule(localctx, 70, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(MiniGoParser.CONTINUE)
            self.state = 408
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

        def endline(self):
            return self.getTypedRuleContext(MiniGoParser.EndlineContext,0)


        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MiniGoParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 410
                self.methodcall()
                pass

            elif la_ == 2:
                self.state = 411
                self.funcall()
                pass


            self.state = 414
            self.endline()
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

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Exp1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Exp1Context,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OR)
            else:
                return self.getToken(MiniGoParser.OR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.exp1()
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.OR:
                self.state = 417
                self.match(MiniGoParser.OR)
                self.state = 418
                self.exp1()
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Exp2Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Exp2Context,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.AND)
            else:
                return self.getToken(MiniGoParser.AND, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = MiniGoParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.exp2()
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.AND:
                self.state = 425
                self.match(MiniGoParser.AND)
                self.state = 426
                self.exp2()
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exp3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Exp3Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Exp3Context,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.EQ)
            else:
                return self.getToken(MiniGoParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEQ)
            else:
                return self.getToken(MiniGoParser.NEQ, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LT)
            else:
                return self.getToken(MiniGoParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LTE)
            else:
                return self.getToken(MiniGoParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.GT)
            else:
                return self.getToken(MiniGoParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.GTE)
            else:
                return self.getToken(MiniGoParser.GTE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = MiniGoParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.exp3()
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0):
                self.state = 433
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 434
                self.exp3()
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exp4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Exp4Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Exp4Context,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.PLUS)
            else:
                return self.getToken(MiniGoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MINUS)
            else:
                return self.getToken(MiniGoParser.MINUS, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MiniGoParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.exp4()
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 441
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.exp4()
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exp5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Exp5Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Exp5Context,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MULT)
            else:
                return self.getToken(MiniGoParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DIV)
            else:
                return self.getToken(MiniGoParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MOD)
            else:
                return self.getToken(MiniGoParser.MOD, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MiniGoParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.exp5()
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULT) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 449
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULT) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                self.exp5()
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exp5(self):
            return self.getTypedRuleContext(MiniGoParser.Exp5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

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
        self.enterRule(localctx, 84, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 457
                self.exp5()
                pass
            elif token in [MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.BOOLLIT, MiniGoParser.NILLIT, MiniGoParser.ID, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Exp7Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Exp7Context,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = MiniGoParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp6)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.exp7()
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK or _la==MiniGoParser.DOT:
                self.state = 468
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DOT]:
                    self.state = 462
                    self.match(MiniGoParser.DOT)
                    self.state = 463
                    self.exp7()
                    pass
                elif token in [MiniGoParser.LBRACK]:
                    self.state = 464
                    self.match(MiniGoParser.LBRACK)
                    self.state = 465
                    self.expr()
                    self.state = 466
                    self.match(MiniGoParser.RBRACK)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 88, self.RULE_exp7)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(MiniGoParser.LPAREN)
                self.state = 474
                self.expr()
                self.state = 475
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 478
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 479
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 480
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 481
                self.match(MiniGoParser.NILLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 482
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 483
                self.funcall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 484
                self.arraylit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 485
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
        self.enterRule(localctx, 90, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.arraytype()
            self.state = 489
            self.match(MiniGoParser.LBRACE)
            self.state = 490
            self.lit_list()
            self.state = 491
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

        def lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LitContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lit_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_list" ):
                return visitor.visitLit_list(self)
            else:
                return visitor.visitChildren(self)




    def lit_list(self):

        localctx = MiniGoParser.Lit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_lit_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.lit()
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 494
                self.match(MiniGoParser.COMMA)
                self.state = 495
                self.lit()
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def lit_list(self):
            return self.getTypedRuleContext(MiniGoParser.Lit_listContext,0)


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
        self.enterRule(localctx, 94, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(MiniGoParser.LBRACE)
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                    self.state = 502
                    self.lit_list()


                self.state = 505
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 508
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 509
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 510
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 511
                self.match(MiniGoParser.NILLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 512
                self.structlit()
                pass


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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def astribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AstributeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AstributeContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructlit" ):
                return visitor.visitStructlit(self)
            else:
                return visitor.visitChildren(self)




    def structlit(self):

        localctx = MiniGoParser.StructlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_structlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.ID)
            self.state = 516
            self.match(MiniGoParser.LBRACE)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 517
                self.astribute()
                self.state = 518
                self.expr()
                self.state = 525
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 519
                    self.match(MiniGoParser.COMMA)
                    self.state = 520
                    self.astribute()
                    self.state = 521
                    self.expr()
                    self.state = 527
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 530
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 98, self.RULE_astribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(MiniGoParser.ID)
            self.state = 533
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

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def structaccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructaccessContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)




    def methodcall(self):

        localctx = MiniGoParser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_methodcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 535
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 536
                self.arrayaccess()
                pass

            elif la_ == 3:
                self.state = 537
                self.structaccess()
                pass


            self.state = 540
            self.match(MiniGoParser.DOT)
            self.state = 541
            self.match(MiniGoParser.ID)
            self.state = 542
            self.match(MiniGoParser.LPAREN)
            self.state = 551
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 543
                self.expr()
                self.state = 548
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 544
                    self.match(MiniGoParser.COMMA)
                    self.state = 545
                    self.expr()
                    self.state = 550
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 553
            self.match(MiniGoParser.RPAREN)
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

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MiniGoParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MiniGoParser.ID)
            self.state = 556
            self.match(MiniGoParser.LPAREN)
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 557
                self.expr()
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 558
                    self.match(MiniGoParser.COMMA)
                    self.state = 559
                    self.expr()
                    self.state = 564
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 567
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
        self.enterRule(localctx, 104, self.RULE_arrayaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.ID)
            self.state = 570
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

        def access(self):
            return self.getTypedRuleContext(MiniGoParser.AccessContext,0)


        def asaccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AsaccessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AsaccessContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructaccess" ):
                return visitor.visitStructaccess(self)
            else:
                return visitor.visitChildren(self)




    def structaccess(self):

        localctx = MiniGoParser.StructaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_structaccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(MiniGoParser.ID)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACK:
                self.state = 573
                self.access()


            self.state = 577 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 576
                    self.asaccess()

                else:
                    raise NoViableAltException(self)
                self.state = 579 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess" ):
                return visitor.visitAccess(self)
            else:
                return visitor.visitChildren(self)




    def access(self):

        localctx = MiniGoParser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 581
                self.match(MiniGoParser.LBRACK)
                self.state = 582
                self.expr()
                self.state = 583
                self.match(MiniGoParser.RBRACK)
                self.state = 587 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACK):
                    break

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

        def access(self):
            return self.getTypedRuleContext(MiniGoParser.AccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsaccess" ):
                return visitor.visitAsaccess(self)
            else:
                return visitor.visitChildren(self)




    def asaccess(self):

        localctx = MiniGoParser.AsaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_asaccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(MiniGoParser.DOT)
            self.state = 590
            self.match(MiniGoParser.ID)
            self.state = 592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACK:
                self.state = 591
                self.access()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_intlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlit" ):
                return visitor.visitIntlit(self)
            else:
                return visitor.visitChildren(self)




    def intlit(self):

        localctx = MiniGoParser.IntlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_intlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MiniGoParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_floatlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatlit" ):
                return visitor.visitFloatlit(self)
            else:
                return visitor.visitChildren(self)




    def floatlit(self):

        localctx = MiniGoParser.FloatlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_floatlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(MiniGoParser.FLOATLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_stringlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringlit" ):
                return visitor.visitStringlit(self)
            else:
                return visitor.visitChildren(self)




    def stringlit(self):

        localctx = MiniGoParser.StringlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_stringlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(MiniGoParser.STRINGLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_boollit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = MiniGoParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_boollit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.BOOLLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NillitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NILLIT(self):
            return self.getToken(MiniGoParser.NILLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nillit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNillit" ):
                return visitor.visitNillit(self)
            else:
                return visitor.visitChildren(self)




    def nillit(self):

        localctx = MiniGoParser.NillitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_nillit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(MiniGoParser.NILLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_idlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlit" ):
                return visitor.visitIdlit(self)
            else:
                return visitor.visitChildren(self)




    def idlit(self):

        localctx = MiniGoParser.IdlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_idlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = MiniGoParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(MiniGoParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





