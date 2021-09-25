#Autor: Tonny Gualdron
#En este codigo se analiza la cantidad de pasos necesarios para la estabilizacion

import Simulacion as simu
import numpy as np
import matplotlib.pyplot as plt

#Los parametros no tiene algun razonamiento particular mas que facilitar la simulacion y 
# economizar recursos.

N_T = 10         #  Numero de temperatura simuladas
N = 10          #  Tamano de la red
N_Pasos = 2**10   #  Numero de pasos

J = 1.0
K_B = 1.0

T = np.linspace(1.50, 3.50, N_T)
Pasos = np.linspace(0, N_Pasos, N_Pasos) 

for temperatura in range(N_T):
    matriz = simu.matrizEspines(N)         #Genera la matriz de espines
    E = np.zeros(N_Pasos)                  #Arreglo para guardar energia

    E1 = 0      #Variable para guardar la energia
    beta =1.0/(K_B*T[temperatura])

    for i in range(N_Pasos):
        #Uiliza monte carlo con el algoritmo metropolis
        simu.MCAM(matriz, N, J, beta) 
        Energia = simu.calcularEnergia(matriz, N, J)     # Calcula la energia

        # Divido por el número de sitios e iteracciones para obtener los valores intensivos
        E1 += Energia
        E[i] = (1/((i+1)*(N**2)))*E1

    plt.plot(Pasos,E, label = 'T = ' + str(round(T[temperatura],2)) + ' K')
plt.xlabel("Numero de pasos")
plt.ylabel("Energía")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)
plt.savefig("E_Vs_N_Pasos.jpg")
plt.close()