senha = 'Python123'
contador = 0
while contador < 3:
    senha1 = str(input('Digite a senha, vc possui 3 tentativas: '))
    contador += 1
    if senha1 == senha:
        print('Parabéns, login efetuado com sucesso.')
        break
    else:
        print('Senha incorreta.')