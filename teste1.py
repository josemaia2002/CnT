def ultima_parada(combustivel,consumo,postos_de_gasolina):
    limite = combustivel * consumo # qte máxima de km
    in_range = []
    maior = 0
    
    for x in postos_de_gasolina:
      if (x <= limite):
        in_range.append(x)

    for x in in_range:
      if (x > maior):
        maior = x

    if(maior == 0):
      maior = -1
        
    return maior  
    pass