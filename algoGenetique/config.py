import random
import numpy as np

DATA = [
    # ["algoGenetique/data/jeu1.txt", 50, 50, 3, "algoGenetique/resultats/jeu1.png", "algoGenetique/resultats/jeu1.txt"],
    # ["algoGenetique/data/jeu2.txt", 50, 70, 6, "algoGenetique/resultats/jeu2.png", "algoGenetique/resultats/jeu2.txt"],
    # ["algoGenetique/data/tai01.txt", 100, 220, 30, "algoGenetique/resultats/tai01.png", "algoGenetique/resultats/tai01.txt"],
    # ["algoGenetique/data/tai11.txt", 100, 300, 30, "algoGenetique/resultats/tai11.png", "algoGenetique/resultats/tai11.txt"],
    ["algoGenetique/data/tai21.txt", 200, 300, 20, "algoGenetique/resultats/tai21.png", "algoGenetique/resultats/tai21.txt"],
    ["algoGenetique/data/tai31.txt", 200, 400, 20, "algoGenetique/resultats/tai31.png", "algoGenetique/resultats/tai31.txt"],
    ["algoGenetique/data/tai41.txt", 200, 500, 15, "algoGenetique/resultats/tai41.png", "algoGenetique/resultats/tai41.txt"],
    ["algoGenetique/data/tai51.txt", 200, 500, 15, "algoGenetique/resultats/tai51.png", "algoGenetique/resultats/tai51.txt"]
    ]

FICHIERS_DONNEES = [data[0] for data in DATA] # Jeu de données avec nombre de jobs, nombre de machines, durées de chaque opération


N = [data[1] for data in DATA] # Taille de la population
AFFICHER_AJUSTEMENT_TAILLE_POPULATION = True # Indique si la taille de la population a été ajustée à N+1 (dans le cas où N impair)

NOMBRE_ITERATIONS = [data[2] for data in DATA] # Nombre d'itérations par exécution de l'algorithme génétique

NOMBRE_EXECUTIONS = [data[3] for data in DATA]

SAUVEGARDE_RESULTATS = True
RESULTATS_GRAPHIQUE = [data[4] for data in DATA]
RESULTATS_TXT = [data[5] for data in DATA]

PROBABILITE_MUTATION_FONCTION = random.uniform # Fonction aléatoire pour déterminer si un individu aura une mutation (ex : np.random.normal)
PROBABILITE_MUTATION_SEUIL_DEPART = 0.2 # Probabilité pour un enfant de subir une mutation
PROBABILITE_MUTATION_DYNAMIQUE = True # Augmente la probabilité d'avoir des mutations lorsqu'il y a un optimum local trouvé
MUTATION_DYNAMIQUE_SEUIL = 0.4 # Si un individu a un taux de présencé dans la population supérieur à ce seuil, alors la mutation dynamique a lieu

SEUIL_SELECTION_MEILLEURS = 1 # Taux de meilleurs individus conservés

AFFICHER_NOM_ALGORITHME = True # Affiche le nom de l'algorithme au lancement du script
AFFICHER_POPULATION = False # Affiche la population à chaque itération
AFFICHER_NOMBRE_DOUBLONS = False # Affiche la population à chaque itération
AFFICHER_NOUVEAUX_INDIVIDUS = False # Affiche les individus créés
AFFICHER_POPULATION_APRES_NAISSANCE = False # Affiche la population à chaque itération
AFFICHER_CORRECTIONS = False # Affiche la correction avec avant/après
AFFICHER_MUTATIONS = False # Affiche les mutations réalisées
AFFICHER_QUAND_MUTATION_DYNAMIQUE = False # Affiche lorsque la mutation dynamique est active
AFFICHER_EVALUATIONS = False # Affiche la valeur de l'évaluation de tous les individus de la population
AFFICHER_SELECTIONNES = False # Affiche les individus sélectionné et leur évaluation
AFFICHER_MEILLEUR_A_CHAQUE_ITERATION = False # Affiche la progression du meilleur individu de la population
AFFICHER_GRAPHIQUE = False # Affiche l'évolution de la recherche de solution optimale
AFFICHER_TEMPS_EXECUTION = True # Affiche le temps nécessaire pour finir l'évaluation