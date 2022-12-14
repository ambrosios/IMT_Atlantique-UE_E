import random
# from individu import Individu

class Individu():
    
    sequence = None;
    
    def __init__(self, sequence: list):
        self.sequence = sequence
        
    def faire_enfant(self, indiv2): #### À MODIFIER ####
        sequence1, sequence2 = self.doubleCoupe(self, indiv2)
        print("Nouv", sequence1, sequence2)
        enfant1 = Individu(sequence1)
        enfant1.corriger(self.sequence)
        enfant2 = Individu(sequence2)
        enfant2.corriger(self.sequence)
        return (enfant1, enfant2)
    
    def doubleCoupe(self, indiv1, indiv2):
        indiceCoupe1 = random.randint(0, len(self.sequence) - 2)
        indiceCoupe2 = random.randint(indiceCoupe1 + 1, len(self.sequence) - 1)
        
        sequence1 = indiv1.sequence[0:indiceCoupe1 - 1] + indiv2.sequence[indiceCoupe1:indiceCoupe2 - 1] + indiv1.sequence[indiceCoupe2:len(self.sequence) - 1]
        sequence2 = indiv2.sequence[0:indiceCoupe1 - 1] + indiv1.sequence[indiceCoupe1:indiceCoupe2 - 1] + indiv2.sequence[indiceCoupe2:len(self.sequence) - 1]
        
        return sequence1, sequence2
    
    def corriger(self, liste_jobs_initiale: list):
        print("corr")
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
                        if c < len(jobs_absents):
                            self.sequence[k] = jobs_absents[c]
                            c += 1
    
    def muter(self, seuil: float):
        probabilite = random.uniform(0, 1)
        if(probabilite < seuil):
            self.faire_mutation()
    
    def faire_mutation(self):
        print([job.numero for job in self.sequence], "va muter")
        self.permuter(random.randint(0, len(self.sequence) - 1), random.randint(0, len(self.sequence) - 1))
        print("Résultat de la mutation :", [job.numero for job in self.sequence])
        
    def permuter(self, e1: int, e2: int):
        e1_sequence = self.sequence[e1]
        e2_sequence = self.sequence[e2]
        
        self.sequence[e1] = e2_sequence
        self.sequence[e2] = e1_sequence
        
    
    def afficher(self):
        print([job.numero for job in self.sequence])