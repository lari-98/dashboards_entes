import requests
import pandas as pd

base_url = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt'
entes = requests.get(f"{base_url}/entes").json()['items'] #tipo lista

entes_data = pd.DataFrame(entes)
print(entes_data)