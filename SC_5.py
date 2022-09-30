import requests
from uf import filtrar_por_uf
from main import uf_selecionadas
import pandas as pd

def filter_5(uf_selecionadas):
    entes_5 = []

    for ente in uf_selecionadas:
        if ente['populacao'] < 5000:
            entes_5.append(ente['ente'])
    
    return entes_5

sc_5 = pd.DataFrame(filter_5(uf_selecionadas))

print(sc_5)