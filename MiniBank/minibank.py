print('===== MINIBANK =====')
print()
print('1 - Consultar Saldo \n2 - Sacar dinheiro \n3 - Depositar dinheiro \n4 - Sair')
saldo = 1000
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    print('Seu saldo atual é de \033[32mR$\033[m {}'.format(saldo))

elif opcao == 2:
    sacar = float(input('Quanto deseja sacar?: '))
    if sacar < 0:
        print('Não é possivel sacar um valor negativo!!')
    elif sacar > saldo:
        print('Saldo insuficiente para o saque.')
    else:
        saldo -= sacar
        print('Saque realizado com sucesso')
        print('Saldo atual {}'.format(saldo))
elif opcao == 3:
    depositar = float(input('Quanto deseja depositar? '))
    if depositar <= 0:
        print('Não é possível depositar um valor negativo!!')
    else:
        saldo += depositar
        print('Deposito realizado com sucesso')
        print('Saldo atual {}'.format(saldo))
elif opcao == 4:
    print('\033[7;31mFechando o programa...\033[m')
else:
    print('\033[31mERRO! Digite um valor relacionado as opções acima\033[m')