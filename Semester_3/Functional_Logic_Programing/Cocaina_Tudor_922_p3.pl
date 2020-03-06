%Write a program to generate the list of all subsets of sum S with the
% elements of a list (S - given). Eg: [1,2,3,4,5,6,10] si S=10 =>
% [[1,2,3,4], [1,4,5], [2,3,5], [4,6], [10]] (not necessary in this
% order), [1,2,3,4,5,6,9] S=9 =>
% [[1,3,5],[1,2,6],[3,6],[2,3,4],[4,5],[9]].
%

%sumList(l1...ln,s)=
%                    s, n=0
%                    suma(l2..ln,s+l1), otherwise
%sumList(L:list,E:int,R:int)
%sumList(i,i,o)

sumList([],E,E).
sumList([H|T],E,R):-
    E1 is H+E,
    sumList(T,E1,R).

%subsets(l1..ln)=
%                  [], n=0
%                  l1+subsets(l2..ln), n>0
%                  subsets(l2..ln), n>0
%subsets(L:list,R:List)
%subsets(i,o)

subsets([],[]).
subsets([H|T],[H|R]):-
    subsets(T,R).
subsets([_|T],R):-
    subsets(T,R).

%solution(L:list,N:int,R:list)
%solution(i,i,o)

solution(L,S,R):-
    subsets(L,R),
    sumList(R,0,S).

%main(L:list, S:int, R:int)
%main(i,i,o)
%
main(L,S,R):-
    findall(R1,solution(L,S,R1),R).














