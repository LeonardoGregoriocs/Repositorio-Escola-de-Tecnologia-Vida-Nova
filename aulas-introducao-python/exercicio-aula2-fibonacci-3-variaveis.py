# sequencia de fibonacci

num1 = 0
num2 = 1
resultado = int(input('\nQuantos números de fibonacci deseja: '))

if(resultado == 1):
        print(num1)
elif(resultado == 2):
        print(num1, num2)
elif(resultado > 2):
    x = 0
    while (x < resultado):
        x+=1
        num3 = num1 
        num1 = num2 
        num2 = num3+num2
        print(num3)
              

        
        
        
