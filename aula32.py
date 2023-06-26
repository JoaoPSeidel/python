"""numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_inter = int(numero)
    par_impar = numero_inter % 2 == 0
    texto_par_impar = 'ímpar'

    if par_impar:
        texto_par_impar = 'par'

    print(f'O número {numero} é {texto_par_impar}')

else:
    print('Você não digitou um número inteiro')"""


'''entrada = input('Digite o horário em números inteiros')
try:
    entrada_int = int(entrada)

    if entrada_int >= 0 and entrada_int <= 11:
        print('Bom dia!')

    elif entrada_int >= 12 and entrada_int <= 17:
        print('Boa tarde!')

    elif entrada_int >= 18 and entrada_int <= 23:
        print('Boa noite')

    else:
        print('Não conheço essa hora')

except:
    print('Você não digitou um número inteiro')'''


nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')

elif tamanho_nome <= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')

elif tamanho_nome >= 7:
    print('Seu nome é grande')
