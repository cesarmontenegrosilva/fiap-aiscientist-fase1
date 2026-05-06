# Roteiro sugerido para vídeo executivo (até 5 minutos)

## 0:00–0:40 — Contexto
O desafio é antecipar clientes promotores e detratores antes da aplicação formal da pesquisa de NPS. Em um e-commerce, isso é importante porque atrasos, reclamações e experiências ruins afetam recompra, boca a boca e retenção.

## 0:40–1:40 — Principais achados da EDA
A base analisada possui 2.500 registros. A maioria dos clientes aparece como detrator. O fator mais crítico é o atraso na entrega: o NPS médio cai já a partir de 1 dia de atraso e se deteriora fortemente entre 4 e 5 dias. Reclamações e contatos com atendimento também reduzem a satisfação.

## 1:40–2:50 — Modelo preditivo
Foi adotada uma abordagem de regressão, pois a variável-alvo é a nota contínua de NPS. Foram comparados modelos tradicionais e uma regressão quantílica. A regressão prevê a nota esperada; a regressão quantílica adiciona uma faixa de incerteza, útil para priorizar clientes com maior risco.

## 2:50–4:00 — Aplicação prática
A recomendação é usar o modelo para criar uma fila diária de clientes em risco. Clientes com previsão baixa ou com intervalo inferior muito crítico devem receber ação proativa: comunicação sobre atraso, priorização logística, atendimento preventivo ou oferta compensatória.

## 4:00–5:00 — Conclusão e riscos
A solução transforma dados operacionais em estratégia de experiência do cliente. As principais limitações são risco de vazamento temporal, variáveis não observadas e necessidade de validar o impacto das ações por teste A/B ou análise antes/depois.
