# Actividad 5 — Cuestionario de 9 preguntas

Actividad de opción múltiple: 5 preguntas conceptuales (Parte I) y 4 sobre un dataset
a elección (Parte II).

**Dataset elegido:** `Lionel Messi Club Goals (adaptado)` — 704 goles, 23 columnas.

El desarrollo completo está en [`messigoals/main.ipynb`](messigoals/main.ipynb). Las
preguntas conceptuales se demuestran ejecutándolas sobre el mismo CSV en vez de
responderlas de memoria, y cada una cita la diapositiva del teórico de la que sale.

## Respuestas

| # | Pregunta | Respuesta | Fundamento |
|---|---|---|---|
| 1 | Faltantes 25 % con patrón MAR | Imputar con media/mediana considerando el patrón | Deck 05, diap. 21: MAR + franja 10-30 % |
| 2 | Stratified split | Mantiene la misma proporción de clases en train y test | Deck 05, diap. 9 |
| 3 | Split antes de transformar | Evita contaminar el train y las métricas optimistas | Deck 06, diap. 5 |
| 4 | Normalizar antes de KNN | KNN es sensible a la escala | Deck 06, diap. 39 |
| 5 | Solo en train, no en test | Balanceo de clases por oversampling (SMOTE) | Deck 06, diap. 31 y 32 |
| 6 | `Playing_Position` | Limpiar la columna y después codificar | 9 categorías que en realidad son 5 |
| 7 | `Opponent` como feature | Frequency Encoding o Target Encoding | 98 rivales = alta cardinalidad |
| 8 | `Minute_num` por tramos | Discretizar en intervalos de igual longitud | `qcut` aplana los tramos |
| 9 | Target `Has_Assist` | Ligeramente desbalanceado | 69.6 / 30.4, sin nulos |

## Los tres puntos que vale la pena defender

1. **El stratified split no corrige el desbalance, lo conserva.** Es la trampa de la
   pregunta 2. Aplicado sobre `Has_Assist`, el test estratificado replica el 69.6 / 30.4
   original; no lo lleva a 50/50. Corregir el desbalance es oversampling, que es la
   respuesta de otra pregunta.

2. **Discretizar por igual frecuencia no puede responder "en qué tramo marca más".**
   `qcut` pone por construcción la misma cantidad de goles en cada intervalo: los seis
   grupos quedan entre 110 y 123 goles. Con intervalos de igual longitud aparece el
   hallazgo real: el último cuarto de hora concentra 171 goles contra 67 del primero.

3. **Los 214 nulos son de `Goal_assist`, no de `Has_Assist`.** Es la trampa de la
   pregunta 9. `Has_Assist` no tiene ningún nulo. Y los de `Goal_assist` son
   estructurales: faltan porque el gol no tuvo asistencia, y coinciden exactamente con
   las 214 filas donde `Has_Assist` vale 0.

## Hallazgo extra: el dataset tiene los marcadores invertidos

No entra en ninguna pregunta, pero apareció al explorar el CSV y está documentado en el
anexo del notebook.

El dataset afirma que **Messi marcó en 254 partidos perdidos**, el 36 % de sus goles. De
local el equipo gana el 91 % de las veces, pero de visitante el dataset dice que pierde
el 86 %.

La causa es que el marcador viene escrito en formato **local : visitante**, así que en
los partidos de visitante `Goals_For` y `Goals_Against` están dados vuelta. El caso
testigo es Atlético de Madrid 0-6 Barcelona de mayo de 2007, que figura como derrota con
cero goles a favor.

Hay una prueba lógica más fuerte: 188 filas tienen `Score_For` en cero justo después de
que Messi marcara, lo cual es imposible, y las 188 son de visitante.

Corrigiendo la inversión, el reparto pasa a 89 % de victorias y 3 % de derrotas, y los
goles en partidos perdidos bajan de 254 a 22. Las columnas afectadas son `Goals_For`,
`Goals_Against`, `Match_Result`, `Score_For`, `Score_Against` y `Score_Diff`.

## Cómo correrlo

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
jupyter notebook messigoals/main.ipynb
```
