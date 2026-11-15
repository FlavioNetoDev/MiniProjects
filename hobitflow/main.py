print('-' * 20)
print('     HobitFlow')
print('-' * 20)
habitos = []
c = 0
contagemhabitos = 0
while True:
    print('[ 1 ] - Cadastrar Hábitos \n[ 2 ] - Listar Hábitos \n[ 3 ] - Sair')
    resposta = int(input('Sua resposta: '))
    if resposta == 1:
        while c < 5:
            cadastrar = str(input('Quais hábitos deseja cadastrar? [5] Para parar: ')).strip().capitalize()
            if cadastrar == '5':
                break
            habitos.append(cadastrar)
            c += 1
    elif resposta == 2:
        if not habitos:
            print('-' * 23)
            print('Sem habitos cadastrados')
            print('-' * 23)

        print('=' * 20)
        print('     MEUS HABITOS')
        print('=' * 20)
        contagemhabitos = 0
        for habito in habitos:
            contagemhabitos += 1
            print(f'{contagemhabitos} - {habito}')

        print('=' * 20)    
        print(f'Hábitos: {contagemhabitos}/5')
        print('=' * 20)           
    elif resposta == 3:
        break
    else:
        print('Opção inválida, digite um numero correspondente')
print('Fechando aplicativo...')