try:
 num = int(input('Informe um número inteiro para a operação de divisão: ')) # Ex: digite 0 para simular erro
 resultado = 10 / num # Essa linha causará erro se
 num = 0
 print(f"Resultado da divisão: {resultado}")
except ZeroDivisionError:
 print('Erro: divisão por zero não é permitida.')
except ValueError:
 print('Erro: valor inválido. Digite um número inteiro.')