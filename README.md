## Links de entrega

- **Link do repositório GitHub:** https://github.com/cesarmontenegrosilva/fiap-aiscientist-fase1.git)
- **Link do vídeo executivo (até 5 min):** [INSERIR_LINK_DO_VIDEO_AQUI]

# NPS Preditivo — Fase 1

Este repositório implementa uma solução de análise e modelagem preditiva para antecipar o `nps_score` de clientes de um e-commerce a partir de dados operacionais de pedido, logística, atendimento e recompra.

## Objetivo do negócio

Identificar, antes da aplicação formal da pesquisa de NPS, quais fatores operacionais aumentam a chance de um cliente se tornar promotor ou detrator. A solução apoia decisões de logística, atendimento, CRM, produto e gestão da experiência do cliente.

## Estrutura do projeto

```text
nps_predictivo_case/
├── app/                         # Dashboard Streamlit opcional
├── data/
│   ├── raw/                     # Base original
│   └── processed/               # Dados tratados e previsões de amostra
├── models/                      # Modelos treinados em formato .pkl
├── notebooks/                   # Notebook principal de EDA e modelagem
├── reports/
│   ├── figures/                 # Gráficos gerados
│   └── tables/                  # Tabelas de métricas e resumo
├── slides/                      # Apresentação executiva
├── src/                         # Scripts reutilizáveis
├── README.md
└── requirements.txt
```

## Variável-alvo

A variável-alvo é `nps_score`, tratada como variável contínua de 0 a 10. A modelagem principal é de regressão. Para análise executiva, também foram criadas categorias de leitura:

- 0 a 6: detrator;
- 7 a 8: neutro;
- 9 a 10: promotor.

## Modelos utilizados

1. **Regressão tradicional**: Ridge Regression, Random Forest Regressor e Gradient Boosting Regressor.
2. **Regressão quantílica**: modelos q=0.10, q=0.50 e q=0.90 para estimar uma faixa provável de NPS e apoiar leitura de risco.

## Resultados principais

Os resultados completos estão em `reports/tables/metricas_modelos.csv`.

| Modelo                                 |   MAE |  RMSE |    R² |
| -------------------------------------- | ----: | ----: | ----: |
| Ridge Regression                       | 1.187 | 1.493 | 0.647 |
| Random Forest Regressor                | 1.247 | 1.558 | 0.616 |
| Gradient Boosting Regressor            | 1.221 | 1.523 | 0.633 |
| Quantile Regression - mediana (q=0.50) | 1.236 | 1.543 | 0.623 |

## Principais insights de negócio

- Atraso na entrega é o principal fator crítico para queda no NPS.
- O ponto de ruptura aparece logo a partir de 1 dia de atraso; atrasos de 2 a 3 dias tornam o cliente majoritariamente detrator.
- Reclamações e contatos com atendimento reduzem fortemente a satisfação.
- CSAT interno e recompra em 30 dias são fortes sinais positivos, mas devem ser usados com cuidado para evitar vazamento temporal se forem coletados depois do NPS.
- A regressão quantílica ajuda a priorizar clientes com maior incerteza ou maior risco de queda.

## Como reproduzir

```bash
python -m venv .venv
Windows: .venv\Scripts\activate
#source .venv/bin/activate
pip install -r requirements.txt

python src/train_model.py
streamlit run app/streamlit_app.py
```

## Arquivos principais

- `notebooks/01_eda_modelagem_nps.ipynb`: EDA, modelagem e interpretação.
- `src/train_model.py`: pipeline reproduzível de treino e avaliação.
- `app/streamlit_app.py`: dashboard executivo/interativo.
- `reports/figures/`: gráficos usados na apresentação.
- `slides/NPS_Apresentacao_Executiva.pptx`: deck executivo para gestores.

## Limitações e riscos

- O NPS pode ser influenciado por fatores não observados na base, como expectativa do cliente, qualidade percebida do produto e histórico anterior de compras.
- Algumas variáveis podem gerar vazamento temporal se só estiverem disponíveis depois da pesquisa de NPS.
- A regressão prevê a nota esperada, mas não substitui uma política de intervenção com validação experimental.
