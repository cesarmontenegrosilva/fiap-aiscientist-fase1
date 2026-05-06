# Resumo executivo dos achados

## Base
- Registros analisados: 2,500
- Variável-alvo: `nps_score` (escala contínua de 0 a 10)
- Detratores: 1851 (74.0%)
- Neutros: 448 (17.9%)
- Promotores: 201 (8.0%)

## Principais fatores associados ao NPS
1. Atraso na entrega (`delivery_delay_days`) é o principal fator negativo observado, com correlação -0.60.
2. Compras repetidas em 30 dias e CSAT interno aparecem como sinais positivos fortes, com correlações 0.57 e 0.56, respectivamente.
3. Reclamações e contatos com atendimento deterioram a percepção do cliente, com correlações -0.50 e -0.35.
4. O ponto de ruptura prático aparece já a partir de 1 dia de atraso: o NPS médio cai de 6.86 para 5.55. A partir de 4-5 dias, o NPS médio cai para 2.15.

## Resultado dos modelos
- Melhor modelo por MAE: Ridge Regression.
- A regressão quantílica adiciona uma leitura de risco: em vez de prever apenas um número, estima uma faixa provável de NPS.
