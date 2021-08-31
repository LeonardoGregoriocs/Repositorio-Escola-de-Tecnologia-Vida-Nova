from datetime import date, datetime

class Motoristas: 

    def __init__(self, nome: str, sobrenome: str, cpf: int, data_de_nascimento: str , numero_cnh: int, classe: str, data_emissao: datetime.date) -> None:
        self.nome = nome 
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.numero_cnh = numero_cnh
        self.classe = classe
        self.data_emissao = data_emissao

    def print(self): 
        print('#------------------------#')
        print('DADOS DO MOTORISTA:')
        print('#------------------------#\n')
        print(f'Nome do cliente:',self.nome)
        print(f'CPF:',self.cpf)
        print(f'Data de nascimento:',self.data_de_nascimento)
        print(f'Número da CNH:',self.numero_cnh )
        print(f'Categoria da CNH:',self.classe)
        print(f'Data de emissão da CNH:',self.data_emissao)
