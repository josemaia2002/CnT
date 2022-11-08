def escolhe_taxi(tf1,vqr1,tf2,vqr2):
  t2 = float(tf2) 
  t1 = float(tf1)
  v1 = float(vqr1)
  v2 = float(vqr2)

  if v1 == v2 :
    if(t2 > t1):
      return "Empresa 1"
    elif t2 < t1:
      return "Empresa 2"
    else:
      return "Tanto faz"

  d = (t2 - t1)/(v1 - v2)
  d = round(d, 2)

  if(t2 == t1) and (v1 == v2):
    return "Tanto faz"

  if d < 0:
    if(t2 > t1):
      return "Empresa 1"
    else:
      return "Empresa 2"
    
  else:
    if(t2 > t1):
      resultado = "Empresa 1 quando a distância < "+ str(d) +  ", Tanto faz quando a distância = " + str(d) + ", Empresa 2 quando a distância > "+  str(d)
      return resultado
    
    else:
      resultado = "Empresa 1 quando a distância < " + srt(d) +  ", Tanto faz quando a distância = " + str(d) + ", Empresa 2 quando a distância > " + str(d)
      return resultado