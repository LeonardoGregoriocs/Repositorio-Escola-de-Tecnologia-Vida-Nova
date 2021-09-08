# Caracteristicas do carro: marca, modelo, ano, chassi e cor. 
#  CRUD - CRIAR / LER / ATUALIZAR / REMOVER 

class Carro: 

    def __init__(self) -> None:
        self.marca = input('Digite a marca do carro: ')
        self.modelo = input('Digite o modelo do carro: ')
        self.ano = int(input('Digite o ano do carro: '))
        self.chassi = input('Digite o chassi do carro: ')
        self.placa = input('Digite a placa do carro: ')
        self.cor =  input('Digite a cor do carro: ')

    def print_carro(self) -> None:
        print('#------------------------#')
        print('DADOS DO VEÍCULO:')
        print('#------------------------#')
        print(f'Marca:', self.marca)
        print(f'Modelo:', self.modelo)
        print(f'Ano:',self.ano)
        print(f'Chassi:',self.chassi)
        print(f'Placa:',self.placa)
        print(f'Cor:', self.cor)

    def trocar_cor(self) -> None:
        self.cor = input('Digite a cor desejada: ')

        