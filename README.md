# Inteligencia Artificial — IUA 2026

Actividades individuales de la materia. Una carpeta por actividad, cada una con su notebook
ya ejecutado y sus datos.

| # | Tema | Carpeta |
|---|---|---|
| 2–3 | EDA del dataset de Pokémon | [`actividad-03-eda-pokemon/`](actividad-03-eda-pokemon/) |
| 4 | Dataset del Servicio Meteorológico Nacional | [`actividad-04-smn/`](actividad-04-smn/) |
| 5 | Cuestionario sobre los goles de Messi | [`actividad-05/`](actividad-05/) |
| 6 | Torre de Hanoi con búsqueda A* | [`actividad-06-hanoi/`](actividad-06-hanoi/) |

## Actividad 3 — EDA del dataset de Pokémon

Análisis exploratorio de 800 registros: caracterización del dataset, detección de outliers
con la regla del IQR, y análisis de desafíos y técnicas aplicables. Entregado como notebook
más tres diapositivas.

Lo que más me llamó la atención es que `Total` es la suma exacta de las 6 stats y no tiene
ningún outlier, aunque sus seis componentes sí tengan. Los extremos se compensan entre sí
porque el juego reparte un presupuesto fijo de puntos, así que los outliers no son de poder
sino de perfil.

Más detalle en el [README de la actividad](actividad-03-eda-pokemon/README.md).

## Actividad 4 — Dataset del SMN

Cruce de las estaciones meteorológicas del SMN con sus estadísticas climatológicas normales
del período 1981-2010, y análisis de la región Pampeana.

Hay dos cosas que definen el resultado. La primera es que los nombres de estación no
coinciden entre los dos archivos: `estaciones_smn.txt` no lleva tildes y `estadisticas.txt`
sí, por ejemplo `CORDOBA AERO` contra `CÓRDOBA AERO`. Un `merge` por nombre exacto descarta
70 de 120 estaciones sin avisar nada, así que hay que normalizar antes de unir.

La segunda es que el nivel de agregación cambia las conclusiones. Las variables `temp` y
`prec_mm` viven en una tabla larga con una fila por estación y por mes, y promediar el año
antes de analizar borra la estacionalidad. El desvío de la temperatura pasa de 5.20 °C a
1.71 °C, y eta cuadrado entre provincia y precipitación pasa de 0.067, que es asociación
débil, a 0.569, que es asociación fuerte. Mismo dato, conclusión opuesta.

`main_entregado.ipynb` conserva la versión original que entregué, con los dos errores, para
poder comparar.

## Actividad 5 — Cuestionario sobre los goles de Messi

Nueve preguntas de opción múltiple, cinco conceptuales y cuatro sobre el dataset
`Lionel Messi Club Goals`. En el notebook dejo de dónde sale cada respuesta y la diapositiva
del teórico que la respalda.

Explorando el dataset apareció un error que no entra en ninguna pregunta: los marcadores de
los partidos de visitante están invertidos, porque vienen escritos como local a visitante.
Por eso el dataset dice que Messi marcó en 254 partidos perdidos, cuando en realidad son 22.
El caso testigo es el 6 a 0 de Barcelona contra Atlético de Madrid, que figura como derrota
con cero goles a favor.

Más detalle en el [README de la actividad](actividad-05/README.md).

## Actividad 6 — Torre de Hanoi con búsqueda A*

Ejercicio de la clase 7, resuelto sobre la plantilla de la cátedra y su biblioteca
`aima_libs`. Implementé A* con una heurística propia, que es la opción de nota máxima.

La heurística razona sobre el disco más grande. Si ya está en la varilla destino no hay que
moverlo, y si no, los discos más chicos tienen que pasar obligatoriamente por la tercera
varilla, lo que cuesta `2^(k-1)` movimientos. Al desplegar esa recursión queda una
heurística que no solo es consistente y admisible sino exacta: coincide con la distancia
real en los 243 estados del problema.

Por eso A* no se desvía del camino óptimo. Resuelve en 31 movimientos, que es el mínimo
teórico, explorando 32 nodos, contra 178 de la heurística que da la cátedra y 233 del costo
uniforme. Subiendo la cantidad de discos se mantiene en `2^n` exacto mientras los otros dos
crecen con el espacio de estados.

Más detalle en el [README de la actividad](actividad-06-hanoi/README.md).

## Herramientas

Python 3.13, con pandas, numpy, matplotlib, seaborn, scipy, scikit-learn y python-pptx.

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn python-pptx jupyter
```

## Autor

Rodeyro, Agustín
