"""
4. Contador de vogais (1,11).
Enunciado:
Faça um algoritmo que:
 Solicite uma palavra ao usuário;
 Conte quantas vogais existem na palavra;
 Mostre na tela o total de vogais.
Objetivo: uso de for, controle condicional e contadores.

"""


palavra= input("digite uma palavra")
tamanho_palavra = len(palavra)
print(tamanho_palavra)
lista_vogais =["a","e","i","o","u"]
vogais = 0
for i in range(0, tamanho_palavra ,1):
    if palavra[i] in lista_vogais:#"a" or "e" or "i" or "o" or "u"
        vogais= vogais + 1 
        


print(f"o total de vogais é: { vogais}")
