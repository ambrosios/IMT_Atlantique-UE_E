import numpy
from DataLoader import DataLoader
from Population import Population
from Evaluateur import Evaluateur
from Execution import Execution
import config

if config.AFFICHER_NOM_ALGORITHME:
    print()
    print("*****************************************")
    print("* Bienvenue dans l'algorithme génétique *")
    print("*****************************************")
    print()

data = DataLoader(config.FICHIER_DONNEES)
LISTE_JOBS = data.get_liste_jobs()
N_MACHINES = data.get_nombre_machines()

best_evaluation = numpy.inf
best_indiv = None
temps_total = 0

for e in range(config.NOMBRE_EXECUTIONS):

    if config.AFFICHER_TEMPS_EXECUTION:
        print("Début de l'exécution " + str(e+1) + " à " + str(round(temps_total, 2)) + "s")

    run = Execution(LISTE_JOBS, N_MACHINES)
    run.executer(config.N, config.NOMBRE_ITERATIONS)
    solution = run.get_solution()
    print("  Meilleure séquence ("+str(e+1)+") :", solution[0].str(), "avec une évaluation à", solution[1])

    if config.AFFICHER_TEMPS_EXECUTION:
        print("Fin de l'exécution " + str(e+1) + " à", str(round(temps_total + run.get_temps(), 2)) + "s")
        print("----")
        print()
    
    temps_total += run.get_temps()

    if best_evaluation > solution[1]:
        best_evaluation = solution[1]
        best_indiv = solution[0]

if config.AFFICHER_TEMPS_EXECUTION:
    print()
    print("Fin de toutes les exécutions", str(round(temps_total, 2)) + "s")
    print()
    
print("Meilleur séquence résultat : " + best_indiv.str() + " avec une évaluation à " + str(best_evaluation))