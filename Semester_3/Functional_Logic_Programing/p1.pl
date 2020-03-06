%6. a. Write a predicate to test if a list is a set.
% b. Write a predicate to remove the first three occurrences of an
% element in a list. If the element occurs less than three times, all
% occurrences will be removed.

%a Mathematical model for set:
% set(l1,...,ln)=
%    0, []
%    1, countOcc(x,l2,...,ln)\=0 where x=l1
%    set(l2,...,ln), otherwise
%
% Mathematical model for countOcc:
% countOcc(x,l1,..,ln)=
%    0, []
%    1+countOcc(x,l2,..,ln), x=l1
%    countOcc(l2,...,ln), otherwise
%
% countOcc(X:element, L:list, C:int)
% flow model(i,i,o)

countOcc(_,[],0).
countOcc(X,[H|T],R):-X=H,
    countOcc(X,T,R1),
    R is R1+1.
countOcc(X,[H|T],R):-X\=H,
    countOcc(X,T,R).

%set(L:list,R:result)
%flow model(i,o)

set([],1).
set([H|T],R):-countOcc(H,T,I),
    I=\=0,
    R is 0.
set([H|T],R):-countOcc(H,T,I),
    I=:=0,
    set(T,R).


%b
%Mathematical model remove_occurances:
%remove_occurances(x,list,k)=
%   [], n=0
%   l1,...,ln,  k=0
%   remove_occurances(x,l2...ln,k-1), l1=x
%   l1 U remove_occurances(x,l2...ln,k),l1\=x
%
%remove_occurances(X:element,L:list,K: integer, R:list)
%flow model(i,i,i,o)
%
remove_occurances(_,[],_,[]):-!.
remove_occurances(_,L,0,L):-!.
remove_occurances(X,[H|T],K,R):-H=:=X,
    K1 is K-1,
    remove_occurances(X,T,K1,R).
remove_occurances(X,[H|T],K,[H|R]):- H\=X,
    remove_occurances(X,T,K,R).

%remove_3_occurances(X:element,L:list,R:list
%flow model(i,i,o)

remove_3_occurances(X,L,R):-remove_occurances(X,L,3,R).





