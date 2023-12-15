class Pile:
    def __init__(self):
        self.__donnees = []
        
    def est_vides(self):
        return len(self.__donnees) == 0
    
    def to_str(self) -> str:
        '''
        Méthode qui renvoie une chaine de caractère correspondant au contenu de la Pile.
        '''
        chaine = ""
        for val in self.__donnees:
            chaine = chaine + ";" + str(val)
        return chaine
    
    def empile(self,val):
        self.__donnees.append(val)
        
    def depile(self):
        if not self.est_vides():
            return self.__donnees.pop()
        else:
            return None
        

class files:
    def __init__(self) -> None:
        self.__donnees = []
    
    def est_vide(self):
        return len(self.__donnees) == 0
        
    def enfile(self,val):
        self.__donnees.append(val)
        
    def defile(self):
        
        if not self.est_vide():
            return self.__donnees.pop(0)
        
        else:
            return None
        
class files_inv:
    def __init__(self) -> None:
        self.__donnees = []
    
    def est_vide(self):
        return len(self.__donnees) == 0
        
    def enfile(self,val):
        self.__donnees.append(val)
        
    def defile(self):
        
        if not self.est_vide():
            return self.__donnees.pop()
        
        else:
            return None
        
class files_pile:
    def __init__(self) -> None:
        self.__donnees = Pile()
    
    def est_vide(self):
        return self.__donnees.est_vides()
        
    def enfile(self,val):
        self.__donnees.empile(val)
        
    def to_str(self) -> str:
        
        return self.__donnees.to_str()
    
    def defile(self):
        if  not self.est_vide():
            Pile_temp = Pile()
            while not self.est_vide():
                Pile_temp.empile(self.__donnees.depile())
            val = Pile_temp.depile()
            while not Pile_temp.est_vides():
                self.__donnees.empile(Pile_temp.depile())
            return val
        
        else:
            return None
        
def nbre_1_n(n:int):
    file_temp = files_pile()
    for i in range(n):
        file_temp.enfile(i+1)
    return file_temp

"""
f1 = nbre_1_n(6)
print(f1.to_str())
while not f1.est_vide():
    print(f1.defile())
"""