from itertools import permutations
import string

def Sort_Tuple(tup): 
  lst = len(tup) 
  for i in range(0, 20): 
    for j in range(0, 20-i-1): 
      if (tup[j] > tup[j + 1]): 
        temp = tup[j] 
        tup[j]= tup[j + 1] 
        tup[j + 1]= temp 
  return tup[0]
  
def menor_string_maior(name):
  if len(name) < 1:
    return "sem resposta"

  if len(name) == 2:
    if name[0] > name[1]:
      return "sem resposta"
    else:
      return name[1] + name[0]
  
  a = string.ascii_letters
  p = permutations(name)

  res = []

  d = []
  d = [i for i in list(p) if i not in d]
  res = [d[i] for i in range(len(d)) if d[i] > d[0]]

  if len(res) == 0:
    return "sem resposta"

  Sort_Tuple(res)

  str = ''
  for item in res[0]:
    str = str + item
  return str