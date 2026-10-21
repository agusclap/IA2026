# Actividad 8 — Regresión sobre el dataset Swiss

Ejercicio de la clase 10: predecir la tasa de fertilidad de 47 provincias suizas a partir de
sus atributos socioeconómicos, entrenando y comparando dos modelos de regresión.

La entrega es
[`01_ejercicio_swiss_regresion.ipynb`](01_ejercicio_swiss_regresion.ipynb), que es la
plantilla de la cátedra. Completé únicamente las secciones marcadas con
`##### COMPLETAR AQUI LO PEDIDO`, más el nombre, la tabla comparativa y la justificación.
No agregué celdas ni toqué nada fuera de eso.

## Resultado

| Modelo | MAE | MSE | R² | Atributos usados |
|---|---|---|---|---|
| Regresión lineal múltiple | 6.0937 | 64.4572 | 0.5744 | 5 de 5 |
| Lasso (L1), alpha 2.1811 | 5.9954 | 64.2943 | 0.5755 | 4 de 5 |

Lasso gana en las tres métricas y además usa un atributo menos.

## Qué hice

**Primera parte, regresión lineal múltiple.** Un pipeline con `StandardScaler` y
`LinearRegression`, entrenado con el set de entrenamiento y evaluado sobre el de testeo.

Poner el escalado adentro del pipeline no es prolijidad: hace que el scaler calcule su media
y su desvío solo con los datos de entrenamiento y después aplique esos mismos valores al
test. Es la regla del deck 06, calcular en train y aplicar en test.

**Segunda parte, modelo regularizado.** Elegí **Lasso**, que es lo que pide la pista. La
consigna quiere selección automática de variables, y esa es la diferencia entre las dos
penalizaciones: L1 penaliza la suma de los valores absolutos de los coeficientes y puede
llevarlos a cero exacto, dejando la variable afuera; L2 penaliza los cuadrados, los achica
pero nunca los anula.

El pipeline combina el escalado con `LassoCV(alphas=alphas, cv=3)`, que prueba los 500
valores del array dado y se queda con el que minimiza el MSE promedio en la validación
cruzada de 3 folds. El alpha elegido fue 2.1811.

## Por qué Lasso tuvo mejor desempeño

Las tres métricas lo favorecen, pero por poco. Con solo 24 observaciones de testeo esas
diferencias son demasiado chicas para decidir por ahí, así que el argumento de peso es otro.

**Eliminó una variable.** Llevó el coeficiente de `Agriculture` a cero exacto. Y tiene
sentido que haya caído esa: correlaciona -0.69 con `Examination` y -0.64 con `Education`,
así que lo que aportaba ya estaba contenido en esas dos.

**Achicó los coeficientes.** En el modelo sin regularizar aparecen valores grandes y de
signos opuestos, `Education` en -9.93 contra `Catholic` en 7.97. En Lasso el mayor es 3.20.

| Atributo | Lineal | Lasso |
|---|---|---|
| Agriculture | -5.2575 | 0.0000 |
| Examination | 3.4068 | -1.7624 |
| Education | -9.9275 | -2.4049 |
| Catholic | 7.9742 | 1.7196 |
| Infant.Mortality | 3.5841 | 3.2004 |

Eso importa porque el modelo lineal ajusta 5 coeficientes con apenas 23 observaciones de
entrenamiento, y según el deck 09 los parámetros entrenables tienen que ser muchos menos que
las observaciones. Coeficientes grandes y opuestos son la señal típica de un modelo que se
apoya en el ruido del entrenamiento. Notar además que `Examination` cambia de signo entre
los dos modelos, otro síntoma de inestabilidad por la correlación entre atributos.

## Una observación que no entra en la consigna

Por curiosidad probé también Ridge con el mismo pipeline y los mismos alphas. Sobre este
split da mejores métricas que los dos: MAE 5.2797, MSE 51.9024 y R² 0.6573.

No lo entregué porque la consigna pide explícitamente el modelo que hace selección
automática de variables, y Ridge no puede: no anula ningún coeficiente. Vale aclarar además
que el alpha que eligió fue 10.0, que es el extremo del array dado, o sea que quería todavía
más regularización de la que el rango permitía.

## Cómo correrlo

```bash
pip install pandas scikit-learn jupyter
jupyter notebook 01_ejercicio_swiss_regresion.ipynb
```

El archivo `swiss.csv` tiene que quedar al lado del notebook. Todo el notebook es
determinista, porque el split usa `random_state=42` y la validación cruzada de `LassoCV` no
mezcla, así que vuelve a dar exactamente los mismos números.
