import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados das variáveis 'joao' e 'maria'
data = {
    'joao': ['Hospital', 'Especialidade', 'Consulta'],
    'maria': ['Hospital', 'Especialidade', 'Exame']
}

# Criando um DataFrame com os dados
df = pd.DataFrame(data)

# Aplicando a codificação one-hot para converter variáveis categóricas em numéricas
df_encoded = pd.get_dummies(df)

# Calculando a correlação entre as variáveis usando o método de Pearson
correlation_matrix = df_encoded.corr()

# Criando o gráfico de heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Variáveis Categóricas')
plt.show()
