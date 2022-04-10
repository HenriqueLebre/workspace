def imprimirGasto(tipoGasto , percentualMaximo, gasto, renda):
    percentual = calcularPercentual(gasto, renda)
    msg = obterMsg(gasto, renda, percentualMaximo, percentual)
    print(f"Seus gastos totais com {tipoGasto} comprometem {percentual}% de sua renda total. O máximo recomendado é de {percentualMaximo}%. {msg}")
    
def calcularPercentual(gasto, renda):
    return gasto * 100 / renda

def calcularValorMax(renda, percentualMaximo):
    return renda * percentualMaximo / 100

def obterMsg(gasto, renda, percentualMaximo, percentual):
    msg = "Seus gastos estão dentro da margem recomendada."
    if percentual > percentualMaximo:    
        msg =f"Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {calcularValorMax(renda, percentualMaximo)}."
        
    return msg     

print("####################################################################")
print("############################ BEM VINDO #############################")
print("############################## AO ##################################")
print("###################### APP DE CALCULAR GASTOS ######################")
print("####################################################################")

print("Primeiro Informa qual o percentual que você pode gastar da sua renda mensal Total ")

percentualMaximoMoradia = float(input("Informe o percentual Máximo com moradia: "))
percentualMaximoEducacao = float(input("Informe o percentual Máximo com Educacao: "))
percentualMaximoTransporte = float(input("Informe o percentual Máximo com Transporte:"))

rendaMensal = float(input("Renda mensal Total: R$ "))
gastoMoradia = float(input('Gastos totais com moradia: R$ '))
gastoEducacao = float(input('Gastos totais com educação: R$ '))
gastoTransporte = float(input('Gastos totais com transporte: R$ '))


calcularPercentual(gastoMoradia, rendaMensal)

print("Diagnóstico:")
imprimirGasto("Moradia", percentualMaximoMoradia, gastoMoradia, rendaMensal)
imprimirGasto("Educacao", percentualMaximoEducacao,  gastoEducacao, rendaMensal)
imprimirGasto("Transporte", percentualMaximoTransporte,  gastoTransporte, rendaMensal)
