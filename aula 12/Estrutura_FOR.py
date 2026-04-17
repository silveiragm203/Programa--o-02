# Contar de 1 até 5 - 
#for número in range(1,6):
#    print(f'Eu sou o número {número}')

# Exemplo de Tabuada -> 5
i = 5 # Variável no escopo global
for número in range(1,11):
    total = i * número # Variável no escopo local
    print(f'5 x {número} = {total}')

## Quando o Python encontra continue:
## Ele ignora o restante do código dentro do loop naquela volta ,Volta para o início do loop para a próxima repetição.

for i in range(5):
    if i == 2:
        continue
    print(i)

##O número 2 é pulado, porque o continue foi executado.