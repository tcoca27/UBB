%a. Given a linear numerical list write a predicate to remove all sequences of
% consecutive values.
% Eg.: remove([1, 2, 4, 6, 7, 8, 10], L) will produce L=[4, 10].
%b. For a heterogeneous list, formed from integer numbers and list of numbers;
% write a predicate to delete from every sublist all sequences of
% consecutive values. Eg.: [1, [2, 3, 5], 9, [1, 2, 4, 3, 4, 5, 7, 9],
% 11, [5, 8, 2], 7] => [1, [5], 9, [4, 7, 9], 11, [5, 8, 2], 7]

%a.
%Mathematical model for removeConsecutive
%removeConsecutive(l1..ln,s)=
%   [], n=0
%   removeConsecutive(l2..ln,1), (l1+1)=l2
%   removeConsecutive(l2..ln,0), (l1+1)!=l2, s=1
%   l1 U removeConsecutive(l2..ln,0), (l1+1)!=l2, s=0
%
%removeConsecutive(L: list, S:integer, R: list)
%flow_model(i,i,o)

removeConsecutive([],_,[]).
removeConsecutive([_],1,[]).
removeConsecutive([A],0,[A]).
removeConsecutive([A,B|T],_,R):-A+1=:=B,
    removeConsecutive([B|T],1,R).
removeConsecutive([A,B|T],S,R):-A+1=\=B,
    S=:=1,
    removeConsecutive([B|T],0,R).
removeConsecutive([A,B|T],S,R):-A+1=\=B,
    S=:=0,
    removeConsecutive([B|T],0,R1),
    R=[A|R1].

%removeConsecutiveW(L:list,R:list)
%flow_model(i,o)

removeConsecutiveW(L,R):-removeConsecutive(L,0,R).

%b
%Mathematical model for removeCLists
%removeCLists(l1..ln)=
%    [], n=0
%    l1 U removeCLists(l2..ln), l1 is not list
%    removeConsecutiveW(l1) U removeCLists(l2..ln), otherwise

%removeCLists(L:list,R:list)
%flow_model(i,o)

removeCLists([],[]).
removeCLists([H|T],R):-is_list(H),
    removeCLists(T,R1),
    removeConsecutiveW(H,R2),
    R=[R2|R1].
removeCLists([H|T],R):-removeCLists(T,R1),
    R=[H|R1].
