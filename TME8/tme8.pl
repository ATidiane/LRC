concatene([],L2,L2).
concatene([T1|Q1],L2,Z):- Z = [T1|Q2], concatene(Q1,L2,Q2).

cacheLettre([],T,[]).
cacheLettre([T|L],T,[_|R]) :- cacheLettre(L,T,R).
cacheLettre([X|L],T,[X|R]) :- X\=T,cacheLettre(L,T,R).

appartient(X, [T|L]) :- X = T.
appartient(X,[T|L]) :- appartient(X,L).
appartient(X,L):- memberchk(X,L).

cacheLettreGroupe([], [], []).
cacheLettreGroupe([], L, []).
cacheLettreGroupe(L, [], L).   
cacheLettreGroupe(X, [T|L], MT) :- appartient(T, X), cacheLettre(X, T, R), cacheLettreGroupe(R, L, MT).


enlevPref([T|L], G, L) :- appartient(T, G).
enlevPref([T|L], G, R):- enlevPref(L, G, R).
%enlevPref([T|L], G, [_,R]) :- appartient(T, G), enlevPref(L, G, R).
cacheGroupeLettreVar(X,L, cacheVar(R, MT)) :- cacheLettreGroupe(X, L, R).

