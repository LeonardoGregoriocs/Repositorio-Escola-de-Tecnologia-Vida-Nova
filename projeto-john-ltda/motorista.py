class Motoristas: 

    def __init__(self) -> None:
        self.nome = input('Digite o seu nome: ')
        self.sobrenome = input('Digite o seu sobrenome: ')
        self.cpf = int(input('Digite seu CPF (Não utilizar traço/ Não utilizar ponto): '))
        self.data_de_nascimento = input('Digite sua data de nascimento: ')
        self.numero_cnh = int(input('Digite o número da sua CNH: '))
        self.classe = input('Digite a classe da sua CNH: ')
        self.data_emissao = input('Digite a data de emissão: ')

    def print_motorista(self): 
        print('#------------------------#')
        print('DADOS DO MOTORISTA:')
        print('#------------------------#\n')
        print(f'Nome do cliente:',self.nome)
        print(f'CPF:',self.cpf)
        print(f'Data de nascimento:',self.data_de_nascimento)
        print(f'Número da CNH:',self.numero_cnh )
        print(f'Categoria da CNH:',self.classe)
        print(f'Data de emissão da CNH:',self.data_emissao)

    def trocar_nome(self):
        self.nome = input('Digite o novo nome: ')

