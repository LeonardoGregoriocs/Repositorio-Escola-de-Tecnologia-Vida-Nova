import os
from carro import Carro
from motorista import Motoristas


marca = str(input('Digite a marca do carro: '))
modelo = str(input('Digite o modelo do carro: '))
ano = int(input('Digite o ano do carro: '))
chassi = str(input('Digite o chassi do carro: '))
placa = str(input('Digite a placa do carro: '))
cor = str(input('Digite a cor do carro: '))

os.system('cls')

carro1 = Carro(marca, modelo, ano, chassi, placa, cor)

nome = str(input('Digite o seu nome: '))
sobrenome = str(input('Digite o seu sobrenome: '))
cpf = int(input('Digite seu CPF (Não utilizar traço/ Não utilizar ponto): '))
data_de_nascimento = str(input('Digite sua data de nascimento: '))
numero_cnh = int(input('Digite o número da sua CNH: '))
classe = str(input('Digite a classe da sua CNH: '))
data_emissao = str(input('Digite a data de emissão: '))

os.system('cls')

motorista1 = Motoristas(nome, sobrenome, cpf, data_de_nascimento,numero_cnh, classe, data_emissao)
motorista1.print()
carro1.print()
