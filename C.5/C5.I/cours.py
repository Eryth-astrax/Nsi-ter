def taille(arbre):
    x = 0
    if arbre == None:
        return x
    else:
        x+=1
        x += taille(arbre[1])
        x += taille(arbre[2])
        return x
    
def hauteur(arbre):
    x = 0
arbre1 = (2,(5,None,None),(8,None,(3,None,None)))
print(taille(arbre1))