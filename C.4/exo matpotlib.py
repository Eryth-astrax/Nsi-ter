import matplotlib.pyplot as plt
from time import perf_counter
from random import randint


#-------------------------fonction recherche-------------------------


def rchSeq(L,E):
    for i in range(len(L)):
        if E == L[i]:
            return i
    return -1
        
        
        
def rchDic(L,E):
    a = 0
    b = len(L) - 1   
    while (a-b) > 1 :
        m = (a+b)//2       
        if E == L[m]:
            return m
        elif E > L[m]:
            a = m+1
        else:
            b = m -1
    
#-------------------------fonction calcul-------------------------

def tps1RechSeq(L,E):
    t0 = perf_counter()
    rchSeq(L,E)
    t1 = perf_counter()
    duree = t1 - t0
    return duree

def tps1RechDic(L,E):
    t0 = perf_counter()
    rchDic(L,E)
    t1 = perf_counter()
    duree = t1 - t0
    return duree
#-------------------------fonction *100-------------------------  
def tps100RechSeq(ent):
    listePop = []
    if ent == 0:
        return 0
    for i in range(ent):
        listePop.append(i)
    dureeTotale = 0
    for i in range(100):
        x = randint(0 , len(listePop)-1)
        dureeTotale = tps1RechSeq(listePop,x) + dureeTotale
    return dureeTotale
    
def tps100RechDic(ent):
    listePop = []
    if ent == 0:
        return 0
    for i in range(ent):
        listePop.append(i)
    dureeTotale = 0
    for i in range(100):
        x = randint(0 , (ent-1))
        dureeTotale = tps1RechDic(listePop,x) + dureeTotale
    return dureeTotale


#-------------------------programme principale-------------------------


#création de la liste pour les abscisses
liste_x = [x for x in range(0,5000,100)]

#création de la liste pour les ordonnées
liste_y = [tps100RechSeq(x) for x in liste_x]

#
#tracé du graphqiue
#dans 'rx ' 'r' ⇨ rouge, 'x' ⇨ croix, ' ' ⇨ pas de lien
plt.plot(liste_x,liste_y,'rx ')

#génération de la fenêtre du tracé
plt.show()