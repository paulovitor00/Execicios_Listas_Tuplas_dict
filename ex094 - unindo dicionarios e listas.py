continuar = 'S'
pessoasdict = dict()
mulhereslist = list()
principal = list()
mediaIdade = list()
acimaMedia = list()

while continuar != 'N':

    pessoasdict['sexo'] = input('Digite o sexo.\n'
                                'F - feminino\n'
                                'M - masculino: ').upper()[0]
    while True:
        if pessoasdict['sexo'] in 'MF':
             break
        else:
            pessoasdict['sexo'] = input('ERRO!! DIGITE APENAS: F OU M.\n'
                                        'F - feminino\n'
                                        'M - masculino: ').upper()[0]
    pessoasdict['idade'] = int(input('Digite a idade: '))
    mediaIdade.append(pessoasdict['idade'])
    principal.append(pessoasdict.copy())
    if pessoasdict['sexo'] == 'F':
        mulhereslist.append(pessoasdict['nome'])
    pessoasdict.clear()
    continuar = input('Deseja cadastrar outra pessoa? S/N: ').upper()[0]

media = sum(mediaIdade) / len(principal)
for p in principal:
    if p['idade'] > media:
        acimaMedia.append(p['nome'])


print('=-'*30)
print(f'- Foram cadastradas {len(principal)} pessoas.')
print('- As mulheres cadastradas foram: ', end='')
for i in mulhereslist:
    print(f'{i}/', end=' ')
print()
print(f'- A média de idade das pessoas cadastradas é: {media} anos.')
print(f'- Pessoas com idade acima da média: ', end='')
for m in acimaMedia:
    print(f'{m}/', end=' ')
print('\n')
print('=-' * 30)
print('Fim da apresentação!')


