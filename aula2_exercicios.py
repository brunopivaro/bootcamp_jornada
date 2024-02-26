# Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input())
num2 = int(input())
soma = num1 + num2
print(f"O valor da soma dos dois números é {soma}")

# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input())
resto = num%5
print(f"O resto da divisão por 5 do número fornecido é {resto}")

# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1 = int(input())
num2 = int(input())
mult = num1 * num2
print(f"O valor da multiplicação dos dois números é {mult}")

# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1 = int(input())
num2 = int(input())
div = num1 / num2
print(f"O valor da divisão dos dois números é {div}")

# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = int(input())
quadrado = num**2
print(f"O resto da quadrado do número fornecido é {quadrado}")

# Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input())
num2 = float(input())
soma = num1 + num2
print(f"O valor da soma dos dois números é {soma}")

# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num1 = float(input())
num2 = float(input())
media = (num1 + num2)/2
print(f"A média dos dois números é {media}")

# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input())
expoente = float(input())
potencia = base ** expoente
print(f"A potência do número é de {potencia}")

# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input())
f = celsius * 9/5 + 32
print(f"A conversão da temperatura fornecida em Celsius para Fahrenheit é de {f}")

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
pi = 3.14
raio = float(input())
area = pi * raio**2
print(f"A área da circunferência é de {area}")

# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto =  str(input())
maiusculas = texto.upper()
print(f"O texto em maiúscula será: {maiuscula}")

# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome =  str(input())
minusculas = texto.lower()
print(f"O nome em minúscula será de : {minusculas}")

# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase =  str(input())
ajuste = texto.strip()
print(f"A frase sem espaços no início e no final será : {ajuste}")

# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input())
lista = data.split("/")
print("Dia: "+lista[0])
print("Mês: "+lista[1])
print("Ano: "+lista[2])

# Escreva um programa que concatene duas strings fornecidas pelo usuário.
str1 = str(input())
str2 = str(input())
print("A concatenação das suas duas strings será: "+ str1+str2)

# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
exp1 = input()
exp2 = input()
valor = exp1 and exp2
print(valor)

# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
exp1 = input()
exp2 = input()
valor = exp1 or exp2
print(valor)

# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
exp1 = input()
negacao = not exp1
print(negacao)

# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
exp1 = int(input())
exp2 = int(input())
valor = exp1 == exp2
print(valor)

# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
exp1 = int(input())
exp2 = int(input())
valor = exp1 != exp2
print(valor)