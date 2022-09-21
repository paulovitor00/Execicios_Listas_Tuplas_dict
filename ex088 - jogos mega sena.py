import random
import time
cont = 1
listprinc = []

jogos = int(input('Digite a quantidade de jogos que deseja realizar: '))
for i in range(jogos):
    j = random.sample(range(0, 100), 6)
    listprinc.append(j)
for c in range(jogos):
    print(f'{cont}° Jogo: {listprinc[c]}\n')
    cont += 1
    time.sleep(2)



