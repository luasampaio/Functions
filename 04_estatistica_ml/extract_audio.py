import scipy.stats as stats


joao = ['hospital', 'especialidade', 'consulta' ]

maria = ['hospital', 'especialidade', 'exame' ]


corr, _ = stats.pearsonr (joao, maria)

print(corr)