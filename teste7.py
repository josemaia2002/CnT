def calcula_total_leds(altura,largura):
  if((altura > 0) and (largura > 0)):
    qte_leds = (altura+1) * (largura+1)
  else:
    qte_leds = 0
    
  return qte_leds