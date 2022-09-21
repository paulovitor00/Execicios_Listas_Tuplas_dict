contador = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
tupla = (n1, n2, n3, n4, n5)
for i in tupla:
    conta = i % 2
    if conta == 0:
        print(f'O número {i} é par')
for i in tupla:
   if 9 == i:
       contador = contador + 1
       print(f'O número 9 aparece {contador} vezes')
   if 9 not in tupla:
       print('Não tem nenhum número 9 na tupla')

if 3 in tupla:
    b = tupla.index(3) + 1
    print(f'A posição em que o primeiro ou único 3 se encontra é a: {b} posição')
    breakpoint()
else:
    print('O valor 3 não apareceu na tupla')
    breakpoint()

for i in tupla:
    print(i)
    if i % 2 == 0:
        print(f'O número {i} é um número par!')
    else:
        print('Não tem número par na tupla!')












