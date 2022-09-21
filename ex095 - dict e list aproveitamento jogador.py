
dict = {}
aproveitamento = []
gols = []
total = 0
cont = 1
contGols = 0
continuar = 'S'
busca = 0

while continuar != 'N':
    dict['nome'] = nome = input('Digite o nome do jogador: ')
    partida = int(input('Quantas partidas o jogador participou? '))
    for i in range(partida):
        qntGols = int(input(f'Quantos gols ele marcou na {i+1}° partida? '))
        gols.append(qntGols)
    dict['gols'] = gols[:]
    total = sum(gols)
    dict['total'] = total
    aproveitamento.append(dict.copy())
    continuar = str(input('Deseja continuar? S/N: ')).upper()[0]
    gols.clear()
    dict.clear()

print()
print('No  jogador          gols     total')
for k, v in enumerate(aproveitamento):
    print(f'{k+1:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while busca != 999:
    busca = int(input('Deseja ver o aproveitamento de algum jogador?\n'
                      ' Se sim, digite o número dele. (para encerrar, digite: 999: '))
    if busca == 999:
        break
    if busca > len(aproveitamento):
        print('Digite um número válido:')
    else:
        busca = busca - 1
        print(f'Levantamento do jogador {aproveitamento[busca]["nome"]}: ')
        for i, v in enumerate(aproveitamento[busca]['gols']):
            print(f'    No jogo {i+1} fez: {v} gols')
        print('=-'*30)
print('Fim do programa')





