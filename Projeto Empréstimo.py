Idade_Usuário = input("18")
salário_Usuário = float(input("2000"))
Tempo= int(input("2"))

if Idade_Usuário >= 18:
    print("Apto para Empréstimo")
elif Idade_Usuário >= 0 and Idade_Usuário < 18:
    print("NEGADO POR MENORIDADE")

if salário_Usuário >= 2000:
    print("Apto para Empréstimo")
elif salário_Usuário < 2000:
    print("Empréstimo Negado")
elif salário_Usuário >= 5000:
    print("Aprovação Automática")

if Tempo >= 2:
    print("Apto para Empréstimo")
elif Tempo >= 0 and Tempo < 2:
    print("Empréstimo negado")

if Idade_Usuário >= 18 and salário_Usuário >= 2000 and Tempo >= 2:
    print("Requisitos Para Empréstimo Aceito")
elif Idade_Usuário < 18 and salário_Usuário >= 2000 and Tempo >= 2:
    print("NEGADO POR MENORIDADE")