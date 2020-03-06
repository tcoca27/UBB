%subPrime= l1 U subPrime(l2...ln,pos+1), ! primeW(pos)
%          l1^2-1 U subPrime(l2...ln,pos+1, primeW(pos)
%subPrime(L:list,P:int,R:list)
%flowmodel(i,i,o)
%
%prime(x,d)=1,d=x
%           0, mod(x,d)=0
%           prime(x,d+1), otherwise
%
%prime(X:int, D:int, R:int)
%flowmodel(i,i,o)
%
%primeW(X,R)=prime(X,2,R)
%primeW(X:int,R:int)
%flowmodel(i,o)

prime(1,_,R):-R is 0.
prime(X,D,R):-D=:=X,
    R is 1,!.
prime(X,D,R):-mod(X,D)=:=0,
    R is 0,!.
prime(X,D,R):-D1 is D+1,
    prime(X,D1,R).

primeW(X,R):-prime(X,2,R).

subPrime([],_,[]).
subPrime([H|T],P,R):-primeW(P,R1),
    R1=:=0,
    P1 is P+1,
    subPrime(T,P1,R2),
    R=[H|R2].
subPrime([H|T],P,R):-primeW(P,R1),
    R1=:=1,
    P1 is P+1,
    H1 is H*H-1,
    subPrime(T,P1,R2),
    R=[H1|R2].

%subPrimeW(L,R)=subPrime(L,1,R)
%subPrimeW(L:list,R:list)
%flowmodel(i,o)

subPrimeW(L,R):-subPrime(L,1,R).
