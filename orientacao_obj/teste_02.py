class Calculadora:
 def operar(self, a=0, b=0, operacao="+"):
    if operacao == "+":
        return a + b
    elif operacao == "-":
     return a - b
    elif operacao == "*":
     return a * b
    elif operacao == "/" and b != 0:
        return a / b
    else:
      return "Operação inválida ou divisãopor zero"
calc = Calculadora()
print(calc.operar()) # 0 + 0 = 0
print(calc.operar(5)) # 5 + 0 = 5
print(calc.operar(5, 3)) # 5 + 3 = 8
print(calc.operar(5, 3, "-")) # 5 - 3 = 2
print(calc.operar(5, 3, "*")) # 5 * 3 = 15
print(calc.operar(5, 0, "/")) # divisão por zero
print(calc.operar(5, 2, "/")) # 5 / 2 = 2.5