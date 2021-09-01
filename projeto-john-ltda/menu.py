import os
from carro import Carro
from motorista import Motoristas

lista_de_carro = []

while True:

    print('#------------------------#   \n1)Criar um veículo \n2)Ver lista de carro: ')
    opcao = int(input('\nDigite a opção desejada: '))
    
    os.system('cls')
    
    if(opcao == 1):
        carro = Carro()
        lista_de_carro.append(carro)

    elif(opcao == 2):
        x = int(input('Digite a posição que deseja vizualizar: '))
        print(lista_de_carro[x].print())