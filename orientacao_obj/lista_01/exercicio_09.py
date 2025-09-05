"""
Implemente em Python um sistema para uma plataforma de
cursos online que utilize herança e polimorfismo,
armazenando os dados em uma lista. Crie uma classe base
chamada Participante, com os atributos nome e email, e um
método emitirCertificado() que retorna uma mensagem
genérica. Em seguida, crie as subclasses Aluno, com o
atributo curso, e Instrutor, com o atributo especialidade,
ambas sobrescrevendo o método emitirCertificado() com
mensagens específicas: o aluno recebe um certificado de
conclusão do curso e o instrutor um certificado de participação
como palestrante. O programa deve conter um menu com as
opções: 1) Cadastrar participante, 2) Listar participantes, 3)
Emitir certificados, e 0) Sair. O usuário deve escolher entre
cadastrar um aluno ou instrutor, e os dados devem ser
armazenados em uma lista de objetos do tipo Participante. O
método emitirCertificado() deve ser chamado de forma
polimórfica para cada participante cadastrado.
"""

class Participante:
    def __init__(self,nome,email):
        self.nome = nome
        self.email=email
        
    def emitirCertificado(self):
        print(f"certificado impresso! parabens participante: {self.nome} , email:{self.email}")
        
class Instrutor(Participante):
    def __init__(self, nome, email,especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade
    def emitirCertificado(self):
        print(f"certificado impresso, Parabens Instrutor {self.nome}, email:{self.email}, especialidade:{self.especialidade}")
        
class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso
    def emitirCertificado(self):
        print(f"certificado impresso, Parabens {self.nome}, email: {self.email}, curso:{self.curso}")
        
    
participantes=[]
if __name__ == "__main__":
        while True:
            escolha = int(input("1-cadastrar participante\n2-Listar participantes\n3-Emitir certificados\n4-sair do programa.\nEscolha"))
            
            if escolha ==1:
                print("==cadastro de participantes")
                esc= int(input("1-cadastrar aluno\n2-cadastrar professor "))
                
                nome= input("Digite o nome:")
                email = input("Digite o email:")
                
                if esc == 1:
                    curso = input("digite o curso do aluno:")
                    aluno = Aluno(nome,email,curso)
                    participantes.append(aluno)
                    print("aluno incluido com sucesso!")
                elif esc == 2:
                    especialidade = input("digite a especialidade do instrutor:")
                    instrutor = Instrutor(nome,email,especialidade)
                    participantes.append(instrutor)
                    print("instrutor adicionado com sucesso!")
            elif escolha == 2:
                if not participantes:
                    print("nenhum participante cadastrado.")
                else:
                    for p in participantes:
                        if isinstance(p,Aluno):
                            print(f"aluno:{p.nome}, email:{p.email}, curso:{p.curso}")
                        elif isinstance(p,Instrutor):
                            print(f"Instrutor:{p.nome}, email:{p.email}, especialidade:{p.especialidade}")
            elif escolha ==3:
                for p in participantes:
                    p.emitirCertificado()
                    
            elif escolha ==4:
                break
                            