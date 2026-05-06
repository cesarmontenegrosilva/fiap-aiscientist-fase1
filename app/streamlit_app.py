from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "nps_features.csv"
PRED = ROOT / "data" / "processed" / "previsoes_amostra.csv"
METRICS = ROOT / "reports" / "tables" / "metricas_modelos.csv"

st.set_page_config(page_title="NPS Preditivo", layout="wide")
st.title("NPS Preditivo — E-commerce")

if not DATA.exists():
    st.error("Execute o notebook ou src/train_model.py antes de abrir o dashboard.")
    st.stop()

df = pd.read_csv(DATA)
metrics = pd.read_csv(METRICS)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Pedidos", f"{len(df):,}".replace(",", "."))
col2.metric("NPS médio", f"{df['nps_score'].mean():.2f}")
col3.metric("Detratores", f"{(df['nps_class']=='Detrator').mean():.1%}")
col4.metric("Promotores", f"{(df['nps_class']=='Promotor').mean():.1%}")

st.subheader("Distribuição de NPS")
st.bar_chart(df['nps_class'].value_counts())

st.subheader("NPS médio por atraso na entrega")
delay = df.groupby('delivery_delay_days')['nps_score'].mean().reset_index()
st.line_chart(delay, x='delivery_delay_days', y='nps_score')

st.subheader("Métricas dos modelos")
st.dataframe(metrics, use_container_width=True)

if PRED.exists():
    st.subheader("Amostra de previsões")
    pred = pd.read_csv(PRED)
    st.dataframe(pred[['nps_real','nps_previsto_regressao','nps_q10','nps_q50','nps_q90']].head(50), use_container_width=True)
