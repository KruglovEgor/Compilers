grammar MyLang;

program: statement+ EOF;

statement: 
    assignment 
    | ifStatement 
    | whileLoop 
    | printStmt
    | inputStmt;

assignment: ID '=' expr ';';

ifStatement: 'if' '(' expr ')' block ('else' block)?;

whileLoop: 'while' '(' expr ')' block;

printStmt: 'print' '(' expr ')' ';';

inputStmt: 'input' '(' ID ')' ';'; 

block: '{' statement* '}' | statement;

expr:
    expr op=('*' | '/' | '%') expr   # MulDivMod
    | expr op=('+' | '-') expr       # AddSub
    | expr op=('>' | '<' | '>=' | '<=' | '==' | '!=') expr # Compare
    | NUMBER                         # Number
    | STRING                         # String
    | ID                             # Variable
    | '(' expr ')'                   # Parens
    | '-' expr                       # UnaryMinus
    | '!' expr                       # LogicalNot
    ;

// Лексер
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
STRING: '"' .*? '"';

// Пропускаем пробелы и переносы строк
WS: [ \t\n\r]+ -> skip;

// Комментарии
COMMENT: '//' ~[\r\n]* -> skip; 