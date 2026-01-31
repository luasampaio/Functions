import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Criando um DataFrame fictício
data = {
    'Variavel_Conhecida': [1, 2],
    'Variavel_Desconhecida': ['Hospital', 'Hospital', 'Especialidade', 'Especialidade','Exame', 'Consulta']
}

df = pd.DataFrame(data)

# Convertendo a variável desconhecida em números usando LabelEncoder
label_encoder = LabelEncoder()
df['Variavel_Desconhecida_Encoded'] = label_encoder.fit_transform(df['Variavel_Desconhecida'])

# Separando os dados conhecidos e desconhecidos
X_known = df[['Variavel_Conhecida']]
y_known = df['Variavel_Desconhecida_Encoded']

# Inicializando e treinando um modelo de regressão linear
model = LinearRegression()
model.fit(X_known, y_known)

# Fazendo previsões para a variável desconhecida
X_pred = [[60], [70]]  # Valores conhecidos para prever a variável desconhecida
predicted_unknown = model.predict(X_pred)

# Invertendo a codificação para obter os valores originais da variável desconhecida
predicted_unknown_labels = label_encoder.inverse_transform(predicted_unknown.astype(int))

# Exibindo os resultados
print("Valores conhecidos para prever a variavel desconhecida:")
print(X_pred)
print("Valores previstos para a variavel desconhecida:")
print(predicted_unknown_labels)
