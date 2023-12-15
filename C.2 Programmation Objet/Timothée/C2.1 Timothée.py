from random import randint

PV1, PV2 = 50, 50
print("-----premier tour-----")
while (PV1 > 0 and PV2 > 0):
    PV1, PV2 = PV1 - randint(1,10), PV2 - randint(1,10)
    print("joueur 1 : " + str(PV1) + "point de vie\njoueur 2 : " + str(PV2) + "point de vie\n")
    if PV1 > 0 and PV2 > 0:
        print("-----Nouveau tour-----")
print("-----fin du match----\n")
if PV1 > PV2 and PV1 > 0:
    print("joueur 1 gagne...")
elif PV1 > PV2 and PV1 > 0:
    print("joueur 2 gagne...")
else:
    print("match nul...")