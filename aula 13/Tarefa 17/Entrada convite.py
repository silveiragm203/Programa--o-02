Nome = input("Informe o nome.")
idade = int(input("Digite Idade."))
convite = input("Possui Convite? [sim],[não]")



if idade < 16:
    print("Entrada negada")
elif idade >= 16 and convite == "sim":
    print("Entrada Liberada")

    if convite == "sim":
        print("Entrada Liberada")
    else:
        print("Entrada Negada")

while True: 
    finalizar = input("Deseja encerrar Sessão? (sim para sair):")

    if finalizar == "sim":
        print("Sessão encerrada")
        break
    