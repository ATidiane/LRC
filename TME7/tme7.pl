%TME7 

subs(chat,felin).
subs(lion,felin).

subs(chien,canide).
subs(canide,chien).

subs(souris,mammifere).
subs(felin,mammifere).
subs(canide,mammifere).

subs(mammifere,animal).
subs(canari,animal).

subs(animal,etreVivant).

subs(and(animal,plante),nothing).
subs(and(animal, some(aMaitre)),pet).
subs(pet, some(aMaitre)).
subs(some(aMaitre), all(aMaitre,humain)).
subs(chihuahua,and(chien,pet)).

subs(carnivore,all(mange,animal)).
subs(all(mange,animal),carnivore).
subs(herbivore,all(mange,plante)).
subs(all(mange,plante),herbivore).

subs(lion,carnivore).
subs(carnivore,predateur).
subs(animal,some(mange)).
subs(and(all(manger,nothing),some(mange)),nothing)

inst(felix, chat).
inst(pierre, humain).
inst(marie, humain).
inst(princesse, chihuahua).
inst(jerry, souris).
inst(titi, canari).

instR(felix, mange, jerry).
instR(felix, mange, titi).
instR(felix, aMaitre, pierre).
instR(princesse, aMaitre, marie).

    not_member(_,[]).
    not_member(E,[T|Q]):-E\==T,not_member(E,Q).

		subS1(C,C). 
		subS1(C,D):-subs(C,D).
		subS1(C,D):-subs(C,Z),Z\==D,subS1(Z,D).

		subsS(C,D):-subsS(C,D,[]).

		subsS(C,C,_). 
		subsS(C,D,_):-subs(C,D). 

    	subsS(C,D,L):-subs(C,Z),Z\==D,not_member(Z,L),subsS(Z,D,[Z|L]).

	    subsS(A,and(E,D),L):-subs(A,and(_,Z)),subs(A,and(X,_)),subsS(E,X,L),subsS(D,Z,L).
    	subsS(A,and(E,D),L):-subs(A,and(Z,_)),subs(A,and(_,X)),subsS(E,X,L),subsS(D,Z,L).

        subsS(A,D,L):-subs(A,and(Z,_)),subsS(Z,D,L).
        subsS(A,D,L):-subs(A,and(_,Z)),subsS(Z,D,L).

		subsS(and(A,B),C,L):-subs(A,X),subs(B,Y),subsS(and(X,Y),C).

		subsS(A,all(X,D),L):-subs(A,all(X,Z)),subsS(D,Z,L).

subsS(lion, X) - felin, mammifere, animal, etreVivant, carnivore,predateur
subsS(X,predateur)- predateur, carnivore, lion 
