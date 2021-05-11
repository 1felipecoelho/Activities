#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculadora Python #
#Qual Operação vc quer fazer?# [input]
#Perguntar o primeiro numero# [input]
#Perguntar o segundo numero# [input]
#Calculo desses 2 numeros#
#Print


# In[5]:


operacao = input ("[+ - * /] O que vc quer calcular? ")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if operacao == '+':
    total = num1 + num2
    print(total)
elif operacao =='-':
    total = num1 - num2
    print(total)
elif operacao =='*':
    total = num1 * num2
    print(total)
elif operacao =='/':
    total = num1 / num2
    print(total)
else:
    print('Operacao Invalida')


# In[ ]:




