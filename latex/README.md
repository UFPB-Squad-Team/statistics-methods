# Relatório LaTeX

Este diretório contém uma versão pronta do relatório em LaTeX com:

- texto estruturado e resultados principais já preenchidos;
- tabelas separadas em arquivos próprios;
- suporte a figuras vetoriais (PDF/SVG).

## Estrutura

- `main.tex`: documento principal
- `tables/tab_descritiva_salario.tex`: tabela descritiva
- `tables/tab_inferencia.tex`: tabela de inferência
- `scripts/export_figures.py`: gera gráficos vetoriais a partir dos dados
- `figures/`: saída dos gráficos vetoriais

## Gerar figuras vetoriais

Na raiz do projeto:

```bash
/Users/brennohdev/development/statistics-method/.venv/bin/python latex/scripts/export_figures.py
```

## Compilar PDF

Dentro de `latex/`:

```bash
pdflatex main.tex
pdflatex main.tex
```

(duas passagens para atualizar referências)
