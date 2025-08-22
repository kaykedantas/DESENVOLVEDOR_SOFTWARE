"""
 Implemente um sistema orientado a objetos em Python para
representar uma biblioteca com as classes Biblioteca, Livro,
Autor e Usuário, aplicando os conceitos de associação,
agregação, composição e dependência. A classe Autor deve
armazenar nome e nacionalidade; a classe Livro deve conter
título, ano e uma referência a um Autor (agregação). A
Biblioteca deve possuir um nome e ser responsável por criar e
armazenar os livros internamente (composição). A classe
Usuario deve conter o nome e manter uma referência à
Biblioteca à qual está associado (associação), além de possuir
um método para pegar um livro emprestado, usando
temporariamente o livro sem armazená-lo (dependência).

biblioteca: nome, armazenar livro
Livro: titulo , ano , autor(agregação)
Autor:nome, nacionalidade
Usuario: nome , e manter a referencia da biblioteca.

"""
class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome 
        self.nacionalidade  = nacionalidade

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []


    def adicionar_livro(self, titulo, ano , autor):
        novo_livro = Livro(titulo, ano, autor)
        self.livros.append(novo_livro)
    def listar_livros(self):
        for livro in self.livros:
            print(f"titulo:{livro.titulo} ano:{livro.ano} autor:{livro.autor.nome}, nacionalidade:{livro.autor.nacionalidade}")
class Usuario: 
    def __init__(self,nome,biblioteca ):
        self.nome = nome 
        self.biblioteca = biblioteca
    def pegar_livro(self, titulo):
        for livro in self.biblioteca.livros:
            if livro.titulo == titulo:
                print(f"livro:{livro.titulo} disponivel, emprestimo feito")
                return 
       
        print("Livro não encontrado, não temos esse livro aqui!")
biblioteca = Biblioteca("Biblioteca Central")
while True:
    escolha = int(input("1. Listar livros disponiveis\n2.Adicionar livros a biblioteca\n3.pegar livro emprestado\n4. Encerrar\n Escolha: "))
    if escolha == 1:
        biblioteca.listar_livros()
    elif escolha == 2: 
        titulo = input("Digite o nome do livro que deseja adicionar:")
        ano=int(input("Digite o ano do livro de deseja adicionar:"))
        autor_nome =input("digite o nome do autor")
        autor_nacionalidade = input("Digite a nacionalidade do autor")
        autor = Autor(autor_nome,autor_nacionalidade)

        biblioteca.adicionar_livro(titulo,ano,autor)
    elif escolha == 3:
        nome_usuario = input("Digite seu nome ")
        usuario = Usuario(nome_usuario,biblioteca)
        titulo = input("digite qual livro deseja pegar emprestado:")
        usuario.pegar_livro(titulo)
    elif escolha == 4:
        break


    