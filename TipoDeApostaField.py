import random
if lista_de_apostasComeOut[0] > 0:
    soma_plb = random.randint(1,6) + random.randint(1,6) 
    if soma_plb == 7 or soma_plb == 11:
        saldo += valor_aposta_plb
        print("Você ganhou sua aposta do tipo Pass Line Bet! Seu saldo agora é de {0} fichas." .format(saldo))
    elif soma_plb == 2 or soma_plb == 3 or soma_plb == 12:
        saldo -= valor_aposta_plb
        print("Você perdeu sua aposta do tipo Pass Line Bet! Seu saldo agora é de {0} fichas." .format(saldo))
    else:
        fase = "Point"
        print("Agora você está na fase Point. Não poderão ser feitas mais apostas do tipo Pass Line Bet")