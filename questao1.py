############################## QUESTÃO-1 ###############################
def menu():
    print("Você deseja sua conta? ")
    print("1 - Sim, por favor me traga a conta.")
    print("2 - Não, vou continuar consumindo.")

    return int(input("Escolha a opção desejada: "))

desejo = 0

ocupaMesa = 0

conta = 0


while desejo != 2:
    desejo = menu()

    if desejo == 1:
        ocupaMesa = int(input("Informe a quantidade de pessoas: "))
        conta = float(input("Informe o valor total do consumo: "))
        taxaServ = float(input("Informe a taxa de serviço: "))
        
        contaTotal = conta + (conta * taxaServ / 100)
                
        diviConta =  (contaTotal / ocupaMesa)
        
        contaTotal = str(contaTotal).replace('.',',')
        diviConta = str(diviConta).replace('.',',')        
        
        print(f"Esse é o valor da sua conta total " + contaTotal + ", esse é o valor da conta divido por essa quantidade de pessoas ",ocupaMesa," divindo fica "+ diviConta +" \npara cada um e já incluindo a taxa de serviço.")

    elif desejo == 2:
        print("Pode continuar consumindo.")
                    
    else:
        print("Opção inválida.")
    break