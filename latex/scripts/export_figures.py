import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "latex" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Dados e colunas
df_pb = pd.read_excel(ROOT / "data" / "dadospb.xlsx")
df_rn = pd.read_excel(ROOT / "data" / "dadosrn.xlsx")

col_salario = "Salário médio mensal dos trabalhadores formais"
colunas_pb = [
    "Municípios",
    "IDEB – Anos iniciais do ensino fundamental (Rede pública)",
    "Percentual da população com rendimento nominal mensal per capita de até 1/2 salário mínimo",
    col_salario,
]
colunas_rn = [
    "Municípios",
    "IDEB – Anos iniciais do ensino fundamental (Rede pública)",
    "Percentual da população com rendimento nominal mensal per capita de até 1/2 salário mínimo (%)",
    col_salario,
]

amostra_pb = df_pb[colunas_pb].sample(n=30, random_state=42)
amostra_rn = df_rn[colunas_rn].sample(n=30, random_state=123)

sns.set_theme(style="whitegrid")

# Figura principal vetorial (PDF)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(hspace=0.35, wspace=0.25)

sns.histplot(amostra_pb[col_salario], kde=True, ax=axes[0, 0], color="#4C78A8")
axes[0, 0].set_title("Histograma de Salários (PB)")
axes[0, 0].set_xlabel("Salário médio mensal")
axes[0, 0].set_ylabel("Frequência")

sns.boxplot(x=amostra_pb[col_salario], ax=axes[0, 1], color="#4C78A8")
axes[0, 1].set_title("Boxplot de Salários (PB)")
axes[0, 1].set_xlabel("Salário médio mensal")

sns.histplot(amostra_rn[col_salario], kde=True, ax=axes[1, 0], color="#E45756")
axes[1, 0].set_title("Histograma de Salários (RN)")
axes[1, 0].set_xlabel("Salário médio mensal")
axes[1, 0].set_ylabel("Frequência")

sns.boxplot(x=amostra_rn[col_salario], ax=axes[1, 1], color="#E45756")
axes[1, 1].set_title("Boxplot de Salários (RN)")
axes[1, 1].set_xlabel("Salário médio mensal")

fig.savefig(FIG_DIR / "painel_salarios.pdf", format="pdf", bbox_inches="tight")
fig.savefig(FIG_DIR / "painel_salarios.svg", format="svg", bbox_inches="tight")
plt.close(fig)

print("Figuras vetoriais geradas em:", FIG_DIR)
