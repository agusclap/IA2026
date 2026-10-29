# Actividad 9 — Detector de SPAM

Ejercicio de la clase 11: detectar SPAM en el dataset Spambase, 4601 correos descritos por
54 atributos de frecuencia de palabras, comparando dos clasificadores.

La entrega es [`01_ejercicio_deteccion_spam.ipynb`]

## Resultado

| Modelo | Precision | Recall | AUC | Falsos positivos | Falsos negativos |
|---|---|---|---|---|---|
| Regresión logística | **0.9383** | 0.8700 | **0.9726** | 33 | 75 |
| Naive Bayes (MultinomialNB) | 0.7828 | **0.9619** | 0.8883 | 154 | 22 |

Sobre un set de testeo de 1381 correos: 804 legítimos y 577 de SPAM.

## Las dos decisiones del ejercicio

**Por qué MultinomialNB.** La consigna pide elegir la implementación más apropiada para
datos de frecuencia de palabras. De las cinco que ofrece scikit-learn, `MultinomialNB` es la
pensada para conteos y frecuencias. Las otras no encajan: `BernoulliNB` espera variables
binarias de presencia o ausencia, `CategoricalNB` espera categorías discretas, y
`GaussianNB` asume que cada atributo sigue una distribución normal, lo cual acá es falso
porque las frecuencias son casi siempre cero y nunca negativas.

**Por qué el Bayes va sin escalado.** No es solo que la consigna lo pida. `MultinomialNB`
necesita valores no negativos para funcionar, y estandarizar genera negativos, así que meter
el escalado rompería el modelo. La regresión logística sí lo lleva, dentro de un `Pipeline`
para que el scaler se ajuste solo con los datos de entrenamiento.

## Qué dicen los resultados

Cada modelo gana en una métrica distinta, y eso no es casualidad: están cometiendo errores
opuestos.

**La regresión logística deja pasar SPAM.** Comete 75 falsos negativos contra 33 falsos
positivos. Se le escapa el 13 % del SPAM, pero solo bloquea el 4 % del correo legítimo.

**Naive Bayes bloquea correo legítimo.** Comete 154 falsos positivos contra 22 falsos
negativos. Casi no se le escapa SPAM, apenas el 4 %, pero manda a la carpeta de SPAM a 154
de los 804 correos legítimos, casi 1 de cada 5.

Por eso Naive Bayes gana en recall y pierde en precision: está marcando SPAM con mucha más
facilidad.

## Cuál error importa más

El **falso positivo**, y por eso conviene la regresión logística.

Los dos errores no cuestan lo mismo. Un falso negativo deja un SPAM en la bandeja de
entrada: molesta, se ve, se borra y listo. Un falso positivo manda un correo real a una
carpeta que casi nadie revisa, así que lo más probable es que no se lea nunca. Si era una
factura o un aviso del banco, el daño no se arregla.

La métrica que penaliza ese error es la precision, y ahí la regresión logística gana por
amplio margen.

Vale aclarar que la decisión depende del contexto. En un sistema donde dejar pasar SPAM sea
peligroso, por ejemplo phishing dirigido a una empresa, la prioridad se invertiría y
convendría maximizar el recall. Qué error tolerar no sale de los datos, sale del problema.

## Cómo correrlo

```bash
pip install pandas scikit-learn matplotlib jupyter
jupyter notebook 01_ejercicio_deteccion_spam.ipynb
```

`spambase.csv` y la carpeta `img/` tienen que quedar al lado del notebook. Todo es
determinista porque el split usa `random_state=42`, así que vuelve a dar los mismos números.
