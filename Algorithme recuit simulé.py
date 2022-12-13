from random import *
from math import *

T = 1
iters_max = 20 #nombre maximal d'itérations
temps_max = 30 #temps maximal
Sc = 1
S_etoile = 2
s=3
alpha = 0,99

def f(a) :
    return(a)

def V(a) :
    return(a)

p = random()
K = 10 #constante, par ex peut être celle de Boltzmann

print(p)

while True :
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