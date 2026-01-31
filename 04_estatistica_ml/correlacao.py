import pandas as pd
from scipy.stats import chi2_contingency

# Vamos criar um DataFrame de exemplo com variáveis categóricas em strings
data = {
    'joao': ['hospital', 'especialidade', 'consulta'],
    'maria': ['hospital', 'especialidade', 'exame']
}

df = pd.DataFrame(data)

# Criação de uma tabela de contingência
contingency_table = pd.crosstab(df['joao'], df['maria'])

# Aplicando o teste qui-quadrado para calcular o coeficiente de contingência de Pearson
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Exibindo o coeficiente de contingência de Pearson
print(f"Coeficiente de contingencia de Pearson: {((chi2)/(chi2 + len(df) * (min(contingency_table.shape) - 1))) ** 0.5}")
