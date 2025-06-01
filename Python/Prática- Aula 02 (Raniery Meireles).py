#!/usr/bin/env python
# coding: utf-8

# In[35]:


# imports das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


# lendo o dataset
df = pd.read_csv("alunos.csv")
df.head()


# # Análise geral do dataframe

# In[14]:


# estrutura dos dados
df.info()


# In[15]:


# número de linhas e colunas (dimensão)
df.shape


# In[16]:


# resumo com estatísticas descritivas
df.describe()


# In[17]:


# quartis
numeros = pd.Series([4, 5, 6, 7, 8, 9, 10])

# como calcular
q1 = numeros.quantile(0.25) #25%
print(q1)

#faça 50% e 75%
q2 = numeros.quantile(0.5) #50%
print(q2)

q3 = numeros.quantile(0.75) #75%
print(q3)

#printe na tela
numeros.describe()



# In[18]:


# verificar dados nulos
df.info()


# # Numpy

# In[ ]:


[
  6.5, 7.0, 8.0, 9.5, 6.0, 7.5, 8.5, 9.0, 5.5, 6.0,
  7.0, 8.0, 9.0, 10.0, 6.5, 7.5, 8.5, 9.5, 6.0, 5.0,
  4.0, 5.5, 6.0, 7.0, 8.0, 9.0, 6.5, 7.5, 8.5, 9.5,
  6.0, 7.0, 8.0, 9.0, 10.0, 6.5, 5.0, 4.5, 5.5, 6.5,
  7.5, 8.0, 9.0, 6.0, 5.0, 4.5, 5.5, 6.5, 7.5, 8.5
]


# In[22]:


notas_uniformes = np.random.uniform(low=0, high=10, size=50)
notas = np.round(notas_uniformes, 1)
notas


# 1. Aplicarem uma operação vetorizada (ex: +1 em todas as notas)
# 
# 

# In[23]:


print(notas + 1)


# 2. Calcularem média, desvio padrão e nota mínima
# 

# In[25]:


media_notas = np.mean(notas)
dp_notas = np.std(notas)
min_notas = np.min(notas)

print(f"Média das notas {media_notas}\n Desvio padrão {dp_notas}\n Nota minima {min_notas}")


# 3. Filtrarem as notas acima da média

# In[26]:


print(notas[notas > media_notas])


# # Matplotlib

# 1. Utilizando um data set do drive,  faça:

# Um gráfico de linha

# In[28]:


df.columns


# Um gráfico de barras

# In[29]:


df[["nota1", "nota2", "nota2"]]


# Um histograma

# In[31]:


df["media"] = df[["nota1", "nota2", "nota3"]].mean(axis=1)
df


# In[32]:


import matplotlib.pyplot as plt


plt.figure(figsize=(8,5))
plt.plot(df.index, df["media"], marker='o')
plt.title("Média das Notas po Aluno")
plt.xlabel("Aluno")
plt.ylabel("Média")
plt.show()


# Obs: use as personalizações básicas apresentadas

# # Searborn

# 1. Utilizando um data set do drive,  faça:

# In[39]:


plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x=df.index, y="media")
plt.title("Média das Notas por Aluno")
plt.xlabel("Aluno")
plt.ylabel("Média")


# Um boxplot

# In[40]:


plt.figure(figsize=(8, 5))
sns.boxplot(data=df[["nota1", "nota2", "nota3"]])
plt.title("Boxplot das Notas")
plt.ylabel("Notas")
plt.show()


# Um histograma com kernel

# In[37]:


plt.figure(figsize=(8, 5))
sns.histplot(data=df[["nota1", "nota2", "nota3"]], kde=True)
plt.title("Histograma com Kernel das Notas")
plt.ylabel("Frequência")
plt.show()


# Um gráfico de dispersão

# In[38]:


plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="nota1", y="nota2")
plt.title("Gráfico de Dispersão das Notas")
plt.xlabel("Nota 1")
plt.ylabel("Nota 2")

