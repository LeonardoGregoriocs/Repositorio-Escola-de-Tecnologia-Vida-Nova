# IMPOSTO DE RENDA 

salarioAtual = float(input('\nDigite seu salário atual: '))
while True: 
        if salarioAtual <= 1903.68:
            print('\nVocê é isento, seu salário líquido é: ', salarioAtual)

        elif salarioAtual > 1903.68 and salarioAtual <= 2826.65:
            print('\nSeu salário líquido é de: ', salarioAtual - (salarioAtual * 0.075)) 
            
           
        elif salarioAtual > 2826.65 and salarioAtual <= 3751.06:
            print('\nSeu salário líquido é de: ', salarioAtual - (salarioAtual * 0.15))
  
            
        elif salarioAtual > 3751.06 and salarioAtual <= 4664.68:
            print('\nSeu salário líquido é de: ', salarioAtual - (salarioAtual * 0.225))

        elif salarioAtual > 4664.68:
            print('\nSeu salário líquido é de: ', salarioAtual - (salarioAtual * 0.275))

        salarioAtual = salarioAtual+float(input('\nDigite seu aumento/correção: '))