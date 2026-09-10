"""Genera las 3 diapositivas de la actividad en formato .pptx."""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

AQUI = Path(__file__).parent

FONDO = RGBColor(0x10, 0x1B, 0x33)
TARJETA = RGBColor(0x1B, 0x29, 0x42)
NARANJA = RGBColor(0xF9, 0x73, 0x16)
BLANCO = RGBColor(0xF8, 0xFA, 0xFC)
GRIS = RGBColor(0x94, 0xA3, 0xB8)
BORDE = RGBColor(0x2B, 0x3B, 0x5C)
FUENTE = "Segoe UI"

REPO = "github.com/agusclap/actividad-eda-pokemon"
AUTOR = "Rodeyro, Agustín"
ACTIVIDAD = "Actividad 3 · Inteligencia Artificial"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
ANCHO = 13.333


def nueva_slide():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    fondo = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0,
                               prs.slide_width, prs.slide_height)
    fondo.fill.solid()
    fondo.fill.fore_color.rgb = FONDO
    fondo.line.fill.background()
    fondo.shadow.inherit = False
    return s


def caja(slide, x, y, w, h, relleno=TARJETA, borde=None, radio=0.035):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(x), Inches(y), Inches(w), Inches(h))
    sh.adjustments[0] = radio
    sh.fill.solid()
    sh.fill.fore_color.rgb = relleno
    if borde is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = borde
        sh.line.width = Pt(1.5)
    sh.shadow.inherit = False
    return sh


def texto(slide, x, y, w, h, lineas, anclaje=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anclaje
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, ln in enumerate(lineas):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = ln.get("align", PP_ALIGN.LEFT)
        if ln.get("antes"):
            p.space_before = Pt(ln["antes"])
        if ln.get("despues"):
            p.space_after = Pt(ln["despues"])
        p.line_spacing = ln.get("interlineado", 1.0)
        r = p.add_run()
        r.text = ln["t"]
        r.font.size = Pt(ln.get("size", 14))
        r.font.bold = ln.get("bold", False)
        r.font.color.rgb = ln.get("color", BLANCO)
        r.font.name = FUENTE
    return tb


def notas(slide, contenido):
    """Carga el guion del orador (visible solo en la vista Moderador)."""
    tf = slide.notes_slide.notes_text_frame
    tf.text = contenido.strip()


def pie(slide, arriba=False):
    y = 0.62 if arriba else 7.02
    texto(slide, ANCHO - 5.6, y, 5.0, 0.3,
          [{"t": REPO, "size": 10, "color": GRIS, "align": PP_ALIGN.RIGHT}])


# ============ DIAPOSITIVA 1 — CARÁTULA ============
s1 = nueva_slide()
texto(s1, 0.9, 1.5, 7.5, 0.35,
      [{"t": "IUA", "size": 15, "bold": True, "color": NARANJA}])
texto(s1, 0.9, 2.0, 7.6, 2.0, [
    {"t": "EDA — Dataset Pokémon", "size": 48, "bold": True, "interlineado": 1.05},
    {"t": "800 registros · 6 generaciones", "size": 23, "color": GRIS, "antes": 10},
])
texto(s1, 0.9, 4.55, 7.5, 1.2, [
    {"t": ACTIVIDAD, "size": 15, "color": GRIS},
    {"t": AUTOR, "size": 20, "bold": True, "antes": 14},
])

caja(s1, 8.7, 1.75, 3.75, 3.9)
texto(s1, 9.15, 2.15, 2.9, 3.2, [
    {"t": "EL DATASET EN NÚMEROS", "size": 11, "bold": True, "color": NARANJA},
    {"t": "800", "size": 30, "bold": True, "antes": 16},
    {"t": "filas × 13 columnas", "size": 12, "color": GRIS},
    {"t": "18", "size": 30, "bold": True, "antes": 14},
    {"t": "tipos primarios", "size": 12, "color": GRIS},
    {"t": "65", "size": 30, "bold": True, "antes": 14},
    {"t": "legendarios (8,1 %)", "size": 12, "color": GRIS},
])
pie(s1)
notas(s1, """
[30 segundos — no te quedes acá]

"Bueno, buenas. Yo elegí el dataset de Pokémon, lo saqué de Kaggle. Son 800 filas,
13 columnas, y cubre las primeras seis generaciones."

"Voy a mostrar dos cosas: primero cómo está armado el dataset, porque tiene un par de
cosas raras que no se ven a simple vista; y después el análisis de outliers, que fue lo
que más me sorprendió."

[Pasá a la siguiente]
""")

# ============ DIAPOSITIVA 2 — EL DATASET ============
s2 = nueva_slide()
texto(s2, 0.6, 0.45, 12.1, 0.7,
      [{"t": "El dataset y sus tres rarezas estructurales", "size": 30, "bold": True}])

caja(s2, 0.6, 1.35, 5.55, 4.11)
texto(s2, 1.0, 1.72, 4.8, 3.4, [
    {"t": "FICHA TÉCNICA", "size": 11, "bold": True, "color": NARANJA},
    {"t": "Pokémon (Kaggle) — 800 × 13 · 179 KB", "size": 14, "antes": 14},
    {"t": "Entra entero en memoria: no requiere muestreo, pero son pocas filas para modelos complejos.",
     "size": 11.5, "color": GRIS, "antes": 5, "interlineado": 1.2},
    {"t": "6 numéricas   stats base (HP … Speed)", "size": 12.5, "antes": 14},
    {"t": "1 derivada   Total", "size": 12.5, "antes": 6},
    {"t": "3 categóricas   Type 1, Type 2, Generation", "size": 12.5, "antes": 6},
    {"t": "1 booleana   Legendary", "size": 12.5, "antes": 6},
    {"t": "2 identificadores   #, Name", "size": 12.5, "antes": 6},
    {"t": "0 duplicados exactos · 0 nulos reales", "size": 13, "bold": True,
     "color": NARANJA, "antes": 16},
])

s2.shapes.add_picture(str(AQUI / "completitud.png"),
                      Inches(6.45), Inches(1.35), width=Inches(6.28))

caja(s2, 0.6, 5.68, 12.13, 1.42, relleno=FONDO, borde=NARANJA)
texto(s2, 0.95, 5.88, 11.5, 1.1, [
    {"t": "⚠  Hallazgo clave", "size": 13, "bold": True, "color": NARANJA},
    {"t": "1.  Los 386 nulos de Type 2 no son datos faltantes: son Pokémon mono-tipo. Un dropna() borraría el 48 % del dataset.",
     "size": 11.5, "antes": 7, "interlineado": 1.15},
    {"t": "2.  # no es clave primaria — 800 filas pero 721 números: las 49 formas Mega comparten número con su forma base.",
     "size": 11.5, "antes": 3, "interlineado": 1.15},
    {"t": "3.  Total es una columna derivada: suma exacta de las 6 stats en las 800 filas → multicolinealidad perfecta.",
     "size": 11.5, "antes": 3, "interlineado": 1.15},
])
pie(s2, arriba=True)
notas(s2, """
[3 a 4 minutos]

— ARRANCÁ POR LO BÁSICO —
"Primero lo general: son 800 filas por 13 columnas, ocupa 179 KB. O sea que es chiquito,
entra entero en memoria sin ningún problema."

"De las columnas, seis son las stats del Pokémon —vida, ataque, defensa y las dos
especiales, más velocidad—. Después está Total, tres categóricas, una booleana que dice
si es legendario, y dos que son identificadores."

"Lo primero que hice fue buscar problemas de calidad. Y la verdad que no encontré: no hay
filas duplicadas, no hay nombres repetidos. Está limpio."

— EL GANCHO (hacé una pausa acá) —
"Pero cuando me puse a mirar bien cómo está construido, aparecieron tres cosas."

— RAREZA 1 (señalá la barra naranja del gráfico) —
"La primera es esta barra de acá. Type 2 tiene 386 nulos, casi la mitad del dataset. Al
principio pensé «bueno, acá hay un problema de datos faltantes»."

"Pero no. Esos 386 son Pokémon que tienen un solo tipo. O sea, el nulo no es que falte el
dato, es que no existe un segundo tipo."

"Y esto importa, porque si yo hacía un dropna para limpiar, me borraba el 48 % del dataset
sin ningún motivo. Lo que corresponde es rellenarlo con una categoría que diga «None»."

— RAREZA 2 —
"La segunda: el número de Pokédex no sirve como identificador único. Hay 800 filas pero
solo 721 números distintos."

"¿Por qué? Porque las Mega evoluciones se quedaron con el número de la forma original.
Por ejemplo, Charizard, Mega Charizard X y Mega Charizard Y son los tres el número 6."

— RAREZA 3 (la que más te costó ver) —
"Y la tercera, que es la que más me costó darme cuenta: la columna Total no es un dato
nuevo, es la suma de las otras seis. Me fijé fila por fila y se cumple en las 800, sin una
sola excepción."

"Esto me explicó algo que había visto en el trabajo anterior y no entendía: en la matriz
de correlación, Total correlacionaba fuerte con todas las stats, entre 0,6 y 0,75. Y no es
que haya una relación interesante ahí — es simplemente que es la suma."

"Si después quisiera armar un modelo, usar Total junto con las seis stats sería un
problema, porque es información repetida."

[Pasá a la siguiente]
""")

# ============ DIAPOSITIVA 3 — OUTLIERS ============
s3 = nueva_slide()
texto(s3, 0.6, 0.45, 12.1, 0.7,
      [{"t": "Outliers: anomalías estadísticas, no errores", "size": 30, "bold": True}])

caja(s3, 0.6, 1.35, 5.55, 1.93)
texto(s3, 1.0, 1.60, 4.75, 1.6, [
    {"t": "DETECCIÓN — regla del IQR (k = 1,5)", "size": 11, "bold": True, "color": NARANJA},
    {"t": "52 Pokémon (6,5 %) son outliers en al menos una stat; ninguna supera el 2,4 %.",
     "size": 11.5, "antes": 9, "interlineado": 1.18},
    {"t": "Total: 0 outliers, pese a que sus 6 componentes sí tienen. Los extremos se compensan (Shuckle: 230 de defensa, 5 de speed).",
     "size": 11.5, "color": NARANJA, "antes": 7, "interlineado": 1.18},
])

caja(s3, 0.6, 3.53, 5.55, 1.93)
texto(s3, 1.0, 3.78, 4.75, 1.6, [
    {"t": "NATURALEZA — ninguno es un error de carga", "size": 11, "bold": True, "color": NARANJA},
    {"t": "Shedinja (HP = 1) es el único outlier inferior y responde a un diseño deliberado del juego, no a un dato mal cargado.",
     "size": 11.5, "antes": 9, "interlineado": 1.18},
    {"t": "El 60 % son legendarios o Megas: pasan del 8,1 % del dataset al 36,5 % de los outliers (4,5×).",
     "size": 11.5, "antes": 7, "interlineado": 1.18},
])

s3.shapes.add_picture(str(AQUI / "boxplot.png"),
                      Inches(6.45), Inches(1.35), width=Inches(6.28))

caja(s3, 0.6, 5.68, 12.13, 1.42, relleno=FONDO, borde=NARANJA)
texto(s3, 0.95, 5.88, 11.5, 1.1, [
    {"t": "✓  Decisión: no se eliminan", "size": 13, "bold": True, "color": NARANJA},
    {"t": "El outlier es la señal, no el ruido: descartarlos borraría 19 de los 65 legendarios (29 % de la clase minoritaria).",
     "size": 11.5, "antes": 7, "interlineado": 1.15},
    {"t": "Técnicas si se modelara:  RobustScaler (mediana + IQR) en vez de StandardScaler  ·  split agrupado por # para evitar fuga",
     "size": 11.5, "antes": 3, "interlineado": 1.15},
    {"t": "entre una forma base y su Mega  ·  stratify + métricas F1 / recall por el desbalance 8 / 92.",
     "size": 11.5, "antes": 0, "interlineado": 1.15},
])
pie(s3, arriba=True)
notas(s3, """
[4 a 5 minutos — es la diapo que más pesa]

— DETECCIÓN —
"Bueno, y acá viene la parte que más me interesó."

"Para los outliers usé la regla del IQR. La idea es: agarro el rango entre el primer y el
tercer cuartil, lo multiplico por 1,5, y todo lo que quede afuera de eso lo marco como
outlier. Es el criterio estándar, el mismo que usa el boxplot para dibujar los puntitos."

"Me dieron 52 Pokémon, que es el 6,5 %. Y ninguna stat sola pasa del 2,4 %, así que ahí
ya descarté que hubiera errores de carga."

— EL REMATE (bajá la velocidad, es lo más importante) —
"Pero acá está lo raro, y es lo que me gustaría que se lleven: Total no tiene ni un
outlier. Cero. Aunque las seis stats que lo forman sí tienen."

"Al principio pensé que me había equivocado en el cálculo. Pero cuando fui a ver quiénes
eran, entendí."

"El caso que lo explica es Shuckle. Tiene 230 de defensa y 230 de defensa especial: son
los dos valores más altos de todo el dataset. Pero tiene 5 de velocidad y 10 de ataque. Y
cuando sumás todo te da 505, que es un Pokémon totalmente normal."

"O sea, los outliers de este dataset no son Pokémon más poderosos. Son Pokémon
desbalanceados. El juego reparte una cantidad fija de puntos, y si sos muy bueno en algo
lo pagás siendo muy malo en otra cosa."

— NATURALEZA (quiénes son) —
"Después me puse a ver quiénes eran, porque eso es lo que decide si los saco o no."

"El caso más extremo es Shedinja, que tiene 1 de vida. Es el único que queda por debajo
del límite en las 800 filas y en las seis stats. Y cuando lo busqué, resulta que no es un
error: en el juego tiene una habilidad que lo hace casi invulnerable, entonces le pusieron
1 de vida a propósito, para compensar."

"Me pareció interesante eso: el dato más raro de todo el dataset está puesto ahí a
propósito."

— LA DECISIÓN —
"Y por eso decidí no eliminarlos. Por dos razones."

"Una, que ya la dije: no son errores, son casos reales."

"Y la otra, que me parece más fuerte: el 36,5 % de los outliers son legendarios, cuando en
el dataset entero los legendarios son el 8,1 %. O sea que están sobrerrepresentados cuatro
veces y media. Ser extremo es justamente lo que hace que un Pokémon sea legendario."

"Si yo los borraba, me quedaba sin 19 de los 65 legendarios. Casi un tercio. Y en un
dataset que ya venía desbalanceado."

"Así que acá el outlier no es ruido, es la señal."

— CIERRE —
"Y para cerrar: lo que aprendí de este dataset es que no tiene problemas de calidad, tiene
problemas de estructura. No hay datos mal cargados. Lo que hay es información repetida,
categorías con muy pocos casos, una clase desbalanceada, y filas que son casi duplicadas
entre sí."

"Por eso las técnicas que propondría son: escalar con RobustScaler, que usa la mediana en
vez del promedio; separar train y test agrupando por número de Pokédex, para que un
Pokémon y su Mega no queden de lados distintos; y usar F1 o recall en vez de accuracy, por
el desbalance."

"Eso es todo. Gracias."
""")

salida = AQUI / "EDA-Pokemon-Rodeyro.pptx"
prs.save(str(salida))
print("OK ->", salida)
