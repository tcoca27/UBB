gcd(A,0,A).
gcd(0,B,B).
gcd(A,B,R):-A<B,
    B1 is B-A,
    gcd(A,B1,R).
gcd(A,B,R):-A>=B,
    A1 is A-B,
    gcd(A1,B,R).

scm(A,B,R):-gcd(A,B,R1),
    R is A*B/R1.

cml([],M,M).
cml([H|T],M,R):-scm(H,M,M1),
    cml(T,M1,R).

addPower([],_,_,_,[]).
addPower([H|T],C,P,E,R):-
    C=:=P,
    C1 is C+1,
    P1 is P*2,
    addPower(T,C1,P1,E,R1),
    R = [H,E|R1].
addPower([H|T],C,P,E,R):-C=\=P,
    C1 is C+1,
    addPower(T,C1,P,E,R1),
    R = [H|R1].

removeAll([],_,[]).
removeAll([H|T],A,R):-H=:=A,
    removeAll(T,A,R).
removeAll([H|T],A,R):-H=\=A,
    removeAll(T,A,R1),
    R=[H|R1].

countOcc([],_,0).
countOcc([H|T],X,R):-H=:=X,
    countOcc(T,X,R1),
    R is 1+R1.
countOcc([H|T],X,R):-H=\=X,
    countOcc(T,X,R).

atomL([],[]).
atomL([H|T],R):-countOcc([H|T],H,O),
    removeAll([H|T],H,R1),
    atomL(R1,R2),
    R=[[H,O]|R2].

removeRep([],[]).
removeRep([H|T],R):-countOcc([H|T],H,O),
    O>1,
    removeAll([H|T],H,R1),
    removeRep(R1,R).
removeRep([H|T],R):-countOcc([H|T],H,O),
    O=:=1,
    removeRep(T,R1),
    R=[H|R1].

setDif([],B,B).
setDif([],[],[]).
setDif([H|T],L,R):-countOcc(L,H,O),
    O=:=0,
    L1=[H|L],
    setDif(T,L1,R).
setDif([H|T],L,R):-countOcc(L,H,O),
    O=\=0,
    removeAll(L,H,R1),
    setDif(T,R1,R).

isEven(X,R):-mod(X,2)=:=0,
    R is 1.
isEven(X,R):-mod(X,2)=:=1,
    R is 0.

addEven([],_,[]).
addEven([H|T],E,R):-isEven(H,R1),
    R1=:=1,
    addEven(T,E,R2),
    R=[H,E|R2].
addEven([H|T],E,R):-isEven(H,R1),
    R1=:=0,
    addEven(T,E,R2),
    R=[H|R2].

