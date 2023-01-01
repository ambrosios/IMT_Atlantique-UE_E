import numpy as np

def evaluer(el):
    return np.x = random.randint(100)

def best(liste,tabou_liste):
    liste_couples=[] #liste des couples (element, valeur)
    for element in liste:
        couple=(element, evaluer(element))
        print(couple)
        liste_couples.append(couple)
    triee = sorted(liste_couples, key=lambda couple: couple[1])

    return triee

""" l=['tt','ijhkbh','uhbu']
print(best(l,[])) """