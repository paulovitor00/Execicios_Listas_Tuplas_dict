valores = []
for i in range(0, 3):
    v = int(input('Digite um valor: '))
    if i == 0 or v > valores[-1]:
        valores.append(v)
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                break
            pos += 1

print(f'O valores adicionados e colocados em ordem foram: {valores}')








