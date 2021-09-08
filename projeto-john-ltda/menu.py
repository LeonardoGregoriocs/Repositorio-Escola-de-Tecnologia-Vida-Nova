from os import terminal_size
from carro import Carro
from motorista import Motoristas

lista_de_carro = []
lista_de_motorista = []

while True: 
    print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
    print('\n 1) Criar um veículo \n 2) Criar um motorista \n')
    print('#-----------------------------------------------------------------------#')
    escolha = int(input('\nDigite a opção desejada: '))

    if(escolha == 1): 

        while True:
            print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
            print('\n1) Criar um veículo: \n2) Ver lista de veículo: \n3) Remover um veículo: \n4) Mudar a cor do carro: \n\n-> Digite zero para sair do programa\n')
            print('#-----------------------------------------------------------------------#')
            opcao = int(input('\nDigite a opção desejada: '))

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

            elif(opcao == 0): 
                break

            else:
                print('Digite um número válido!')

    elif(escolha == 2):

        while True: 
            print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
            print('\n1) Criar um motorista: \n2) Ver lista de motorista: \n3) Remover um motorista: \n4) Alterar nome do motorista \n\n-> Digite zero para sair do programa\n')
            print('#-----------------------------------------------------------------------#')
            opcao = int(input('\nDigite a opção desejada: '))

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

            elif(opcao == 0): 
                break

            else:
                print('Digite um número válido!')    

            

            
