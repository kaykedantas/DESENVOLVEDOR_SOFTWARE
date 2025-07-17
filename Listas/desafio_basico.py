"""
Nível Básico
Crie uma lista com 5 nomes e imprima cada nome usando um loop for.

Peça para o usuário digitar 3 números e armazene-os em uma lista. Depois mostre a soma desses números.

Crie uma lista com 10 números e mostre apenas os números pares.


"""
nomes= ["Marina", "Kayke", "Lara", "Sophia", "Rafael"]
for i,nome in enumerate(nomes,start=1) :
    print(f"{i}-{nome}")

    
numero1 = int(input("1 - Digite um número: "))
numero2 = int(input("2 - Digite um número: "))
numero3 = int(input("3 - Digite um número: "))

numeros = []
numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

print("Números digitados:", numeros)

soma =0
for numero in numeros:
    soma +=numero
    
print(f"a soma dos numeros sao:{soma}")

