
#Alunos: Amanda Constante, Karoline Custodio, Vitor Baptista e Jonas Schuh


#Responda:
# Nao. Na nossa concepcao, um bom agente tracaria um caminho que passasse pelo minimo de casas para limpar o ambiente.
# No nosso caso, estamos fazendo um caminho fixo padrao, mas quando ele identifica que o ambiente esta limpo, ele para.

# o cinza eh a sujeira e o preto eh o limpo
#o verde sao as paredes

import numpy as np
import matplotlib.pyplot as plt
import random 

pontos = 0
contadorDeLixoGerado = 0
contadorDePassos = 0
linhaFinal = 0
colunaFinal = 0

matriz = np.array([[1,1,1,1,1,1],
                  [1,0,0,0,0,1],
                  [1,0,0,0,0,1],
                  [1,0,0,0,0,1],
                  [1,0,0,0,0,1],
                  [1,1,1,1,1,1]]
                  )


# funcao que exibe o ambiente na tela
def exibir(I):    
    global posAPAx
    global posAPAy
    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral() 
    #plt.plot([posAPAy],[posAPAx], marker='o', color='r', ls='')
    plt.show(block=False)
    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.2)    
    plt.clf()
    
def imprimir(linha, coluna):
    plt.plot([linha],[coluna], marker='o', color='r', ls='')
    exibir(matriz)

#funcao que constroi o ambiente 
#Percorre a matriz exluindo os extremos que sao 1 e insere as sujeiras aleatoriamente  
def construirAmbiente():
  global contadorDeLixoGerado
  for linha in range(6):
    for coluna in range(6):
      if (linha >= 1 and coluna >= 1) and (linha < 5 and coluna < 5):
        limpoOuSujo = random.randint(0, 2)
        if limpoOuSujo == 1:
          matriz[linha][coluna] = 0
        else:
          matriz[linha][coluna] = limpoOuSujo 
        if limpoOuSujo == 2:
          contadorDeLixoGerado += 1

#Verfica a posicao do agente no mundo e se ele deve parar
def agenteObjetivo(linha, coluna, salaEstaLimpa):
  global pontos
  global contadorDePassos
  global linhaFinal
  global colunaFinal
  
  if salaEstaLimpa == True:
      print("Acao escolhida: NoOp" + str(linhaFinal))
      return "NoOp"
  
  contadorDePassos += 1
  imprimir(coluna,linha)
  
  if matriz[linha][coluna] == 2:
    
    matriz[linha][coluna] = 0
    pontos += 1
    
    if checkObj(matriz):
        imprimir(coluna,linha)
    
    print("Estado da percepcao:1 Acao escolhida: aspirar")
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
 

#Verifica se a sala ja esta limpa
def checkObj(sala):
    if  contadorDeLixoGerado == pontos:
        return True
    else:
        return False

#Define um caminho padrao para o robo no mundo
def mapeamento():
    
    if agenteObjetivo(1, 1, checkObj(matriz)) == "NoOp":
        return 
 
    if agenteObjetivo(2, 1, checkObj(matriz)) == "NoOp":
        return
  
    if agenteObjetivo(3, 1, checkObj(matriz)) == "NoOp":
        return
       
    if agenteObjetivo(4, 1, checkObj(matriz)) == "NoOp":
        return
   
    if agenteObjetivo(4, 2, checkObj(matriz)) == "NoOp":
        return
           
    if agenteObjetivo(4, 3, checkObj(matriz)) == "NoOp":
        return
     
    if agenteObjetivo(4, 4, checkObj(matriz)) == "NoOp":
        return
       
    if agenteObjetivo(3, 4, checkObj(matriz)) == "NoOp":
        return
        
    if agenteObjetivo(3, 3, checkObj(matriz)) == "NoOp":
        return 
      
    if agenteObjetivo(3, 2, checkObj(matriz)) == "NoOp":
        return
     
    if agenteObjetivo(2, 2, checkObj(matriz)) == "NoOp":
        return
 
    if agenteObjetivo(2, 3, checkObj(matriz)) == "NoOp":
        return
   
    if agenteObjetivo(2, 4, checkObj(matriz)) == "NoOp":
        return
  
    if agenteObjetivo(1, 4, checkObj(matriz)) == "NoOp":
        return 
   
    if agenteObjetivo(1, 3, checkObj(matriz)) == "NoOp":
        return
  
    if agenteObjetivo(1, 2, checkObj(matriz)) == "NoOp":
        return 
    

construirAmbiente()
print("Matriz Com Sujeiras: \n")
print(matriz)
print("\n")

exibir(matriz)
mapeamento()
print("Matriz Limpa: \n")
print(matriz)
print("\n")



print("Total de sujeiras: ", pontos)
print("Total de passos para limpar a sala toda: ", contadorDePassos)
totalDePontos = pontos + contadorDePassos
print("Total geral: " , totalDePontos)


