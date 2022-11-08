def calcula_top_ocorrencias_de_queries(texto,queries,k):
  queries_cpy = []
  queries_times = []
  prioridade = []
  resultado = []
  result_sorted = []
  
  
  for i in range(len(queries)):
    x = texto.count(queries[i])
    ocorrencia = texto.find(queries[i])
    prioridade.append(ocorrencia)
    queries_times.append(x)

  for i in range(len(queries)):
    for j in range(len(queries)):
      if queries_times[i] == queries_times[j]:
        if prioridade[i] < prioridade[j]:
          queries_times[i] += 1
        elif prioridade[i] > prioridade[j]:
          queries_times[j] += 1

  new_list = sorted(queries_times)

  for i in range(len(new_list)):
    for j in range(len(new_list)):
      if (new_list[i] == queries_times[j]) and (queries[j] not in resultado):
        resultado.append(queries[j])
  
  for i in range(len(new_list) - 1, (len(new_list) - k) - 1, -1):
    result_sorted.append(resultado[i])

  return result_sorted