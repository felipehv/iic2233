
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time
ex = pd.read_csv("examenes.csv")

#Buscamos los nombres de los examenes
nombres = []
for e in ex:
    if "examen" in e:
        nombres.append(e)

print(len(nombres))

for i in range(len(nombres)):
    e = nombres[i]
    for j in range(i+1,len(nombres)):
        lista1 = []
        lista2 = []
        lista_color = []
        e2 = nombres[j]
        if "examen" in e and "examen" in e2:
            for i in range(len(ex)):
                if ex["diagnostico"][i] == "sano":
                    lista_color.append("green")
                else:
                    lista_color.append("red")
                lista1.append(ex[e][i])
                lista2.append(ex[e2][i])
            lista3 = []
            lista1 = np.array(lista1)
            lista2 = np.array(lista2)
            pf = np.polyfit(lista1,lista2,1)
            for i in range(len(lista1)):
                lista3.append(lista1[i]*pf[0]+pf[1])
            lista3 = np.array(lista3)
            plt.scatter(lista1,lista2,color=lista_color)
            plt.plot(lista1,lista3)
            plt.show(block=False)
            plt.pause(2)
            plt.clf()


