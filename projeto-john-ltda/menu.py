from carro import Carro
from motorista import Motoristas

lista_de_carro = []

while True:
    print('\n#------------------------# PROJETO JOHN-LTDA #------------------------#')
    print('\n1) Criar um veículo: \n2) Ver lista de veículo: \n3) Remover um veículo: \n4) Mudar a cor do carro: \n\n-> Digite zero para sair do programa\n')
    print('#-----------------------------------------------------------------------#')
    opcao = int(input('\nDigite a opção desejada: '))

    if(opcao == 1):
        carro = Carro()
        lista_de_carro.append(carro)

    elif(opcao == 2):
        x = int(input('Qual a posição do veículo deseja visualizar: '))
        lista_de_carro[x-1] = carro.print()

    elif(opcao == 3):
        x = int(input('Qual a posição do veículo deseja excluir: '))
        lista_de_carro.pop(x-1)

    elif(opcao == 4):
        x = int(input('Qual a posição do veículo que deseja alterar a cor: '))
        lista_de_carro[x-1] = carro.trocar_cor()

    elif(opcao == 0): 
        break

    else:
        print('Digite um número válido!')
        
