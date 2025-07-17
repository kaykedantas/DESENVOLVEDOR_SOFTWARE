# Criando listas
numeros = [10, 20, 30, 40]
nomes = ["Ana", "Bruno", "Carlos"]

# Acessando elementos
print(numeros[0])     # 10
print(numeros[-1])    # 40 (último elemento)

# Adicionando e removendo
numeros.append(50)
numeros.insert(2, 25)
numeros.remove(20)
print(numeros)        # [10, 25, 30, 40, 50]

# Ordenando
numeros.sort()
print(numeros)        # [10, 25, 30, 40, 50]

# Iterando
for n in numeros:
    print(n)

