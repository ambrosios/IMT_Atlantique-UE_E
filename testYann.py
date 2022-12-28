"""
def definir_par_fichier(self, nom):
        # crée un problème de flowshop à partir d'un fichier
        # ouverture du fichier en mode lecture
        fdonnees = open(nom,"r")
        # lecture de la première ligne
        ligne = fdonnees.readline() 
        l = ligne.split() # on récupère les valeurs dans une liste
        self.nombre_jobs = int(l[0])
        self.nombre_machines = int(l[1])
       
        self.liste_jobs = []
        for i in range(self.nombre_jobs):
            ligne = fdonnees.readline() 
            l = ligne.split()
            # on transforme la suite de chaînes de caractères représentant
            # les durées des opérations en une liste d'entiers
            l = [int(i) for i in l]
            j = job.Job(i, l)
            self.liste_jobs.append(j)
        # fermeture du fichier
        fdonnees.close()
"""
print(3)

print('test push 2')

def f(x): #fonction d'evaluation, x est une liste
    res = 0
    plus = True
    for el in x:
        if plus:
            res += el
        else:
            res -= el
        plus = plus * (-1)
    return res

print (f([1,2,5,4,9,8]))

iter_max=30 #nombre d'iterartions max
sc = [1,2,3,4,5,6] #heuristique
sb = sc #meilleure solution
L = [sc] #liste des tabous
critere = True
while not critere:
    voisins_sc = [2,6,1,5,4] #voisins de sc
    sc  = voisins_sc[2] #best voisin de sc
    if f(sc)<=f(sb):
        sb = sc
    L.append(sc)
