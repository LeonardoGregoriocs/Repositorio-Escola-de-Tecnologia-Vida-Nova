# sequencia de fibonacci

num1 = 0
num2 = 1
resultado = int(input('\nQuantos números de fibonacci deseja: '))

if(resultado == 1):
        print(num1)
elif(resultado == 2):
        print(num1, num2)
elif(resultado > 2):
    x=0
    while(x<(resultado/2)-1):
        x+=1
        print(num1, num2, end=(' '))
        num1 = num2+num1
        num2 = num1+num2
x = resultado%2        
if(x == 0):
    print(num1, num2)
elif(x == 1):
    print(num1)