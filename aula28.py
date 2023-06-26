nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é',  nome[::-1])
    if ' ' in nome:
        print('Seu nome contém espaço')
        print('Seu nome tem ', (len(nome)-1), 'letras')
    else:
        print('Seu nome não contém espaço')
        print('Seu nome tem ', (len(nome)), 'letras')

    print('A primeira letra do seu nome é ', nome[:0])
    print('A última letra do seu nome é ', nome[:-1])
else:
    print('Desculpe, você deixou campos vazios')
