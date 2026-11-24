# instalacion en terminal: pip -m install [nombre de la libreria]
# numpy matplotlib turtle pandas
# [nombre de la libreria] docs -ai
# https://docs.python.org/3/

import numpy as np
from random import randint

arreglo1, arreglo2 = np.array( [ i for i in range(0,5) ] ), np.array([11,15,2,34,16])
print(arreglo1, arreglo2)
print(arreglo1 + 2*arreglo2)
