import heapq
import random
from classes.Evaluateur import Evaluateur
from classes.Individu import Individu
import config

# Une instance de Population correspond à un ensemble d'ordonnancement (Individus)
# Une Population peut :
#   * générer des Individus (ordonnancemens)
#   * associer des Individus entre eux
#   * faire des enfants à partir de 2 Individus
#   * faire des mutations
#   * évaluer ses Individus
#   * sélectionner (et éliminer) ses Individus

class Population():
    
    # individus : liste de tous les individus de la population
    
    # n : taille de la population
    def __init__(self, n: int, sequence: list):
        # On s'assure que n est pair
        if n % 2 == 0:
            self.n = n
        else:
            self.n = n+1
            if config.AFFICHER_AJUSTEMENT_TAILLE_POPULATION:
                print("La valeur de n a été modifiée à ", n+1);
            
        self.sequence = sequence
        self.generer()
        
    # generer génère une population de n individus
    def generer(self):
        self.individus = [];
        
        for _ in range(0, self.n):
            sequence = self.sequence[:]
            random.shuffle(sequence)
            i = Individu(sequence)
            self.ajouter_individu(i)
    
    # ajouter_individu ajoute un inidividu à la population
    def ajouter_individu(self, indiv: Individu):
        self.individus = self.individus + [indiv]
        if config.AFFICHER_NOUVEAUX_INDIVIDUS:
            print("L'individu ", indiv.liste_job(), "a été ajouté à la population")
    
    # associer créer des paires d'individus au sein de la population (les parents)
    def associer(self):
        parents = []
        
        individus_melanges = self.individus[:]
        random.shuffle(individus_melanges)
        
        for k in range(0, int(self.n/2)):
            parents.append((individus_melanges[2*k], individus_melanges[2*k+1]))
        
        self.parents = parents;
    
    # faire_enfants crée des enfants à partir des parents et les ajoute à la population
    def faire_enfants(self):
        enfants = []
        for parents in self.parents:
            nouveaux_enfants = parents[0].faire_enfant(parents[1])
            enfants.append(nouveaux_enfants)
            self.ajouter_individu(nouveaux_enfants[0])
            self.ajouter_individu(nouveaux_enfants[1])
            
        self.enfants = enfants;
        
    # muter expose les enfants à des mutations
    # la mutation dynamique est appliquée lorsqu'il y a trop d'individus identiques dans la population. Elle augmente la probabilité d'avoir des mutations sur les enfants.
    def muter(self, seuil: int, dynamique: bool):
        seuil_mutation = seuil
        
        if config.AFFICHER_NOMBRE_DOUBLONS or dynamique:
            doublons = self.taux_doublons()
        
        if dynamique:
            if doublons[1] > config.MUTATION_DYNAMIQUE_SEUIL:
                seuil_mutation = random.uniform(seuil, 1 - seuil + 0.01)
        
        if config.AFFICHER_NOMBRE_DOUBLONS:
            print("L'individu le plus répété est", doublons[2].liste_job(), ": ", doublons[0], "/", len(self.individus), "=", doublons[1]*100, "%")
        
        for (enfant1, enfant2) in self.enfants:
            enfant1.muter(seuil_mutation)
            enfant2.muter(seuil_mutation)
    
    # taux_doublons détermine l'individu qui est le plus présent dans la population ainsi que son nombre d'occurrence
    def taux_doublons(self) -> tuple[float, list]:
        indiv_en_doublon = None
        nombre_indiv_en_doublon_max = 0
        
        for indiv in self.individus:
            nb = self.nombre_doublon_individu(indiv)
            if nombre_indiv_en_doublon_max < nb:
                nombre_indiv_en_doublon_max = nb
                indiv_en_doublon = indiv
        
        return (nombre_indiv_en_doublon_max, nombre_indiv_en_doublon_max / len(self.individus), indiv_en_doublon)
    
    # nombre_doublon_individu détermine le nombre d'occurrence d'un individu dans la population
    def nombre_doublon_individu(self, individu) -> int:
        c = 0
        for indiv in self.individus:
            identique = True
            for j in range(len(indiv.sequence)):
                identique = identique and indiv.sequence[j].numero == individu.sequence[j].numero
            if identique:
                c += 1
        return c
    
    # evaluer classe les individus de la population selon leur évaluation (définie par Evaluateur)
    # note : on utilise une heapq pour faciliter le classement des évaluations
    def evaluer(self, nb_machines):
        evaluations = []
        heapq.heapify(evaluations)
        
        for indiv in self.individus:
            e = Evaluateur(indiv, nb_machines)
            heapq.heappush(evaluations, e)
            
            if config.AFFICHER_EVALUATIONS:
                print("L'individu", indiv.liste_job(), "a été évalué à", e.evaluer())

        self.evaluations = evaluations
    
    # selectionner sélectionne les individus les plus performants (dans la limite d'un taux de bons élèves) et complète avec d'autres individus choisis aléatoirement
    def selectionner(self, taux_meilleurs: float):
        selection = []
        nombre_meilleurs = int(taux_meilleurs * self.n)
        nombre_moins_bons = self.n - nombre_meilleurs
        
        for _ in range(nombre_meilleurs):
            eval = heapq.heappop(self.evaluations)
            selection.append(eval.get_individu())
            
            if config.AFFICHER_SELECTIONNES:
                print("L'individu ", eval.get_individu().liste_job(), "a été sélectionné avec une bonne évaluation à", (eval).evaluer())
        
        reste_individus_possibles = random.sample(range(0, len(self.evaluations)), nombre_moins_bons)
        
        for i in range(0, len(reste_individus_possibles)):
            selection.append(self.evaluations[i].get_individu())
            
            if config.AFFICHER_SELECTIONNES:
                print("L'individu ", self.evaluations[i].get_individu().liste_job(), "a été sélectionné avec une moins bonne évaluation à", (self.evaluations[i]).evaluer())
        
        self.individus = selection
    
    # afficher affiche les individus qui composent la population     
    def afficher(self):
        affichage = "La population est composée de " + str(len(self.individus)) + " individus avec "
        for indiv in self.individus:
            affichage += indiv.str() + ", "
        affichage = affichage[: -2]

        print(affichage)