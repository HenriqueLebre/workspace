import matplotlib.pyplot as plt


valorInicial = float(input('Informe o investimento incial: '))
dividendo = float(input('Fnforme o rendimento do período (%): '))
qtdeMeses = int(input('Informe a quantidade de meses: '))
investimentoMensal = float(input('Informe o aporte mensal: '))

print(f"Valor Inicial: R$ {valorInicial}")
print(f"Rendimento por período (%): {dividendo}",'%')
print(f"Aporte a cada período: R$ {investimentoMensal}")
print(f"Total de períodos: {qtdeMeses}")

def rendimento (valorInicial, dividendo, qtdeMeses, investimentoMensal):
    
    porcentagem = dividendo / 100
    montante = valorInicial
    rendaAcumulado = []
    totalMeses = []
    
    for meses in range(qtdeMeses):
        acumularJuros =  montante * porcentagem
        montante = montante + acumularJuros + investimentoMensal
        
        print(f"Após {meses + 1} período(s), o montante será de: R${montante:.2f}")
        rendaAcumulado.append(montante)
        totalMeses.append(meses)
        
    x = totalMeses
    y = rendaAcumulado
    
    plt.xlabel("Período")
    plt.ylabel("Investimento")
    plt.plot(x,y)
    plt.show()  
rendimento(valorInicial, dividendo, qtdeMeses, investimentoMensal)
