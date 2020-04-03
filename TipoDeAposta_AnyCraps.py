import random
if lista_de_apostasComeOut[2] > 0:
    soma_anycraps = random.randint(1,6) + random.randint(1,6)
    if soma_anycraps in {2,3,12}:
        saldo += valor_aposta_ac*7
        print("Você ganhou sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
    else:
        saldo -= valor_aposta_ac
        print("Você perdeu sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))