prim_valor = input('Digite um valor: ')
seg_valor = input('Digite outro valor: ')

if prim_valor > seg_valor:
    print(f'{prim_valor=} é maior que {seg_valor=}.')
elif seg_valor > prim_valor:
    print(f'{seg_valor=} é maior que {prim_valor=}.')
elif prim_valor == seg_valor:
    print(f'{prim_valor=} e {seg_valor=} são iguais.')
else:
    print('Inválido')
