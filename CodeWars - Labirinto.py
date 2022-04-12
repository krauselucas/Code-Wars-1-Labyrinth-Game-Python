'''Code Wars - Desafio Stone + How:

Equipe 42:
Bruno Tropia
Felipe Lira
Lucas Krause
Tamara Passos'''

import random
import queue
import copy
from time import sleep

# O critério utilizado para saber se o labirinto é válido ou não, foi: se o robô volta para o início, o labirinto é descartado; se o robô chega ao S, o labirinto é validado.
verificador_de_labirinto = 1 
# Dígito verificador para identificar se o labirinto tem solução ou não.
while verificador_de_labirinto == 1: 
 
 def gerador_labirinto():
  labirinto = []

  espaco_cerquilha = [' ', '#']

  linha_zero = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
  labirinto.append(linha_zero)
  linha_um = [random.choice(espaco_cerquilha) for x in range(17)]
  linha_um.insert(0, '#'), linha_um.insert(18, '#')
  inicio = random.randint(1, 7) #Limitação do 1 ao 7 para que o início fique mais distante do final do labirinto.
  linha_um.insert(inicio, 'X') #Variavel início criada para guardar onde o robô vai iniciar o trajeto.
  labirinto.append(linha_um) 
  linha_dois = [random.choice(espaco_cerquilha) for x in range(17)] 
  linha_dois.insert(0, '#'), linha_dois.insert(19, '#')
  linha_dois.insert(inicio, ' ') #Espaço criado para que o robô dê o primeiro passo e comece a validar as condições.
  labirinto.append(linha_dois)
  linha_tres = [random.choice(espaco_cerquilha) for x in range(18)]
  linha_tres.insert(0, '#'), linha_tres.insert(19, '#')
  labirinto.append(linha_tres)
  linha_quatro = [random.choice(espaco_cerquilha) for x in range(18)]
  linha_quatro.insert(0, '#'), linha_quatro.insert(19, '#')
  labirinto.append(linha_quatro)
  linha_cinco = [random.choice(espaco_cerquilha) for x in range(18)]
  linha_cinco.insert(0, '#'), linha_cinco.insert(19, '#')
  labirinto.append(linha_cinco)
  linha_seis = [random.choice(espaco_cerquilha) for x in range(18)]
  linha_seis.insert(0, '#'), linha_seis.insert(19, '#')
  labirinto.append(linha_seis)
  linha_sete = [random.choice(espaco_cerquilha) for x in range(18)]
  linha_sete.insert(0, '#'), linha_sete.insert(19, '#')
  labirinto.append(linha_sete)
  linha_oito = [random.choice(espaco_cerquilha) for x in range(18)]
  linha_oito.insert(0, '#'), linha_oito.insert(19, '#')
  labirinto.append(linha_oito)
  linha_nove = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
  linha_nove.insert((random.randint(15, 18)), 'S') #Limitação do 15 ao 18 para que o final fique mais distante do início do labirinto.
  labirinto.append(linha_nove)
   
  return labirinto
   
 labirinto = gerador_labirinto()
 labirinto_certo = copy.deepcopy(labirinto)
 
#Processo de validação do labirinto utilizando o próprio robô para descartar mapas sem resolução. 
 for lista in labirinto:
   if 'X' in lista:
    x = lista.index('X')
    y = labirinto.index(lista)

 caminho_percorrido = queue.LifoQueue()
 
 n = 0
 inicio_x = x
 inicio_y = y

 while True:
   
    posicao_atual = labirinto[y][x]
    posicao_acima = labirinto[y-1][x]
    posicao_direita = labirinto[y][x+1]
    posicao_abaixo = labirinto[y+1][x]
    posicao_esquerda = labirinto[y][x-1]
    
#Contador de passos.
    n += 1
   
#Movimento final/vitória
    if posicao_acima == 'S':
      labirinto[y][x] = '.'
      labirinto[y-1][x] = 'X'
      y -= 1
      verificador_de_labirinto = 0
      break
     
    elif posicao_direita == 'S':
      labirinto[y][x] = '.'
      labirinto[y][x+1] = 'X'
      x += 1
      verificador_de_labirinto = 0
      break
     
    elif posicao_abaixo == 'S':
      labirinto[y][x] = '.'
      labirinto[y+1][x] = 'X'
      y += 1
      verificador_de_labirinto = 0
      break
     
    elif posicao_esquerda == 'S':
      labirinto[y][x] = '.'
      labirinto[y][x-1] = 'X'
      x -= 1
    
      verificador_de_labirinto = 0
      break
     
    elif n != 1 and (x == inicio_x) and (y == inicio_y): 
      break
       
    else:
#Movimento padrão
      if posicao_acima == ' ':
        caminho_percorrido.put(tuple([x , y]))
        labirinto[y][x] = '.'
        labirinto[y-1][x] = 'X'
        y -= 1
      elif posicao_direita == ' ':
        caminho_percorrido.put(tuple([x , y]))
        labirinto[y][x] = '.'
        labirinto[y][x+1] = 'X'
        x += 1
      elif posicao_abaixo == ' ':
        caminho_percorrido.put(tuple([x , y]))
        labirinto[y][x] = '.'
        labirinto[y+1][x] = 'X'
        y += 1
      elif posicao_esquerda == ' ':
        caminho_percorrido.put(tuple([x , y]))
        labirinto[y][x] = '.'
        labirinto[y][x-1] = 'X'
        x -= 1
      else:

#Movimento beco sem saída
        andar_pra_tras = caminho_percorrido.get()
        labirinto[y][x] = '.'
        x , y = andar_pra_tras
        labirinto[y][x] = 'X'
  
   
labirinto = labirinto_certo

print('Este é o labirinto com a posição inicial do robô.')
for lista in labirinto:
  for posicao in lista:
    print(posicao, end=' ')
  print()
print('\n')

#Regra de movimentação do robô
#Posição inicial do robô
for lista in labirinto:
  if 'X' in lista:
    x = lista.index('X')
    y = labirinto.index(lista)

caminho_percorrido = queue.LifoQueue()

#Variável n fora do while para contabilizar todos os passos
n = 0

while True:
#Definição das variáveis dentro do while pq precisam ser atualizadas a cada movimento
  posicao_atual = labirinto[y][x]
  posicao_acima = labirinto[y-1][x]
  posicao_direita = labirinto[y][x+1]
  posicao_abaixo = labirinto[y+1][x]
  posicao_esquerda = labirinto[y][x-1]
  
#Contador de passos
  n += 1
  if n == 1:
    print(f'Foi dado {n} passo até aqui.')
  else:
    print(f'Foram dados {n} passos até aqui.')


#Movimento final/vitória
  if posicao_acima == 'S':
    labirinto[y][x] = '.'
    labirinto[y-1][x] = 'X'
    y -= 1
    for lista in labirinto:
      for posicao in lista:
        print(posicao, end=' ')
      print()
    print('O robô encontrou a saída do labirinto!')
    print('\n')
    break
  elif posicao_direita == 'S':
    labirinto[y][x] = '.'
    labirinto[y][x+1] = 'X'
    x += 1
    for lista in labirinto:
      for posicao in lista:
        print(posicao, end=' ')
      print()
    print('O robô encontrou a saída do labirinto!')
    print('\n')
    break
  elif posicao_abaixo == 'S':
    labirinto[y][x] = '.'
    labirinto[y+1][x] = 'X'
    y += 1
    for lista in labirinto:
      for posicao in lista:
        print(posicao, end=' ')
      print()    
    print('O robô encontrou a saída do labirinto!')
    print('\n')
    break
  elif posicao_esquerda == 'S':
    labirinto[y][x] = '.'
    labirinto[y][x-1] = 'X'
    x -= 1
    for lista in labirinto:
      for posicao in lista:
        print(posicao, end=' ')
      print()    
    print('O robô encontrou a saída do labirinto!')
    print('\n')
    break
  else:
  
#Movimento padrão
    if posicao_acima == ' ':
      caminho_percorrido.put(tuple([x , y]))
      labirinto[y][x] = '.'
      labirinto[y-1][x] = 'X'
      y -= 1
    elif posicao_direita == ' ':
      caminho_percorrido.put(tuple([x , y]))
      labirinto[y][x] = '.'
      labirinto[y][x+1] = 'X'
      x += 1
    elif posicao_abaixo == ' ':
      caminho_percorrido.put(tuple([x , y]))
      labirinto[y][x] = '.'
      labirinto[y+1][x] = 'X'
      y += 1
    elif posicao_esquerda == ' ':
      caminho_percorrido.put(tuple([x , y]))
      labirinto[y][x] = '.'
      labirinto[y][x-1] = 'X'
      x -= 1
    else:

#Movimento beco sem saída
      andar_pra_tras = caminho_percorrido.get()
      labirinto[y][x] = '.'
      x , y = andar_pra_tras
      labirinto[y][x] = 'X'

  sleep(0.7)
  for lista in labirinto:
    for posicao in lista:
        print(posicao, end=' ')
    print()
  print('\n')
