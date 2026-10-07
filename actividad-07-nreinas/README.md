# Actividad 7 — N reinas con Simulated Annealing

Ejercicio de la clase 8: implementar Simulated Annealing para resolver el problema de las N
reinas, que consiste en ubicar N reinas en un tablero de N por N sin que ninguna ataque a
otra.

La entrega es [`01_ejercicio_n_reinas.ipynb`](01_ejercicio_n_reinas.ipynb), que es la
plantilla de la cátedra. Completé únicamente las secciones marcadas, como pide el enunciado:
el nombre, la función `simulated_annealing` dentro del bloque `TODO`, los valores de
`initial_temp` y `cooling_rate` en las cinco corridas, y la respuesta final. No toqué nada
más, ni la firma de la función ni el tipo de salida.

## Resultado

| Algoritmo | Soluciones en 5 corridas |
|---|---|
| Gradiente descendente (ya venía en la plantilla) | 3 de 5 |
| Simulated Annealing | 5 de 5 |

## Cómo funciona la implementación

Seguí la estructura del Simulated Annealing para Sudoku que el README del ejercicio indica
como referencia, en `03_sudoku_simulated_annealing.ipynb`.

En cada iteración se recorren los vecinos en orden aleatorio hasta aceptar uno. Si el vecino
mejora el costo, nos movemos siempre. Si lo empeora, igual nos podemos mover, con la
probabilidad de Boltzmann que vimos en la teoría:

```
P(aceptar) = exp(-delta / temperature)
```

donde `delta` es cuánto empeora. Esa es la pieza que permite escapar de los mínimos locales
donde el gradiente descendente se queda trabado, que es exactamente su problema según el
deck 08.

Si se recorren todos los vecinos y no se acepta ninguno, ya no hay a dónde moverse y el
bucle termina. También corta antes de `max_steps` si el costo llega a 0. En los dos casos
`last_step` queda con la cantidad real de iteraciones ejecutadas.

La temperatura baja de forma geométrica, multiplicándose por `cooling_rate` en cada
iteración. Así el algoritmo explora mucho al principio y sobre el final ya casi solo acepta
mejoras, que es la idea del enfriamiento.

## Por qué esos parámetros

Elegí `initial_temp = 2.0` y `cooling_rate = 0.99`.

Con temperatura 2, un movimiento que empeora el costo en 1 conflicto se acepta con
probabilidad `exp(-1/2)`, que es aproximadamente 0.61. O sea que al principio el algoritmo
acepta casi dos de cada tres movimientos malos y se mueve con libertad por el tablero.

Enfriando al 0.99 por paso, después de 1000 iteraciones la temperatura queda del orden de
0.00009. Con eso la probabilidad de aceptar un movimiento que empeora es prácticamente cero,
así que el final del proceso es puro descenso. El enfriamiento cubre todo el presupuesto de
pasos sin quedarse frío demasiado pronto ni seguir caliente hasta el final.

## Qué tan estable es el resultado

Antes de elegir, medí las tasas de éxito con 2000 corridas por configuración, en un script
aparte. Las 5 corridas del notebook son una muestra chica, así que conviene saber qué hay
detrás:

| Configuración | Éxito |
|---|---|
| Gradiente descendente | 16 % |
| Simulated Annealing, recorriendo vecinos hasta aceptar uno | 98 % |
| Simulated Annealing, tomando un solo vecino al azar por iteración | 75 % |

La segunda y la tercera fila usan los mismos parámetros y el mismo presupuesto de 1000
iteraciones. La diferencia es cómo se gasta cada iteración: tomando un vecino al azar, la
mayoría de las iteraciones se desperdician en rechazos cuando la temperatura ya bajó, y el
presupuesto se agota antes de converger. Recorriendo los vecinos hasta aceptar uno, cada
iteración avanza de verdad.

Con el 98 %, sacar 5 de 5 tiene una probabilidad del 92 %, así que el resultado del notebook
es el esperable y no una casualidad.

Vale aclarar que el 3 de 5 del gradiente descendente que muestra la plantilla es bastante
mejor que su tasa real del 16 %, así que esa corrida salió con suerte.

## Cómo correrlo

```bash
pip install jupyter
jupyter notebook 01_ejercicio_n_reinas.ipynb
```

El notebook es autocontenido y solo usa `random` de la biblioteca estándar. Las celdas de
gradiente descendente conservan la corrida original; si se vuelven a ejecutar van a dar otro
resultado, porque el estado inicial es aleatorio.
