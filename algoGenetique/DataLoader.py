from algoGenetique.job import Job

class DataLoader():
    def __init__(self, data_filename):
        self.definir_par_fichier(data_filename)
        
    def definir_par_fichier(self, nom):
        """ crée un problème de flowshop à partir d'un fichier """
        # ouverture du fichier en mode lecture
        fdonnees = open(nom,"r")
        # lecture de la première ligne
        ligne = fdonnees.readline() 
        l = ligne.split() # on récupère les valeurs dans une liste
        self.nombre_jobs = int(l[0])
        self.nombre_machines = int(l[1])
       
        self.liste_jobs = []
        for i in range(self.nombre_jobs):
            ligne = fdonnees.readline() 
            l = ligne.split()
            # on transforme la suite de chaînes de caractères représentant
            # les durées des opérations en une liste d'entiers
            l = [int(i) for i in l]
            j = Job(i, l)
            self.liste_jobs.append(j)
        # fermeture du fichier
        fdonnees.close()
        
    def get_nombre_jobs(self):
        return self.nombre_jobs
    
    def get_nombre_machines(self):
        return self.nombre_machines
    
    def get_liste_jobs(self):
        return self.liste_jobs