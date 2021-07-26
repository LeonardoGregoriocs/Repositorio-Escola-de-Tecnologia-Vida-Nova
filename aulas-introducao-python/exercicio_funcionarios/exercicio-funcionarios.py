import os 

def dadosPessoais () -> None: #coletando dados pessoais dos usuarios.
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    cargo = input('Digite seu cargo: ')
    tabela = [nome, sobrenome, cargo]
    return tabela

def informacoesFuncionario(nome, sobrenome, cargo): #imprimindo as informacoes na tela
    os.system('cls')
    print('Olá, %s %s!\nSeu cargo é: %s' %(nome, sobrenome, cargo))

def salarioFuncionario() -> None: #solicitando o salario do funcionario
    salario = (input('\nDigite seu salário para calcularmos seu imposto de renda: '))


var1 = dadosPessoais()
informacoesFuncionario(var1[0], var1[1], var1[2])
var2 = salarioFuncionario()