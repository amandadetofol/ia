#Alunos: Amanda Constante, Karoline Custodio, Vitor Baptista e Jonas Schuh

#Responda: E para um mundo 6 x 6? Explique sua resposta.
#No momento nao, por que a matriz e a analise do ambiente nao criada de forma fixa.

# o cinza eh a sujeira e o preto eh o limpo
#o verde sao as paredes

import numpy as np
import matplotlib.pyplot as plt
import random

#Matriz inicial limpa com as paredes
matriz = np.array([[1,1,1,1,1,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,1,1,1,1,1]
                   ])

# Função que exibe o ambiente na tela
def exibir(I):    
    global posAPAx
    global posAPAy
    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral() 
    #plt.plot([posAPAy],[posAPAx], marker='o', color='r', ls='')
    plt.show(block=False)
    # Pausa a execucao do codigo por 0.5 segundos para facilitar a visualizacao
    plt.pause(1)    
    plt.clf()
    
#funcao que constroi o ambiente 
#Percorre a matriz exluindo os extremos que sao 1 e insere as sujeiras aleatoriamente  
def construirAmbiente():
  for linha in range(6):
    for coluna in range(6):
      if (linha >= 1 and coluna >= 1) and (linha < 5 and coluna < 5):
        limpoOuSujo = random.randint(0, 2)
        if limpoOuSujo == 1:
          matriz[linha][coluna] = 0
        else:
          matriz[linha][coluna] = limpoOuSujo  
          

def imprimir(linha, coluna):
    plt.plot([linha],[coluna], marker='o', color='r', ls='')
    exibir(matriz)

#Verifica qual direcao ele vai
def agenteReativoSimples(linha, coluna):

  imprimir(coluna, linha)
  if matriz[linha][coluna] == 2:
    matriz[linha][coluna] = 0
    return "aspirar"
  else:
     if coluna == 1:
       print("Estado da percepcao:0 Acao escolhida: abaixo")
       return "abaixo"
     if (linha == 4 or linha ==2) and coluna!=4:
       print("Estado da percepcao:0 Acao escolhida: direita")
       return "direita"
     if coluna == 1 or (linha==2 and coluna==2) or (linha==3 and coluna==2) or (linha==4 and coluna==4)  or (linha==2 and coluna==4):
       print("Estado da percepcao:0 Acao escolhida: acima")
       return "acima"
     if linha == 3 or linha == 1:
       print("Estado da percepcao:0 Acao escolhida: esquerda")
       return "esquerda"

#Define o caminho padrao para o robo no tabuleiro
def mapeamento():   
    agenteReativoSimples(1, 1)
    agenteReativoSimples(2, 1)
    agenteReativoSimples(3, 1)
    agenteReativoSimples(4, 1)
    
    agenteReativoSimples(4, 2)
    agenteReativoSimples(4, 3)
    agenteReativoSimples(4, 4)
    
    agenteReativoSimples(3, 4)
    agenteReativoSimples(3, 3)
    agenteReativoSimples(3, 2)
    
    agenteReativoSimples(2, 2)
    agenteReativoSimples(2, 3)
    agenteReativoSimples(2, 4)
    
    agenteReativoSimples(1, 4)
    agenteReativoSimples(1, 3)
    agenteReativoSimples(1, 2)
    agenteReativoSimples(1, 1)

print(matriz)
construirAmbiente()
print(matriz)
exibir(matriz)
mapeamento()
