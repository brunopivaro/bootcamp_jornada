const = 1000
nome = input("Digite seu nome:")
salario = float(input("Digite seu salário:"))
bonus = float(input("Digite o bônus:"))
kpi = const + salario * bonus

print(f"O usuário {nome} possui o bonûs de {kpi} reais")