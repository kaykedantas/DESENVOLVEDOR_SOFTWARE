"""
2. Menu interativo com repetição (1,11).
Enunciado:
Crie um algoritmo com um menu que permita ao usuário:
1. Inserir um nome em uma lista.
2. Listar os nomes adicionados.
3. Sair do programa.
O programa deve repetir o menu até o usuário escolher a opção de sair.
Objetivo: estruturas de repetição (enquanto), listas e controle com
condicional.

"""
nomes=[]

while True:
    escolha = int(input("1.para inserir um nome a lista\n2.listar nomes\n3.sair do programa\n escolha:"))
    if escolha == 1:
        nome = input("qual nome deseja colocar na lista:")
        try:
            nomes.append(nome)
            print("nome adicionado com sucesso")
        except:
            print("nome não adicionado, tente novamente")
    elif escolha == 2:
        for nome in nomes:
            print(nome)
    elif escolha == 3:
        break
