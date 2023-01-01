#import Job
#import Ordonnancement
import math as m

class Algorithme():
    def __init__(self, nombre_jobs=0, nombre_machines=0, liste_jobs=None):

        # nombre de jobs pour le problème
        self.nombre_jobs = nombre_jobs

        # nombre de machines pour le problème
        self.nombre_machines = nombre_machines

        # ensemble des jobs pour le problème (l'ordre n'est pas important)
        self.liste_jobs = liste_jobs
    
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
            j = job.Job(i, l)
            self.liste_jobs.append(j)
        # fermeture du fichier
        fdonnees.close()

def ordre_NEH(self):
        """renvoie la liste des jobs ordonnée selon NEH"""
    	
        # on trie les jobs selon leurs durées décroissantes
        l = [job for job in self.liste_jobs]
        l = sorted(l, key=lambda job:job.duree_job, reverse=True)
        
        for i in l:
            i.afficher()
        
        l_opt=[l[0]] #liste à laquelle on va ajouter successivement les jobs (qui reste optimisée)
        l_test=[l[0]] #liste que l'on va utiliser pour tester les ajouts successifs
        for ind in range(1,len(self.liste_jobs)):
            #print("indice job :",ind)
            new_job = l[ind]
            #print("le job à tester : ",new_job)
            best_date = m.inf
            best_liste = []
            for i in range(len(l_opt)+1): #indice d'ajout de new_job dans l_test
                l_test=l_opt[:i]+[new_job]+l_opt[i:]
                o = ordonnancement.Ordonnancement(prob.nombre_machines) #pas oublier de réinitialiser l'ordonnancement
                o.ordonnancer_liste_job(l_test)
                date_de_fin = o.duree
                #print("bd : ",best_date)
                #print("df : ",date_de_fin)
                if date_de_fin<best_date:
                    best_date = date_de_fin
                    best_liste = l_test                
                l_test=l_opt.copy()
            l_opt=best_liste.copy()
            
                
        return l_opt


def f(x): #fonction d'evaluation, x est une liste
    pass

def voisinage(s):
    size=len(s)
    voisins=[]
    for i in range(size-1):
        new=s.copy()
        temporaire=new[i]
        new[i]=new[i+1]
        new[i+1]=temporaire
        voisins.append(new)
    return voisins

def best(liste,tabou_liste, best_valeur):
    liste_couples=[] #liste des couples (element, valeur)
    for element in liste:
        liste_couples.append((element, evaluer(element)))
    liste_triee = sorted(liste_couples, key=lambda couple: couple[1])
    for couple in liste_triee:
        if couple[1]<best_valeur or couple[0] not in tabou_liste:
            return couple

def evaluer(liste):
    ordonnancement.Ordonnancement(prob.nombre_machines)
    o.ordonnancer_liste_job(liste)
    return o.duree

def tabou(self):
    iter_max=30 #nombre d'iterations max
    current_list = prob.ordreNEH #heuristique
    best_list = current_list #meilleure solution
    best_duree = evaluer(best_list)
    tabou_liste = [sc] #liste des tabous
    critere = True
    while not critere:
        voisins = voisinage(current_list)
        current_list, current_duree = best(voisins, tabou_liste, best_duree) #best voisin de sc
        if current_duree<best_duree:
            sb = sc
            best_duree = current_duree
        if current_list not in tabou_liste:
            tabou_liste.append(current_list)
        if len(tabou_liste)>10:
            tabou_liste.pop(0) #tabou_liste est un FIFO


# Pour tester
if __name__ == "__main__":

    print("JEU 1 :")
    prob = Algorithme()
    prob.definir_par_fichier("jeu1.txt")
    o = ordonnancement.Ordonnancement(prob.nombre_machines)