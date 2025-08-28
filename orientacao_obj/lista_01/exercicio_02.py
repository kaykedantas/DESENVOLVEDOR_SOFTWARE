
"""
Faça um programa em Python orientado a objetos que, a
partir de uma string digitada pelo usuário, imprima:
◦ O número de caracteres da string;
◦ A string com todas suas letras em maiúsculo;
◦ A string com todas suas letras em minúsculo;
◦ O número de vogais da string;
◦ Se a substring “IFB” aparece no texto (ignorando
maiúsculas/minúsculas).
"""
class AnaliseTexto:
    def __init__(self, texto):
        self.texto = texto
    def tamanho(self):
        i=0
        for palavra in self.texto:
            if palavra != " ":
                i+=1
        return i
        #return len(self.texto)
    def maiusculo(self):
        return self.texto.upper()
    def minusculo(self):
        return self.texto.lower()
    def vogais(self):
        v="aeiou"
        #v=["a","e","i","o","u"]
        i=0
        for texto in self.texto.lower():
            if texto in v:
                i+=1
        return i             
    def contem_IFB(self):
        return "ifb" in self.texto.lower()
palavra = "Kayke  "
pa=AnaliseTexto(palavra)
print(f"tamanho da palavra:{pa.tamanho()}")
print(f"quantidade de vogais:{pa.vogais()}")
print(f"palavra em maiusculo:{pa.maiusculo()}")
print(f"palavra en minusculo:{pa.minusculo()}")
if pa.contem_IFB(): 
    print("a palavra ifb aparece no texto")
else : 
    print("A palavra ifb nao aparece no texto")
        
    
