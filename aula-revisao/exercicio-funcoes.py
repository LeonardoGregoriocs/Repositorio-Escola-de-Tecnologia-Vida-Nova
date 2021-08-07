def get_name() -> str: 
    return input('Digite seu nome: ')

def greet(name) -> str: 
    print("Olá, seja bem vindo %s!" %name)

def get_float() -> float:
    return float(input('Digite um número usando ponto para separar a casa decimal: '))

def sum_3_numbers(x: float, y: float, z: float) -> float: 
    sum_of_3_numbers = x + y + z
    return sum_of_3_numbers

def calculate_avg(x: float, y: float, z: float) -> float:
    calculate = sum_3_numbers(x, y, z) / 3 
    return calculate

def bigger_or_equal(x: float, y: float) -> float: 
    if(x > y):
        print("Entre o primeiro e o segundo número, o maior é:  ", x)
    
    elif(x == y):
        print("Os dois números são iguais")

    else:
        print("Entre o primeiro e o segundo número, o maior é: ", y)
    


def main() -> None: 
    name = get_name()
    greet(name)

    number1 = get_float()
    number2 = get_float()
    number3 = get_float()

    sum = sum_3_numbers (number1, number2, number3)
    print("A soma dos três números é: ", sum)

    calculate = calculate_avg (number1, number2, number3)
    print("A média é: ", calculate)

    bigger_or_equal(number1, number2)

main()