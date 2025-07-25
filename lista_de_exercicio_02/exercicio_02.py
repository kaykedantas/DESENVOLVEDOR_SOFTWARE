"""
Faça um programa em Python que simula as operações de
um banco. O programa deve apresentar um menu com as
seguintes opções:
1. Depositar (O programa deve pedir o valor a ser
depositado e somá-lo ao saldo)
2. Sacar (O programa deve pedir o valor a ser sacado e
subtrair do saldo, desde que o valor seja menor ou igual
ao saldo disponível)
3. Consultar Saldo (O programa deve exibir o saldo
atual)
4. Sair (O programa termina)
O programa deve manter um saldo inicial de R$ 1000,00
e permitir ao usuário realizar depósitos e saques até que
ele escolha a opção "Sair".
"""
print("CAiXA ELETRONICO")
conta = 1000 
while True:
    escolha = int(input("1- Depositar\n2- Sacar\n 3- Consultar saldo\n4- Sair:"))
    
    if escolha == 1:
        deposito = float(input("Digite o valor que deseja depositar:"))
        conta = conta + deposito 
    elif escolha == 2:
        saque = float(input("Digite a quantidade que deseja sacar:"))
        if saque <= conta:
            conta = conta - saque
            print(f"saque efetuado com sucesso, no valor de R${saque}")
        else: 
            print("Não foi possivel efetuar o saque, saldo insuficiente para isso ")
    elif escolha == 3:
        print(f"Seu saldo atual é R${conta}")
    elif escolha == 4:
        break
