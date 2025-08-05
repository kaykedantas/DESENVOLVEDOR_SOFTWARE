"""
Uma escola aplicou provas em várias turmas e deseja
registrar as maiores notas obtidas por seus alunos. Cada
nota é representada por uma tupla no formato:
(nome_do_aluno, nota, disciplina). Escreva um programa
com o seguinte menu interativo:

1. Adicionar nota: o usuário deve informar o nome do aluno,
a nota (float) e a disciplina, e esses dados devem ser
adicionados como uma nova tupla à lista.

2. Mostrar melhor aluno por disciplina: para cada disciplina
presente na lista, exiba o nome do aluno com a maior nota.

3. Consultar notas por aluno: o usuário digita o nome de um
aluno e o programa mostra todas as notas dele, com a
respectiva disciplina.

4. Exibir notas ordenadas (decrescente): mostre todas as
tuplas da lista ordenadas da maior para a menor nota, no
formato (nota, nome_do_aluno, disciplina).

5. Sair

O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Use tuplas para armazenar as notas
e manipule-as sem alterar sua estrutura original. Utilizar
função.

"""
alunos=[("Kayke Andrade",9.7,"TI"),]

while True:
    escolha = int(input("1. Para adiocionar uma nota a lista.\n 2. Mostrar maior nota de cada disciplina. \n 3. Consultar notas por aluno.\n 4. Exibir notas ordenadas\n 5. Sair"))
    if escolha == 1:
        nome_aluno=input("Digite o nome do aluno:")
        nota = float(input("Digite a nota do aluno:"))
        disciplina = input("Digite o nome da disciplina:")
        alunos.append((nome_aluno,nota,disciplina))
        for aluno in alunos:
            print(f"nome:{aluno[0]}, nota:aluno{aluno[1]}, discplina{aluno[2]}")
    elif escolha == 2:
        """
        2. Mostrar melhor aluno por disciplina: para cada disciplina
        presente na lista, exiba o nome do aluno com a maior nota.
        """
        """
        meu_dicionario = {
          "chave1": valor1,
          "chave2": valor2,
        }
        """
        melhores = {}#declara que vai ser um dicionario 
        for nome,nota,disciplina in  alunos:# aqui ele vai percorrer todo as tuplas da lista
            if disciplina not in melhores:# aqui vai fazer a verificacao se a disciplina nao existe no dicionario, se nao existir ela vai criar no dicionario e ja vai colocar um primeiro valor la
                melhores[disciplina] = (nome,nota)
            else: 
                if nota > melhores[disciplina][1]:# aqui ele vai verficar se a nota da lista de tuplas é maior do que a que esta no dicionario, se for ele substitui o nome e a nota.
                    melhores[disciplina]= (nome,nota)
            
        """        for aluno in  alunos:
            if aluno[2] not in melhores:
                melhores[aluno[2]] = (nome,nota)
            else: 
                if aluno[1] > melhores[dis]
                """
        

            
            

    elif escolha == 4:
        break
        



