"""
Crie um programa em Python que recebe um valor em reais e
o converte para outra moeda. Use um menu para escolher a
moeda de destino:
1. Dólar
2. Euro
3. Libra
4. Iene
O programa deve perguntar o valor em reais e exibir o
valor convertido para a moeda escolhida. Use valores
fictícios para as taxas de conversão:
1 Real = 0.19 Dólar
1 Real = 0.17 Euro
1 Real = 0.15 Libra
1 Real = 25 Ienes
"""

print("MENU-CONVERTA SEU REAL PARA QUALQUER MOEDA")
escolha= int(input("1- Dolar\n2- Euro\n3- Libra\n4- Iene:"))
real = float(input("digite a quantidade de real para conversão"))
conversao = 0 
if escolha == 1:
    conversao = real * 0.19
    print(f"{real} reais equivale a {conversao} dolares")
elif escolha == 2 :
    conversao = real * 0.17
    print(f"{real} reais equivale a {conversao} euros")
elif escolha == 3:
    conversao =real* 0.15
    print(f"{real} reais equivale a {conversao} libras")
elif escolha == 4:
    conversao = real * 25
    print= (f"{real} reais equivale a {conversao} Ienes")
