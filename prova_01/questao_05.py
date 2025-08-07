"""
5. Algoritmo com tratamento de erro (1,11).
Enunciado:
Crie um algoritmo que:
 Solicite ao usuário um número inteiro;
 Divida 10 por esse número;
 Se o usuário digitar 0 ou um valor inválido, mostre uma mensagem de erro e
solicite novamente.
Objetivo: entrada e validação, e controle de erro.
 Faça o fluxograma no Flowgorithm
"""
try:
    numero= int(input("digite um numero inteiro:"))
except:
    print ("você digitou um numero invalido, digite um numero inteiro.")
    
if numero == 0:
    print("valor invalido.")
else:
    calculo = 10/numero
    print(f"resultado:{calculo}")
    