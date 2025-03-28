import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
datas = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "Vendas": [1200, 1500, 1700, 1300, 1600, 1400, 1800, 2100, 1900, 2000, 2200, 2500],
}

df = pd.DataFrame(datas)
st.title("--Dashboard de Vendas Mensais--")
st.sidebar.header("Filtrar por Mês")
meses = st.sidebar.multiselect("Selecione o meses", options=df["Mês"], default=df["Mês"])

if meses:
  df_filtro = df[df["Mês"].isin(meses)]
else:
  df_filtro = df

st.subheader("Gragico de Vendas por Mês")
st.write(f"R$ {df_filtro['Vendas'].sum():.2f}")
fig, ax = plt.subplots()
ax.bar(df_filtro["Mês"], df_filtro["Vendas"])
plt.xticks(rotation=45)
plt.ylabel ("vendas")
plt.xlabel ("mes")
st.pyplot(fig)