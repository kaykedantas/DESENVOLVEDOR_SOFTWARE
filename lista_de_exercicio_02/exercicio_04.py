"""
4. Faça um programa em Python que imprima todos múltiplos de
x, entre 1 e 100, onde x é um número informado pelo usuário.
Utilizar função.
"""
def multiplos(x):
    for i in range(1, 100, 1):
        print(f"{x} x {i} = {x*i}")
if __name__ == "__main__":  
    multiplos(10)
    multiplos(5)