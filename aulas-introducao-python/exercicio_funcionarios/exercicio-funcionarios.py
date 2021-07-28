import os 

global salario

#Ler o nome, sobrenome e cargo de um funcionário e retornar essas informações dentro de um vetor.
def dadosPessoais () -> None: 
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    cargo = input('Digite seu cargo: ')
    tabela = [nome, sobrenome, cargo]
    return tabela

#Exibir na tela as informações do funcionário que devem ser passadas por parâmetro.
def informacoesFuncionario(nome, sobrenome, cargo):
    os.system('cls')
    print('Olá, %s %s!\nSeu cargo é: %s' %(nome, sobrenome, cargo))

#Ler e retornar um salário para esse funcionário.
def salarioFuncionario() -> None:
    global salario
    salario = float(input('\nDigite seu salário para calcularmos seu imposto de renda: '))
    return salario

#Calcular e exibir na tela o salário Líquido desse funcionário depois de calcular o Imposto de Renda.
def calculoImpostoDeRenda(salario: float):
        if salario <= 1903.68:
            print('\nVocê é isento, seu salário líquido é: ', salario)

        elif salario > 1903.68 and salario <= 2826.65:
            print('\nSeu salário líquido é de: ', salario - (salario * 0.075)) 
            
           
        elif salario > 2826.65 and salario <= 3751.06:
            print('\nSeu salário líquido é de: ', salario - (salario * 0.15))
  
            
        elif salario > 3751.06 and salario <= 4664.68:
            print('\nSeu salário líquido é de: ', salario - (salario * 0.225))

        elif salario > 4664.68:
            print('\nSeu salário líquido é de: ', salario - (salario * 0.275))

while True: 
    print('\nBem-vindo!\n\n1)Dados Pessoais \n2)Calcular Imposto de Renda\n3)Digite 0 para fechar o programa\n')
    operacao = int(input('Favor selecionar a opção desejada: '))
    os.system('cls')

    if(operacao == 1): 
        var1 = dadosPessoais()
        informacoesFuncionario(var1[0], var1[1], var1[2])
        var2 = salarioFuncionario()
        calculoImpostoDeRenda(salario)
    
    elif(operacao == 2):
        print("Favor informar seus dados pessoais para darmos andamento no calculo do imposto de renda: ")
        var1 = dadosPessoais()
        informacoesFuncionario(var1[0], var1[1], var1[2])
        var2 = salarioFuncionario()
        calculoImpostoDeRenda(salario)

    elif(operacao == 0):
        print('Seu programa foi encerrado, você digitou 0!')
        break