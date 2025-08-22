
from abc import ABC, abstractmethod

"""
Você foi contratado para desenvolver um sistema para gerenciar
informações e estatísticas dos clubes participantes da Copa do Mundo
de Clubes da FIFA. Para isso, implemente uma classe abstrata chamada
ClubeParticipante com os atributos nome, pais, confederacao,
ranking_fifa, gols_marcados e vitorias, incluindo um método concreto
exibir_dados() para mostrar os dados do clube, e métodos abstratos
calcular_desempenho() — que deve calcular um índice baseado na
fórmula específica da confederação (para clubes da UEFA: desempenho
= vitórias × 3 + gols marcados × 0,5; para clubes da CONMEBOL:
desempenho = vitórias × 3 + gols marcados × 0,7) — e
gerar_relatorio_tecnico(), que deve exibir as informações básicas do
clube junto com o desempenho calculado. Crie duas subclasses
concretas, ClubeUEFA e ClubeCONMEBOL, que implementem esses
métodos de acordo com as regras definidas, e teste a aplicação criando
instâncias de cada tipo, demonstrando o uso de abstração, herança e
polimorfismo em Python.
"""
class ClubesParticipantes(ABC):
    def __init__(self, nome,pais,confederacao, ranking_fifa,gols_marcados,vitorias):
        self.nome = nome 
        self.pais = pais
        self.confederacao = confederacao 
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias
    def exibir_dados(self):
        print(f"Nome:{self.nome}\nPais:{self.pais}\nConfederacao:{self.confederacao}\nRanking Fifa:{self.ranking_fifa}\nGols:{self.gols_marcados}\nVitorias:{self.vitorias}")
    @abstractmethod
    def calcular_desempenho(self):
        pass
    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass
class ClubeUEFA(ClubesParticipantes):
    def __init__(self, nome, pais, ranking_fifa, gols_marcados, vitorias):
        super().__init__(nome, pais, "UEFA", ranking_fifa, gols_marcados, vitorias)
    def calcular_desempenho(self):
        return self.vitorias*3 + self.gols_marcados * 0,7
    def gerar_relatorio_tecnico(self):
        print(f"desempenho:{self.calcular_desempenho()}")
    
    
    
clube1 = ClubeUEFA("Real Madrid", "Espanha", 1, 10, 4)
clube1.gerar_relatorio_tecnico()
    
        
        
        


