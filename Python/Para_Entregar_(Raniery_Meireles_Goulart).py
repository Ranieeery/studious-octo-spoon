#!/usr/bin/env python
# coding: utf-8

# # **Atividade para Entregar**

# 
# 
# ---
# 
# Use o dataframe de filmes e crie um gráfico para dados qualitativos e um gráfico para dados quantitativos.
# 
# O gráfico pode ser de sua escolha.
# 
# Ao final, escreva uma análise exploratória a respeito dos gráficos e dados analisados.
# 
# ---
# 
# 

# ## Importando Bibliotecas

# In[1]:


# Importe bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# ## Inserindo Dataframe

# In[15]:


# Definir dataframe qualitativo
df = pd.read_csv("filmes_avaliacoes.csv")


# ### Dado Quantitativo Escolhido

# In[16]:


# Gráfico para dados quantitativos - Distribuição das Notas

plt.hist(df['Avaliacao'], bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.title('Distribuição das Notas dos Filmes')
plt.xlabel('Avaliacao')
plt.ylabel('Frequência')


# ## Dados Qualitativos

# In[23]:


# Criar gráfico

# Contagem de avaliações por gênero
genero_counts = df['Genero'].value_counts()

genero_counts.plot(kind='bar', color='lightcoral')
plt.title('Número de Avaliações por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Avaliações')
plt.xticks(rotation=45)


# 
# 
# ---
# 
# ## Análise exploratória
# 
# ---
# 
# 

# Exemplo de análises que podem ser feitas (Responda apenas 3):
# 
# Quantos filmes diferentes existem no dataset?
# 
# Qual é a média, mediana, nota mínima e nota máxima das avaliações?
# 
# Qual gênero possui mais avaliações?
# 
# Quais são os 5 filmes com as melhores médias de nota?
# 
# Existe algum usuário que avaliou muitos filmes? Quem são os 3 usuários mais ativos?
# 
# A nota média varia entre os gêneros? Qual gênero tem a maior e menor média de nota?
# 
# Existe diferença nas avaliações dos filmes lançados antes e depois de 2010?
# 
# Quais são os filmes mais polarizadores (com maior desvio padrão nas notas)?
# 
# Quais são os comentários mais frequentes?
# 
# Existe alguma relação visível entre comentários negativos e notas baixas?

# 
# 
# ---
# 
# ## **Insira sua resposta aqui**
# 

# In[32]:


# Quantos filmes existem
filme_counts = df['Filme'].nunique()
print(filme_counts)

# Qual é a média, mediana, nota mínima e nota máxima das avaliações?
media = df['Avaliacao'].mean()
mediana = df['Avaliacao'].median()
minima = df['Avaliacao'].min()
maxima = df['Avaliacao'].max()

print(f"Estatísticas das notas - Média: {media:.2f}, Mediana: {mediana:.2f}, Min: {minima:.2f}, Max: {maxima:.2f}")

# Qual gênero possui mais avaliações?
genero_avaliacoes = df['Genero'].value_counts().index[0]
num_avaliacoes = df['Genero'].value_counts().iloc[0]

print(f"Gênero com mais avaliações: {genero_avaliacoes} ({num_avaliacoes} avaliações)")

