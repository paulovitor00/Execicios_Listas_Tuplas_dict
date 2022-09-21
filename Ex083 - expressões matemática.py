pilha1 = []
pilha2 = []
expr = input('Digite uma expressão matemática: ')
for simb in expr:
    if simb == '(':
        pilha1.append(1)
    elif simb == ')':
        pilha2.append(1)

if len(pilha1) == len(pilha2):
    print(f'A expressão {expr} é válida!')
else:
    print(f'A expressão {expr} NÃO É VALIDA! :( ')

print(pilha2, pilha1)
