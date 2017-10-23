pere(biro, ahmed).
mere(aissatou, ahmed).
pere(biro, mariama).
mere(aissatou, mariama).
parent(X, ahmed) :- pere(X,ahmed).
parent(X, ahmed) :- mere(X, ahmed).
parent(biro, aissatou, ahmed).
grandpere(saikou, ahmed).
frereOuSoeur(mariama, ahmed).
grandpere(ousmane, biro).
ancetre(X, Y) :- grandpere(X, Y).

    
    
