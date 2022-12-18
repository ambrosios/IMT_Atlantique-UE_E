import random
import config

# Une instance de Individu correspond à un ordonnancement
# Un Individu peut :
#   * faire des enfants avec un autre individu
#   * se corriger lorsqu'il y a des jobs qui se répètent
#   * muter

class Individu():
    
    sequence = None;
    
    def __init__(self, sequence: list):
        self.sequence = sequence
    
    # faire_enfant génère 2 individus à partir de l'individu courant et d'un second individu
    def faire_enfant(self, indiv2):
        sequence1, sequence2 = self.double_coupe(indiv2)
        enfant1 = Individu(sequence1)
        enfant1.corriger(self.sequence)
        enfant2 = Individu(sequence2)
        enfant2.corriger(self.sequence)
        return (enfant1, enfant2)
    
    # double_coupe réalise 2 coupes dans les séquences de l'individus courant et d'un autre individu
    # la méthode intervertit les sous-séquences entre les 2 coupes pour la séquence de chaque individu pour créer 2 nouvelles séquences
    def double_coupe(self, indiv2):
        indiceCoupe1 = random.randint(1, len(self.sequence) - 2)
        indiceCoupe2 = random.randint(indiceCoupe1 + 1, len(self.sequence) - 1)
        
        sequence1 = self.sequence[0:indiceCoupe1] + indiv2.sequence[indiceCoupe1:indiceCoupe2] + self.sequence[indiceCoupe2:len(self.sequence)]
        sequence2 = indiv2.sequence[0:indiceCoupe1] + self.sequence[indiceCoupe1:indiceCoupe2] + indiv2.sequence[indiceCoupe2:len(self.sequence)]
        
        return sequence1, sequence2
    
    # corriger corrige les doublons de jobs en remplaçant la première instance d'un job en double par un job non présent dans la séquence
    def corriger(self, liste_jobs_initiale: list):
        
        # print("corr_debut", [j.numero for j in self.sequence])
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
                            change = True
    
        # print("corr_fin", [j.numero for j in self.sequence])
    
    # muter réalise une mutation de l'individu par rapport à un seuil donné
    def muter(self, seuil: float):
        probabilite = config.PROBABILITE_MUTATION_FONCTION(0, 1)
        if(probabilite < seuil):
            self.faire_mutation()
    
    # faire_mutation effectue la mutation selon la méthode choisie (ex : permutation)
    def faire_mutation(self):
        
        self.permuter(random.randint(0, len(self.sequence) - 1), random.randint(0, len(self.sequence) - 1))
        
    # permuter inverse 2 jobs dans la séquence
    def permuter(self, e1: int, e2: int):
        sequence_avant = self.str()
        
        e1_sequence = self.sequence[e1]
        e2_sequence = self.sequence[e2]
        
        self.sequence[e1] = e2_sequence
        self.sequence[e2] = e1_sequence
        
        if config.AFFICHER_MUTATIONS:
            print(sequence_avant, "a muté en", self.str(), "(jobs échangés : " + str(e1_sequence.numero) + " et " + str(e2_sequence.numero) + ")")
        
        return e1_sequence, e2_sequence
        
    # liste_job renvoie la liste des jobs de l'ordonnancement sous forme de numéros
    def liste_job(self):
        return [job.numero for job in self.sequence]
    
    # str renvoie la liste en format string des jobs de l'ordonnancement sous forme de numéros
    def str(self):
        affichage = "["
        for job in self.sequence:
            affichage += str(job.numero) + ", "
            
        affichage = affichage[: -2] + "]"
        return affichage
    
    # afficher affiche la liste des jobs de l'ordonnancement sous forme de numéros
    def afficher(self):
        print(self.str())