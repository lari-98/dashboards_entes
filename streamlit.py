import streamlit as st
import pandas as pd
from main import uf_selecionadas, uf_maiores
from SC_5 import filter_5
from SC_dataframe import sc

st.write("Informações de Santa Catarina")

# Utilizando metric
st.metric(label="Quantidade de Entes em SC", value=len(uf_selecionadas), delta="Santa Catarina")
st.metric(label="Quantidade de Entes de SC com população maior que 10 mil habitantes", value=len(uf_maiores), delta="Santa Catarina")
st.metric(label="Quantidade de Entes de SC com população menor que 5 mil habitantes", value=len(filter_5(uf_selecionadas)), delta="Santa Catarina")

# Utilizando barplot

sc_bp = pd.DataFrame(
    sc,
    columns=["populacao", "ente"])

st.bar_chart(data=sc_bp, y="População", x="Nome do Ente", use_container_width=True)

sc
