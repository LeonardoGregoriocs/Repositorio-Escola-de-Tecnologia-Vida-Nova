import os
from carro import Carro
from motorista import Motoristas

lista_de_carro = []
lista_de_motorista = []

def menu_carro():
    while True:
        print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
        print('\n1) Criar um veículo: \n2) Ver lista de veículo: \n3) Remover um veículo: \n4) Mudar a cor do carro: \n9) Menu Principal \n\n-> Digite zero para sair do programa\n')
        print('#-----------------------------------------------------------------------#')
        opcao = int(input('\nDigite a opção desejada: '))

        os.system('cls')

        if(opcao == 1):
            carro = Carro()
            lista_de_carro.append(carro)
            print('Carro cadastrado com ID: ', len(lista_de_carro))

        elif(opcao == 2):
            x = int(input('Qual a posição do veículo deseja visualizar: '))
            carro = lista_de_carro[x-1]
            carro.print_carro()

        elif(opcao == 3):
            x = int(input('Qual a posição do veículo deseja excluir: '))
            lista_de_carro.pop(x-1)

        elif(opcao == 4):
            x = int(input('Qual a posição do veículo que deseja alterar a cor: '))
            carro = lista_de_carro[x-1] 
            carro.trocar_cor()

        elif(opcao == 9):
            menu_principal()

        elif(opcao == 0): 
            break

        else:
            print('Digite um número válido!')

def menu_motorista():
    while True: 
        print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
        print('\n1) Criar um motorista: \n2) Ver lista de motorista: \n3) Remover um motorista: \n4) Alterar nome do motorista \n9) Menu Principal \n\n-> Digite zero para sair do programa\n')
        print('#-----------------------------------------------------------------------#')
        opcao = int(input('\nDigite a opção desejada: '))

        os.system('cls')

        if(opcao == 1):
            motorista = Motoristas()
            lista_de_motorista.append(motorista)
            print('Esse motorista tem o ID: ', len(lista_de_motorista))

        elif(opcao == 2):
            x = int(input('Digite o ID do motorista que deseja visualizar: '))
            motorista = lista_de_motorista[x-1]
            motorista.print_motorista()

        elif(opcao == 3):
            x = int(input('Digite o ID do motorista que deseja remover: '))
            lista_de_motorista.pop(x-1)

        elif(opcao == 4):
            x = int(input('Qual o ID do motorista que deseja trocar o nome: '))
            motorista = lista_de_motorista[x-1]
            motorista.trocar_nome()

        elif(opcao == 9):
            menu_principal()

        elif(opcao == 0): 
            break

        else:
            print('Digite um número válido!')   

def menu_principal():          
    while True: 
        print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
        print('\n 1) Menu veículo \n 2) Menu motorista \n\n-> Digite zero para sair do programa ')
        print('#-----------------------------------------------------------------------#')
        escolha = int(input('\nDigite a opção desejada: '))

        os.system('cls')

        if(escolha == 1): 
            menu_carro()

        elif(escolha == 2):
            menu_motorista()

        elif(escolha == 0):
            break  

menu_principal()
