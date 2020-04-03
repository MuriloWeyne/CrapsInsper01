'''Esta é a versão final do Exercício Problema 1 de Design de Software.
   Aqui está implementado tudo que é necessário para que o jogo rode de maneira contínua.
   Quando comparado com os arquivos GuardaApostasComeOut e GuardaApostasPoint algumas linhas de código foram melhoradas e outras foram
   adicionadas para que o jogo rodasse da forma correta.
'''
import random
saldo = 5000
fase = "Come Out"
while saldo > 0:
  inicio = input("Você quer jogar Craps? s/n ") 
  lista_de_apostasComeOut = [0,0,0,0]
  if inicio == "s":
    if fase == "Come Out":
      print("Você está na fase Come Out. Podem ser realizadas apostas do tipo: Pass Line Bet, Field, Any Craps e Twelve.")
      aposta_plb = input("Você quer fazer uma aposta do tipo Pass Line Bet? s / n ")
      if aposta_plb == 's':
        valor_aposta_plb = int(input("Insira o valor de fichas que você deseja apostar em uma Pass Line Bet: "))
        lista_de_apostasComeOut[0]=valor_aposta_plb
      aposta_f = input("Você quer fazer uma aposta do Field? s / n ")
      if aposta_f == 's':
        valor_aposta_f = int(input("Insira o valor de fichas que você deseja apostar em uma Field: "))
        lista_de_apostasComeOut[1]=valor_aposta_f
      aposta_ac = input("Você quer fazer uma aposta do Any Craps? s / n ")
      if aposta_ac == 's':
        valor_aposta_ac = int(input("Insira o valor de fichas que você deseja apostar em uma Any Craps: "))
        lista_de_apostasComeOut[2]=valor_aposta_ac
      aposta_t = input("Você quer fazer uma aposta do tipo Twelve? s / n ")
      if aposta_t == 's':
        valor_aposta_t = int(input("Insira o valor de fichas que você deseja apostar em uma Twelve: "))
        lista_de_apostasComeOut[3]=valor_aposta_t
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
      if lista_de_apostasComeOut[1] > 0:
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
      if lista_de_apostasComeOut[2] > 0:
        soma_anycraps = random.randint(1,6) + random.randint(1,6)
        if soma_anycraps in {2,3,12}:
          saldo += valor_aposta_ac*7
          print("Você ganhou sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
        else:
          saldo -= valor_aposta_ac
          print("Você perdeu sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
      if lista_de_apostasComeOut[3] > 0:
        soma_twelve = random.randint(1,6) + random.randint(1,6)
        if soma_twelve == 12:
          saldo += valor_aposta_t*30
          print("Você ganhou sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))
        else:
          saldo -= valor_aposta_t
          print("Você perdeu sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))
    if fase == "Point":
      print("Como foi dito anteriormente, você agora está na fase Point e apostas do tipo Pass Line Bet não poderão ser realizadas mais.")
      lista_de_apostasPoint = [0,0,0]
      aposta_f = input("Você quer fazer uma aposta do tipo Field? s / n ")
      if aposta_f == 's':
        valor_aposta_f = int(input("Insira o valor de fichas que você deseja apostar em Field: "))
        lista_de_apostasPoint[0] =valor_aposta_f
      aposta_ac = input("Você quer fazer uma aposta do tipo Any Craps? s / n ")
      if aposta_ac == 's':
        valor_aposta_ac = int(input("Insira o valor de fichas que você deseja apostar em Any Craps: "))
        lista_de_apostasPoint[1] =valor_aposta_ac
      aposta_t = input("Você quer fazer uma aposta do tipo Twelve? s / n ")
      if aposta_t == 's':
        valor_aposta_t = int(input("Insira o valor de fichas que você deseja apostar em Twelve: "))
        lista_de_apostasPoint[2] =valor_aposta_t
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
        elif soma_field == soma_plb:
          saldo += valor_aposta_plb
          print("Você ganhou o Point! Seu saldo agora é de {0} fichas. Agora o jogo voltará para a fase Come Out." .format(saldo))
          fase = "Come Out"
        else:
          saldo += valor_aposta_f*3
          print("Você ganhou sua aposta do tipo Field! Seu saldo agora é de {0} fichas." .format(saldo))
      if lista_de_apostasPoint[1] > 0:
        soma_anycraps = random.randint(1,6) + random.randint(1,6)
        if soma_anycraps in {2,3,12}:
          saldo += valor_aposta_ac*7
          print("Você ganhou sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
        elif soma_anycraps == soma_plb:
          saldo += valor_aposta_plb
          print("Você ganhou o Point! Seu saldo agora é de {0} fichas. Agora o jogo voltará para a fase Come Out." .format(saldo))
          fase = "Come Out"
        else:
          saldo -= valor_aposta_ac
          print("Você perdeu sua aposta do tipo Any Craps! Seu saldo agora é de {0} fichas." .format(saldo))
      if lista_de_apostasPoint[2] > 0:
        soma_twelve = random.randint(1,6) + random.randint(1,6)
        if soma_twelve == 12:
          saldo += valor_aposta_t*30
          print("Você ganhou sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))
        elif soma_twelve == soma_plb:
          saldo += valor_aposta_plb
          print("Você ganhou o Point! Seu saldo agora é de {0} fichas. Agora o jogo voltará para a fase Come Out." .format(saldo))
          fase = "Come Out"
        else:
          saldo -= valor_aposta_t
          print("Você perdeu sua aposta do tipo Twelve! Seu saldo agora é de {0} fichas." .format(saldo))
  elif inicio == 'n':
    print("Okay, até a próxima!")