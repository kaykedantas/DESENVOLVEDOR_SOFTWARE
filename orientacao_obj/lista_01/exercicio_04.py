"""
Crie um programa em Python utilizando orientação a objetos
para gerenciar uma lista de produtos de um carrinho de
compras. Implemente uma classe chamada Produto, com
atributos privados (__nome, __preco e __quantidade) e
métodos públicos para acessar e modificar esses valores de
forma segura (getters e setters). Em seguida, implemente uma
classe CarrinhoDeCompras, que mantém uma lista de objetos
Produto e possui métodos para adicionar um produto ao
carrinho, remover um produto pelo nome, calcular o valor total
da compra e listar os produtos com suas quantidades e
preços individuais. O programa principal deve permitir que o
usuário adicione e remova produtos, visualize o conteúdo do
carrinho e o total da compra. Utilize encapsulamento para
proteger os dados dos produtos e boas práticas de
organização orientada a objetos.
"""

class Produto:
    
    def __init__(self,nome,preco,quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_quantidade(self):
        return self.__quantidade
    def set_nome(self,novo_nome):
        self.__nome = novo_nome
    def set_preco(self,novo_preco):
        self.__preco = novo_preco
    def set_quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade        
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    def addcarrinho(self,produto):
        self.produtos.append(produto)
    def remove(self,nome):
        for produto in self.produtos:
            if produto.get_nome() == nome.lowe():
                self.produtos.remove(produto)
                print(f"produto removido com sucesso")
            return
            print("o produto não foi excluido, tente novamente")
        
    def calcular_valor(self):
        total = 0 
        for produto in self.produtos:
            valor = 0
            valor = produto.get_preco() * produto.get_quantidade()
            total += valor 
            return total
    def listar(self):
        for produto in self.produtos:
            #print(f"nome:{produto.nome} preco:{produto.preco} quantidade;{produto.quantidade}")
            print(f"nome:{produto.get_nome()} preco:{produto.get_preco()} quantidade:{produto.get_quantidade()}")
if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()

    while True:
        print("\n=== MENU CARRINHO DE COMPRAS ===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Ver total da compra")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome, preco, quantidade)  # cria objeto Produto
            carrinho.addcarrinho(produto)
            print(f"Produto '{nome}' adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do produto a remover: ")
            carrinho.remove(nome)

        elif opcao == "3":
            carrinho.listar()

        elif opcao == "4":
            print(f"Valor total da compra: R${carrinho.calcular_valor():.2f}")

        elif opcao == "5":
            print("Saindo do programa... Obrigado por usar o carrinho!")
            break

        else:
            print("Opção inválida! Tente novamente.")
            
            
        
        
    
        

    

    
        