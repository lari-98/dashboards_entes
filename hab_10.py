def filtrar_por_populacao(entes_selecionados):
    entes_maiores = []

    for ente in entes_selecionados:
        if ente['populacao'] > 10000:
            entes_maiores.append(ente['ente'])
    
    return entes_maiores