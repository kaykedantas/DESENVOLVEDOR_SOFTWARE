temperatura = float(input("Digite a temperatura em graus Celsius:"))

if temperatura < 0 :
    print("frio extremo")
elif temperatura >= 0 and temperatura <=10:
    print("Frio")
elif temperatura >= 11 and temperatura <=25:
    print("Ameno")
elif temperatura >= 26 and temperatura <= 35:
    print("Quente ")
else: 
    print("Muito Quente.")
