Entradas = [1, 7, 5]
Pesos = [0.8, 0.1, 0]


def calculaEntradasXPesos(entradas, pesos):
    somaValores = 0;
    
    for i in range(len(entradas)):
        somaValores += entradas[i] * pesos[i]
        
    return somaValores

def stepFunction(valorSoma):
    if(valorSoma >= 1):
        return 1
    return 0

calculoEntradasPesos = calculaEntradasXPesos(Entradas, Pesos)
valorStepFunction = stepFunction(calculoEntradasPesos)

print(calculaEntradasXPesos)
print(valorStepFunction)