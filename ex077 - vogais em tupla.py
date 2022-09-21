Palavras = ('Esporte', 'Futevolei', 'Cerveja', 'Resenha', 'bebidas', 'bola', 'quadra', 'areia')
#for palavra in Palavras:
   #a = palavra.count('a')
   #e = palavra.count('e')
   #i = palavra.count('i')
   ##u = palavra.count('u')

   #print(f'\nNa palavra --{palavra}-- temos as vogais: ', end='')

   #if a > 0:
       #a = a * 'a'
       #print(a, end=' ')
   #if e > 0:
       #e = e * 'e'
       #print(e, end=' ')
   #if i > 0:
      #i = i * 'i'
       #print(i, end=' ')
   #if o > 0:
       #o = o * 'o'
       #print(o, end=' ')
   #if u > 0:
       #u = u * 'u'
       #print(u)

for p in Palavras:
    print(f'\nNa palavra --{p}-- temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')














