#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:59:27 2017

@author: 3502069
"""

from definitions import compositionSet,transposeSet

class Graphe():


    def __init__(self): 
        self.noeuds = set()
        self.relations = dict()
        
        
        
        
    def getRelations(self,i,j):
        if (i,j) in self.relations.keys():
            return self.relations[(i,j)]
        if (j,i) in self.relations.keys():
            return set(transposeSet(self.relations[(j,i)]))
        return {'o','ot','e','et','d','dt','st','s','=','<','>','m','mt'}
    
    def propagation(self,i,j):
        re = list(set(self.getRelations(i,j)))
        P = [re]
        while len(P) != 0 :
            Rij = set(P.pop())
            node = self.noeuds.copy()
            node.remove(i)
            node.remove(j)
            for k in node:
                Rik = self.getRelations(i,k)
                Rjk = self.getRelations(j,k)
                contrainte = compositionSet(Rij,Rjk)
                nvRik = { l for l in contrainte if l in Rik } 
                Rki = self.getRelations(k,i)
                Rkj = self.getRelations(k,j)
                contrainte = compositionSet(Rki,Rij)
                nvRkj = { l for l in contrainte if l in Rkj }

                if len(nvRik) == 0 or len(nvRkj) == 0 :
                    return False
                
                if nvRik != Rik:
                    self.ajouter(i,k,nvRik)
                    P.insert(0,Rik)
                    
                if nvRkj != Rkj:
                    self.ajouter(k,j,nvRkj)
                    P.insert(0,Rkj)
                    
        return True
    
    
    
    def ajouter(self,i,j, relation):
        if i not in self.noeuds :
            self.noeuds.add(i)
        if j not in self.noeuds :
            self.noeuds.add(j)
        self.relations[(i,j)] = relation
        self.propagation(i,j)
            

#G = Graphe()
#G.ajouter('A','B',{'<'})
#G.ajouter('A','C',{'<'})      
#G.ajouter('B','C',{'='})  
#print(G.propagation('B','C'))


#Question 5
G = Graphe()
G.ajouter('L','S',{'ot','mt'})
G.ajouter('S','R',{'<','m','mt','>'})
G.ajouter('S','R',{'d','o','e','s'})
print(G.relations)
