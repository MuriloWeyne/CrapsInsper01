import random
if fase == "Point":
    print("Como foi dito anteriormente, você agora está na fase Point e apostas do tipo Pass Line Bet não poderão ser realizadas mais.")
    lista_de_apostasPoint = [0,0,0]
    aposta_f = input("Você quer fazer uma aposta do tipo Field? s / n")
    if aposta_f == 's':
        valor_aposta_f = int(input("Insira o valor de fichas que você deseja apostar em Field: "))
        lista_de_apostasPoint[0] = valor_aposta_f 
    aposta_ac = input("Você quer fazer uma aposta do tipo Any Craps? s / n")
    if aposta_ac == 's': 
        valor_aposta_ac = int(input("Insira o valor de fichas que você deseja apostar em Any Craps: "))
        lista_de_apostasPoint[1] = valor_aposta_ac 
    aposta_t = input("Você quer fazer uma aposta do tipo Twelve? s / n")
    if aposta_t == 's': 
        valor_aposta_t = int(input("Insira o valor de fichas que você deseja apostar em Twelve: "))
        lista_de_apostasPoint[2] = valor_aposta_t
    if lista_de_apostasPoint[0] > 0: 
        soma_field = random.randint(1,6) + random.randint(1,6)
        if soma_field in {3,4,9,10,11}:
          saldo += valor_aposta_f
          print("Você ganhou sua aposta do tipo Field! Seu saldo agora é de {0} fichas." .format(saldo))
        elif soma_field in {5,6,7,8}:
          saldo = 0
          print("Você perdeu tudo em sua aposta do tipo Field! Boa sorte na próxima vez.")
          break
        elif soma_field == 2:
          saldo += valor_aposta_f*2
          print("Você ganhou sua aposta do tipo Field! Seu saldo agora é de {0} fichas." .format(saldo))
        else:
          saldo += valor_aposta_f*3
          print("Você ganhou sua aposta do tipo Field! Seu saldo agora é de {0} fichas." .format(saldo))
    if lista_de_apostasPoint[1] > 0:
        soma_anycraps = random.randint(1,6) + random.randint(1,6)
        if soma_anycraps in {2,3,12}:
          saldo += valor_aposta_ac*7
          print("Você ganhou sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
        else:
          saldo -= valor_aposta_ac
          print("Você perdeu sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
    if lista_de_apostasPoint[2] > 0:
        soma_twelve = random.randint(1,6) + random.randint(1,6)
        if soma_twelve == 12:
          saldo += valor_aposta_t*30
          print("Você ganhou sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))
        else:
          saldo -= valor_aposta_t
          print("Você perdeu sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))