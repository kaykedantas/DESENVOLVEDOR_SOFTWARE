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
    def __init__(self, nome ):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, titulo, ano , autor):
        novo_livro = Livro(titulo, ano, autor)
        self.livros.append(novo_livro)
    def listar_livros():
        for livro in self.livros:
            print(f"titulo:{livro[0]} ano:{livro[1]} autor:{livro[2]}")
class Usuario: 
    def __init__(self,nome,biblioteca ):
        self.nome = nome 
        self.biblioteca = biblioteca
    def pegar_livro(self, titulo):
        for livro in self.biblioteca.livros:
            if livro.titulo == titulo:
                print(f"livro:{self.titulo} disponivel, emprestimo feito")

        

        