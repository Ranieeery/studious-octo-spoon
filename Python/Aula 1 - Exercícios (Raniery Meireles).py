#!/usr/bin/env python
# coding: utf-8

# 1 -  Peça ao usuário para digitar sua idade e mostre uma mensagem indicando se ele e menor ou maior de idade

# In[4]:


idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Você é maior de idade!")
else:
    print(f"Você é menor de idade!")


# 2 -  Utilize um laço for para imprimir os números de 1 a 10

# In[6]:


for i in range(1, 11):
    print(i)


#  3 - Crie uma função que receba duas notas como parametros, calcule a média e retorne o resultado.
#  Depois, chame a função e exiba a média calculada

# In[11]:


def calc_media(nota1, nota2):
  media = (nota1 + nota2) / 2
  return media

def main():
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))
  media = calc_media(nota1, nota2)
  print(f"A média é: {media}")

if __name__ == "__main__":
  main()


#  4 - Crie uma lista com três nomes e use um laço for para exibir uma saudação personalizada para cada nome.

# In[12]:


list = ["Pedro", "Gabriel", "Arthur"]

for i in list:
  print(f"Olá {i}, tudo bem?")

