# -*- coding: utf-8 -*-
"""

Dictionnaires décrivants les transposés et symétries de relations, 
ainsi que les listes de relations obtenues avec les compositions de base
dans le tableau donné en TD

"""

transpose = {
    '<':'>',
    '>':'<',
    'e':'et',
    's':'st',
    'et':'e',
    'st':'s',
    'd':'dt',
    'm':'mt',
    'dt':'d',
    'mt':'m',
    'o':'ot',
    'ot':'o',
    '=':'='                 
    }
 
symetrie = {
    '<':'>',
    '>':'<',
    'e':'s',
    's':'e',
    'et':'st',
    'st':'et',
    'd':'d',
    'm':'mt',
    'dt':'dt',
    'mt':'m',
    'o':'ot',
    'ot':'o',
    '=':'='
    }            
             
compositionBase = {
        
        ('<','<'):{'<'},
        ('<','m'):{'<'},
        ('<','o'):{'<'},
        ('<','et'):{'<'},
        ('<','s'):{'<'},
        ('<','d'):{'<','m','o','s','d'},
        ('<','dt'):{'<'},
        ('<','e'):{'<','m','o','s','d'},
        ('<','st'):{'<'},
        ('<','ot'):{'<','m','o','s','d'},
        ('<','mt'):{'<','m','o','s','d'},
        ('<','>'):{'<','>','m','mt','o','ot','e','et','s','st','d','dt','='},
        ('m','m'):{'<'},
        ('m','o'):{'<'},
        ('m','et'):{'<'},
        ('m','s'):{'m'},
        ('m','d'):{'o','s','d'},
        ('m','dt'):{'<'},
        ('m','e'):{'o','s','d'},
        ('m','st'):{'m'},
        ('m','ot'):{'o','s','d'},
        ('m','mt'):{'e','et','='},
        ('o','o'):{'<','m','o'},
        ('o','et'):{'<','m','o'},
        ('o','s'):{'o'},
        ('o','d'):{'o','s','d'},
        ('o','dt'):{'<','m','o','et','dt'},
        ('o','e'):{'o','s','d'},
        ('o','st'):{'o','et','dt'},
        ('o','ot'):{'o','ot','e','et','d','dt','st','s','='},
        ('s','et'):{'<','m','o'},
        ('s','s'):{'s'},
        ('s','d'):{'d'},
        ('s','dt'):{'<','m','o','et','dt'},
        ('s','e'):{'d'},
        ('s','st'):{'s','st','='},
        ('et','s'):{'o'},
        ('et','d'):{'o','s','d'},
        ('et','dt'):{'dt'},
        ('et','e'):{'e','et','='},
        ('d','d'):{'d'},
        ('d','dt'):{'<','>','m','mt','o','ot','e','et','s','st','d','dt','='},
        ('dt','d'):{'o','ot','e','et','d','dt','st','s','='}
                           
                   }




def transposeSet(S) :
    L = set()
    for s in S:
        L.add(transpose[s])
    return L

def symetrieSet(S) :
    L = set()
    for s in S:
        L.add(symetrie[s])
    return L


def compose(r1,r2) :
    
    if r1 == '=':
        return {r2}
    if r2 == '=':
        return {r1}

    if (r1,r2) in compositionBase.keys() :
        return compositionBase[(r1,r2)]
    
    tr2 = transpose[r2]    
    tr1  = transpose[r1]
    if (tr2,tr1) in compositionBase.keys():
        return transposeSet(compositionBase[(tr2,tr1)])
    
    sr2 = symetrie[r2]
    sr1 = symetrie[r1]
    if (sr1,sr2) in compositionBase.keys():
        return symetrieSet(compositionBase[(sr1,sr2)])
    
    str1 = transpose[sr1]
    str2 = transpose[sr2]    
    
    if (str2,str1) in compositionBase.keys() :
        return symetrieSet(transposeSet(compositionBase[(str2,str1)]))
    
    return {}
    

def compositionSet(S1, S2) :
    
    if len(S1) == 0:
        return S2
    if len(S2) == 0:
        return S1
    L=set()  
    for s1 in S1 :
        for s2 in S2 :
            L = L.union(compose(s1,s2).copy())
    return L

##print(compositionBase[('m','d')])
#print(compose('=','d'))
#
#print(compositionSet(['='],['d','e']))