#Autor: Tonny Gualdron
#Se omitieron caracteres especiales de los comentarios de este codigo

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from scipy.sparse import spdiags,linalg,eye

def matrizEspines(N):
    #Genera una matriz de espines NxN con direcciones aleatorias 1 o -1
    matriz = 2*np.random.randint(2, size=(N,N))-1
    return matriz

def MCAM(matriz, N, J, beta):
    #Simulacion Monte Carlo del modelo de Ising con el algoritmo de Metropolis 
    for i in range(N):
        for j in range(N):
                #Se genera una posicion aleatoria a,b
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                
                # Espin en la posición a,b
                s =  matriz[a, b]
               
                # Espines vecinos
                # (x+1)%N 0 (X-1)%N aplica condiciones periódicas utilizando el residuo
                # Cuando x+1 = N o x-1= N en este caso el vecino de la posición N es el de la posición 0.
                # Cuando x = 0, entonces x-1= -1 en este caso el vecino de la posición N es el de la posición -1. 
                sv = matriz[(a+1)%N,b] + matriz[a,(b+1)%N] + matriz[(a-1)%N,b] + matriz[a,(b-1)%N]

                #Calculo del deta de energia si se cambiara el espin
                deltaEnergia = 2*J*s*sv
                
                #Condiciones para aceptar el cambio de energia
                if deltaEnergia <= 0:
                    s *= -1
                elif rand() < np.exp(-deltaEnergia*beta):
                    s *= -1
                
                #Actualiza el espin de la posición a,b
                matriz[a, b] = s
    return matriz

def calcularEnergia(matriz,N,J):
    #Calculo de energia dada una configuracion
    energia = 0 
    
    for i in range(N):
        for j in range(N):
            s = matriz[i,j]
            sv = matriz[(i+1)%N, j] + matriz[i,(j+1)%N] + matriz[(i-1)%N, j] + matriz[i,(j-1)%N]
            energia += -J*sv*s
    return energia/2.  #Evita el sobre conteo

def calcMag(matriz):
    #Calculo de magnetizacion dada una configuracion
    magnetizacion = np.sum(matriz)
    return magnetizacion
