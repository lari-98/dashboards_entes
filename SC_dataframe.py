import requests
from uf import filtrar_por_uf
from hab_10 import filtrar_por_populacao
from cod_ibge import achar_codigo
from main import entes, uf_selecionadas

import pandas as pd

sc = pd.DataFrame(uf_selecionadas)

print(sc)

sc = pd.Dataframe()