"""
Par ou Ímpar (1,11).
Enunciado:
Faça um algoritmo que:
 Solicite um número ao usuário;
 Informe se o número é par ou ímpar.
Objetivo: decisão com if e operador módulo (%).
 Faça o fluxograma no Flowgorithm
"""

numero = float(input("Digite um numero para verificar: "))
if numero % 2 == 0:
    print("o numero digitado é par")
else: 
    print("o numero digitado é ìmpar")