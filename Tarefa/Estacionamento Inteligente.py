idade = int(input("Digite Idade."))
Tipo_Cadastro = input("Possui cadastro.") #[Funcionario],[ViP][cadastrado],[sem cadastro]
tipo_veiculo = input("Tipo de veiculo.[Carro],[Moto],[Caminhão]")


#Criar 3 regras de negocio
#Tipo de veiculo,(Caminhão) , (carro), (moto)
#Ordem de prioridade Funcionarios, VIPS , Cadastrado , sem cadastro.
#Veiculos de carga , prioridade para entrega nas docas.

#Controle de Vagas
vagas_total = 400
vagas_prioritarias = 100  # funcionarios + vip
vagas_pcd = 50
vagas_comuns = 250

if idade < 18:
    print("Entrada negada Menor de idade")
elif idade >= 18 and Tipo_Cadastro == True and tipo_veiculo ==["Carro"] or ["Moto"]:
    print("Entrada liberada! Bem-vindo ao estacionamento.")

elif tipo_veiculo == "caminhao":
    entrega = input("O caminhão está fazendo entrega? (sim/nao): ").lower()

    if entrega == "sim":
        print("Entrada liberada para docas.")
    else:
        print("Entrada negada! Caminhões só entram para entrega.")

def prioridade():
    Tipo_Cadastro = input("funcionario, vip, cadastrado, nenhum): ").lower()   

    if Tipo_Cadastro == "funcionario":
        print("Prioridade MÁXIMA - Acesso liberado imediatamente.")

    elif Tipo_Cadastro == "vip":
        print("Alta prioridade - Acesso preferencial.")

    elif Tipo_Cadastro == "cadastrado":
        print("Prioridade normal - Acesso permitido.")

    elif Tipo_Cadastro == "nenhum":
        print("Baixa prioridade - Necessário realizar cadastro.")

    else:
        print("Tipo inválido.")

def entrada_veiculo():
    global vagas_total, vagas_prioritarias, vagas_pcd, vagas_comuns

    Tipo_Cadastro = input("Tipo de usuário (funcionario, vip, pcd, comum): ").lower()

    if Tipo_Cadastro == "funcionario" or Tipo_Cadastro == "vip":
        if vagas_prioritarias > 0:
            vagas_prioritarias -= 1
            vagas_total -= 1
            print("Entrada liberada (vaga prioritária).")
        else:
            print("Sem vagas prioritárias disponíveis.")

    elif Tipo_Cadastro == "pcd":
        if vagas_pcd > 0:
            vagas_pcd -= 1
            vagas_total -= 1
            print("Entrada liberada (vaga PCD).")
        else:
            print("Sem vagas PCD disponíveis.")

    elif Tipo_Cadastro == "comum":
        if vagas_comuns > 0:
            vagas_comuns -= 1
            vagas_total -= 1
            print("Entrada liberada (vaga comum).")
        else:
            print("Sem vagas comuns disponíveis.")

    else:
        print("Tipo inválido.")

    print(f"\nVagas restantes:")
    print(f"Total: {vagas_total}")
    print(f"Prioritárias: {vagas_prioritarias}")
    print(f"PCD: {vagas_pcd}")
    print(f"Comuns: {vagas_comuns}")