import numpy as np
import scipy.stats
x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

pearsons_coefficient = np.corrcoef(x, y)
print("Coeficiente Pearson: \n" ,pearsons_coefficient)


#analise com numpy para verificar a coeficiente
import numpy as np
import scipy.stats

x = np.arrange(10,20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])