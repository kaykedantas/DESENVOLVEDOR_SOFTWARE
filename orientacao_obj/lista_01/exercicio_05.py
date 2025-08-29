"""
Implemente uma classe Impressora com o método
imprimir(Documento d), que recebe um objeto da classe
Documento e imprime suas informações na tela. A classe
Documento deve conter os atributos título e conteúdo. A
classe Impressora apenas utiliza o documento, sem manter
uma referência permanente a ele, caracterizando uma relação
de dependência. Desenvolva um programa com um menu
interativo no console que permita criar vários documentos,
visualizar seu conteúdo por meio da impressora e encerrar o
programa.

"""
class Documento:
    def __init__(self,titulo,conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        
    def get_titulo(self):
        return self.titulo
    def get_conteudo(self):
        return self.conteudo
        

class Impressora:
    def __init__(self):
        self.documentos = []
        
    def adicionardocumento(self,documento):
        self.documentos.append(documento)
    def listar_documentos(self):
        if not self.documentos:
            print("Sem documentos")
        else:
            for doc in self.documentos:
                print(f"Titulo documento:{doc.get_titulo() }, conteudo: {doc.get_conteudo()}")
impressora = Impressora()


while True:
    escolha = int(input("1-Adicionar um documento\n2-listar documentos\n3-encerrar\nescolha:"))
    if escolha == 1:
        titulo= input("digite o titulo do documento:")
        conteudo = input("digite o conteudo do documentos:")
        doc = Documento(titulo,conteudo)
        impressora.adicionardocumento(doc)
    elif escolha == 2:
        impressora.listar_documentos()
    else:
        break

    