
grammar tlang;

start : instruction_list EOF
      ;

instruction_list : (instruction)*
		 ;

strict_ilist : (instruction)+
             ;

instruction : assignment
	    | ifConditional
	    | loop
	    | moveCommand
	    | penCommand
	    | gotoCommand
	    | pauseCommand
		| functionDeclaration
		| functionCall
		| returnInstruction
	    ;

call : NAME | VAR ;
functionDeclaration : 'to' NAME (VAR)* strict_ilist 'end';
functionCall : call '(' argumentList? ')' ;
argumentList : expression (',' expression)* ;
returnInstruction : 'return' expression? ;

ifConditional : 'if' condition '[' strict_ilist ']' (elifConditional)* elseConditional? ;

elifConditional : 'elif' condition '[' strict_ilist ']' ;

elseConditional : 'else' '[' strict_ilist ']' ;

loop : 'repeat' value '[' strict_ilist ']' ;

gotoCommand : 'goto' '(' expression ',' expression ')';

assignment : VAR '=' expression
	   ;

moveCommand : moveOp expression ;
moveOp : 'forward' | 'backward' | 'left' | 'right' ;

penCommand : 'penup' | 'pendown' ;

pauseCommand : 'pause' ;

expression : 
             MINUS expression               	   #unaryExpr
           | expression multiplicative expression  #mulExpr
		   | expression additive expression        #addExpr
		   | functionCall				   	   	   #funcExpr
		   | lambdaExpr							   #lambdaExpression
		   | lazyExpr							   #lazyExpression
		   | rangeExpr							   #rangeExpression
		   | matchExpr							   #matchExpression
		   | value                                 #valueExpr
		   | '(' expression ')'                    #parenExpr
 	   ;

lambdaExpr : 'lambda' (VAR)* '=>' expression ;

lazyExpr : 'lazy' expression ;

rangeExpr : '[' expression '..' expression? ']' ;

matchExpr : 'match' expression 'with' matchCase+ ;
matchCase : '|' pattern '=>' expression ;
pattern : NUM | VAR | '_' ;

multiplicative : MUL | DIV;
additive : PLUS | MINUS;

PLUS     : '+' ;
MINUS    : '-' ;
MUL  	 : '*' ;
DIV      : '/' ;

condition : NOT condition
      | expression binCondOp expression
	  | condition logicOp condition
	  | PENCOND
	  | '(' condition ')'
	  ;


binCondOp :  EQ | NEQ | LT | GT | LTE | GTE
	 ;

logicOp : AND | OR ;

PENCOND : 'pendown?';
LT : '<' ;
GT : '>' ;
EQ : '==';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
AND: '&&';
OR : '||';
NOT: '!' ;

value : NUM
      | VAR
	  | NAME
      ;

NUM  : [0-9]+        ;

VAR  : ':'[a-zA-Z_] [a-zA-Z0-9]* ;

NAME : [a-zA-Z]+     ;

Whitespace: [ \t\n\r]+ -> skip;
