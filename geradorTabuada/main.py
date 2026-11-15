from time import sleep
num = int(input('Digite um numero inteiro que deseja ver a tabuada: '))
print('\033[3;31;40m===== TABUADA =====\033[m')
print('\033[3;31;40mCalculando...\033[m')
sleep(3)
for c in range(1, 11):
    tabuada = num * c
    print(f'{num} x {c} = {tabuada}')
print('===== FIM =====')