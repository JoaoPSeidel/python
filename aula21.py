"""entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(0 or False or 0 or 'abc')"""

senha = input('Senha: ') or 'Sem senha'
print(senha)
