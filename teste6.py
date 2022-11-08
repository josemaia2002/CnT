def checa_numero_escondido(numero,numero_oculto):

  my_list = [int(x) for x in str(numero)]
  my_sub_list = [int(x) for x in str(numero_oculto)]

  print(my_list)
  print(my_sub_list)

  tam = len(my_list)
  inside = 0

  for i in range(len(my_sub_list)):
    for j in range(tam):
      if my_sub_list[i] in my_list:
        inside = 1
      else:
        inside = 0

  if inside: 
    return True
    
  else:
    return False