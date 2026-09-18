# Inteligencia Artificial — IUA 2026

Actividades individuales de la materia Inteligencia Artificial.
Una carpeta por actividad, cada una con su notebook ejecutado y sus datos.

## Actividades

| # | Tema | Carpeta | Entregable |
|---|---|---|---|
| 2–3 | EDA del dataset de Pokémon | [`actividad-03-eda-pokemon/`](actividad-03-eda-pokemon/) | Notebook + 3 diapositivas |
| 4 | Dataset del Servicio Meteorológico Nacional | [`actividad-04-smn/`](actividad-04-smn/) | Notebook |
| 5 | Cuestionario sobre los goles de Messi | [`actividad5/`](actividad5/) | Cuestionario + notebook |

## Actividad 3 — EDA del dataset de Pokémon

Análisis exploratorio completo de 800 registros: caracterización del dataset,
detección de outliers por la regla del IQR, y análisis de desafíos y técnicas
aplicables.

Hallazgo principal: `Total` es la suma exacta de las 6 stats y **no tiene ningún
outlier**, aunque sus seis componentes sí — los extremos se compensan porque el juego
reparte un presupuesto fijo de puntos. Los outliers no son de poder, son de perfil.

Detalle completo en el [README de la actividad](actividad-03-eda-pokemon/README.md).

## Actividad 4 — Dataset del SMN

Cruce de las estaciones meteorológicas del SMN con sus estadísticas climatológicas
normales (período 1981-2010), y análisis de la región Pampeana.

Los dos puntos que definen el resultado:

1. **Los nombres de estación no coinciden entre los dos archivos.**
   `estaciones_smn.txt` no lleva tildes y `estadisticas.txt` sí (`CORDOBA AERO` contra
   `CÓRDOBA AERO`), así que un `merge` por nombre exacto descarta 70 de 120 estaciones
   sin avisar. Hay que normalizar los nombres antes de unir.

2. **El nivel de agregación cambia las conclusiones.** Las variables `temp` y `prec_mm`
   viven en una tabla larga con una fila por estación y por mes. Promediar el año antes
   de analizar borra la estacionalidad: el desvío de la temperatura pasa de 5.20 °C a
   1.71 °C, y eta cuadrado entre provincia y precipitación pasa de 0.067 ("asociación
   débil") a 0.569 ("asociación fuerte"). Mismo dato, conclusión opuesta.

`main_entregado.ipynb` conserva la versión original entregada, con ambos errores, para
poder comparar.

## Actividad 5 — Cuestionario sobre los goles de Messi

Nueve preguntas de opción múltiple: cinco conceptuales y cuatro sobre el dataset
`Lionel Messi Club Goals`. El notebook deriva cada respuesta desde el CSV y cita la
diapositiva del teórico que la respalda.

Explorando el dataset apareció un error que no entra en ninguna pregunta: **los
marcadores de los partidos de visitante están invertidos**, porque vienen escritos en
formato local:visitante. Por eso el dataset dice que Messi marcó en 254 partidos
perdidos. Corregido son 22. El caso testigo es el 6-0 de Barcelona contra Atlético de
Madrid, que figura como derrota con cero goles a favor.

Detalle completo en el [README de la actividad](actividad5/README.md).

## Herramientas

Python 3.13 · pandas · numpy · matplotlib · seaborn · scipy · scikit-learn · python-pptx

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn python-pptx jupyter
```

## Autor

Rodeyro, Agustín
