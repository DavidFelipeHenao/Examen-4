# Parcial 4
Este repositorio contiene dos codigos que intentan dar solucion a las dos preguntas del parcial 4 del curso de computacion.

El archivo Reimann contiene un codigo en python crea una funcion `zeta(n)` que evalua los 
primeros n terminos de la funcion zeta de Riemann y evalua si `zeta(n)` se aproxima a $\frac{\pi^{2}}{6}$ cuando n se hace grande.

El archivo sumatoria2a contiene un codigo en R crea una funcion `sumatroria_a(x, n)` que evalua 
la suma de los primeros n terminos de una serie en un numero real x.

## Problema 1
(Funcion zeta de Riemann $\zeta(2)$). En 1735, el matematico suizo Leonhard Euler resolvio un famoso problema en teorıa de numeros, al mostrar que la suma
$$\sum_{k=1}^{n}=\frac{1}{k^{2}}=1+\frac{1}{2^{2}}+\frac{1}{3^{2}}+...+\frac{1}{n^{2}}$$
se aproxima a $\frac{\pi^{2}}{6}$, cuando el numero de sumandos `n` se hace “grande”. Implemente una funcion llamada `zeta(n)` que evalue la serie. A medida que `n` se hace “grande”,
¿`zeta(n)` se aproxima a $\frac{\pi^{2}}{6}$?

Al evaluar `zeta(n)` con un pequeño n = 15 se obtuvo que  `zeta(15)` tiene una diferencia de 0.0644937834032393 con respecto a $\frac{\pi^{2}}{6}$, mientras que al hacer `n` mas grande `zeta(9999)` el error en la aproximacion era tan solo de 0.0001000050001611.

Comparando ambos resultados se observa que si n es un numero grande, la aproximacion es mucho mas cercana al valor propuesto por Leonhard Euler.

## Problema 2

Para cada una de las expresiones (“series”) dadas a continuación, elabore una función
f(x,n) que evalúe la suma de los primeros n términos en un número real *x*.

 1. $$x+\frac{x^{2}}{4}+\frac{x^{3}}{27}+\frac{x^{4}}{256}+...$$

Para hacer una funcion que calcule esta serie se halló su representacion en sumatoria:
$$\sum_{i=1}^{n}=\frac{x^{i}}{i^{i}}$$

## Autores
* David Felipe Henao




