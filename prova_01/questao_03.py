"""
3. Simulador de caixa eletrônico (1,11).
Enunciado:
Implemente um algoritmo que:
 Inicie com saldo de R$ 500.
 Permita ao usuário:
1. Ver saldo
2. Sacar valor (verificando se há saldo suficiente)
3. Depositar valor
4. Sair
Use estruturas de decisão e laço de repetição.
Objetivo: simular interação com estrutura while, if, operações
aritméticas e controle de fluxo.
"""

conta = 500 

while True: 
    escolha = int(input("1.ver saldo\n2.sacar valor\n3.depositar valor\n4.sair"))

    if escolha == 1:
        print(f"seu saldo é: R${conta}")
    elif escolha == 2:
        saque = float(input("Digite o valor que deseja sacar:"))
        
        if saque > conta:
            print("Saque não efetuado, saque maior do que seu saldo")
        else: 
            conta = conta - saque
            print("Saque efetuado com sucesso.")
    elif escolha == 3:
        deposito = float(input("digite o valor que deseja depositar:"))
        conta = conta + deposito
        print("deposito efetuado com sucesso.")
    elif escolha == 4:
        break