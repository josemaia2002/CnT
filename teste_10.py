def shuffle_musicas(musicas_tocadas):
  tam = len(musicas_tocadas)
  resultado = []
  
  if tam == 0:
    return resultado
  
  musicas_tocadas.sort(reverse = True)
  
  a = 0
  b = -1
  idx = 0

  if tam > 1:
    for i in range(tam):
      if i%2 == 0:
        idx = a
        a += 1
      else:
        idx = b
        b -= 1
      resultado.append(musicas_tocadas[idx])
  else:
      resultado.append(musicas_tocadas[0])

  return resultado