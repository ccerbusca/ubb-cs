%{
#include <stdio.h>
#include <stdlib.h>


#define YYDEBUG 1
%}

%token VAR
%token VAL
%token DEF
%token FOR
%token WHILE
%token IF
%token ELSE
%token PRINTLN
%token PRINT
%token CHAR
%token INTINPUT
%token INPUT
%token BREAK
%token STRING
%token VOID
%token INTEGER
%token BOOLEAN
%token ARRAY
%token MAIN
%token IDENTIFIER_
%token NUMBER
%token CHARACTER
%token WORD
%token CONSTANT
%token COLON
%token SEMICOLON
%token LEFT_CURLY_BRACKET
%token RIGHT_CURLY_BRACKET
%token LEFT_BRACKET
%token RIGHT_BRACKET
%token LEFT_SQUARE_BRACKET
%token RIGHT_SQUARE_BRACKET
%token PLUS
%token MINUS
%token STAR
%token SLASH
%token ASSIGN
%token EQUALS
%token NOT_EQUALS
%token LT
%token LTE
%token GT
%token GTE
%token PLUS_EQUAL
%token MINUS_EQUAL
%token STAR_EQUAL
%token SLASH_EQUAL
%token MODULO
%token ARRAY_DOTS
%token OR
%token AND

%start program

%%

program : DEF MAIN LEFT_BRACKET RIGHT_BRACKET COLON LEFT_CURLY_BRACKET statements RIGHT_CURLY_BRACKET ;
statements : statement | statement statements ;
statement : simple_statement SEMI_COLON | complex_statement ;
simple_statement : variable_decl | variable_assign | print_stmt ;
variable_decl : variable_decl_keywords IDENTIFIER_ COLON TYPE ASSIGN values ;
variable_decl_keywords : VAR | VAL ;
values : value | range_decl | input_statement ;
value : NUMBER | CHARACTER | WORD | IDENTIFIER_ | array_element | expression ; 
range_decl : 




program : FCT MAIN LEFT_ROUND_PARENTHESIS RIGHT_ROUND_PARENTHESIS cmpstmt ;
cmpstmt : LEFT_CURLY_PARENTHESIS stmtlist RIGHT_CURLY_PARENTHESIS ;
stmtlist : stmt SEMI_COLON | stmt SEMI_COLON stmtlist ;
stmt : decl | assignment | iostmt | ifstmt | whilestmt | forstmt | cmpstmt ;
decl : type IDENTIFIER ;
assignment : IDENTIFIER ASSIGNMENT expression ;
iostmt : OUT term | IN term ;
ifstmt : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt | IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt ELSE cmpstmt ;
whilestmt : WHILE LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt ;
forstmt : FOR LEFT_ROUND_PARENTHESIS assignment SEMI_COLON condition SEMI_COLON assignment RIGHT_ROUND_PARENTHESIS cmpstmt ;
relation : LESS_THAN | GREATER_THAN | LESS_OR_EQUAL_THAN | GREATER_OR_EQUAL_THAN | DIFFERENT | EQUAL ;
expression : term | term PLUS expression | term MINUS expression | term MULTIPLY expression | term DIVISION expression | term MOD expression | LEFT_ROUND_PARENTHESIS expression RIGHT_SQUARE_PARENTHESIS ;
term : IDENTIFIER | CONSTANT | IDENTIFIER LEFT_SQUARE_PARENTHESIS term RIGHT_SQUARE_PARENTHESIS  ;
type : primitiveType | arrayDeclaration ;
primitiveType : CHAR | NUMBER | BULA ;
arrayDeclaration : primitiveType LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS  ;
condition : expression relation expression ;


%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1)
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) )
    yydebug = 1;
  if ( !yyparse() )
    fprintf(stderr,"\t hmmm\n");
}