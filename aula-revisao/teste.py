def greet() -> None:
    print("Olá, bem vindo ao meu programa\n")

def get_number() -> int:
    return int(input("Insira um número inteiro: "))

def sum_two_number(number1: int, numbert2: int) -> int:
    sum_of_two_number = number1 + numbert2
    return sum_of_two_number

def show_sum(sum : int) -> None: 
    print("A soma dos dois números é: ", sum)

def main() -> None:
    greet()

    number1 = get_number()
    number2 = get_number()

    sum = sum_two_number(number1, number2)   

    show_sum(sum)

main()