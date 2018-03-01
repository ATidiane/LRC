et(0,0,0).
et(1,0,0).
et(0,1,0).
et(1,1,1).
ou(0,0,0).
ou(0,1,1).
ou(1,0,1).
ou(1,1,1).
non(0,1).
non(1,0).
nand(0,0,1).
nand(1,0,1).
nand(0,1,1).
nand(1,1,0).
xor(0,0,0).
xor(0,1,1).
xor(1,0,1).
xor(1,1,0).
<<<<<<< HEAD

/*circuit(0, 0, Z) :- non(xor(non(X, R), nand(X,Y,S)), Z).*/

=======
>>>>>>> b1b544c2f5ceede59a9dedb109b2dc823da949a5
circuit(X, Y, 0) :- non(A, 1), xor(B,C,A), non(X, B), nand(X, Y, C).
circuit(X, Y, 1) :- non(A, 0), xor(B,C,A ), non(X, B), nand(X, Y, C).

