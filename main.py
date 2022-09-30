import requests
from uf import filtrar_por_uf
from hab_10 import filtrar_por_populacao
from cod_ibge import achar_codigo

base_url = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt'
entes = requests.get(f"{base_url}/entes").json()['items'] #tipo lista

# criar variáveis para armazenar o retorno da função. Não dá pra chamar retorno, só variáveis. 

uf_selecionadas = filtrar_por_uf(entes,'SC')
print(uf_selecionadas[:10])

uf_maiores = filtrar_por_populacao(uf_selecionadas)
print(uf_maiores)

balneario_codigo = achar_codigo(entes)
print(balneario_codigo)