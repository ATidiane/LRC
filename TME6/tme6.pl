concatene([],L2,L2).
concatene([T1|Q1],L2,Z):- Z = [T1|Q2], concatene(Q1,L2,Q2).


inverse([], []).
inverse([T1],[T1]).
inverse([T1|Q1],Z):- concatene(R,[T1],Z), inverse(Q1,R) .


supprime([],X,[]).
supprime([X],X,[]).
supprime([T1|Q1],T1,Z) :- supprime(Q1,T1,Z).
supprime([T1|Q1],X,Z) :- concatene([T1],R,Z), supprime(Q1,X,R).    


filtre([],[],[]).
filtre([],L2,[]).
filtre(L1,[],L1).
filtre(L1,[T2|Q2],Z) :- supprime(L1,T2,R), filtre(R,Q2,Z).      


palindrome([]).
palindrome([T1]).
palindrome([T1,T1]).
palindrome([T1|Q1]) :- inverse([T1|Q1],[T1|Q2]),palindrome(Q1).     
    
