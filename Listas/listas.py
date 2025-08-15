produtos =[(1001,"Caneta",1.50),(1002,"Mochila",75.50),(1003,"Caderno",12.50),]

codigo_busca = int(input("digite o codigo de busca:"))



for produto in produtos:
    if produto[0] == codigo_busca:
        print(f"Produto encontrado:{produto[1]}, valor dele é: R${produto[2]}")
        break
    
else: 
    print("produto não encontrado.")