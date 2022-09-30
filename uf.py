def filtrar_por_uf(entes, uf):
    entes_selecionados = []

    for ente in entes:
        if ente['uf'] == 'SC':
            entes_selecionados.append(ente)

    return entes_selecionados
    