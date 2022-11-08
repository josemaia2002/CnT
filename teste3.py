def calcula_numero_da_senha(senha):
  count_zero = 0
  count_one = 0

  bin_out = []
    
  for i in range(len(senha)):
    count_zero = 0
    count_one = 0
    for j in range(len(senha)):
      if(senha[j][i] == "0"):
        count_zero = count_zero + 1
      else:
        count_one = count_one + 1
    if(count_zero > count_one):
      bin_out.append(0)
    else:
      bin_out.append(1)
    
  exp = 9
  dec = 0
    
  for x in range(10):
    dec = dec + bin_out[x] * pow(2, exp)
    exp = exp - 1

  return dec

