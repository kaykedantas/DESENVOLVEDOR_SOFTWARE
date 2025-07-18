custo_fabrica = float(input("digite o preco de custo do carro."))

imposto_fabrica= custo_fabrica*(30/100)
porcentagem_distribuidor = custo_fabrica *(12/100)
preco_venda= custo_fabrica+imposto_fabrica+porcentagem_distribuidor
print(f"o custo do carro para o consumidor sera de R${preco_venda}")