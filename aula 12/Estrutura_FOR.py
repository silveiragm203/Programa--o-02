# Contar de 1 até 5 - 
#for número in range(1,6):
#    print(f'Eu sou o número {número}')

# Exemplo de Tabuada -> 5
i = 5 # Variável no escopo global
for número in range(1,11):
    total = i * número # Variável no escopo local
    print(f'5 x {número} = {total}')