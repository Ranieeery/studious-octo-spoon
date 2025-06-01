#!/usr/bin/env python
# coding: utf-8

# # Atividade Assíncrona - Aula 3 - Python para Iniciantes na Análise de Dados
# 
# Este exercício tem como objetivo revisar todos os conceitos apresentados na Aula 2.  
# 
# Siga as instruções abaixo e envie para avaliação utilizando o dataset (alunos_classificados.csv)

# 
# 1. Mostre a quantidade de alunos por tipo de vaga (VAGA)
# 
# 
# 2. Mostre a distribuição de alunos por sexo (SEXO)
# 
# 
# 3. Mostre a distribuição da pontuação (PONTUACAO)
# 
# 
# 4. Compare a pontuação entre os sexos
# 
# 
# Instruções: <br>
# Execute cada gráfico e observe o comportamento dos dados.
# 
# Escreva uma frase interpretando o que o gráfico mostra.
# 
# Tente modificar um dos gráficos (ex: trocando SEXO por VAGA) e veja como o resultado muda.
# 
# ### Envio
# 
# Salve seu código no colab e envie no formulário de atividade assíncrona localizado no drive.
# 

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


df = pd.read_csv("alunos_classificados.csv")

df.head()


# In[22]:


# 1. Mostre a quantidade de alunos por tipo de vaga (VAGA)

plt.bar(df['VAGA'], df.index)

plt.title('Gráfico de quantidade de alunos por tipo de vaga')
plt.xlabel('Tipos de vagas')
plt.ylabel('Qntd. alunos')
plt.show()


# In[24]:


# Distribuição de alunos por sexo (SEXO)

plt.figure(figsize=(6, 6))
df['SEXO'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de alunos por sexo')
plt.ylabel('')
plt.show()


# In[1]:


# Distribuição da pontuação (PONTUACAO)

plt.figure(figsize=(10, 6))
sns.histplot(df['PONTUACAO'], kde=True)
plt.title('Distribuição da Pontuação')
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.show()


# In[40]:


# Compare a pontuação entre os sexos

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="SEXO", y="PONTUACAO")

plt.title("Comparação de pontuação entre os sexos")
plt.xlabel("Sexo")
plt.ylabel("Pontuação")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

