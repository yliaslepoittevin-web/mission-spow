# mission.py - Programme de vol de l'equipage
# Lancer le programme : python mission.py

NOM_VAISSEAU = "CESI-1"

DESTINATION = "Mars"

CARBURANT = 100  # en litres

cargaison = [
    "eau",
    "pommes de terre",
    "ruban adhesif",
]


def compte_a_rebours(depart):
    for i in range(depart, 0, -1):
        print(i, "...")
    print("Decollage !")


def afficher_mission():
    print("=== Mission", NOM_VAISSEAU, "vers", DESTINATION, "===")
    print("Cargaison :", ", ".join(cargaison))
    print("Carburant :", CARBURANT, "L")


afficher_mission()
compte_a_rebours(3)
