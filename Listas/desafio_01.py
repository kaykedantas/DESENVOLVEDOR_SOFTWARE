alunos= ["Matheus", "Debora", "Amanda", "Geovana"]
escolha = int(input("1-adicionar alguem a lista\n2-para excluir um aluno da lista pelo nome\n3-excluir algum aluno pela posição\n4-ordenar a lista\n5-visualisar o tamanho da lista"))

if escolha ==1:
    add= input("qual o nome do aluno a ser adicionado a lista")
    alunos.append(add)
    print(alunos)
elif escolha == 2:
    excluir =input("digite o nome do aluno a ser excluido:")
    try:
        alunos.remove(excluir)
        print("aluno excluido com sucesso")
        print(alunos)
    except:
        print("o aluno nao existe")
elif escolha == 3:
    posição = int(input("digite a posição que deseja excluir um aluno"))
    try:
        alunos.pop(posição)
        print("Posição excluida")
        print(alunos)
    except:
        print("essa posicao não existe")
elif escolha == 4:
    alunos.sort()
    print(alunos)
elif escolha == 5:
    print(f"tamanho da lista é:{len(alunos)}")
    
