checkifexists(_,[],0).
checkifexists(X,[H|_],R):-X=H,!,R is 1.
checkifexists(X,[H|T],R):-X\=H,checkifexists(X,T,R).

lts([],[]).
lts([H|T],X):-checkifexists(H,T,R),R=:=0,lts(T,Y),X=[H|Y].
lts([H|T],X):-checkifexists(H,T,R),R=:=1,lts(T,X).
