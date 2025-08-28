"""
Crie um programa em Python utilizando herança para
representar um sistema simples de funcionários. Implemente
uma classe base chamada Funcionario, com os atributos nome
(String) e salarioBase (double), além de um método
calcularSalario() que retorna o salário base e um método
exibirDados() que imprime o nome e o salário. Em seguida, crie
uma subclasse chamada FuncionarioComissionado, que herda
de Funcionario e possui o atributo adicional comissao (double).
Essa subclasse deve sobrescrever o método calcularSalario()
para retornar a soma do salário base com a comissão, e
também sobrescrever exibirDados() para incluir a comissão nas
informações exibidas. Por fim, instancie um objeto de cada
classe e utilize os métodos definidos para mostrar os dados
dos funcionários.
"""
"""
funcionario:
atributos:
nome(string)
salariobase(double)
funcoes:
CalcularDados(retorna o salario )
exibirDados(imprime o nome e o salario)

subclasse():
FuncionarioComissionado(herda):
comissao(adicional de salario(double))
sobrescrever  metodo calcularsalario()

"""
class Funcionario:
    def __init__(self,nome,salariobase):
        self.nome = nome
        self.salariobase = salariobase
    
    def calcularsalario(self):
        print(f"Seu salario é:{self.salariobase}")
    def exibirdados(self):
        print(f"Nome:{self.nome}")
        print(f"salario:{self.salariobase}")
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salariobase, comissao):
        super().__init__(nome, salariobase)#aproveita o que ja foi feito no construtor de Funcionario
        self.comissao = comissao 
    def calcularsalario(self):
        return print(self.salariobase + self.comissao)
    def pq(self):
        print(f"Nome:{self.nome}\nSalario base:{self.salariobase}\nComissao:{self.comissao}\n Salario Total:{self.calcularsalario()}")

func1 = Funcionario("Kayke",1000)
func1.calcularsalario()
func1.exibirdados()

func2= FuncionarioComissionado("Sophia", 2000, 500)
func2.calcularsalario()
func2.exibirdados()



    


