import os 
from implement import *
import random

fila1 = MaxHeap()
fila2_fifo = []
qtd_pessoas = 0
tempo_preparo = 0
nome_reserva = ""

while True:
    os.system('color 6')
    print('''

    1 - Escolher tamanho da fila com prioridades
    
    2 - Adicionar novo grupo na fila com prioridades

    3 - Mostrar próximo grupo aguardando

    4 - Preparar próximo prato

    5 - Entregar prato

    6 - Gerar Simulação

    ''')

    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        tamanho = int(input('Digite o tamanho da fila com prioridades: '))
        fila1 = MaxHeap(tamanho)
        print('Fila com prioridades criada com sucesso!')
        input('Pressione ENTER para continuar...')
    elif opcao == 2:
        try:
            qtd_pessoas = int(input('Digite a quantidade de pessoas: '))
            tempo_preparo = int(input('Digite o tempo de preparo: '))
            nome_reserva = input('Digite o nome da reserva: ')
            fila1.put((qtd_pessoas, tempo_preparo, nome_reserva))
            print('Grupo adicionado com sucesso!')
            input('Pressione ENTER para continuar...')
        except:
            print('Fila lotada!')
            input('Pressione ENTER para continuar...')
    elif opcao == 3:
        print('Próximo grupo aguardando: ', fila1.peek())
        input('Pressione ENTER para continuar...')

    elif opcao == 4:
        fila2_fifo.append(fila1.get())
        print('Próximo grupo a ser preparado: ', fila2_fifo[-1])
        input('Pressione ENTER para continuar...')
    elif opcao == 5:
        fila2_fifo.pop(0)
        print('incluindo o nome do grupo!')

    elif opcao == 6:
        for i in range(0, 10):
            qtd_pessoas = random.randint(1, 10)
            tempo_preparo = random.randint(1, 10)
            nome_reserva = 'Grupo ' + str(i)
            fila1.put((qtd_pessoas, tempo_preparo, nome_reserva))
        print('Simulação realizada com sucesso!')
        input('Pressione ENTER para continuar...')