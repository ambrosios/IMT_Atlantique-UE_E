import random
from math import *

M=[[0,6,6,1,4],[6,0,8,3,5],[6,8,0,6,4],[1,3,6,0,2],[4,5,4,2,0]]
villes = [0,1,2,3,4]
T = 1
iters_max = 300 #nombre maximal d'itérations
#temps_max = 30 #temps maximal



#point_depart = 0
chemin = [0,1,2,3,4]
chemin_h = [0,1,2,3,4]
chemin_etoile = [0,1,2,3,4]
alpha = 0,99

#temps du chemin, où chemin est une liste de taille 5 de l'ordre des villes
def temps_chemin(chemin) :
    temps = M[chemin[0]][chemin[1]]+M[chemin[1]][chemin[2]]+M[chemin[2]][chemin[3]]+M[chemin[3]][chemin[4]]
    return(temps)

def permutation(chemin,elt):
    idx1=chemin.index(elt)
    pos=[0,1,2,3,4]
    pos.remove(elt)
    val2=random.sample(pos,1)
    idx2=chemin.index(val2[0])
    chemin_permuté = chemin
    chemin_permuté[idx1],chemin_permuté[idx2] = chemin_permuté[idx2],chemin_permuté[idx1]
    return(chemin_permuté)

def V(a) :
    L = [0,1,2,3,4]
    del L[a]
    return(random.sample(L, 1)[0])
    

K = 1000 #constante, par ex peut être celle de Boltzmann

iter = 0
liste_temps=[]

while iter < iters_max :
    iter +=  1
    ville_voisine = V(0) #fonction voision pris aléatoirement
    chemin = permutation(chemin,ville_voisine)
    print(chemin)
    if temps_chemin(chemin)<=temps_chemin(chemin_etoile) :
        chemin_etoile = chemin
        liste_temps.append(temps_chemin(chemin_etoile))
    else :
        p = random()
        if p <= exp((temps_chemin(chemin_h)-temps_chemin(chemin))/(K*T)) :
            chemin_h = chemin
        if temps_chemin(chemin_h)<temps_chemin(chemin_etoile) :
            chemin_etoile = chemin_h
            liste_temps.append(temps_chemin(chemin_etoile))
        T = T * alpha

print(chemin_etoile)
print(temps_chemin(chemin_etoile))
print(min(liste_temps))