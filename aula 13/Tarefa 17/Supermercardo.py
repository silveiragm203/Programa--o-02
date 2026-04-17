Produto = input("nome do produto")
quantidade = float(input("Unidades."))
Valor_Produto = float(input("Valor em R$"))
Total = int == Produto * quantidade 


for Valor_Produto in range(1,15):
    print(f'{Valor_Produto} x {quantidade} = {Total}')


if Total > 100:
    print("Légivel para desconto de 10%")
elif Total <= 100:
    print("pagamento normal")