import math
# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm
def calcul_inertie_rectangulaire() -> float: 
    I_rectangulaire = (b * (h ** 3)) / 12
    return I_rectangulaire

def calcul_delta_max_rectangulaire() -> float:
    delta_max_rectangulaire = (F * (L ** 3)) / (3 * (E * 1000) * calcul_inertie_rectangulaire())
    return delta_max_rectangulaire
# poutre carrée
a = 15  # en mm
def calcul_inertie_carree() -> float:
    I_carree = (a ** 4) /12
    return I_carree
def calcul_delta_max_carree() -> float:
    delta_max_carree = (F * (L ** 3)) / (3 * (E * 1000) * calcul_inertie_carree())
    return delta_max_carree

# poutre ronde
d = 5  # en mm
def calcul_inertie_ronde() -> float:
    I_ronde = (math.pi * (d ** 4)) / 64
    return I_ronde
def calcul_delta_max_ronde() -> float:
    delta_max_ronde = (F * (L ** 3)) / (3 * (E * 1000) * calcul_inertie_ronde())
    return delta_max_ronde

# poutre creuse
D = 15  # en mm
d = 5  # en mm
def calcul_inertie_creuse() -> float:
    I_creuse = (math.pi * ((D ** 4) - (d ** 4))) / 64
    return I_creuse
def calcul_delta_max_creuse() -> float:
    delta_max_creuse = (F * (L ** 3)) / (3 * (E * 1000) * calcul_inertie_creuse())
    return delta_max_creuse

# Calcul de la section optimale
if __name__ == '__main__':
    list_delta_max = [calcul_delta_max_rectangulaire(), calcul_delta_max_creuse(), calcul_delta_max_ronde(), calcul_delta_max_carree()]
    delta_max_minimum = min(list_delta_max)
    if delta_max_minimum == calcul_delta_max_rectangulaire():
        print (f"Le type de section minimisant la déformation maximale est la section rectangulaire, avec une déformation de {delta_max_minimum} mm")
    if delta_max_minimum == calcul_inertie_carree():
        print (f"Le type de section minimisant la déformation maximale est la section carree, avec une déformation de {delta_max_minimum} mm")
    if delta_max_minimum == calcul_delta_max_ronde():
        print (f"Le type de section minimisant la déformation maximale est la section ronde, avec une déformation de {delta_max_minimum} mm")
    if delta_max_minimum == calcul_delta_max_creuse():
        print (f"Le type de section minimisant la déformation maximale est la section creuse, avec une déformation de {delta_max_minimum} mm")

