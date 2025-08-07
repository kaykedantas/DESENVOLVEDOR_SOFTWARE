"""
 
Uma livraria quer controlar seu estoque usando um dicionário 
onde as chaves são os títulos dos livros e os valores são a 
quantidade disponível em estoque.  Implemente um programa 
com as seguintes funcionalidades: 
1. Adicionar um livro ao estoque: o usuário informa o título e a 
quantidade (se o livro já existir, some a quantidade nova à 
existente). 
2. Remover unidades de um livro: o usuário informa o título e 
a quantidade a remover; o programa deve atualizar o estoque 
e avisar se o estoque ficar zerado ou se o livro não existir. 
3. Consultar quantidade de um livro: o usuário digita o título e 
o programa mostra a quantidade disponível ou informa que o 
livro não está no estoque. 
4. Mostrar todos os livros com suas quantidades ordenados 
alfabeticamente. 
5. Sair 
O programa deve repetir o menu até que o usuário escolha 
sair. Utilizar função. 
"""






# Dicionário para armazenar o estoque de livros
estoque = {}

def adicionar_livro():
    titulo = input("Digite o título do livro: ").strip()
    try:
        quantidade = int(input("Digite a quantidade a adicionar: "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            return
    except ValueError:
        print("Quantidade inválida.")
        return

    if titulo in estoque:
        estoque[titulo] += quantidade
        print(f"{quantidade} unidades adicionadas ao livro '{titulo}'.")
    else:
        estoque[titulo] = quantidade
        print(f"Livro '{titulo}' adicionado ao estoque com {quantidade} unidades.")

def remover_livro():
    titulo = input("Digite o título do livro: ").strip()
    if titulo not in estoque:
        print(f"O livro '{titulo}' não está no estoque.")
        return

    try:
        quantidade = int(input("Digite a quantidade a remover: "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            return
    except ValueError:
        print("Quantidade inválida.")
        return

    if quantidade >= estoque[titulo]:
        print(f"Todas as unidades do livro '{titulo}' foram removidas do estoque.")
        del estoque[titulo]
    else:
        estoque[titulo] -= quantidade
        print(f"{quantidade} unidades removidas. Agora há {estoque[titulo]} unidades de '{titulo}'.")

def consultar_livro():
    titulo = input("Digite o título do livro: ").strip()
    if titulo in estoque:
        print(f"O livro '{titulo}' tem {estoque[titulo]} unidades disponíveis.")
    else:
        print(f"O livro '{titulo}' não está no estoque.")

def mostrar_todos_livros():
    if not estoque:
        print("O estoque está vazio.")
        return

    print("\n--- Estoque de Livros ---")
    for titulo in sorted(estoque):
        print(f"{titulo}: {estoque[titulo]} unidade(s)")
    print("-------------------------")

def exibir_menu():
    print("\n==== MENU ====")
    print("1. Adicionar um livro ao estoque")
    print("2. Remover unidades de um livro")
    print("3. Consultar quantidade de um livro")
    print("4. Mostrar todos os livros com suas quantidades")
    print("5. Sair")

# Loop principal
while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        adicionar_livro()
    elif opcao == 2:
        remover_livro()
    elif opcao == 3:
        consultar_livro()
    elif opcao == 4:
        mostrar_todos_livros()
    elif opcao == 5:
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
