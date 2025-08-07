"""
Função que calcula o quadrado de um número (1,11).
Enunciado:
Crie um algoritmo que:
1. Solicite ao usuário um número inteiro.
2. Envie esse número para uma função chamada CalcularQuadrado, que retorne
o quadrado do número.
3. Mostre o resultado na tela.
4. Faça o fluxograma no Flowgorithm
"""

def CalcularQuadrado(x):
    resultado = x * x 
    return resultado

if __name__ == "__main__":
    numero = float(input("digite um numero para calcular a area de um quadrado."))
    print(CalcularQuadrado(numero))
    
