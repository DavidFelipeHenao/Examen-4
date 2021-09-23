'''
El siguiente codigo en python crea una funcion zeta(n) que evalua los 
primeros n terminos de la funcion zeta de Riemann y evalua si zeta(n) se 
aproxima a π^2/6 cuando n aumenta.

Parametros de entrada: 
    n: Numero de sumas a calcular.

Datos de salida: Aproximacion de las sumas calculadas.

Autor: David Felipe Henao
Ultima actualizacion: 22/09/2021
'''

def zeta(n):
    
    # Iniciamos el acumulador
    suma = 0 
    
    for k in range(1, n+1):
        
        # Calculamos los termino de la sumatoria
        sumatoria = 1/(k**2)
        
        # Sumamos cada termino
        suma += sumatoria
    
    return suma

# A medida que n se hace “grande”, ¿zeta(n) se aproxima a π^2/6?

# Calculamos un aproximado de π^2/6
import numpy as np
ValorAprox = (np.pi**2)/6

# Evaluamos zeta(n) en un n pequeño y uno grande y comparamos con ValorAprox

print(abs(ValorAprox-zeta(9999))) 
print(abs(ValorAprox-zeta(15)))

# Conclusion: cuando n se hace grande zeta(n) se aproxima mas y mas a π^2/6






