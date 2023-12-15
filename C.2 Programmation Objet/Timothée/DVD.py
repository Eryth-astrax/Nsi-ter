class Voiture:
    def __init__(self, places):
        self.__places = places
        self.__vitesse = 0
        self.__passagers = 0

    def accelere(self):
        self.__vitesse = self.__vitesse + 10/(self.__passagers+1)

    def ralenti(self):
        self.__vitesse = self.__vitesse - 10/(self.__passagers+1)
        if self.__vitesse <= 0 :
            self.__vitesse = 0

    def ajout_passager(self):
        assert self.__passagers <= self.__places - 2, "Trop de passagers dans la voiture"
        self.__passagers = self.__passagers + 1

    def get_passager(self):
        return self.__passagers

    def get_vitesse(self):
        return self.__vitesse
    
    def get_places(self):
        return self.__places
    
ma_voiture = Voiture(5)
for i in range(3):
    ma_voiture.ajout_passager()
print(ma_voiture.get_passager())
for i in range(2):
    ma_voiture.accelere()
print(ma_voiture.get_vitesse())
for i in range(2):
    ma_voiture.ralenti()
print(ma_voiture.get_vitesse())

