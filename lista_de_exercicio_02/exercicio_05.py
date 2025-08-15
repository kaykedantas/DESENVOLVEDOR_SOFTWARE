"""
Você foi contratado para desenvolver um pequeno sistema de
gerenciamento de uma lista de tarefas pessoais. Escreva um
programa em Python que utilize um menu interativo para
permitir ao usuário as seguintes opções:
1. Adicionar uma nova tarefa
2. Listar todas as tarefas
3. Remover uma tarefa pelo nome
4. Sair do programa
O programa deve manter as tarefas em uma lista e permitir
que o usuário realize várias operações até optar por sair.
Utilizar função.
"""
def listar(lista):
    for i,atividade in enumerate(lista, start=1):
        print(f"N°-{i}, {atividade}")
def adicionar(add,lista):
    lista.append(add)
    return lista
def excluir(nome, lista):
    try:
        lista.remove(nome)
    except:
        print("esta tarefa não existe na lista")
    return lista

if __name__ == "__main__":  
    lista=["varrer a casa"]
    while True:
        escolha = int(input("1. adicionar tarefa a lista\n 2. listar todas as tarefas\n 3. Remover uma tarefa pelo nome\n 4. Sair do programa\n Sua escolha:"))
        
        if escolha == 1:
            add = input("Digite o nome de uma nova atividade:")
            adicionar(add,lista)
            print(lista)
        elif escolha == 2:
            listar(lista)
        

        elif escolha == 3:
            tarefa_tirar =input("digite a tarefa que deseja excluir:")
            excluir(tarefa_tirar,lista)
            print(lista)
        elif escolha == 4:
            break

