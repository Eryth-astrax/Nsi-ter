import file

def parcours_largeur(a):
    l = []
    F = file.files()
    F.enfile(a)
    while not F.est_vide():
        arbre_temp = F.defile()
        if arbre_temp != None:
            l.append(arbre_temp[0])
            F.enfile(arbre_temp[1])
            F.enfile(arbre_temp[2])
    return l

def parcours_infixe(a):
    l = []
    F = file.files()
    F.enfile(a)
    while not F.est_vide():
        arbre_temp = F.defile()
        if arbre_temp != None:
            F.enfile(arbre_temp[1])
            l.append(arbre_temp[0])
            F.enfile(arbre_temp[2])
    return l

def parcours_suffixe(a):
    l = []
    F = file.files()
    F.enfile(a)
    while not F.est_vide():
        arbre_temp = F.defile()
        if arbre_temp != None:
            F.enfile(arbre_temp[1])
            F.enfile(arbre_temp[2])
            l.append(arbre_temp[0])
    return l

def recherche_ABR(a, research):
    x = False
    if a[0] == research:
        return True
    if a[1] != None:
        x_temp = recherche_ABR(a[1], research)
        if x_temp != False:
            x = x_temp
    if a[2] != None:
        x_temp = recherche_ABR(a[2], research)
        if x_temp != False:
            x = x_temp
    return x

def draw_arbre(abr,t=0):
    print('    '*t+'|_'+str(abr[0]))
    if abr[1] == None:
        print('    '*(t+1)+'|_'+str(abr[1]))
    else:
        draw_arbre(abr[1],t+1)
    if abr[2] == None:
        print('    '*(t+1)+'|_'+str(abr[2]))
    else:
        draw_arbre(abr[2],t+1)
    
    
arb = ()