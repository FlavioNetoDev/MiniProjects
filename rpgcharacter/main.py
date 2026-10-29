print('\033[7;35;46m======ESCOLHA UMA CLASSE======\033[m')
print('1 - Guerreiro \n2 - Mago \n3 - Arqueiro')
escolha = int(input('Escolha: '))

if escolha == 1:
    name = str(input('Digite o nome do seu personagem: ')).lstrip()
    if name == '':
        print('Você precisa digitar um nome!')
        exit()
    else:
        print('===== PERSONAGEM CRIADO =====')
    hp = 1900
    ataque = 115
    defesa = 375
    print('{} \nCLASSE - GUERREIRO \nHP - {} \nATAQUE - {} \nDEFESA - {}'.format(name, hp, ataque, defesa))
elif escolha == 2:
    name = str(input('Digite o nome do seu personagem: ')).lstrip()
    if name == '':
        print('Você precisa digitar um nome!')
        exit()
    else:
        print('===== PERSONAGEM CRIADO =====')
    hp = 1350
    ataque = 295
    defesa = 140
    print('{} \nCLASSE - MAGO \nHP - {} \nATAQUE - {} \nDEFESA - {}'.format(name, hp, ataque, defesa))
elif escolha == 3:
    name = str(input('Digite o nome do seu personagem: ')).lstrip()
    if name == '':
        print('Você precisa digitar um nome!')
        exit()
    else:
        print('===== PERSONAGEM CRIADO =====')
    hp = 1220
    ataque = 230
    defesa = 185
    print('{} \nCLASSE - ARQUEIRO \nHP - {} \nATAQUE - {} \nDEFESA - {}'.format(name, hp, ataque, defesa))
else:
    print('Escolha uma das opções acima')
   