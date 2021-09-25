#Autor: Tonny Gualdron
#En este codigo se analiza la cantidad de pasos necesarios para la estabilizacion

import simulacion as simu


#Los parametros no tiene algun razonamiento particular mas que facilitar la simulacion y 
# economizar recursos.

N_T = 5         #  Numero de temperatura simuladas
N = 10          #  Tamano de la red
N_Pasos = 2**12   #  Numero de pasos

J = 1.0
K_B = 1.0

T = np.linspace(1.00, 4.00, N_T)
Pasos = np.linspace(2, N_Pasos, N_Pasos-1) 

for temperatura in range(N_T):
    matriz = initialstate(N)         # Genera la matriz de espines
    E,M = np.zeros(N_Pasos-1), np.zeros(N_Pasos-1)  #Arreglos para guardar energia y magnetización

    E1 = M1 = 0
    E_Inicial = M_Inicial = 0
    beta =1.0/(K_B*T[temperatura])

    for i in range(N_Pasos):
        simu.MCAM(matriz, N, J, beta)       
        Energia = simu.calcularEnergia(matriz, N, J)     # calculate the energy
        Magnetizacion = simu.calcularMagnetizacion(matriz)        # calculate the magnetisation

        E1 += Ene
        M1 += Mag

        # Divido por el número de sitios e iteracciones para obtener los valores intensivos
        # Analizo las diferencias pocentual
        if(i == 0):
            E_Inicial = (1/(N*N))*E1
            M_Inicial = (1/(N*N))*M1
        else if (i == 1):
            E[i] = abs((1/((i+1)*N*N))*E1 - E_Inicial)/E_Inicial
            M[i] = abs((1/((i+1)*N*N))*M1 - M_Inicial)/M_Inicial
        else:
            E[i] = abs((1/((i+1)*N*N))*E1 - E[i-1])/E[i-1]
            M[i] = abs((1/((i+1)*N*N))*M1 - M[i-1])/M[i-1]

        plt.plot(E, Pasos, label = 'T = ' + T[temperatura])

plt.xlabel("Numero de pasos", fontsize=20)
plt.ylabel("Variación energía", fontsize=20)