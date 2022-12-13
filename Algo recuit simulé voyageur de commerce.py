from random import *
from math import *

M=[[0,6,6,1,4],[6,0,8,3,5],[6,8,0,6,4],[1,3,6,0,2],[4,5,4,2,0]]
villes = [0,1,2,3,4]
T = 1
iters_max = 20 #nombre maximal d'itérations
#temps_max = 30 #temps maximal

Sc = 1
S_etoile = 2
s=3
alpha = 0,99

def f(a) :
    return(a)

def V(a) :
    L = villes
    del L[a]
    return(random.sample(L, 1))
    

p = random()
K = 10 #constante, par ex peut être celle de Boltzmann

iter = 0

while iter < iters_max :
    iter =+1
    s = V(Sc) #fonction voision pris aléatoirement
    if f(s)<=f(Sc) :
        s = S_etoile
    else :
        if p <= exp((f(Sc)-f(s))/K*T) :
            s = Sc
        if f(Sc)<f(S_etoile) :
            Sc = S_etoile
        T = T * alpha

print(S_etoile)