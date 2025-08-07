"""
1. Cadastro e Cálculo de Média (1,11).
Enunciado:
Crie um algoritmo que:
 Solicite o nome de um aluno e duas notas (de 0 a 10);
 Calcule a média aritmética;
 Mostre o nome do aluno e a situação: "Aprovado" (média ≥ 7), "Recuperação"
(entre 5 e 7) ou "Reprovado" (média < 5).
Objetivo: trabalhar entrada, saída, cálculo, decisão condicional.
"""

nome = input("digite seu nome:")
nota_01 = float(input("Digite a sua primeira nota:"))
nota_02 = float(input("Digite a sua segunda nota:"))
media = (nota_01+nota_02)/2

if media >= 7:
    print(f"Aluno:{nome}")
    print(f"Aprovado com a media final de:{media} pontos ")
elif media >= 5 and media <7:
    print(f"Aluno:{nome}")
    print(f"Recuperação, sua media final foi: {media} pontos")
elif media <5:
    print(f"Aluno:{nome}")
    print(f"Reprovado, sua media final foi:{ media } pontos")
