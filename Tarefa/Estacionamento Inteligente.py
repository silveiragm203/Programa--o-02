idade = int(input("Digite Idade."))
Tipo_Cadastro = float(input("Possui cadastro.")) #[Funcionario],[ViP][cadastrado],[sem cadastro]
tipo_veiculo = int(input("Tipo de veiculo.[Carro],[Moto],[Caminhão]"))
carga = int(input("Informe o tipo de carga"))


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
elif tipo_veiculo== "caminhao":
     entrega = input("O caminhão está fazendo entrega para as docas? (sim/nao): ")

if entrega == "sim":
      print("Entrada liberada para docas.")
else:
    print("Entrada negada! Caminhões só podem entrar para entregas.")

def verificar_prioridade():
    tipo = input("Digite o tipo (funcionario, vip, cadastrado, nenhum): ").lower()

    if tipo == "funcionario":
        print("Prioridade MÁXIMA - Acesso liberado imediatamente.")

    elif tipo == "vip":
        print("Alta prioridade - Acesso preferencial.")

    elif tipo == "cadastrado":
        print("Prioridade normal - Acesso permitido.")

    elif tipo == "nenhum":
        print("Baixa prioridade - Necessário realizar cadastro.")

    else:
        print("Tipo inválido.")

def entrada_veiculo():
    global vagas_total, vagas_prioritarias, vagas_pcd, vagas_comuns

    tipo = input("Tipo de usuário (funcionario, vip, pcd, comum): ").lower()

    if tipo == "funcionario" or tipo == "vip":
        if vagas_prioritarias > 0:
            vagas_prioritarias -= 1
            vagas_total -= 1
            print("Entrada liberada (vaga prioritária).")
        else:
            print("Sem vagas prioritárias disponíveis.")

    elif tipo == "pcd":
        if vagas_pcd > 0:
            vagas_pcd -= 1
            vagas_total -= 1
            print("Entrada liberada (vaga PCD).")
        else:
            print("Sem vagas PCD disponíveis.")

    elif tipo == "comum":
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