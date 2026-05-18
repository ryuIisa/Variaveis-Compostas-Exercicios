listanum = list()
for contagem in range(0, 5):
    valor = int(input('Digite um valor: '))
    if contagem == 0 or valor > listanum[-1]:
        listanum.append(valor)
        print('Adicionado ao final da lista...')
    else:
        índice = 0
        while índice < len(listanum):
            if valor <= listanum[índice]:
                listanum.insert(índice, valor)
                print(f'Adicionado na posição {índice} da lista')
                break
        índice += 1
print('▹▸▹▸▹' * 5)
print(f'Os valores digitados em ordem foram {listanum}')
