#lista de exercícios.

#1. Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'hum', 'dois'].
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


#2. crie um método que receba duas matrizes, some os valores total de cada matriz e 
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


#3. __________Criar uma matriz nxm (n = 5, m =7)

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


#3.1 __________faça a matriz transposta desta matriz

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)


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

#3.2 __________somar toda matriz

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)


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

#3.3 __________somar todas as colunas

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)


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

#3.4 __________somar todas as linhas.

m = int(input("Num Linhas: "))
n = int(input("Num Colunas: "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)


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

#3.5 __________retorne o maior valor
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

#3.6 __________retorne o menor valor.

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


#4. Crie uma matriz nxn (n=5). 

n = 5
m = 1
matriz_x = []

for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz_x.append(linha)

joke = ("Agora se prepare p/ digitar até amanhã...") 



def exibir_matriz(matriz_x):
 for linha in matriz_x:
     print("Matriz do Exercicio deste exercício: ",linha, joke)

exibir_matriz(matriz_x)

#[Exercicio 3__________Criar uma matriz nxm (n = 5, m =7)

m = 7
n = 5

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        elemento = int(input("Elemento da linha {} e coluna {}".format(i,j)))
        linha.append(int(elemento))
    matriz.append(linha)

def exibir_matriz(matriz):
 for linha in matriz:
     print("Matriz do Exercício 3: ",linha)


exibir_matriz(matriz)

# Agora some essa matriz com a matriz do exercício 3.

def somar(matriz, matriz_x):
    C = []
    nLinhasA, nlinhasB = len(matriz), len(matriz_x)
    nColA, nColB = len(matriz[0]), len(matriz_x)

    if (nLinhasA == nLinhasB) and (nColA == nColB):
        for i in nLinhasA:
            linha = [0]*nColA
            C.append(linha)
            for j in nColA:
                C[i][j] = matriz[[i][j]] + matriz_x[[i][j]]
    else:
        print("Matrizes não tem a mesma ordem :( ")   

    return C




#5. crie um array de números que vai de 0 a 1000.
import numpy as np
Numeros = np.array([n for n in range(0,1000)])
print(Numeros)

#6. crie uma matriz só de zeros.

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