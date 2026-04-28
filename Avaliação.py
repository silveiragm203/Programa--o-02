#Lista de Gerenciamento de Notas
Quantidade = int(input("Digite Quantos alunos: "))

Nomes = []
média_Final = 7.00
média_Reprovação = 4.00

for i in range(Quantidade):
    nome = input(f"Digite o nome{i + 1}: ")
    Nomes.append(nome)

    Notas = []

    Av1 = float(input("Digite sua nota 1: "))
    Av2 = float(input("Digite sua nota 2: "))
    Av3 = float(input("Digite sua nota 3: "))

    média =(Av1+Av2+Av3) / 3


    if média > média_Reprovação < média_Final:
        print("Você está de Recuperação. ")
    elif média <= média_Reprovação:
        print("Você está Reprovado. ")
    elif média >= média_Final:
        print("Você está Aprovado. ")
    
    print(f"Média do Aluno {nome} é: {média:.2f}")

    print("Lista de Alunos: ")
    for Aluno in Nomes:
        print(Aluno)

    Aluno = [nome,média] 
    Nomes.append(Aluno)

print('''---Resumo da turma---''')   

for Aluno in Nomes:
    print(f"Nome: {Aluno[0]}")
    print(f"Média: {Aluno[1]:.2f}")

