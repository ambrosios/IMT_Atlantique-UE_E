from random import random
# from individu import Individu

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
        
    def faire_enfant(self, indiv2): #### À MODIFIER ####
        sequence1, sequence2 = self.sequence, self.sequence
        enfant1 = Individu(sequence1)
        enfant1.corriger(self.sequence)
        enfant2 = Individu(sequence2)
        enfant2.corriger(self.sequence)
        return (enfant1, enfant2)
    
    def corriger(self, liste_jobs_initiale: list):
        jobs_de_sequence = []
        jobs_en_double = []
        for job in self.sequence:
            if not(job in jobs_de_sequence):
                jobs_de_sequence.append(job)
            else:
                jobs_en_double.append(job)
        
        jobs_absents = []
        for job in liste_jobs_initiale:
            if job not in self.sequence:
                jobs_absents.append(job)
        
        if len(jobs_en_double) != 0:
            c = 0
            for job in jobs_en_double:
                change = False
                for k in range(len(self.sequence)):
                    if not(change) and self.sequence[k].numero == job.numero:
                        self.sequence[k] = jobs_absents[c]
                        c += 1
        
    def afficher(self):
        print([job.numero for job in self.sequence])