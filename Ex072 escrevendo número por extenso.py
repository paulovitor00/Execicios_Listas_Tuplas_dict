t1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

n = int(input('Digite um número de 0 até 10: '))
while n > 10 or n < 0:
    print('Digite um número válido!')
    n = int(input('Digite um número de 0 até 10: '))
c = n
print(f'Você digitou o número {t1[c]}')







