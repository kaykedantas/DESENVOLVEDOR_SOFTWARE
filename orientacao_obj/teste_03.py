from abc import ABC, abstractmethod
class Cavaleiro(ABC):
    def __init__(self, nome, signo, golpe_especial):
        self.nome = nome
        self.signo = signo
        self.golpe_especial = golpe_especial
    def apresentar(self):
        print(f"Eu sou {self.nome}, Cavaleiro de {self.signo}!")
    @abstractmethod
    def usar_golpe_especial(self):
        pass

class CavaleiroDeBronze(Cavaleiro):
    def usar_golpe_especial(self):
        print(f"{self.nome} usa o golpe: {self.golpe_especial}!")
class CavaleiroDeOuro(Cavaleiro):
    def usar_golpe_especial(self):
        print(f"{self.nome} invoca o golpe supremo: {self.golpe_especial}!")
seiya = CavaleiroDeBronze("Seiya", "Pégaso", "Meteoro de Pégaso")
shaka = CavaleiroDeOuro("Shaka", "Virgem", "Tesouro do Céu")
seiya.apresentar()
seiya.usar_golpe_especial()
shaka.apresentar()
shaka.usar_golpe_especial()