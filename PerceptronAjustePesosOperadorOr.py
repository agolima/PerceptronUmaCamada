import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
pesos = np.array([[0.0], [0.0]])
saidas = np.array([0, 1, 1, 1])
taxaAtualizacaoSinapse = 0.1



def stepFunction(valorSoma):
    if(valorSoma >= 1):
        return 1
    return 0

def calculoSaida(registro):
    #dot product / produto escalar
    valorSomatorio = registro.dot(pesos)
    return stepFunction(valorSomatorio);

def treinar():
    continuaLoop = True
    
    while(continuaLoop):
        totalErros = 0;
        for i in range (len(saidas)):
            valorCalculado = calculoSaida(np.asanyarray(entradas[i]))
            
            if(valorCalculado != saidas[i]):
                erro = abs(saidas[i] - valorCalculado)
                totalErros += erro;
                
                for j in range(len(pesos)):
                    pesos[j] = (pesos[j] + (taxaAtualizacaoSinapse * (entradas[i][j]) * erro))
                    print("Peso Atualizado: " + str(pesos[j]))
                    
        print(f"Total de erros: {totalErros}")
        
        if(totalErros > 0):
            continuaLoop = True
        else:
            continuaLoop = False
            


treinar()

#Códigos para verificação manual.
print("\r\nRede Neural Treinada. \r\n")
print("Valores da saída: ")
print(calculoSaida(entradas[0]))
print(calculoSaida(entradas[1]))
print(calculoSaida(entradas[2]))
print(calculoSaida(entradas[3]))
