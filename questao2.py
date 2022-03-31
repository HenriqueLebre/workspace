############################## QUESTÃO-2 ###############################

idade = 0

idade = int(input("Informe sua idade: "))

if idade <= 16:
    print("Você não pode votar!")
elif idade >= 16 and idade < 18 or idade >= 70:
    print("Você pode votar, mas não é obrigado!")
else:
    print("Você é obrigado a votar!")

