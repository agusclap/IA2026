# Actividad 6 — Torre de Hanoi con búsqueda A*

Ejercicio de la clase 7: implementar un algoritmo de búsqueda que no sea BFS para resolver
la Torre de Hanoi de 5 discos.

Elegí A* con una heurística propia, que es la opción de nota máxima 10.

## Archivos

La entrega es [`01_ejercicio_torre_de_hanoi.ipynb`](01_ejercicio_torre_de_hanoi.ipynb), que
es la plantilla de la cátedra con `search_algorithm` completada, más la verificación y la
comparación. Al lado va `aima_libs/`, la biblioteca de la cátedra, copiada para que el
notebook corra solo.

Dejo también [`anexo_analisis_independiente.ipynb`](anexo_analisis_independiente.ipynb), que
es una versión que armé antes con una formulación propia del estado, sin la biblioteca. Lo
conservo porque ahí probé además profundidad, profundidad iterativa y búsqueda voraz, que en
la entrega no están.

## Resultado

Las métricas que devuelve la función:

```
solution_found: True        nodes_in_frontier: 16
nodes_explored: 32          max_depth: 31
states_visited: 32          cost_total: 31.0
```

Los 31 movimientos son el óptimo teórico `2⁵ - 1`. La secuencia la valido en el notebook
paso por paso contra las acciones legales del problema.

## La heurística

Razono sobre el disco más grande. Llamo `d(k, t)` al mínimo de movimientos para llevar los
discos `1..k` a la varilla `t`, y ahí se dan dos casos.

Si el disco `k` ya está en `t`, no conviene moverlo, porque sacarlo y volverlo a poner solo
suma movimientos. El problema queda reducido a los discos más chicos sobre esa misma
varilla, o sea `d(k, t) = d(k-1, t)`.

Si está en otra varilla `p`, para moverlo a `t` los `k-1` discos de arriba tienen que estar
apilados en la tercera varilla `o`, que es la única donde no molestan. Ahí hacen falta tres
cosas obligatorias: llevarlos a `o`, mover el disco `k`, y después pasar la torre entera de
`o` a `t`, que cuesta `2^(k-1) - 1`. Sumando queda `d(k, t) = d(k-1, o) + 2^(k-1)`.

Como esas tres cosas son obligatorias y no se pisan entre sí, la suma da el mínimo y no una
cota floja. Desplegando la recursión alcanza con recorrer los discos de mayor a menor
sumando `2^(k-1)` cada vez que el disco `k` no está donde va.

### Por qué es válida

En el notebook genero los 243 estados del problema, que son las `3⁵` maneras de repartir 5
discos en 3 varillas, y verifico sobre todos que la heurística es consistente,
`h(n) ≤ costo(n, a, n') + h(n')`, y que vale cero en el objetivo. Por el teorema que vimos
en clase, con eso ya queda admisible.

Además resulta exacta: coincide con la distancia real en los 243 estados. La distancia real
la calculo con una búsqueda de costo uniforme hacia atrás desde el objetivo, que se puede
hacer porque los movimientos son reversibles. Eso es solo para verificar, no es el algoritmo
que entrego.

Que sea exacta explica el resultado. Si `h` es la distancia real, `f(n) = g(n) + h(n)` es el
costo del mejor camino que pasa por `n`, así que todos los nodos del camino óptimo tienen el
mismo `f` y cualquier nodo que se salga tiene uno más grande. Por eso A* no se desvía y
explora solo los 31 nodos del camino más el objetivo.

## Comparación

Las tres heurísticas son admisibles, así que las tres llegan al óptimo de 31 movimientos. Lo
que cambia es el trabajo:

| Algoritmo | Movimientos | Nodos explorados |
|---|---|---|
| Costo uniforme (`h = 0`) | 31 | 233 |
| A* con la heurística del aula virtual | 31 | 178 |
| A* con la heurística propia | 31 | 32 |

La heurística del aula penaliza con un punto por cada disco mal ubicado. Es correcta pero
informa poco, porque como mucho vale 5 cuando faltan 31 movimientos y casi no distingue un
estado de otro.

Probando con más discos, la propia se queda en `2^n` exacto mientras las otras dos crecen
con el espacio de estados:

| Discos | Óptimo | A* propia | 2ⁿ | A* aula | Costo uniforme |
|---|---|---|---|---|---|
| 3 | 7 | 8 | 8 | 18 | 25 |
| 4 | 15 | 16 | 16 | 54 | 71 |
| 5 | 31 | 32 | 32 | 178 | 233 |
| 6 | 63 | 64 | 64 | 586 | 687 |

Ese `2^n` es la cantidad de nodos del camino que hay que devolver, así que menos no se
puede.

## Atribución

La carpeta `aima_libs/` no es código mío: es material de la cátedra, sacado del repositorio
`halexisgonzalez/inteligencia-artificial` de la materia (CRUC-IUA), licenciado bajo
CC BY-NC-SA 4.0. Lo incluyo acá para que el notebook de la entrega corra sin dependencias
externas. A su vez `aima_libs/aima.py` deriva de
[aima-python](https://github.com/aimacode/aima-python), con licencia MIT.

Lo mío en esta entrega es la heurística, el algoritmo de búsqueda y el análisis.

## Cómo correrlo

```bash
pip install jupyter
jupyter notebook 01_ejercicio_torre_de_hanoi.ipynb
```

La carpeta `aima_libs/` tiene que quedar al lado del notebook. Corre en segundos y no
necesita datos externos.

El anexo además usa matplotlib, y su celda de profundidad iterativa tarda alrededor de un
minuto.
