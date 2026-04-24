# Sistema de Caixa de Supermercado
total_compra = 0
quantidade_produtos = 0

while True:
    valor = float(input("Digite o valor do produto (0 para finalizar): R$ "))
    if valor == 0:
        break

    total_compra += valor

    quantidade_produtos += 1

# cálculo da média
if quantidade_produtos > 0:
    media = total_compra / quantidade_produtos
else:
    media = 0

# desconto
if total_compra > 100:
    desconto = total_compra * 0.10
    total_final = total_compra - desconto
else:
    desconto = 0
    total_final = total_compra

# saída
print("\n--- RESUMO DA COMPRA ---")
print(f"Quantidade de produtos: {quantidade_produtos}")
print(f"Total sem desconto: R$ {total_compra:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print(f"Média dos valores: R$ {media:.2f}")
