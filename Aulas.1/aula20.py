primeiro_valor = int (input('Digite um valor '))
segundo_valor = int (input('Digite outro valor '))

print (f'a soma dos numero é >= 10 ? {primeiro_valor + segundo_valor >=10}')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor = } é maior ou igual '
          f'ao  {segundo_valor = }')
else:
    print (f'{segundo_valor = } é maior do que {primeiro_valor}')