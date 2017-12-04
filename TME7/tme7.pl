subs(chat,felin).
subs(lion,felin).
subs(chien, canide).
subs(canide,chien).    
subs(souris, mammifere).
subs(canide, mammifere).
subs(felin, mammifere).
subs(mammifere, animal).
subs(canari, animal).
susb(animal, etreVivant).
subs(and(plante, animal), nothing).
subs(pet,and(animal,some(aMaitre))).
equiv(pet,and(animal,some(aMaitre))).    
and(animal,some(aMaitre)).
equiv(chihuahua, and(pet, chien)).    
equiv(carnivoreExc, all(mange, animal)).
equiv(herbivoreExc, all(mange, plante)).
subs(lion, carnivoreExc).
equiv(carnivoreExc, predateur).
subs(animal,some(mange)).     
and(all(mange, nothing), some(mange)).
subsS1(C, C).
subsS1(C, D) :- subs(C, D), C\==D.    
subsS1(C, D) :- subs(C, E), subsS1(E, D).
    

    
