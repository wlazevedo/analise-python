import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregar os datasets
df_casos = pd.read_excel('CasosSudeste2020.xlsx')
df_obitos = pd.read_excel('ObitosSudeste2020.xlsx')

# Ajuste do tamanho da interface gráfica e adição das informações dos dados coletados dos datasets
plt.figure(figsize=(16, 12))
plt.figtext(0.1, 0.02, "Sudeste: 27/03/2020 a 31/12/2020", fontsize=10, color='gray')
plt.figtext(0.1, 0.01, "Atualização dos dados em 08/05/2024 às 15:31:27, com dados contidos nas Secretarias Estaduais de Saúde.", fontsize=10, color='gray')

# Análise de Casos Novos e Óbitos Novos por Semana Epidemiológica
sns.scatterplot(x='Semana_Ano', y='Casos Novos', data=df_casos, color='blue', label='Casos Novos')
sns.scatterplot(x='Semana_Ano', y='Obitos_novos', data=df_obitos, color='red', label='Óbitos Novos')
plt.xticks(rotation=45)
plt.title('Casos Novos e Óbitos Novos por Semana Epidemiológica na Região Sudeste no ano de 2020 - MG, ES, RJ e SP')
plt.xlabel('Semana/Ano')
plt.ylabel('Quantidade')
plt.legend()
plt.grid(True)  # Adiciona as grades ao gráfico

# Adição da linha de regressão para Casos Novos
X_casos = np.arange(1, len(df_casos)+1).reshape(-1, 1)
y_casos = df_casos['Casos Novos']
model_casos = LinearRegression()
model_casos.fit(X_casos, y_casos)
plt.plot([1, len(df_casos)], [model_casos.predict([[1]]), model_casos.predict([[len(df_casos)]])], color='blue', label='Linha de Regressão - Casos Novos')

# Adição da linha de regressão para Óbitos Novos
X_obitos = np.arange(1, len(df_obitos)+1).reshape(-1, 1)
y_obitos = df_obitos['Obitos_novos']
model_obitos = LinearRegression()
model_obitos.fit(X_obitos, y_obitos)
plt.plot([1, len(df_obitos)], [model_obitos.predict([[1]]), model_obitos.predict([[len(df_obitos)]])], color='red', label='Linha de Regressão - Óbitos Novos')

# Carregar os datasets
df_casos = pd.read_excel('CasosSudeste2020.xlsx')
df_obitos = pd.read_excel('ObitosSudeste2020.xlsx')

# Criar o gráfico de outliers para Casos Novos
plt.figure(figsize=(8, 6))
sns.boxplot(y='Casos Novos', data=df_casos, color='green', width=0.3)
plt.title('Gráfico de Outliers - Casos Novos na Região Sudeste no ano de 2020')
plt.ylabel('Casos Novos')
plt.grid(True)
plt.show()

# Criar o gráfico de outliers para Óbitos Novos
plt.figure(figsize=(8, 6))
sns.boxplot(y='Obitos_novos', data=df_obitos, color='orange', width=0.3)
plt.title('Gráfico de Outliers - Óbitos Novos na Região Sudeste no ano de 2020')
plt.ylabel('Óbitos Novos')
plt.grid(True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregar os datasets
df_casos = pd.read_excel('CasosSudeste2021.xlsx')
df_obitos = pd.read_excel('ObitosSudeste2021.xlsx')

# Ajuste do tamanho da interface gráfica e adição das informações dos dados coletados dos datasets
plt.figure(figsize=(16, 12))
plt.figtext(0.1, 0.02, "Sudeste: 01/01/2021 a 31/12/2021", fontsize=10, color='gray')
plt.figtext(0.1, 0.01, "Atualização do painel em 09/05/2024 às 15:31:34, com dados contidos nas Secretarias Estaduais de Saúde.", fontsize=10, color='gray')

# Análise de Casos Novos e Óbitos Novos por Semana Epidemiológica
sns.scatterplot(x='Semana_Ano', y='Casos Novos', data=df_casos, color='blue', label='Casos Novos')
sns.scatterplot(x='Semana_Ano', y='Obitos novos', data=df_obitos, color='red', label='Óbitos Novos')
plt.xticks(rotation=45)
plt.title('Casos Novos e Óbitos Novos por Semana Epidemiológica na Região Sudeste no ano de 2021 - MG, ES, RJ e SP')
plt.xlabel('Semana/Ano')
plt.ylabel('Quantidade')
plt.legend()
plt.grid(True)  # Adiciona as grades ao gráfico

# Adição da linha de regressão para Casos Novos
X_casos = np.arange(1, len(df_casos) + 1).reshape(-1, 1)
y_casos = df_casos['Casos Novos']
model_casos = LinearRegression()
model_casos.fit(X_casos, y_casos)
plt.plot([1, len(df_casos)], [model_casos.predict([[1]]), model_casos.predict([[len(df_casos)]])], color='blue', label='Linha de Regressão - Casos Novos')

# Adição da linha de regressão para Óbitos Novos
X_obitos = np.arange(1, len(df_obitos) + 1).reshape(-1, 1)
y_obitos = df_obitos['Obitos novos']
model_obitos = LinearRegression()
model_obitos.fit(X_obitos, y_obitos)
plt.plot([1, len(df_obitos)], [model_obitos.predict([[1]]), model_obitos.predict([[len(df_obitos)]])], color='red', label='Linha de Regressão - Óbitos Novos')

# Criar o gráfico de outliers para Casos Novos
plt.figure(figsize=(8, 6))
sns.boxplot(y='Casos Novos', data=df_casos, color='green', width=0.3)
plt.title('Gráfico de Outliers - Casos Novos na Região Sudeste no ano de 2021')
plt.ylabel('Casos Novos')
plt.grid(True)
plt.show()

# Criar o gráfico de outliers para Óbitos Novos
plt.figure(figsize=(8, 6))
sns.boxplot(y='Obitos novos', data=df_obitos, color='orange', width=0.3)
plt.title('Gráfico de Outliers - Óbitos Novos na Região Sudeste no ano de 2021')
plt.ylabel('Óbitos Novos')
plt.grid(True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregar os datasets
df_casos = pd.read_excel('CasosSudeste2022.xlsx')
df_obitos = pd.read_excel('ObitosSudeste2022.xlsx')

# Ajuste do tamanho da interface gráfica e adição das informações dos dados coletados dos datasets
plt.figure(figsize=(16, 12))
plt.figtext(0.1, 0.02, "Sudeste: 01/01/2022 a 30/12/2022", fontsize=10, color='gray')
plt.figtext(0.1, 0.01, "Atualização do painel em 09/05/2024 às 15:31:34, com dados contidos nas Secretarias Estaduais de Saúde.", fontsize=10, color='gray')

# Análise de Casos Novos e Óbitos Novos por Semana Epidemiológica
sns.scatterplot(x='Semana_Ano', y='Casos Novos', data=df_casos, color='blue', label='Casos Novos')
sns.scatterplot(x='Semana_Ano', y='Obitos novos', data=df_obitos, color='red', label='Óbitos Novos')
plt.xticks(rotation=45)
plt.title('Casos Novos e Óbitos Novos por Semana Epidemiológica na Região Sudeste no ano de 2022 - MG, ES, RJ e SP')
plt.xlabel('Semana/Ano')
plt.ylabel('Quantidade')
plt.legend()
plt.grid(True)  # Adiciona as grades ao gráfico

# Adição da linha de regressão para Casos Novos
X_casos = np.arange(1, len(df_casos)+1).reshape(-1, 1)
y_casos = df_casos['Casos Novos']
model_casos = LinearRegression()
model_casos.fit(X_casos, y_casos)
plt.plot([1, len(df_casos)], [model_casos.predict([[1]]), model_casos.predict([[len(df_casos)]])], color='blue', label='Linha de Regressão - Casos Novos')

# Adição da linha de regressão para Óbitos Novos
X_obitos = np.arange(1, len(df_obitos)+1).reshape(-1, 1)
y_obitos = df_obitos['Obitos novos']
model_obitos = LinearRegression()
model_obitos.fit(X_obitos, y_obitos)
plt.plot([1, len(df_obitos)], [model_obitos.predict([[1]]), model_obitos.predict([[len(df_obitos)]])], color='red', label='Linha de Regressão - Óbitos Novos')

# Criar o gráfico de outliers para Casos Novos em um gráfico separado
plt.figure(figsize=(8, 6))
sns.boxplot(y='Casos Novos', data=df_casos, color='green', width=0.3)
plt.title('Gráfico de Outliers - Casos Novos na Região Sudeste no ano de 2022')
plt.ylabel('Casos Novos')
plt.grid(True)
plt.show()

# Criar o gráfico de outliers para Óbitos Novos em um gráfico separado
plt.figure(figsize=(8, 6))
sns.boxplot(y='Obitos novos', data=df_obitos, color='orange', width=0.3)
plt.title('Gráfico de Outliers - Óbitos Novos na Região Sudeste no ano de 2022')
plt.ylabel('Óbitos Novos')
plt.grid(True)
plt.show()