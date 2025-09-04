


class Motor:
 def __init__(self, tipo):
    self.tipo = tipo
class Pneu:
 def __init__(self, marca):
    self.marca = marca
class Porta:
 def __init__(self, lado):
    self.lado = lado
class Carro:
 def __init__(self, modelo, motor, pneus, portas):
    self.modelo = modelo
    self.motor = motor # agregação
    self.pneus = pneus # lista objetos Pneu
    self.portas = portas # lista objetos Porta
 def exibir_info(self):
    print(f"Carro: {self.modelo}")
    print(f"Motor: {self.motor.tipo}")

    print("Pneus:  ")
    for pneu in self.pneus:
        print(f" - {pneu.marca}")
        print("Portas:")
    for porta in self.portas:
     print(f" - {porta.lado}")

# Criando as partes
motor_v8 = Motor("v8")
motor = Motor("AP")
pneus = [Pneu("Michelin"), Pneu("Michelin"), Pneu("Michelin"),
Pneu("Michelin")]
portas = [
 Porta("Dianteira esquerda"),
 Porta("Dianteira direita"),
 Porta("Traseira esquerda"),
 Porta("Traseira direita")
]
# Criando o carro com agregação
carro = Carro("Mustang GT", motor_v8, pneus, portas)
carro2 = Carro("chevette", motor, pneus,portas)
# Exibindo informações
carro.exibir_info()
carro2.exibir_info()