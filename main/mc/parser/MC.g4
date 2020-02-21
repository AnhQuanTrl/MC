//1712830
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program:  declaration+ EOF;
declaration: var_dec | func_dec;
var_dec: primitive_type variable (CM variable)* SM;
variable: ID (LS INTLIT RS)?;
func_dec: mctype ID LB (par_dec (CM par_dec)*)? RB block_statement;
par_dec: primitive_type ID (LS RS)?;
block_statement: LP (var_dec | statement)* RP;
statement: matched_statement| unmatched_statment;
matched_statement: IF LB expression RB matched_statement ELSE matched_statement| other_statement;
unmatched_statment: IF LB expression RB statement | IF LB expression RB matched_statement ELSE unmatched_statment;
other_statement: for_statement | dowhile_statement | break_statement | continue_statement | return_statment | expression_statement | block_statement;
dowhile_statement: DO statement+ WHILE expression SM;
for_statement: FOR LB expression SM expression SM expression RB statement;
break_statement: BREAK SM;
continue_statement: CONTINUE SM;
return_statment: RETURN (expression)? SM;
expression_statement: expression SM;
expression: or_expression ASSIGN expression | or_expression;
or_expression: or_expression OR and_expression | and_expression;
and_expression: and_expression AND eq_expression | eq_expression;
eq_expression: rel_expression ((EQ | NE) rel_expression)?;
rel_expression: arithmetic_expression ((LT | LTE | GT | GTE) arithmetic_expression)?;
arithmetic_expression: arithmetic_expression (ADD | SUB) factor | factor;
factor: factor (DIV | MUL | MOD) term | term;
term: (SUB | NOT) term | index_expression;
index_expression: basic_expression (LS expression RS)?;
basic_expression: ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB expression RB | invo_expression;
invo_expression: ID LB (expression (CM expression)*)? RB;
mctype: primitive_type (LS RS)? | VOID; 
primitive_type: BOOLEAN | INT | FLOAT | STRING;

INT: 'int' ;

VOID: 'void' ;

BOOLEAN: 'boolean';

BREAK: 'break';

CONTINUE: 'continue';

ELSE: 'else';

FOR: 'for';

FLOAT: 'float';

IF: 'if';

RETURN: 'return';

DO: 'do';

WHILE: 'while';


STRING: 'string';
BOOLLIT: 'true' | 'false';
FLOATLIT: ((DIGIT+ (('.' DIGIT* EXP?) | EXP)) | ('.' DIGIT+ EXP?));
INTLIT: DIGIT+;
STRINGLIT: '"' (~["\\\r\n] | ESCAPE_SEQUENCE)*? '"' {self.text = self.text[1:-1]};
ID: (LETTER | '_') (LETTER | DIGIT | '_')* ;
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment EXP: ('e' | 'E')  '-'? [0-9]+;
fragment ESCAPE_SEQUENCE: '\\' [bfrnt"\\];


ADD: '+';
MUL: '*';
NOT: '!';
OR: '||';
NE: '!=';
LT: '<';
LTE: '<=';
EQ: '==';
GT: '>';
GTE: '>=';
ASSIGN: '=';
SUB: '-';
DIV: '/';
MOD: '%';
AND: '&&';

LS: '[';

RS: ']';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SM: ';' ;

CM: ',';
COMMENT: ('/*' .*? '*/' | '//' ~[\r\n]* ) -> skip;
WS : [ \t\r\n\f]+ -> skip ; 
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESCAPE_SEQUENCE)*('\\'(~[bfrnt"\\] | EOF)) ;
UNCLOSE_STRING: '"' (~["\\\r\n] | ESCAPE_SEQUENCE)*;
ERROR_CHAR: .;




