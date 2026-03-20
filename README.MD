# Projeto de Métodos Estatísticos

Análise estatística comparativa entre municípios da **Paraíba (PB)** e do **Rio Grande do Norte (RN)**, com foco em indicadores educacionais e socioeconômicos.

## 📌 Visão geral

Este projeto organiza um estudo acadêmico em formato de notebook para:

- construir amostras aleatórias simples de municípios;
- calcular estatísticas descritivas;
- analisar distribuições com gráficos;
- realizar testes de hipóteses (proporções e médias);
- apresentar os resultados em estrutura de paper (introdução, método, resultados e conclusão).

Fonte principal dos dados: [IBGE — Cidades e Estados](https://www.ibge.gov.br/cidades-e-estados.html?view=municipio)

---

## 👥 Integrantes

- Brenno Henrique Alves da Silva Costa
- Deivyson Henrique Gomes Ribeiro
- Gustavo Henrique
- Italo
- Samuel

---

## 🧰 Tecnologias e dependências

- Python 3.11+
- Poetry
- pandas
- numpy
- openpyxl
- ipykernel (desenvolvimento/notebook)

As dependências estão definidas em [pyproject.toml](pyproject.toml).

---

## 📁 Estrutura do projeto

- [METODOS-ESTATISTICOS-PROJETO.ipynb](METODOS-ESTATISTICOS-PROJETO.ipynb) — notebook principal (estrutura do paper + análises)
- [data/](data/) — planilhas de entrada e amostras geradas
- [pyproject.toml](pyproject.toml) — configuração do projeto Python
- [poetry.lock](poetry.lock) — lock de dependências

---

## 🚀 Como iniciar o ambiente

### 1) Pré-requisitos

- Python 3.11 ou superior
- Poetry instalado

Se não tiver Poetry:

```bash
pip install poetry
```

### 2) Instalar dependências

Na raiz do projeto:

```bash
poetry install
```

### 3) Ativar o ambiente virtual

Opção recomendada (Poetry):

```bash
poetry shell
```

Alternativa (ativação direta da venv local):

```bash
source .venv/bin/activate
```

> No Windows (PowerShell):
>
> ```powershell
> .venv\Scripts\Activate.ps1
> ```

### 4) Executar o notebook

Com o ambiente ativo:

```bash
jupyter notebook
```

ou

```bash
jupyter lab
```

Abra o arquivo [METODOS-ESTATISTICOS-PROJETO.ipynb](METODOS-ESTATISTICOS-PROJETO.ipynb).

---

## 🗂️ Dados esperados

Garanta que as planilhas base estejam na pasta [data/](data/), por exemplo:

- `data/dadospb.xlsx`
- `data/dadosrn.xlsx`

As amostras podem ser exportadas no próprio notebook para arquivos como:

- `data/Amostra1_Paraiba_30_municipios.xlsx`
- `data/Amostra2_RN_30_municipios.xlsx`

---

## ✅ Boas práticas de execução

1. Execute as células na ordem do notebook.
2. Mantenha o mesmo `random_state` para reprodutibilidade da amostragem.
3. Revise nomes de colunas das planilhas antes da execução.
4. Salve versões finais com resultados e texto interpretativo.

---

## 📚 Objetivo acadêmico

O notebook foi estruturado para que a leitura dos resultados seja clara mesmo para quem não domina Python, mantendo:

- **reprodutibilidade** (código executável),
- **clareza textual** (explicação e insights),
- **formato acadêmico** (pronto para migração para LaTeX, se necessário).
