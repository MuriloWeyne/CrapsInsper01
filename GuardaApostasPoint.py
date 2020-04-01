lista_de_apostasPoint = [0,0,0]
aposta_f = input("Você quer fazer uma aposta do tipo Field? s / n")
if aposta_f == 's':
        valor_aposta_f = int(input("Insira o valor de fichas que você deseja apostar em Field: "))
        lista_de_apostasPoint[0] =valor_aposta_f
aposta_ac = input("Você quer fazer uma aposta do tipo Any Craps? s / n")
if aposta_ac == 's':
    valor_aposta_ac = int(input("Insira o valor de fichas que você deseja apostar em Any Craps: "))
    lista_de_apostasPoint[1] =valor_aposta_ac
aposta_t = input("Você quer fazer uma aposta do tipo Twelve? s / n")
if aposta_t == 's':
    valor_aposta_t = int(input("Insira o valor de fichas que você deseja apostar em Twelve: "))
    lista_de_apostasPoint[2] =valor_aposta_t