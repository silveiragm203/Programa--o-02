# Programa para analisar aprovação de empréstimo

def analisar_emprestimo(idade, salario, tempo_trabalho):
    # Regra: menor de idade sempre reprovado
    if idade < 18:
        return "Empréstimo NEGADO: cliente menor de idade."

    # Regra especial: salário alto
    if salario >= 5000:
        "Empréstimo APROVADO: aprovação instantânea por alto salário."

    # Regras padrão
    if idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
        print("Empréstimo APROVADO.")
    else:
        print("Empréstimo NEGADO: critérios não atendidos.")


# Entrada de dados
idade = int(input("Digite a idade do cliente: "))
salario = float(input("Digite o salário do cliente: "))
tempo_trabalho = float(input("Digite o tempo de trabalho (anos): "))

# Resultado
resultado = analisar_emprestimo(idade, salario, tempo_trabalho)
print(resultado)
