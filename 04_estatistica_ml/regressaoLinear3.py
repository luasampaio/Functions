import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

# Dados das variáveis 'joao' e 'maria'
data = {
    'joao': ['Hospital', 'Especialidade', 'Consulta'],
    'maria': ['Hospital', 'Especialidade', 'Exame']
}

# Criando um DataFrame com os dados
df = pd.DataFrame(data)

# Usando a codificação one-hot para converter variáveis categóricas em variáveis numéricas
encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(df[['Hospital', 'Especialidade', 'Consulta','Exame']])

# Adicionando as variáveis numéricas ao DataFrame
df_encoded = pd.concat([df, pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Hospital', 'Especialidade', 'Consulta','Exame']))], axis=1)

# Criando o modelo de regressão linear
model = LinearRegression()

# Variáveis independentes (variáveis categóricas codificadas) e variável dependente (Paciente)
X = df_encoded.drop(['Paciente', 'Hospital', 'Especialidade', 'Consulta','Exame'], axis=1)
y = df_encoded['Paciente']

# Treinando o modelo
model.fit(X, y)

# Fazendo previsões
# Por exemplo, dados de um novo paciente com hospital 'hospital', especialidade 'especialidade' e consulta 'exame'
new_data = {'Hospital': [1], 'Especialidade': [2], 'Exame': [3],'Consulta':[4]}
new_df = pd.DataFrame(new_data)
new_encoded = encoder.transform(new_df)
predicted_patient = model.predict(new_encoded)

print("Paciente previsto para os dados fornecidos:", predicted_patient)
