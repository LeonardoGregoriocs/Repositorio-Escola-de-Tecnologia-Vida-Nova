# Caracteristicas do carro: marca, modelo, ano, chassi e cor. 
#  CRUD - CRIAR / LER / ATUALIZAR / REMOVER 

class Carro: 

    def __init__(self, marca: str, modelo: str, ano: int, chassi: str, placa: str, cor: str) -> None: 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.placa = placa
        self.cor = cor

    def print(self): 
        print('\n#------------------------#')
        print('DADOS DO VEÍCULO:')
        print('#------------------------#\n')
        print(f'Marca:', self.marca)
        print(f'Modelo:', self.modelo)
        print(f'Ano:',self.ano)
        print(f'Chassi:',self.chassi)
        print(f'Placa:',self.placa)
        print(f'Cor:', self.cor)
    


