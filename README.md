# EDA — Dataset de Pokémon

Análisis exploratorio de datos del dataset de Pokémon (800 registros, Kaggle),
realizado para las actividades individuales de la materia **Inteligencia Artificial**
del IUA.

## Contenido

| Archivo | Descripción |
|---|---|
| `main.ipynb` | Notebook con el análisis completo, ejecutado. |
| `Pokemon.csv` | Dataset utilizado (800 × 13). |
| `slides/EDA-Pokemon-Rodeyro.pptx` | Las 3 diapositivas de la entrega. |
| `slides/graficos.py` | Genera los gráficos del deck. |
| `slides/armar_pptx.py` | Genera el `.pptx` a partir de esos gráficos. |

## Análisis realizado

**Actividad 2 — EDA base**
- Identificación de tipos de variables.
- Estadística descriptiva.
- Relaciones entre variables (matriz de correlación).
- Visualizaciones: histograma, heatmap y gráfico de barras.

**Actividad 3 — Caracterización, outliers y técnicas**
- Características generales: tamaño, tipos de información, completitud y duplicados.
- Detección de outliers por la regla del IQR (k = 1.5) e identificación de cada caso.
- Análisis de asimetría (*skewness*) por variable.
- Desafíos a priori del dataset y técnicas aplicables.

## Hallazgos principales

1. **Los 386 nulos de `Type 2` no son datos faltantes.** Corresponden a Pokémon
   mono-tipo: la ausencia de un segundo tipo *es* la información. Un `dropna()`
   eliminaría el 48 % del dataset sin motivo.

2. **`#` no es una clave primaria.** Hay 800 filas pero solo 721 números distintos:
   las 49 formas Mega comparten el número de Pokédex con su forma base.

3. **`Total` es una columna derivada.** Es la suma exacta de las 6 stats en las 800
   filas, lo que implica multicolinealidad perfecta si se usa junto a ellas.

4. **Los outliers no son errores, son diseño.** 52 Pokémon (6.5 %) son outliers en al
   menos una stat, pero `Total` no tiene ninguno: los extremos se compensan entre sí
   porque el juego reparte un presupuesto fijo de puntos. Shedinja (HP = 1) es el único
   outlier inferior y responde a una mecánica deliberada del juego. Los legendarios
   están 4.5× sobrerrepresentados entre los outliers (36.5 % vs 8.1 %), por lo que
   **el outlier es la señal, no el ruido**: no se eliminan.

## Herramientas

Python 3.13 · pandas · numpy · matplotlib · seaborn · python-pptx

## Reproducir

```bash
pip install pandas numpy matplotlib seaborn python-pptx
jupyter lab main.ipynb          # el análisis
python slides/graficos.py       # regenera los gráficos
python slides/armar_pptx.py     # regenera las diapositivas
```

## Autor

Rodeyro, Agustín
