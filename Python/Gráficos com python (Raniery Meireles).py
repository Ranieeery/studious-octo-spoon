#!/usr/bin/env python
# coding: utf-8

# # **Construção de Gráficos com Matplot e Seaborn**

# ## Importando Bibliotecas

# In[1]:


# Importe bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## Inserindo Dataframe de Dados Qualitativos

# In[3]:


# Definir dataframe qualitativo
df_quali = pd.DataFrame({
    "Sabores de pizza": ["Calabresa", "Quatro Queijos", "Presunto", "A moda", "Frango a Bolonhesa"],
    "Valores": [10, 20, 15, 20, 35]
})


# ### Gráfico de Barras

# In[6]:


# Matplotlib

# Variáveis
pizza = df_quali['Sabores de pizza']
valores = df_quali['Valores']

# Criar gráfico
plt.bar(df_quali['Sabores de pizza'], df_quali['Valores'], color=['blue', 'green', 'red', 'purple', 'orange'])

plt.title('Gráfico de consumo de pizza')
plt.xlabel('Sabores de pizza')
plt.ylabel('Consumo')
plt.show()


# In[ ]:


#Seaborn

#Variáveis
pizza = df_quali['Sabores de pizza']
valores = df_quali['Valores']

#Criar gráfico
sns.barplot(x='Sabores de pizza', y='Valores', data=df_quali, palette=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Gráfico de consumo de pizza')
plt.show()


# ### Gráfico de Setores

# In[17]:


#Matplotlib

# Variáveis


#Criar gráfico
plt.pie(df_quali["Valores"], labels=df_quali["Sabores de pizza"], autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Gráfico de consumo de pizza')
plt.axis('equal')
plt.show()


# In[ ]:


#Seaborn

#Criar gráfico


# ## Inserindo Dataframe de Dados Quantitativos

# In[ ]:


#Definir dataframe quantitativo


# ### Gráfico de Linhas

# In[ ]:


#Matplotlib

#Construir gráficos


# In[ ]:


#Seaborn

#Construir gráficos


# ### Gráfico Boxplot

# In[ ]:


#Matplotlib

#Construir gráficos


# In[ ]:


#Seaborn

#Construir gráficos


# ---
# 
# 
# 
# # Análise com Dataframe Externo
# 
# 
# 
# ---
# 
# 

# ## Definir dataframe

# In[ ]:


#Inserir bibliotecas novamente se quiser
#Defina e visualize o dataframe


# ## Dados Qualitativos

# In[ ]:


#Matplotlib
#Barras


# In[ ]:


#Seaborn
#Barras


# In[ ]:


#Matplotlib
#Setores


# In[ ]:


#Seaborn
#Setores


# ## Dados Quantitativos

# In[ ]:


#Matplotlib
#Linhas


# In[ ]:


#Seaborn
#Linhas


# In[ ]:


#Matplotlib
#Boxplot


# In[ ]:


#Seaborn
#Boxplot

