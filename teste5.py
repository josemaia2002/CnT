import math

def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
  vet = [] #quantidade de horas 
  resultado = [] # porcentagem

  for i in range(len(assinante)):
    if(assinante[i] == True):
      vet.append(math.ceil(((minutos_assistidos[i]))/60))
    else:
      vet.append(math.ceil((minutos_assistidos[i])/60))

  print(vet)

  for i in range(len(assinante)):
    if(assinante[i] == True):
      vet[i] = vet[i] * 2
  
  for i in range(len(vet)):
    x = round((vet[i] / sum(vet)) * 100)
    resultado.append(x)

  return resultado