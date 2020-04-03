#Este programa contém os códigos necessários para a fase Come Out do jogo Craps. Assume-se que todas estas linhas de códgi menos a "import random" estarão dentro de um loop while.
import random
if fase == "Come Out":
      aposta_plb = input("Você quer fazer uma aposta do tipo Pass Line Bet? s / n")
      if aposta_plb == 's': 
        valor_aposta_plb = int(input("Insira o valor de fichas que você deseja apostar em uma Pass Line Bet: ")) 
        lista_de_apostasComeOut[0]=valor_aposta_plb
      aposta_f = input("Você quer fazer uma aposta do Field? s / n")
      if aposta_f == 's':
        valor_aposta_f = int(input("Insira o valor de fichas que você deseja apostar em uma Field: "))
        lista_de_apostasComeOut[1]=valor_aposta_f
      aposta_ac = input("Você quer fazer uma aposta do Any Craps? s / n")
      if aposta_ac == 's':
        valor_aposta_ac = int(input("Insira o valor de fichas que você deseja apostar em uma Any Craps: "))
        lista_de_apostasComeOut[2]=valor_aposta_ac
      aposta_t = input("Você quer fazer uma aposta do tipo Twelve? s / n")
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
