class Arbre:
    def __init__(self, etiquette):
        self._valeur = etiquette
        self._gauche = None
        self._droit = None

    def get_v(self):
        return self._valeur

    def get_g(self):
        return self._gauche

    def get_d(self):
        return self._droit

    def est_feuille(self):
        return not self._gauche and not self._droit

    def greffe_gauche(self, arbre_greffe):
        self._gauche = arbre_greffe

    def greffe_droit(self, arbre_greffe):
        self._droit = arbre_greffe
 
class ABR:
    def __init__(self) -> None:
        self._valeur = None
        self._gauche = None
        self._droit = None
        
    def ajout(self, val):
        if self._valeur == None:
            self._valeur = val
        elif val < self._valeur :
            if self._gauche == None:
                self._gauche = ABR()
            self._gauche.ajout(val)
        elif val > self._valeur :
            if self._droit == None:
                self._droit = ABR()
            self._droit.ajout(val)
            
    def contient(self, val):
        if self._valeur == None:
            return False
        elif val < self._valeur :
            if self._gauche == None:
                return False
            return self._gauche.contient(val)
        elif val > self._valeur :
            if self._droit == None:
                return False
            return self._droit.contient(val)
        elif val == self._valeur:
            return True
        
    def get_v(self):
        return self._valeur

    def get_g(self):
        return self._gauche

    def get_d(self):
        return self._droit

    def est_feuille(self):
        return not self._gauche and not self._droit

    def greffe_gauche(self, arbre_greffe):
        self._gauche = arbre_greffe

    def greffe_droit(self, arbre_greffe):
        self._droit = arbre_greffe
 
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
            
   
def transfert_tuple(a):
    if a == None:
        return None
    else:
        return(a.get_v(),transfert_tuple(a.get_g()),transfert_tuple(a.get_d()))
    
def parcours_infixe(a):
    l = []
    if a.get_g() != None:
        l += parcours_infixe(a.get_g())
    l.append(a.get_v())
    if a.get_d() != None:
        l += parcours_infixe(a.get_d())
    return l
    


arb = Arbre("I")
o = Arbre("O")
t = Arbre("T")
l = Arbre("L")
r = Arbre("R")
m = Arbre("M")
a = Arbre("A")
g = Arbre("G")
h = Arbre("H")
e = Arbre("E")
l.greffe_gauche(a)
l.greffe_droit(g)
m.greffe_gauche(h)
m.greffe_droit(e)
o.greffe_gauche(l)
o.greffe_droit(r)
t.greffe_droit(m)
arb.greffe_gauche(o)
arb.greffe_droit(t)

arb2 = ABR()
arb2.ajout(2)
arb2.ajout(0)
arb2.ajout(3)
print(transfert_tuple(arb2))
arb2.ajout(1)
print(transfert_tuple(arb2))
print(arb2.contient(4))
print(arb2.contient(1))


print(parcours_infixe(arb))
#print(transfert_tuple(arb))
#draw_arbre(transfert_tuple(arb))