#!/usr/bin/env python
# coding: utf-8

# # **Atividade com Biblioteca Pandas**

# ## Importe a biblioteca

# In[24]:


#Importar Biblioteca
import pandas as pd
import statistics as st


# ## Importe o dataframe

# In[11]:


#Importar o dataframe
quali_vinho = pd.read_csv('qualidade_vinho.csv', sep=";")


# ## Faça a visualização dos dados

# In[12]:


#Visualizar dados
display(quali_vinho)


# ## Fazer uma análise geral

# In[22]:


#Utilize o .info() .describe() .shape()
#Utilize o groupby() e size() nos valores qualitativos
#Verifique se há valores nulos
print(quali_vinho.shape)

print("-"*50)

display(quali_vinho.describe)

print("-"*50)

display(quali_vinho.info())
display(quali_vinho.isnull().sum())

print("-"*50)

display(quali_vinho.groupby('qualidade').size())


# ## Limpe os valores nulos e corrija os valores discrepantes ou errados

# In[37]:


#Limpe os valores nulos e errados
display(quali_vinho.head())

moda_acucar = st.mode(quali_vinho["acucar residual"])
print(moda_acucar)

moda_densidade = st.mode(quali_vinho["desidade"])
print(moda_densidade)

quali_vinho.fillna({"acucar residual": moda_acucar}, inplace=True)
quali_vinho.fillna({"desidade": moda_densidade}, inplace=True)


# ## Verifique se está tudo certo

# In[38]:


#Verificando se os dados foram corrigidos
display(quali_vinho.isnull().sum())

