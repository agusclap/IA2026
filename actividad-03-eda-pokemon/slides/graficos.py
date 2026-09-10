"""Genera los graficos de las diapositivas con el tema oscuro del deck."""
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

matplotlib.use("Agg")

AQUI = Path(__file__).parent
BG = "#101B33"
NARANJA = "#F97316"
GRIS = "#94A3B8"
BLANCO = "#F8FAFC"
AZUL = "#38BDF8"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": BLANCO,
    "axes.labelcolor": GRIS,
    "xtick.color": GRIS,
    "ytick.color": GRIS,
    "axes.edgecolor": "#2B3B5C",
    "grid.color": "#1E2C49",
    "font.size": 13,
})

df = pd.read_csv(AQUI.parent / "Pokemon.csv")
stats = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

# ---------- Grafico 1: completitud por columna (diapo 2) ----------
completos = df.notna().sum().sort_values()
colores = [NARANJA if c == "Type 2" else "#3E5580" for c in completos.index]

fig, ax = plt.subplots(figsize=(8, 5.2))
ax.barh(completos.index, completos.values, color=colores)
ax.axvline(800, color=GRIS, ls="--", lw=1, alpha=0.6)
ax.text(795, len(completos) - 0.4, "800 filas", color=GRIS, fontsize=11, ha="right")
ax.set_xlim(0, 900)
ax.set_xlabel("Registros no nulos")
ax.set_title("Completitud por columna", color=BLANCO, fontsize=15, pad=12, loc="left")
ax.annotate(
    "414 / 800  →  386 mono-tipo",
    xy=(420, 0),
    xytext=(455, 1.45),
    color=NARANJA, fontsize=12, fontweight="bold", va="center",
    arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.5,
                    connectionstyle="arc3,rad=-0.2"),
)
ax.set_ylim(-0.8, len(completos) - 0.2)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(AQUI / "completitud.png", dpi=200)
plt.close(fig)

# ---------- Grafico 2: boxplot de stats (diapo 3) ----------
fig, ax = plt.subplots(figsize=(8.6, 5.2))
sns.boxplot(
    data=df[stats], ax=ax,
    color="#3E5580", linewidth=1.3,
    flierprops=dict(marker="o", markersize=5, markerfacecolor=NARANJA,
                    markeredgecolor=NARANJA, alpha=0.8),
    medianprops=dict(color=BLANCO, linewidth=2),
    whiskerprops=dict(color=GRIS), capprops=dict(color=GRIS),
    boxprops=dict(edgecolor=GRIS),
)
ax.set_ylabel("Valor de la stat")
ax.set_title("Outliers por stat (regla del IQR, k = 1.5)",
             color=BLANCO, fontsize=15, pad=12, loc="left")
ax.grid(axis="y", alpha=0.25)
ax.set_axisbelow(True)
ax.annotate(
    "Shedinja\nHP = 1",
    xy=(0, 1), xytext=(0.75, -32),
    color=AZUL, fontsize=11.5, fontweight="bold", ha="center",
    arrowprops=dict(arrowstyle="->", color=AZUL, lw=1.6),
)
ax.annotate(
    "Blissey / Chansey\nHP 255 y 250",
    xy=(0.06, 252), xytext=(1.15, 243),
    color=NARANJA, fontsize=11.5, fontweight="bold",
    arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.6),
)
ax.set_ylim(-45, 285)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(AQUI / "boxplot.png", dpi=200)
plt.close(fig)

print("OK -> completitud.png y boxplot.png")
