
dict = {}
aproveitamento = []
gols = []
total = 0
cont = 1
contGols = 0


dict['nome'] = nome = input('Digite o nome do jogador: ')
partida = int(input('Quantas partidas o jogador participou? '))

for i in range(partida):
    qntGols = int(input(f'Quantos gols ele marcou na {i+1}° partida? '))
    gols.append(qntGols)

dict['gols'] = gols
dict['total'] = sum(gols)
print('=-'*30)
aproveitamento = dict.copy()
print(aproveitamento)
print('=-'*30)
print(f'O jogador {dict["nome"]} jogou {partida} partidas.')
aproveitamento = dict.copy()
for k, v in dict.items():
    print(f'O campo {k} tem o valor: {v}.')
print('=-'*30)
print(f'No total o jogador: {dict["nome"]} fez: {sum(gols)} gols. ')
for k, v in enumerate(dict['gols']):
    print(f'    => Na {k+1}° partida, fez: {v} gols.')


