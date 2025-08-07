
"""
Você foi contratado para desenvolver um sistema simples 
para gerenciar um campeonato de futebol. O sistema deve 
usar um dicionário onde as chaves são os nomes dos times e 
os valores são os pontos conquistados. O programa deve 
apresentar o seguinte menu: 
1. Adicionar time: permite cadastrar um novo time com 0 
pontos iniciais. 
2. Registrar resultado de partida: o usuário informa os nomes 
de dois times e o resultado da partida (quantidade de gols de 
cada time). O programa atualiza os pontos dos times: 3 
pontos para o vencedor, 1 ponto para empate, 0 para o 
perdedor. 
3. Mostrar classificação: exibe a lista dos times e seus 
pontos, ordenada do maior para o menor número de pontos. 
4. Remover time: permite remover um time da competição. 
5. Sair 
O programa deve funcionar em loop até o usuário escolher 
sair. Utilizar função.
"""




# Dicionário para armazenar os times e seus pontos
tabela = {}

def adicionar_time():
    time = input("Digite o nome do time: ").strip()
    if time in tabela:
        print(f"O time '{time}' já está cadastrado.")
    else:
        tabela[time] = 0
        print(f"Time '{time}' adicionado com 0 pontos.")

def registrar_partida():
    time1 = input("Digite o nome do primeiro time: ").strip()
    time2 = input("Digite o nome do segundo time: ").strip()

    if time1 not in tabela or time2 not in tabela:
        print("Ambos os times devem estar cadastrados antes da partida.")
        return

    try:
        gols1 = int(input(f"Gols do {time1}: "))
        gols2 = int(input(f"Gols do {time2}: "))
    except ValueError:
        print("Os gols devem ser números inteiros.")
        return

    if gols1 > gols2:
        tabela[time1] += 3
        print(f"{time1} venceu! 3 pontos adicionados.")
    elif gols2 > gols1:
        tabela[time2] += 3
        print(f"{time2} venceu! 3 pontos adicionados.")
    else:
        tabela[time1] += 1
        tabela[time2] += 1
        print("Empate! 1 ponto para cada time.")

def mostrar_classificacao():
    if not tabela:
        print("Nenhum time cadastrado ainda.")
        return

    print("\n--- Classificação ---")
    classificacao = sorted(tabela.items(), key=lambda item: item[1], reverse=True)
    for pos, (time, pontos) in enumerate(classificacao, start=1):
        print(f"{pos}. {time} - {pontos} ponto(s)")
    print("----------------------")

def remover_time():
    time = input("Digite o nome do time a ser removido: ").strip()
    if time in tabela:
        del tabela[time]
        print(f"Time '{time}' removido da competição.")
    else:
        print(f"Time '{time}' não encontrado.")

def exibir_menu():
    print("\n==== MENU ====")
    print("1. Adicionar time")
    print("2. Registrar resultado de partida")
    print("3. Mostrar classificação")
    print("4. Remover time")
    print("5. Sair")

# Loop principal do sistema
while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        adicionar_time()
    elif opcao == 2:
        registrar_partida()
    elif opcao == 3:
        mostrar_classificacao()
    elif opcao == 4:
        remover_time()
    elif opcao == 5:
        print("Encerrando o programa. Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
