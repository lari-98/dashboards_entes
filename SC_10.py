import requests
from uf import filtrar_por_uf
from hab_10 import filtrar_por_populacao
from main import entes, uf_maiores

import pandas as pd

sc_10 = pd.DataFrame(uf_maiores)

print(sc_10)