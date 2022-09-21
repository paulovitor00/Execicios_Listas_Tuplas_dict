cont = 1
list = []
for i in range(0, 9):
    n = int(input(f'Digite o {cont}° número: '))
    cont += 1
    list.append(n)

for a in range(0, 3):
    print(f'[{list[a]}]', end=' ')
print()
for a in range(3, 6):
    print(f'[{list[a]}]', end=' ')
print()
for a in range(6, 9):
    print(f'[{list[a]}]', end=' ')











