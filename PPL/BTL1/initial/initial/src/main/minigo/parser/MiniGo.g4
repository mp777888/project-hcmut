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
program: decl_list EOF;
decl_list: decl decl_tail;
decl_tail: decl decl_tail | /* empty */;

decl: funcdecl
    | methoddecl
    | vardecl
    | constdecl
    | typedecl
    | NEWLINE
    ;

/* VARIABLE DECLARATIONS */
vardecl: VAR idlist var_init endline;
var_init: vartype var_init_extra | EQUAL exprlist;
var_init_extra: EQUAL exprlist | /* empty */;

idlist: ID id_tail;
id_tail: COMMA ID id_tail | /* empty */;

exprlist: expr expr_tail;
expr_tail: COMMA expr expr_tail | /* empty */;

vartype: INT | FLOAT | STRING | BOOLEAN | arraytype | structtype;
scalartype: INT | FLOAT | STRING | BOOLEAN;

constdecl: CONST idlist const_init endline;
const_init: vartype EQUAL exprlist | EQUAL exprlist;

arraytype: LBRACK array_size RBRACK array_type_tail vartype;
array_size: INTLIT | ID;
array_type_tail: LBRACK array_size RBRACK array_type_tail | /* empty */;

structtype: ID;

structdecl: STRUCT LBRACE element_list RBRACE;
element_list: elements element_list | elements;

interfacedecl: INTERFACE LBRACE method_list RBRACE;
method_list: methodbody method_list | methodbody;

elements: ID vartype endline;
methodbody: ID LPAREN paramlist_opt RPAREN vartype_opt endline;
vartype_opt: vartype | /* empty */;

typedecl: TYPE ID type_body endline;
type_body: structdecl | interfacedecl;

// Xử lý newline
multiple_newline: NEWLINE multiple_newline_tail;
multiple_newline_tail: NEWLINE multiple_newline_tail | /* empty */;
endline: NEWLINE | SEMI;

/* FUNCTION */
methoddecl: FUNC recevier ID LPAREN paramlist_opt RPAREN vartype_opt block endline;
funcdecl: FUNC ID LPAREN paramlist_opt RPAREN vartype_opt block endline;
paramlist_opt: paramlist | /* empty */;

recevier: LPAREN ID ID RPAREN;
paramlist: param param_tail;
param_tail: COMMA param param_tail | /* empty */;
param: ID id_param_tail vartype;
id_param_tail: COMMA ID id_param_tail | /* empty */;

stmt_list: stmt stmt_list | /* empty */;
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

assignstmt: lhs assign_op expr endline;
lhs: ID | arrayaccess | structaccess;
assign_op: ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

ifstmt: IF LPAREN expr RPAREN block elseif_list else_part;
elseif_list: ELSEIF LPAREN expr RPAREN block elseif_list | /* empty */;
else_part: ELSE block | /* empty */;

forstmt: forbasic | forstep | foreach;
forbasic: FOR forcondition block endline_opt;
endline_opt: endline | /* empty */;
forstep: FOR forinit SEMI forcondition SEMI forupdate block endline_opt;
foreach: FOR ID COMMA ID ASSIGN RANGE expr block endline_opt;
forinit: ID assign_op expr | VAR ID forinit_var;
forinit_var: vartype_opt EQUAL expr;
forcondition: expr;
forupdate: ID assign_op expr;

block: LBRACE stmt_list RBRACE;

returnstmt: RETURN expr_opt endline;
expr_opt: expr | /* empty */;

breakstmt: BREAK endline;
continuestmt: CONTINUE endline;
callstmt: call_expr endline;
call_expr: methodcall | funcall;

expr: exp1 expr_or;
expr_or: OR exp1 expr_or | /* empty */;
exp1: exp2 exp1_and;
exp1_and: AND exp2 exp1_and | /* empty */;
exp2: exp3 exp2_rel;
exp2_rel: rel_op exp3 exp2_rel | /* empty */;
rel_op: EQ | NEQ | LT | LTE | GT | GTE;
exp3: exp4 exp3_add;
exp3_add: add_op exp4 exp3_add | /* empty */;
add_op: PLUS | MINUS;
exp4: exp5 exp4_mul;
exp4_mul: mul_op exp5 exp4_mul | /* empty */;
mul_op: MULT | DIV | MOD;
exp5: unary_op exp5 | exp6;
unary_op: NOT | MINUS;
exp6: exp7 exp6_access;
exp6_access: access_part exp6_access | /* empty */;
access_part: DOT exp7 | LBRACK expr RBRACK;
exp7: LPAREN expr RPAREN
    | INTLIT
    | FLOATLIT
    | STRINGLIT
    | BOOLLIT
    | NILLIT
    | ID
    | funcall
    | arraylit
    | structlit;

arraylit: arraytype LBRACE lit_list RBRACE;
lit_list: lit lit_tail;
lit_tail: COMMA lit lit_tail | /* empty */;
lit: LBRACE lit_list_opt RBRACE
    | ID
    | INTLIT
    | FLOATLIT
    | BOOLLIT
    | STRINGLIT
    | NILLIT
    | structlit;
lit_list_opt: lit_list | /* empty */;

structlit: ID LBRACE structlit_items_opt RBRACE;
structlit_items_opt: astribute expr structlit_items_tail | /* empty */;
structlit_items_tail: COMMA astribute expr structlit_items_tail | /* empty */;
astribute: ID COLON;

methodcall: method_receiver DOT ID LPAREN arg_list_opt RPAREN;
method_receiver: ID | arrayaccess | structaccess;
arg_list_opt: arg_list | /* empty */;
arg_list: expr arg_tail;
arg_tail: COMMA expr arg_tail | /* empty */;

funcall: ID LPAREN arg_list_opt RPAREN;

arrayaccess: ID access;
structaccess: ID access_opt asaccess_list;
access_opt: access | /* empty */;
asaccess_list: asaccess asaccess_list | /* empty */;
access: LBRACK expr RBRACK access_tail;
access_tail: LBRACK expr RBRACK access_tail | /* empty */;
asaccess: DOT ID access_opt;

// Các lexer rules
// Từ khóa
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

// Các literal
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

// Comment và whitespace
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' (MULTILINE_COMMENT| .)*? '*/' -> skip;

NEWLINE: ('\r'? '\n'){
    if self.InsertSemi():
       self.text = ';'
    else:
       self.skip()
};
WS: [ \t\r\f]+ -> skip;

// Error handling
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
    raise IllegalEscape(self.text);
};

ERROR_CHAR: . { raise ErrorToken(self.text)};