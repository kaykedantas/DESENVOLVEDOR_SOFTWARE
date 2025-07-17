"""
Nível Básico
Crie uma lista com 5 nomes e imprima cada nome usando um loop for.

Peça para o usuário digitar 3 números e armazene-os em uma lista. Depois mostre a soma desses números.

Crie uma lista com 10 números e mostre apenas os números pares.


"""
pares=[]
impares=[]

numeros=[ 1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero %2==0:
        pares.append(numero)
for numero in numeros:
    if numero %2==1:
        impares.append(numero)
print("pares:")
print(pares)
print("impares:")
print(impares)