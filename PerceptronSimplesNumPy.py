import numpy as np

Entradas = np.array([-1, 7, 5])
Pesos = np.array([0.8, 0.1, 0])


def calculaEntradasXPesos(entradas, pesos):
    return entradas.dot(pesos);
#dot product / produto escalar

def stepFunction(valorSoma):
    if(valorSoma >= 1):
        return 1
    return 0

calculoEntradasPesos = calculaEntradasXPesos(Entradas, Pesos)
valorStepFunction = stepFunction(calculoEntradasPesos)

print(calculaEntradasXPesos)
print(valorStepFunction)