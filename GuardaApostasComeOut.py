import random
while saldo > 0:
  inicio = input("Você quer jogar Craps? s/n") 
  lista_de_apostasComeOut = [0,0,0,0]
  if inicio == "s":
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