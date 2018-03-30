
likes(ann, john). % s-Socrates, f(x) - Wife of x, f(s) - Wife of Socrates
likes(john, jul).
likes(jack, jul).
likes(jul, jack).


ok(X,Y):-
    likes(X,Y),
    likes(Y,X).

lt1(X, Y, Z) :-
    likes(X,Y),
    likes(Y,Z),
    X\=Z.

lt2(X, Y, Z) :-
    likes(X,Y),
    likes(Z,Y),
    X\=Z.

lt(X, Y, Z):-lt1(X, Y, Z).
lt(X, Y, Z):-lt2(X, Y, Z).




p([],[]).
p(L, [N|P]):-
    del(L,N, LL),
    p(LL,P).

% L=[1,2,3,4,5], L=[X|T], X=1, T=[2,3,4,5]

del([X|T],X, T).
del([Y|T],X, [Y | DT]):-
    del(T,X, DT).
