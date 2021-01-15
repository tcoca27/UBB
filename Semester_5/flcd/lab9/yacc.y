%{
	#include<stdio.h>
	#include<stdlib.h>
	#define YYDEBUG 1
%}
%error-verbose


%token MAIN
%token INTREG
%token CITESTE
%token CARACTER
%token ADEVAR
%token PRINTEAZA
%token RAPORTEAZA
%token ADEVARAT
%token FALS
%token DACA
%token DACA_NU
%token EVENTUAL
%token IN_TIMP_CE
%token NU
%token STD_IN
%token STD_OUT
%token IDENTIFIER
%token CONSTANT
%token COMMA
%token SEMI_COLON
%token OPEN_SQUARE_BRACKET
%token CLOSED_SQUARE_BRACKET
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token PLUS
%token MINUS
%token POWER
%token DIV
%token MUL
%token PERCENT
%token EQ
%token RELATION

%start program

%% 

program: INTREG MAIN OPEN_ROUND_BRACKET CLOSED_ROUND_BRACKET compound_stmt;
declaration: type IDENTIFIER;
type: INTREG|CARACTER|ADEVAR;
stmt_list: stmt SEMI_COLON stmt_list|stmt SEMI_COLON;
stmt: declaration|simple_stmt|struct_stmt;
simple_stmt: assignment_stmt|io_stmt|return_stmt;
struct_stmt: compound_stmt|if_stmt|while_stmt;
assignment_stmt: IDENTIFIER EQ expression;
return_stmt: RAPORTEAZA IDENTIFIER|RAPORTEAZA CONSTANT;
io_stmt: read_stmt|print_stmt;
read_stmt: CITESTE OPEN_ROUND_BRACKET STD_IN COMMA IDENTIFIER CLOSED_ROUND_BRACKET;
print_stmt: CITESTE OPEN_ROUND_BRACKET STD_OUT COMMA IDENTIFIER CLOSED_ROUND_BRACKET;
compound_stmt: OPEN_CURLY_BRACKET stmt_list CLOSED_CURLY_BRACKET;
if_stmt: simple_if|simple_if else|simple_if else_if else;
simple_if: DACA OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET compound_stmt;
else: EVENTUAL compound_stmt;
else_if: DACA_NU OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET compound_stmt;
while_stmt: IN_TIMP_CE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET compound_stmt;
condition: expression RELATION expression;
expression: term|expression operator expression
term: IDENTIFIER|CONSTANT|IDENTIFIER OPEN_SQUARE_BRACKET INTREG CLOSED_SQUARE_BRACKET;
operator: PLUS|MINUS|DIV|MUL|POWER|PERCENT;


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
    fprintf(stderr,"\t CORRECT\n");
}