#!/usr/bin/env python
# coding: utf-8

# # **Biblioteca Pandas**

# ### **Importando a biblioteca**

# In[4]:


import pandas as pd
import statistics as st


# ### **Criando um dataframe com dicionário**

# In[5]:


vendas = {
    "data": ["20/05/2025", "21/05/2025", "22/05/2025"],
    "lucro": ["50.000", "180.000", "350.000"],
    "marca":["Ford", "KIA", "Fiat"],
    "quantidade": ["1", "3", '5']
}

vendas_df = pd.DataFrame(vendas)




print("-"*50)
display(vendas_df)



# In[5]:





# ### **Vizualizando os Dados do Dicionário**

# In[ ]:


print(vendas)
print("-"*50)
print(vendas_df)

print("-"*50)
display(vendas_df)


# ### **Importando Arquivo e base de dados**

# In[8]:


#Importando base de dados externa - .csv

tempo_df = pd.read_csv("tempo.csv", sep=";")


# ### **Visualização dos dados**

# In[ ]:


# print(tempo_df)
# display(tempo_df)
tempo_df.head()


# print(tempo_df.head())


# ### **Análise Geral**

# In[ ]:


#shape
tempo_df.shape


# In[ ]:


#describe
tempo_df.describe


# In[9]:


#info()
tempo_df.info()


# In[ ]:


# Agrupando valores qualitativos
print("-"*25)

cond_ap = tempo_df.groupby(["Aparencia"]).size()
display(cond_ap)

print("-"*25)

cond_ve = tempo_df.groupby(["Vento"]).size()
display(cond_ve)

print("-"*25)

cond_jo = tempo_df.groupby(["Jogar"]).size()
display(cond_jo)

print("-"*25)


# ### **Verificando Dados Nulos**

# In[10]:


# verificando dados nulos
tempo_df.isnull().sum()


# ### **Limpando Dados Nulos**

# **Dados Qualitativos**

# In[13]:


# calculando a moda de vento
moda_vento = st.mode(tempo_df["Vento"])
print(moda_vento)


# In[11]:


# calculando a moda de aparencia
moda_aparencia = st.mode(tempo_df["Aparencia"])
print(moda_aparencia)


# Substituindo

# In[14]:


# #substituir  NAN pela moda no vento
tempo_df["Vento"].fillna(moda_vento, inplace=True)

display(tempo_df["Vento"])


# In[ ]:


#localizando dado e substituindo pela moda em aparencia
tempo_df.loc[tempo_df["Aparencia"] == "menos", "Aparencia"] = moda_aparencia
display(tempo_df["Aparencia"])


# **Dados Quantitativos**

# In[ ]:


#calcular a mediana de umidade
mediana_umidade = st.median(tempo_df["Umidade"])
print(mediana_umidade)


# In[ ]:


#calcular a mediana de temperatura
mediana_temperatura = st.median(tempo_df["Temperatura"])
print(mediana_temperatura)


# Substituindo

# In[ ]:


#substituindo dados nulos e discrepantes
tempo_df["Umidade"].fillna(mediana_umidade, inplace=True)
tempo_df.loc[tempo_df["Umidade"] > 100, "Umidade"] = mediana_umidade
tempo_df.loc[tempo_df["Umidade"] < 0, "Umidade"] = mediana_umidade

display(tempo_df["Umidade"])


# In[ ]:


#substituindo dado discrepante
tempo_df.loc[tempo_df["Umidade"] > 100, "Umidade"] = mediana_umidade


# ### **Checando correções**

# In[ ]:


tempo_df.isnull().sum()


# In[ ]:


display(tempo_df)

