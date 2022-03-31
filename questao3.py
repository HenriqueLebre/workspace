############################## QUESTÃO-3 ###############################
nomeMaior = ''
notaMaior = 0.0



for competicao in range(1,6):
    
    nome = input(f'Informe o nome do {competicao}º participante: ')
    nota = float(input(f'Informe a nota do {competicao}° participante: '))

    if nota >= 0 and nota <= 10:
        if nota > notaMaior:
            nomeMaior = nome
            notaMaior = nota
            
    else:
        print('ERRO! Verique o valor informado.')
        exit() 

print(f'O(a) vencedor(a) foi {nomeMaior} com nota de {notaMaior}!')