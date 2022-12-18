import heapq
from multiprocessing import parent_process
import time
from DataLoader import DataLoader
from Population import Population
from Evaluateur import Evaluateur
import config

print()
print("*****************************************")
print("* Bienvenue dans l'algorithme génétique *")
print("*****************************************")
print()

t_debut = time.perf_counter() 
if config.AFFICHER_TEMPS_EXECUTION:
    print("Début de l'exécution à 0s")

data = DataLoader(config.FICHIER_DONNEES)
LISTE_JOBS = data.get_liste_jobs()
N_MACHINES = data.get_nombre_machines()

CMAX = config.CMAX

pop = Population(config.N, LISTE_JOBS)
pop.generer()

for c in range(CMAX):
    if config.AFFICHER_POPULATION:
        pop.afficher()
    pop.associer()
    pop.faire_enfants() # OK pour double coupe - Ajouter des types de croisements de gênes
    if config.AFFICHER_POPULATION_APRES_NAISSANCE:
        pop.afficher()
    pop.muter(config.PROBABILITE_MUTATION_SEUIL_DEPART, config.PROBABILITE_MUTATION_DYNAMIQUE)
    pop.evaluer(N_MACHINES)
    pop.selectionner(config.SEUIL_SELECTION_MEILLEURS)
    
    if config.AFFICHER_MEILLEUR_A_CHAQUE_ITERATION:
        h = [];
        heapq.heapify(h)
        for i in pop.individus:
            heapq.heappush(h, (Evaluateur(i, N_MACHINES)))

        res = heapq.heappop(h)
        print("[" + str(c + 1) + "] Meilleure séquence : ", [j.numero for j in res.get_individu().sequence], "avec une évaluation à ", res.evaluer())
    
    
print()
print("Conclusion :")
h = [];
heapq.heapify(h)
for i in pop.individus:
    heapq.heappush(h, (Evaluateur(i, N_MACHINES)))

res = heapq.heappop(h)
print("Meilleure séquence :", [j.numero for j in res.get_individu().sequence], "avec une évaluation à ", res.evaluer())

if config.AFFICHER_TEMPS_EXECUTION:
    print()
    print("Fin de l'exécution à", str(round(time.perf_counter() - t_debut, 2)) + "s")
    print()