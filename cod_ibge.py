def achar_codigo(entes):
    codigo_uf = []

    for ente in entes:
        if ente['ente'] == 'Balneário Camboriú':
            codigo_uf.append(ente['cod_ibge'])

    return codigo_uf