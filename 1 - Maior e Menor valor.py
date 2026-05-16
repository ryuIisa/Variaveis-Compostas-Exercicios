valores = list()
for contagem in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {contagem}: ')))
    maior = max(valores)
    menor = min(valores)
print('✦ · · · ' * 6)
print(f'Você digitou os valores: {valores}')

if len([ocorrência for ocorrência in valores if ocorrência == maior]) == 1:
    print(f'O maior valor digitado foi {maior} na posição ', end=' ')
else:
    print(f'O maior valor digitado foi {maior} nas posições ', end=' ')
for numero, valor in enumerate(valores):
    if valor == maior:
        print(f'{numero}...', end=' ')
print()
if len([ocorrência for ocorrência in valores if ocorrência == menor]) == 1:
    print(f'O menor valor digitado foi {menor} na posição ', end=' ')
else:
    print(f'O menor valor digitado foi {menor} nas posições ', end=' ')
for numero, valor in enumerate(valores):
    if valor == menor:
        print(f'{numero}...', end=' ')
print()
