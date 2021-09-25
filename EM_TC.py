#Autor: Tonny Gualdron
#En este codigo se calcula el valor promedio de la energia y la magnetizacion para diferentes valores
#de temperatura por encima y debajo de la temperatura critica.

import Simulacion as simu
import numpy as np
import matplotlib.pyplot as plt

#Los parametros no tiene algun razonamiento particular mas que facilitar la simulacion y 
# economizar recursos.

N_T = 50         #  Numero de temperatura simuladas
N = 10          #  Tamano de la red
N_Pasos = 2**10   #  Numero de pasos
NE_Pasos = 2**9   #  Numero de pasos para la estabilizacion
 
J = 1.0
K_B = 1.0
#Para estos parametros la Temperatura Critica es 2.269185314213022 K

T = np.linspace(1.50, 3.50, N_T)

matriz = simu.matrizEspines(N)         #Genera la matriz de espines
E,M = np.zeros(N_T), np.zeros(N_T)     #Arreglo para guardar energia y magnetizacion

for temperatura in range(N_T):
    E1 = M1 = 0       #Variable para guardar la energia y la magnetizacion
    beta =1.0/(K_B*T[temperatura])

    for i in range(NE_Pasos):
        #Uiliza monte carlo con el algoritmo metropolis por el numero de pasos necesario
        #para lograr la estabilizacion
        simu.MCAM(matriz, N, J, beta) 

    for i in range(N_Pasos):
        #Uiliza monte carlo con el algoritmo metropolis
        simu.MCAM(matriz, N, J, beta) 
        Energia = simu.calcularEnergia(matriz, N, J)     # Calcular la energia
        Magnetizacion = simu.calcularMagnetizacion(matriz)  #Calcular la magnetizacion

        # Divido por el número de sitios e iteracciones para obtener los valores intensivos
        E1 += Energia
        M1 += Magnetizacion

    E[temperatura] = (1/(N_Pasos*(N**2)))*E1
    M[temperatura] = (1/(N_Pasos*(N**2)))*M1

plt.scatter(T,E, s=50, marker='*')
plt.xlabel("Temperatura")
plt.ylabel("Energía")
plt.axvline(x=2/np.arcsinh(1))
plt.savefig("E_Vs_T.jpg")
plt.close()

plt.scatter(T,abs(M), s=50, marker='*')
plt.xlabel("Temperatura")
plt.ylabel("Magnetización")
plt.axvline(x=2/np.arcsinh(1))
plt.savefig("M_Vs_T.jpg")
plt.close()