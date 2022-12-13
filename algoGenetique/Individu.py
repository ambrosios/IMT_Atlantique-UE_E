from random import random
from algoGenetique.Individu import Individu

class Individu():
    
    sequence = None;
    
    def __init__(self, sequence: list):
        self.sequence = sequence
        
    def muter(self, seuil: float):
        probabilite = random.rand(0, 1)
        if(probabilite < seuil):
            self.faire_mutation()
    
    def faire_mutation(self):
        self.permuter(random.randint(0, len(self.sequence)), random.randint(0, len(self.sequence)))
        
    def permuter(self, e1: int, e2: int):
        e1_sequence = self.sequence[e1]
        e2_sequence = self.sequence[e2]
        
        self.sequence[e1] = e2_sequence
        self.sequence[e2] = e1_sequence
        
    def faire_enfant(self, indiv2: Individu): #### À MODIFIER ####
        sequence1, sequence2 = self.sequence, self.sequence
        enfant1 = Individu(sequence1)
        enfant2 = Individu(sequence2)
        return (enfant1, enfant2)