# test
import random
from algoGenetique.Evaluateur import Evaluateur
from algoGenetique.Individu import Individu


class Population():
    
    # n : taille de la population
    def __init__(self, n: int, sequence: list):
        if self.n % 2 == 0:
            self.n = n
        else:
            self.n = n+1
            print("La valeur de n a été modifiée à ", n+1);
            
        self.sequence = sequence
        self.generer()
        
    
    def generer(self):
        self.individus = [None for _ in range(self.n)];
        
        for _ in range(0, self.n):
            sequence = self.sequence #### À MODIFIER ####
            i = Individu(sequence)
            self.ajouter_individu(i)
        
    
    def ajouter_individu(self, indiv: Individu):
        self.individus = self.individus + [indiv]
    
    def associer(self):
        parents = []
        
        individus_melanges = self.individus[:]
        random.shuffle(individus_melanges)
        
        for k in range(0, self.n/2):
            parents.append((individus_melanges[2*k], individus_melanges[2*k+1]))
        
        self.parents = parents;
    
    def faire_enfants(self):
        enfants = []
        for parents in self.parents:
            
    
    def selectionner(self): #### À MODIFIER ####
        evaluations = []
        for indiv in self.sequence:
            evaluations.append((Evaluateur(indiv)).evaluer())