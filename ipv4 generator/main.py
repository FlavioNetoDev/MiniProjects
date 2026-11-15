import random
from time import sleep
print('===== IP GENERATOR =====')
print('1 - Gerar ipv4 aleatorio \n2 - Sair')
pergunta = int(input('Sua Resposta: '))

if pergunta == 1:
    for c in range(4):
        numeros = random.randint(0, 255)
        if c != 3:
            print(f'{numeros}',end = '.')
        else: 
            print(f'{numeros}')
elif pergunta ==2:
    print('Fechando...')
    sleep(3)
    exit()
else:
    print('Selecione uma opção válida: ')