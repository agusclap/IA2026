# Actividad 5 — Cuestionario de 9 preguntas

Actividad de opción múltiple: cinco preguntas conceptuales y cuatro sobre un dataset a
elección. Elegí `Lionel Messi Club Goals (adaptado)`, que tiene 704 goles y 23 columnas.

El desarrollo está en [`messigoals/main.ipynb`](messigoals/main.ipynb). Las preguntas
conceptuales las probé corriéndolas sobre el mismo CSV en vez de contestarlas de memoria, y
en cada una dejo la diapositiva del teórico de donde sale.

## Respuestas

| # | Pregunta | Respuesta | De dónde sale |
|---|---|---|---|
| 1 | Faltantes 25 % con patrón MAR | Imputar con media o mediana considerando el patrón | Deck 05, diap. 21: MAR + franja 10-30 % |
| 2 | Stratified split | Mantiene la misma proporción de clases en train y test | Deck 05, diap. 9 |
| 3 | Split antes de transformar | Evita contaminar el train y las métricas optimistas | Deck 06, diap. 5 |
| 4 | Normalizar antes de KNN | KNN es sensible a la escala | Deck 06, diap. 39 |
| 5 | Solo en train, no en test | Balanceo de clases por oversampling | Deck 06, diap. 31 y 32 |
| 6 | `Playing_Position` | Limpiar la columna y después codificar | 9 categorías que en realidad son 5 |
| 7 | `Opponent` como feature | Frequency o Target Encoding | 98 rivales, alta cardinalidad |
| 8 | `Minute_num` por tramos | Discretizar en intervalos de igual longitud | `qcut` aplana los tramos |
| 9 | Target `Has_Assist` | Ligeramente desbalanceado | 69.6 contra 30.4, sin nulos |

## Las tres que más se prestan a error

La 2 es la más tramposa. El stratified split no corrige el desbalance, lo conserva. Sobre
`Has_Assist`, el test estratificado replica el 69.6 / 30.4 original en vez de llevarlo a
mitad y mitad. Corregir el desbalance es oversampling, que justamente es la respuesta de
otra pregunta.

En la 8, discretizar por igual frecuencia directamente no puede responder en qué tramo marca
más, porque `qcut` pone por construcción la misma cantidad de goles en cada intervalo y los
seis grupos quedan entre 110 y 123. Con intervalos de igual longitud aparece el dato real:
el último cuarto de hora concentra 171 goles contra 67 del primero.

En la 9 la trampa son los nulos. Los 214 son de `Goal_assist`, el nombre del asistidor, no
de `Has_Assist`, que no tiene ninguno. Y encima son estructurales, porque faltan cuando el
gol no tuvo asistencia: verifiqué que coinciden exactamente con las 214 filas donde
`Has_Assist` vale 0.

## Un error del dataset que encontré de paso

No entra en ninguna pregunta, pero está documentado en el anexo del notebook.

El dataset dice que Messi marcó en 254 partidos perdidos, o sea el 36 % de sus goles. De
local el equipo gana el 91 % de las veces, pero de visitante el dataset dice que pierde el
86 %, lo cual no cierra.

La causa es que el marcador viene escrito como local a visitante, así que en los partidos de
visitante `Goals_For` y `Goals_Against` están dados vuelta. El caso testigo es Atlético de
Madrid 0-6 Barcelona de mayo de 2007, que figura como derrota con cero goles a favor.

Hay una prueba más fuerte todavía: 188 filas tienen `Score_For` en cero justo después de que
Messi marcara, lo cual es imposible, y las 188 son de visitante.

Corrigiendo la inversión queda 89 % de victorias y 3 % de derrotas, y los goles en partidos
perdidos bajan de 254 a 22. Las columnas afectadas son `Goals_For`, `Goals_Against`,
`Match_Result`, `Score_For`, `Score_Against` y `Score_Diff`.

## Cómo correrlo

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
jupyter notebook messigoals/main.ipynb
```
