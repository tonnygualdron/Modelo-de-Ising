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
Pasos = np.linspace(1, N_Pasos, N_Pasos) 

for temperatura in range(N_T):
    matriz = initialstate(N)         # Genera la matriz de espines
    E,M = np.zeros(N_Pasos), np.zeros(N_Pasos)  #Arreglos para guardar energia y magnetización

    E1 = M1 = 0
    beta =1.0/(K_B*T[temperatura])

    for i in range(N_Pasos):
        simu.MCAM(matriz, N, J, beta)       
        Energia = simu.calcularEnergia(matriz, N, J)     # calculate the energy
        mMgnetizacion = simu.calcularMagnetizacion        # calculate the magnetisation

        E1 = E1 + Ene
        M1 = M1 + Mag
        M2 = M2 + Mag*Mag 
        E2 = E2 + Ene*Ene


    # divide by number of sites and iteractions to obtain intensive values    
    E[tt] = n1*E1
    M[tt] = n1*M1
    C[tt] = (n1*E2 - n2*E1*E1)*iT2
    X[tt] = (n1*M2 - n2*M1*M1)*iT
