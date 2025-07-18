
conta = 0
while True:
    escolha = int(input("1-consultar saldo\n2-depositar dinheiro\n3-sacar dinheiro\n4-sair")) 
    if escolha == 1:
        print(f"seu saldo é: R${conta}")
    elif escolha == 2:
        deposito =float(input("Digite o valor que deseja depositar:"))
        conta=+ deposito
        print("deposito efetuado com sucesso.")
    elif escolha == 3:
        sacar = float(input("Digite o quanto deseja sacar:"))
        if sacar > conta:
            print("Não tem saldo suficiente em conta ")
        else: 
            conta= conta - sacar 
            print(f"saque efeutado com sucesso, tome aqui os seus {sacar} reais")
    elif escolha == 4:
        break

