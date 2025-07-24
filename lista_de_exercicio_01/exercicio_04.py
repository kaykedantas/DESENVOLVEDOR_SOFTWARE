p1 = float(input("Digite a nota da primeira prova:"))
p2 = float(input("Digite a nota da segunda prova:"))
t1 = float(input("digite a nota do primeiro trabalho:"))
t2 = float(input("Digite a nota do segundo trabalho:"))
mp = (p1+p2)/2
mt = (t1+t2)/2
mf = mp*0.8+mt*0.2

if mf >= 6:
    print(f"aprovado com a nota final de: {mf}")
else: 
    print (f"reprovado, sua nota final foi: {mf}, para passar é necessario de 6")