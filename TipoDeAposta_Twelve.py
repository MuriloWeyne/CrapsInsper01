import random
 if lista_de_apostasComeOut[3] > 0:
    soma_twelve = random.randint(1,6) + random.randint(1,6)
    if soma_twelve == 12:
        saldo += valor_aposta_t*30
        print("Você ganhou sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))
    else:
        saldo -= valor_aposta_t
        print("Você perdeu sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))