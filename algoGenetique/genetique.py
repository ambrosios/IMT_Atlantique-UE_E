from multiprocessing import parent_process
from dataLoader import DataLoader
from population import Population


print("Et c'est parti pour l'algo génétique")

N = 100 # Taille de la population
liste_jobs = (DataLoader("algoGenetique/jeu1.txt")).get_liste_jobs()

c = 0
CMAX = 1000

pop = Population(N, liste_jobs)
pop.generer()
pop.associer()
pop.faire_enfants()
pop.muter(0.1)

#pop.enfants[0].afficher()

pop.afficher()

# while c < CMAX:
#     c += 1
#     pop.associer();
#    pop.faire_enfants();
#    pop.muter(niveau_probabilite);
#    pop.evaluer();
    
# pop.afficher_meilleur()

# 1- Créer la population avec N individus OK
# 2- Faire des couples de parents - N indivs presque OK
# 3- Faire les enfants - 2N indiv NOK
# 4- Mutations - probabilite à x% de mutation
# 5- Évaluation en vue de la sélection de N individus - N indivs
# 6- On recommence