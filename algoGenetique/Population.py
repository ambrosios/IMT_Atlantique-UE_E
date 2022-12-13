import random
from evaluateur import Evaluateur
from individu import Individu


class Population():
    
    # n : taille de la population
    def __init__(self, n: int, sequence: list):
        if n % 2 == 0:
            self.n = n
        else:
            self.n = n+1
            print("La valeur de n a été modifiée à ", n+1);
            
        self.sequence = sequence
        self.generer()
        
    
    def generer(self):
        self.individus = [];
        
        for _ in range(0, self.n):
            sequence = self.sequence[:]
            random.shuffle(sequence)
            i = Individu(sequence)
            self.ajouter_individu(i)
        
    
    def ajouter_individu(self, indiv: Individu):
        self.individus = self.individus + [indiv]
    
    def associer(self):
        parents = []
        
        individus_melanges = self.individus[:]
        random.shuffle(individus_melanges)
        
        for k in range(0, int(self.n/2)):
            parents.append((individus_melanges[2*k], individus_melanges[2*k+1]))
        
        self.parents = parents;
    
    def faire_enfants(self):
        enfants = []
        for parents in self.parents:
            nouveaux_enfants = parents[0].faire_enfant(parents[1])
            enfants.append(nouveaux_enfants)
            self.individus += [nouveaux_enfants[0], nouveaux_enfants[1]]
            
        self.enfants = enfants;
    
    def selectionner(self): #### À MODIFIER ####
        evaluations = []
        for indiv in self.sequence:
            evaluations.append((Evaluateur(indiv)).evaluer())
            
            
    def afficher(self):
        for indiv in self.individus:
            indiv.afficher()