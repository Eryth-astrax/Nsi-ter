class Pile:
    def __init__(self):
        self.__donnees = []
        
    def est_vides(self):
        return len(self.__donnees) == 0
    
    def empile(self,val):
        self.__donnees.append(val)
        
    def depile(self):
        if not self.est_vide():
            return self.donnees.pop()
        else:
            return None
        
        # j'te rappelle que tu mas créé le dossier de toi meme ptdr