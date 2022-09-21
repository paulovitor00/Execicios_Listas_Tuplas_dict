aluno = {}
aluno['Nome'] = input('Digite o nome do(a) aluno(a): ')
aluno['Media'] = float(input('Digite a média do(a) aluno(a): '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado!'
else:
    aluno['Situacao'] = 'Reprovado!'

print(f'O nome do(a) aluno(a) é: {aluno["Nome"]} e está: {aluno["Situacao"]} com média: {aluno["Media"]}')
