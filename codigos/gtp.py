import pandas as pd
import streamlit as st
dados = {
    "Nome": ["arthur", "miguel", "kenzo", "marco", "tulio", "jr", "yuri", "pedro", "henrique", "bastos", "almeida", "leugim", "borges", "antunes", "tanaka", "fernandes", "rocha", "joao", "felipe", "ribeiro"],
    "Idade": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "Profissão": ["Profissão 1", "Profissão 2", "Profissão 3", "Profissão 4", "Profissão 5", "Profissão 1", "Profissão 2", "Profissão 3", "Profissão 4", "Profissão 5", "Profissão 1", "Profissão 2", "Profissão 3", "Profissão 4", "Profissão 5", "Profissão 1", "Profissão 2", "Profissão 3", "Profissão 4", "Profissão 5"]
}
df = pd.DataFrame(dados)
st.title("data frame de dados")
st.dataframe(df)
