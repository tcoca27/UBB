%1a
gcd(0,B,B).
gcd(A,0,A).
gcd(A,B,R):-A>=B,
    A1 is A mod B,
    gcd(A1,B,R).
gcd(A,B,R):-B>A,
    B1 is B mod A,
    gcd(A,B1,R).

glm(A,B,R):-gcd(A,B,Rez),
    R is A*B/Rez.

glmL([],R,R):-!.
glmL([H|T],R,R1):-
    glm(H,R,Rez),
    glmL(T,Rez,R1).

glmW(L,R):-glmL(L,1,R).

%b
insertPos([],0,A,[A]).
insertPos([],_,_,[]).
insertPos([H|T],P,A,R):-
    P=\=0,
    P1 is P-1,
    insertPos(T,P1,A,R1),
    R=[H|R1].
insertPos([H|T],P,A,R):-P=:=0,
    P1 is P-1,
    insertPos(T,P1,A,R1),
    R=[A,H|R1].

insertPow([],_,_,_,[]).
insertPow([H|T],P,C,X,R):-C=\=P,
    C1 is C+1,
    insertPow(T,P,C1,X,R1),
    R = [H|R1].
insertPow([H|T],P,C,X,R):-C=:=P,
    C1 is C+1,
    P1 is P*2,
    insertPow(T,P1,C1,X,R1),
    R = [H,X|R1].
