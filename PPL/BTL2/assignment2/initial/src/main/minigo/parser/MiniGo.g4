//2211583
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
    language=Python3;
}

// Parser rules
program  : decl+ EOF ;
//decl_list: decl decl_list | decl;
decl: funcdecl
    | methoddecl
    | vardecl
    | constdecl
    | typedecl
    | NEWLINE
    ;



/* VARIABLE DECLARATIONS */
vardecl: (VAR idlist (vartype (EQUAL exprlist)? | EQUAL exprlist) endline) ;

idlist: ID (COMMA ID)*;
exprlist: expr (COMMA expr)* ;
//expr_scalar_list: expr_scalar (COMMA expr_scalar)*;
vartype: INT | FLOAT | STRING | BOOLEAN | arraytype | structtype ;
scalartype: INT | FLOAT | STRING | BOOLEAN;

constdecl: CONST idlist vartype? EQUAL exprlist endline;

arraytype: (LBRACK (INTLIT | ID) RBRACK)+ vartype ;
structtype: ID;


structdecl: STRUCT LBRACE elements+ RBRACE ;
interfacedecl: INTERFACE LBRACE methodbody+ RBRACE;
elements: ID vartype endline;
methodbody: ID LPAREN paramlist? RPAREN vartype? endline;
typedecl: TYPE ID (structdecl | interfacedecl) endline;


// Xử lý newline
multiple_newline: NEWLINE multiple_newline| NEWLINE;
endline: NEWLINE | SEMI;

/* FUNCTION */
methoddecl: FUNC recevier ID LPAREN paramlist? RPAREN vartype? block endline;
funcdecl: FUNC ID LPAREN paramlist? RPAREN vartype? block endline;
recevier: LPAREN ID ID RPAREN;
paramlist: param (COMMA param)* ;
param: ID (COMMA ID)* vartype ;


stmt: vardecl
    | constdecl
    | assignstmt
    | ifstmt
    | forstmt
    | returnstmt
    | breakstmt
    | continuestmt
    | callstmt
    | NEWLINE
    ;

assignstmt: (ID | arrayaccess | structaccess) (ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr endline;

ifstmt: IF LPAREN expr RPAREN block
    (ELSEIF LPAREN expr RPAREN block )*
    (ELSE block)? ;
//boolexpr: expr (EQ | NEQ | LT | LTE | GT | GTE) expr;

forstmt: forbasic | forstep | foreach;
forbasic: FOR forcondition block endline?;
forstep: FOR forinit SEMI forcondition SEMI forupdate block endline?;
foreach: FOR ID COMMA ID ASSIGN RANGE expr block endline?;
forinit: ID (ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr | (VAR ID vartype? EQUAL expr) ;
forcondition: expr ;
forupdate: ID (ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expr;

//expr_scalar: exp1_scalar ( OR exp1_scalar )* ;
//exp1_scalar: exp2_scalar ( AND exp2_scalar )* ;
//exp2_scalar: exp3_scalar ( (EQ | NEQ | LT | LTE | GT | GTE) exp3_scalar )* ;
//exp3_scalar: exp4_scalar ( (PLUS | MINUS) exp4_scalar )* ;
//exp4_scalar: exp5_scalar ( (MULT | DIV | MOD) exp5_scalar )* ;
//exp5_scalar: (NOT | MINUS) exp5_scalar | exp6_scalar;
//exp6_scalar: exp7_scalar ( (DOT ID) | (LBRACK expr_scalar RBRACK) )* ;
//exp7_scalar: LPAREN expr_scalar RPAREN
//           | INTLIT
//           | FLOATLIT
//           | STRINGLIT
//           | BOOLLIT
//           | NILLIT
//           | ID
//           | funcall
//           ;



block: LBRACE stmt* RBRACE ;

returnstmt: RETURN expr? endline ;

breakstmt: BREAK endline ;
continuestmt: CONTINUE endline ;
callstmt: (methodcall | funcall) endline ;

expr: exp1 ( OR exp1 )* ;
exp1 : exp2 ( AND exp2 )* ;
exp2: exp3 ( (EQ | NEQ | LT | LTE | GT | GTE) exp3 )* ;
exp3: exp4 ( (PLUS | MINUS) exp4 )* ;
exp4: exp5 ( (MULT | DIV | MOD) exp5 )* ;
exp5: (NOT | MINUS) exp5 | exp6;
exp6: exp7 ( (DOT exp7) | (LBRACK expr RBRACK) )* ;
exp7: LPAREN expr RPAREN | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | NILLIT | ID | funcall| arraylit| structlit;


arraylit: arraytype LBRACE lit_list RBRACE;
lit_list: lit (COMMA lit)*;
lit: LBRACE lit_list? RBRACE
    | ID
    | INTLIT
    | FLOATLIT
    | BOOLLIT
    | STRINGLIT
    | NILLIT
    | structlit;
structlit: ID LBRACE (astribute expr (COMMA astribute expr)*)? RBRACE ;
astribute: ID COLON;
methodcall: (ID | arrayaccess | structaccess ) DOT ID LPAREN (expr (COMMA expr)*)? RPAREN ;
funcall: ID LPAREN (expr (COMMA expr)*)? RPAREN ;

arrayaccess: ID access ;
structaccess: ID access? (asaccess)+ ;
access: (LBRACK expr RBRACK)+;
asaccess: DOT ID access?;

intlit: INTLIT;
floatlit: FLOATLIT;
stringlit: STRINGLIT;
boollit: BOOLLIT;
nillit: NILLIT;
idlit: ID;
newline: NEWLINE;
// Lexer rules cho từ khóa
VAR: 'var';
CONST: 'const';
STRUCT: 'struct';
INTERFACE: 'interface';
TYPE: 'type';
FUNC: 'func';
IF: 'if';
ELSEIF: 'else if';
ELSE: 'else';
FOR: 'for';
RANGE: 'range';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';

// Các toán tử và dấu câu
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI: ';';
COLON: ':';
DOT: '.';

EQUAL: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

ASSIGN: ':=';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULT_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

// Built-in functions
//BUILTIN_FUNC: 'getInt' | 'putInt' | 'putIntLn' | 'getFloat' | 'putFloat' | 'putFloatLn'
//            | 'getBool' | 'putBool' | 'putBoolLn' | 'getString' | 'putString' | 'putStringLn'
//            | 'putLn';

// Lexer rules khác
BOOLLIT: 'true' | 'false';
NILLIT: 'nil';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INTLIT: ('0b' | '0B') [01]+
      | ('0o' | '0O') [0-7]+
      | ('0x' | '0X') [0-9a-fA-F]+
      | [0]
      | [1-9][0-9]*;
FLOATLIT: [0-9]+ DOT [0-9]* ([eE] [+-]? [0-9]+)?;
STRINGLIT: '"' ( ~[\r\n"\\] | ESC_SEQ )* '"';
fragment ESC_SEQ: '\\' [ntr"\\] ;


COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' (MULTILINE_COMMENT| .)*? '*/' -> skip;

NEWLINE: ('\r'? '\n'){
    if self.InsertSemi():
       self.text = ';'
    else:
       self.skip()
};
WS: [ \t\r\f]+ -> skip;



UNCLOSE_STRING: '"' ( ESC_SEQ | ~["\\])* ([\r\n] | EOF)
{
    index = self.text.find('\n')
    pos_of_r = self.text.find('\r')
    if  pos_of_r <= index - 1 and pos_of_r >0:
        raise UncloseString(self.text[:pos_of_r ])
    else:
        if index != -1:
            raise UncloseString(self.text[:index])
        else:
            raise UncloseString(self.text)
};

ILLEGAL_ESCAPE: '"' ( ~["\\] | ESC_SEQ )* '\\' ~[ntr"\\]
{
    raise IllegalEscape(self.text) ;
};


ERROR_CHAR: . { raise ErrorToken(self.text)};