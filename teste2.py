def retorna_menor_e_maior_valor_de_vendas(tickets):
  maior = 0
  menor = 500
  
  for i in range(len(tickets)):  
    for j in tickets[i]:
      if((j > maior) and (j <= 500)):
        maior = j

  for i in range(len(tickets)):  
    for j in tickets[i]:
      if((j < menor) and (j >= 20)):
        menor = j

  maior_menor = []
  maior_menor.append(menor)
  maior_menor.append(maior)

  return maior_menor
