# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Calcul de l'inertie
def calcul_inertie_rectangulaire() -> float: 
    I = (b * (h ** 3)) / 12
    return I

 #Calcul de la déformation maximale
def calcul_delta_max_rectangulaire() -> float:
    delta_max = (F * (L ** 3)) / (3 * (E * 1000) * calcul_inertie_rectangulaire())
    return delta_max

if __name__ == '__main__':
    print (f"le moment d'inertie est de {calcul_inertie_rectangulaire()} mm^4")
    print (f"la deformation maximale de la poutre est de {calcul_delta_max_rectangulaire()} mm")
