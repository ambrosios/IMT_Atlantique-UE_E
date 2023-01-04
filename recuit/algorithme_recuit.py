from classes.Recuit import Recuit
import config
import matplotlib.pyplot as plt

L = []
for i in range (0,config.NOMBRE_EXECUTIONS) :
    r = Recuit()
    r.set_temps_initial(0)
    r.executer()
    L.append(r.liste_temps_S_star)
    if config.AFFICHAGE_STAT :
        r.afficher_stats()

print(len(L))
print(len(L[0]))
x = range(len(L[0]))

for i in range(0,len(L)) :
    plt.plot(x, L[i])

plt.title('Evolution de la meilleure solution trouvée en fonction du nombre d\'itération ')
plt.grid(True)
plt.show()








