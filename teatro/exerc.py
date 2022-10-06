


import numpy

opcao = 9
aberto = False
escolha = 'n'
ingresso = 0.0
prTotal = 0.0
reservados = 0
ocupados = 0
vendidas = 0

while opcao != 0:
    print('1 - Iniciar teatro')
    print('2 - Listar Posições')
    print('3 - Reservar poltrona')
    print('4 - Comprar Cadeira')
    print('5 - Encerrar Teatro')
    print('6 - Exibir parciais')
    print('0 - Encerrar o programa')
    opcao = int(input('Informe a opcao desejada: '))
    if not aberto:
        if opcao == 1:
            vendidas = 0
            ocupados = 0
            vendidas = 0
            aberto = True
            prTotal = 0
            linhas = 0
            colunas = 0
            while linhas < 1 or linhas > 20:
                linhas = int(input('Informe o total de fileiras que teremos: '))
            while colunas < 1 or colunas > 20:
                colunas = int(input('Informe o total de colunas que teremos: '))
            ingresso = float(input('Qual o preço do Ingresso: '))
            teatro = numpy.empty([linhas, colunas],dtype=object)
            for i in range(0,linhas):
                for j in range (0, colunas):
                    teatro[i,j] = 'V'
            posicoes = linhas * colunas
    else:
        if opcao == 1:
            if aberto:
                print('Impossível limpar o teatro. O mesmo ainda está limpo.')
        elif opcao == 2:
                print(teatro)
        elif opcao == 3:
            print(teatro)
            l = int(input('Informe a fileira desejada'))
            l -= 1
            c = int(input('Informe a coluna desejada'))
            c -= 1
            if teatro[l,c] == 'V':
                escolha = input('A vaga está vaga, deseja realmente reserva-la (s/n)?')
                if escolha == 's' or escolha == 'S' :
                    teatro[l,c] = 'R'
                    print('O valor a ser pago é ',ingresso*(30/100))
                    prTotal = prTotal + (ingresso * (30 / 100))
                    reservados += 1
            else:
                if teatro[l,c] == 'O':
                    print('Impossivel realizar a operação. A posição está ocupada já.')
        elif opcao == 4:
            print(teatro)
            l = int(input('Informe a fileira desejada'))
            l -= 1
            c = int(input('Informe a coluna desejada'))
            c -= 1
            if teatro[l,c] == 'V':
                escolha = input('A vaga está vaga, deseja realmente comprar (s/n)?')
                if escolha == 's' or escolha == 'S' :
                    teatro[l,c] = 'O'
                    print('O valor a ser pago é ',ingresso)
                    prTotal = prTotal + (ingresso)
                    ocupados += 1
            else:
                if teatro[l,c] == 'R':
                    escolha = input('A poltrona está reservada. Deseja realmente alterar para ocupada (s/n)?')
                    if escolha == 's' or escolha == 'S' :
                        teatro[l,c] = 'O'
                        reservados -= 1
                        print('O valor a ser pago é ',ingresso*(70/100))
                        prTotal = prTotal + (ingresso * (70/100))
                        ocupados += 1
        elif opcao == 5:
            parcial = (posicoes / 2) + 1
            vendidas = ocupados + reservados
            if vendidas > parcial:
                print('O espetáculo já atingiu o total de vendas necessárias.')
                print('Foram Vendidas no total ',vendidas,' poltronas')
                print('destas ',reservados,' poltronas reservadas')
                print('O total arrecadado foi de ',prTotal)
                aberto = False
            else:
                print('Impossível encerrar o espetáculo. Não atingido o mínimo necessário para encerramento.')
        elif opcao == 6:
            print('Valor do Ingresso (100%): ',ingresso)
            print('Total de Vendas até o momento: ',prTotal)
            print('Reservas:',reservados)
            print('Vendidos: ',ocupados)
            vendidas = reservados + ocupados
            print('Total entre vendas e reservas: ',vendidas)
            aberto = True



