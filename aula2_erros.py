# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro


numero = 10
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")