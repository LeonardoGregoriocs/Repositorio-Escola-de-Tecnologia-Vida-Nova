#CINEMA
import os

quantidade_assentos = int(input('Digite a quantidade de assentos: '))
assentos = ['-']*quantidade_assentos

dicionario = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
}

y = 0
while(y < len(assentos)):

    letras_coluna = print('\nA B C D E F G H I J')
    numero_da_fila = 1
    for x in range(1,quantidade_assentos+1):
        print(assentos[x-1], end = " ")
        if(x%10 == 0) or (x == quantidade_assentos):
            print(numero_da_fila, '\n')
            numero_da_fila+=1

    fila = int(input('\nDigite a fila desejada: '))
    coluna = input('Digite a coluna desejada: ')

    os.system('cls')
    lugarNoCinema = (fila-1)*10+(dicionario[coluna])
    
    if(assentos[lugarNoCinema-1] == 'x'):
        os.system('cls')
        print('A CADEIRA ESTÁ OCUPADA! ESCOLHA OUTRO LUGAR: ')

    assentos[lugarNoCinema-1] = 'x'

    if(lugarNoCinema == quantidade_assentos):
        os.system('cls')
        print('\t-- CINEMA LOTADO -- \n A SESSÃO IRÁ COMEÇAR.. BOM FILME! \n')
        break
    