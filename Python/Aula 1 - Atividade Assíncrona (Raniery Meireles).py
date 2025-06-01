#!/usr/bin/env python
# coding: utf-8

# # Atividade Assíncrona - Aula 1 - Python para Iniciantes na Análise de Dados
# 
# Este exercício tem como objetivo revisar todos os conceitos apresentados na Aula 1.  
# Siga as instruções abaixo e envie para avaliação:
# 
# 1. Crie variáveis para armazenar o **nome**, **idade** e **nota de duas matérias** de um aluno.  
# 2. Crie uma **função** chamada `calcular_media` que receba duas notas e retorne a média.  
# 3. Use a função para calcular a média do aluno e exiba com `print()`.  
# 4. Use uma **condicional (if/else)** para verificar se o aluno foi aprovado (`média >= 7`).  
# 5. Crie uma **lista** com os nomes de três alunos e use um **laço `for`** para cumprimentar cada um.  
# 6. Mostre com `type()` o tipo das variáveis criadas.  
# 7. Mostre com `len()` quantas letras tem o nome do aluno.  
# 
# **Opcional**: Use comentários para explicar cada parte do seu código.
# 
# ---
# 
# ### Envio
# 
# Salve seu código no colab e envie no formulário de atividade assíncrona localizado no drive.

# In[5]:


def calcular_media(nota1, nota2):
  return (nota1 + nota2) / 2

def main():
  nota1 = int(input("Insira a primeira nota: "))
  nota2 = int(input("Insira a segunda nota: "))

  media = calcular_media(nota1, nota2)
  print(f"A média é {media}")

  if(media >= 7):
    print("Você foi aprovado!")
  else:
    print("Você foi reprovado :(")

  list_nomes = ["Pedro", "Hugo", "Carolina"]

  for i in list_nomes:
    print(f"O tipo de variável do nome {i} é {type(i)}")
    print(f"O nome tem {len(i)} letras")


if __name__ == "__main__":
  main()


# In[ ]:




