import config
import time
import heapq
import matplotlib.pyplot as plt
from classes.Population import Population
from classes.Evaluateur import Evaluateur

class Execution():
    
    def __init__(self, liste_jobs: int, nombre_machines: int):
        self.liste_jobs = liste_jobs
        self.nombre_machines = nombre_machines
        self.meilleurs = []
        
    # executer permet d'exécuter l'algorithme génétique pour une taille de population donnée et un nombre d'itérations choisi
    def executer(self, taille_population: int, nombre_iteration: int):
        t_debut = time.perf_counter() 

        self.pop = Population(taille_population, self.liste_jobs)
        self.pop.generer()

        for c in range(nombre_iteration):
            if config.AFFICHER_POPULATION:
                self.pop.afficher()
            self.pop.associer()
            self.pop.faire_enfants() # OK pour double coupe - Ajouter des types de croisements de gênes
            if config.AFFICHER_POPULATION_APRES_NAISSANCE:
                self.pop.afficher()
            self.pop.muter(config.PROBABILITE_MUTATION_SEUIL_DEPART, config.PROBABILITE_MUTATION_DYNAMIQUE, c)
            self.pop.evaluer(self.nombre_machines)
            self.pop.selectionner(config.SEUIL_SELECTION_MEILLEURS)
            
            if config.AFFICHER_MEILLEUR_A_CHAQUE_ITERATION or config.AFFICHER_GRAPHIQUE or config.SAUVEGARDE_RESULTATS:
                h = [];
                heapq.heapify(h)
                for i in self.pop.individus:
                    heapq.heappush(h, (Evaluateur(i, self.nombre_machines)))

                res = heapq.heappop(h)
                self.meilleurs.append(res.evaluer())
                
                if config.AFFICHER_MEILLEUR_A_CHAQUE_ITERATION:
                    print("[" + str(c + 1) + "] Meilleure séquence : ", [j.numero for j in res.get_individu().sequence], "avec une évaluation à ", res.evaluer())
        
        self.temps = round(time.perf_counter() - t_debut, 2)
    
    # get_solution permet de récupérer la solution optimale (locale) pour l'exécution réalisée
    def get_solution(self):
        h = [];
        heapq.heapify(h)
        for i in self.pop.individus:
            heapq.heappush(h, (Evaluateur(i, self.nombre_machines)))
        res = heapq.heappop(h)
        
        return res.get_individu(), res.evaluer()
    
    def get_meilleur_chaque_iteration(self):
        return self.meilleurs
    
    # get_temps retourne le temps qui a été nécessaire pour trouver une solution optimale localement (temps d'exécution)
    def get_temps(self):
        return self.temps
    
        
        