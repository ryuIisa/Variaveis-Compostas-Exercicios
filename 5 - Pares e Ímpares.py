lista = []
pares = []
ímpares = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('‿︵' * 15)
print(f'A lista completa é {lista}')
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        ímpares.append(valor)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
