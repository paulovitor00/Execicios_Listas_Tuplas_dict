lista = list()
pares = list()
impares = list()
continuar = 's'
while continuar != 'n':
    n = int(input('Digite um número inteiro: '))
    continuar = input('Deseja continuar? \n'
                      's - para sim\n'
                      'n - para não: ')
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista principal foi: {lista} \n'
      f'a lista de números pares: {pares} \n e de números impares: {impares}')

