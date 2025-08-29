"""
Desenvolva uma classe Departamento com nome e um vetor
de objetos Funcionario, onde cada funcionário tem nome e
salário, permitindo que funcionários existam
independentemente do departamento para que possam ser
adicionados ou removidos livremente (agregação).
Implemente métodos no Departamento para adicionar
funcionários, calcular a média salarial e listar todos os
funcionários. Crie um programa com menu interativo no
console que permita criar departamentos, criar funcionários,
adicionar funcionários a departamentos, listar funcionários e
mostrar a média salarial, além de permitir sair do programa
"""

"""
funcionario:atributos(nome,salario)
Departamento:atributos(nome,lista de objetos(funcionarios))
departamento:motedodos: adicionar funcionarios, calcular media salaria e listar todos os funcionarios 
principal: criar departamentos,funcionario. adicionar funcionario e departamentos, listar departamentos e funcionario.
mostrar a media salarial e sair do programa 
"""
class Funcionario:
    def __init__(self, nome,salario):
        self.nome = nome 
        self.salario = salario
    
    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def set_salario(self, novo_salario):
        self.salario = novo_salario
        
class Departamento:
    def __init__(self, nome):
        self.nome= nome 
        self.funcionarios = []
        
    def addfuncionario(self,func):
        self.funcionarios.append(func)
    def media_salarial(self):
        i=0
        total = 0
        for funcionario in self.funcionarios:
           total = total + funcionario.get_salario()
           i+=1
        print(f"Media salarial do departamento {self.nome}")
        print(f"media salarial:{total}")
    def listar(self):
        print(f"funcionarios do departamento: {self.nome}")
        for i,funcionario in enumerate(self.funcionarios, start=1):
            print(f"{i}-nome funcionario{funcionario.get_nome()}, Salario:{funcionario.get_salario()}")
    
if __name__ == "__main__":
    funcionarios=[]
    departamentos=[]
    
    while True:
        escolha = int(input("1-criar funcionario\n2-criar departamento\n3-adicionar um funcionario a um departamento\n4-listar funcionarios de um departamento\n5-mostrar media salarial de um departamento\n6-Sair\nescolha:"))
        if escolha == 1:
            nome = input("Digite o nome do funcionario: ")
            salario = input("Digite o salario do funcionario:")
            func=Funcionario(nome,salario)
            funcionarios.append(func)
        elif escolha == 2:
            nome_departamento = input("Digite o nome do departamento que deseja criar:")
            dep = Departamento(nome_departamento)
            departamentos.append(dep)
        elif escolha == 3:
            for i,funcionario in enumerate(funcionarios, start=1):
                print(f"{i}-nome:{funcionario.get_nome()}, salario:{funcionario.get_salario()}")
            escolha_func = input("escolha:")
            for i, departamento in enumerate(departamentos, start=1):
                print(f"{i}-Departamento:{departamento.nome}")
            
        
        
    
    

        