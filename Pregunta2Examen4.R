'''
El siguiente codigo en R crea una funcion sumatroria_a(x, n) que evalua 
la suma de los primeros n terminos de una serie en un real x.

Parametros de entrada: 
    n: Numero de sumas a calcular.
    x: numero real en la serie

Datos de salida: Aproximacion de las sumas calculadas.

Autor: David Felipe Henao 
Ultima actualizacion: 22/09/2021
'''

sumatoria_a <- function(x, n) {
  
  # Iniciamos el acomulador
  suma <- 0
  
  for (i in 1:n){
    
    # Calculamos cada termino de la serie
    sumatoria <- (x^i)/(i^i)
    
    # Sumamos los terminos
    suma <- suma + sumatoria
  } 
  return(suma)
}