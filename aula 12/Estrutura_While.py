# Cire um sistema aonde o valor inicial é de R$1000 e o usuário consiga realizar um saque e ao final seja exibido o valor restante do saldo.
Saldo = 1000
while Saldo > 0:
    saque = float(input("Digite o valor do saque: "))
    Saldo -= saque  #Saldo = Saldo - saque
    print(f'Saldo restante: {Saldo}')