#lista de exercícios.

#Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'hum', 'dois'].
#A ideia do exercício é tirar a média de todos os valores contidos na lista, 
# porém para fazer o cálculo precisa remover as strings.

Listanumeros = [6,7,4,7,8,4,2,5,7,'hum','dois']
print (Listanumeros)
Listanumeros.pop()
print(Listanumeros)
Listanumeros.pop()
print (Listanumeros)

def soma(Listanumeros):
    totalsoma=0
    for numlista in Listanumeros:
        totalsoma += numlista
    return totalsoma

def media(Listanumeros):
    return (soma(Listanumeros)/len(Listanumeros))

print ("A Soma da Lista é ",soma(Listanumeros))
print ("A Média da Lista é ", media(Listanumeros))


#crie um método que receba duas matrizes, some os valores total de cada matriz e 
# depois multiple o resultado delas e retorne o valor.

Matriz_A = [1,2,3]
Matriz_B = [4,5,6]
print (Matriz_A)
print (Matriz_B)

def soma_A(Matriz_A):
    totalsoma=0
    for numlista in Matriz_A:
        totalsoma += numlista
    return int(totalsoma)

def soma_B(Matriz_B):
    totalsoma=0
    for numlista in Matriz_B:
        totalsoma += numlista
    return int(totalsoma)

Multp = soma_A(Matriz_A) * soma_B(Matriz_B)


print ("A soma da Matriz A é",soma_A(Matriz_A))
print ("Soma da Matriz B é",soma_B(Matriz_B))
print ("A Multiplicação das Matrizes é",Multp)


#__________Criar uma matriz nxm (n = 5, m =7)

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)

def exibir_matriz(matriz):
 for linha in matriz:
     print(linha)

exibir_matriz(matriz)


#__________faça a matriz transposta desta matriz

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)

#print(matriz)  #visualização da lista

exibir_matriz(matriz)
def exibir_matriz(matriz): #visualização como matriz
 for linha in matriz:
     print(linha)

def somaLinhas(matriz):
    totalsoma=0
    for i in range(m):
        totalsoma += int(m)
    return totalsoma

print("A soma das linhas é: ", somaLinhas(matriz))

def transposta(matriz):
  T = []
  nLinhas = len(m)
  nColunas = len(m[0])
  for i in range(nLinhas):
    for j in range(nColunas):
      T[j][i] = M[i][j]
  return T

print ("A transposição da Matriz é: ",transposta(matriz))

#__________somar toda matriz

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)

#print(matriz)  #visualização da lista

exibir_matriz(matriz)
def exibir_matriz(matriz): #visualização como matriz
 for linha in matriz:
     print(linha)

soma(matriz)

def soma(matriz):
    totalsoma=0
    for soma in matriz:
        totalsoma += soma
    return totalsoma


print("A soma da Matriz é: ", soma(matriz)) 

#__________somar todas as colunas

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)

#print(matriz)  #visualização da lista

exibir_matriz(matriz)
def exibir_matriz(matriz): #visualização como matriz
 for linha in matriz:
     print(linha)

def somaColunas(matriz):
    totalsoma=0
    for i in range(n):
        totalsoma += int(n)
    return totalsoma

print("A soma das colunas é: ", somaColunas(matriz))

#__________somar todas as linhas.

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)

#print(matriz)  #visualização da lista

exibir_matriz(matriz)
def exibir_matriz(matriz): #visualização como matriz
 for linha in matriz:
     print(linha)

def somaLinhas(matriz):
    totalsoma=0
    for i in range(m):
        totalsoma += int(m)
    return totalsoma

print("A soma das linhas é: ", somaLinhas(matriz))

#__________retorne o maior valor
import random
matriz = [0]*10
for i in range(10):
    matriz[i] = [0]*10

for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint (10,70)

print (matriz)

maior = matriz[0][0]
for i in range(10):
    for j in range(10):
        if matriz [i][j] > maior:
            maior = matriz[i][j]

print (maior)

#__________retorne o menor valor.

import random
matriz = [0]*10
for i in range(10):
    matriz[i] = [0]*10

for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint (10,70)

print (matriz)

menor = matriz[0][0]
for i in range(10):
    for j in range(10):
        if matriz [i][j] < menor:
            menor = matriz[i][j]

print (menor)

#4. Crie uma matriz nxn (n=5). Agora some essa matriz com a matriz do exercício 3.

import numpy as np

A = np.array([1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15])
A


#5. crie um array de números que vai de 0 a 1000.

#6. crie uma matriz só de zeros.

