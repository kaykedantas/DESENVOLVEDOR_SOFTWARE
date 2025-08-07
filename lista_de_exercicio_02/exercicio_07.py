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
alunos = [
    ("Kayke Andrade", 9.7, "TI"),
    ("Ana Beatriz", 8.5, "Matemática"),
    ("Lucas Silva", 7.2, "História"),
    ("Carla Mendes", 9.0, "TI"),
    ("João Pedro", 6.8, "Matemática"),
    ("Bruna Rocha", 8.9, "Português"),
    ("Felipe Souza", 7.5, "Geografia"),
    ("Mariana Lima", 9.3, "Português"),
    ("Rafael Gomes", 5.4, "História"),
    ("Luana Pereira", 10.0, "TI"),
    ("Thiago Martins", 8.7, "Geografia"),
    ("Paula Fernandes", 6.4, "História"),
    ("Igor Oliveira", 9.9, "Matemática"),
    ("Jéssica Dias", 8.1, "TI"),
    ("André Costa", 7.8, "Português"),
    ("Natália Ramos", 9.5, "Geografia"),
    ("Daniel Moreira", 6.3, "Matemática"),
    ("Camila Araújo", 8.6, "Português"),
    ("Vinícius Braga", 7.9, "TI"),
    ("Fernanda Castro", 9.2, "História"),
]

melhores = {}#declara que vai ser um dicionario

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
        for nome,nota,disciplina in alunos:#aqui ele vai percorrer todo as tuplas da lista
            if disciplina not in melhores:#aqui vai fazer a verificacao se a disciplina nao existe no dicionario, se nao existir ela vai criar no dicionario e ja vai colocar um primeiro valor la
                melhores[disciplina] = (nome,nota)
            else:
                if nota > melhores[disciplina][1]:# aqui ele vai verficar se a nota da lista de tuplas é maior do que a que esta no dicionario, se for ele substitui o nome e a nota.
                    melhores[disciplina] = (nome,nota)
        for disciplina, (nome,nota)in melhores.items():
            print(f"O melhor aluno da disciplina: {disciplina} é o {nome} com a nota de {nota}")
        
        """
        2. Mostrar melhor aluno por disciplina: para cada disciplina
        presente na lista, exiba o nome do aluno com a maior nota.
        """
        """
        meu_dicionario = {
          "chave1": (valor1,valor2),
           "chave2": valor2,
         }
        """

    elif escolha == 3:
        """
        3. Consultar notas por aluno: o usuário digita o nome de um
        aluno e o programa mostra todas as notas dele, com a
        respectiva disciplina.

        """
        escolha_nome = input("digite o nome do aluno:")
        for aluno in alunos:
            if aluno[0] == escolha_nome:
                print(f"aluno:{aluno[0]} disciplina:{aluno[2]}, nota:{aluno[1]}")
    elif escolha == 4:
        break
        



