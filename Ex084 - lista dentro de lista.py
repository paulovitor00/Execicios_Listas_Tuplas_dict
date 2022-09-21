dados = list()
pessoas = list()
continuar = 's'
pesomenorcont = pesomaiorcont = 0

while continuar != 'n':
    dados.append(input('Digite o nome da pessoa: '))
    dados.append(int(input('Digite o peso da pessoa: ')))
    if len(pessoas) == 0:
        pesomaior = pesomenor = dados[1]
    else:
        if dados[1] > pesomaior:
            pesomaior = dados[1]
            print(f'O menor peso é agora: {pesomaior}')
        elif dados[1] < pesomenor:
            pesomenor = dados[1]
            print(f'O menor peso é agora: {pesomenor}')
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar? s/n: ')
print(f'Na lista principal foram cadastradas: {len(pessoas)} pessoas.')
print(f'O maior peso registrado foi: {pesomaior} e pertence as pessoas: ', end='')
for d in pessoas:
    if d[1] == pesomaior:
        print({d[0]}, end=' ')
print()
print(f'O menor peso registrado foi: {pesomenor} e pertence as pessoas: ', end='')
for d in pessoas:
    if d[1] == pesomenor:
        print({d[0]}, end=' ')


