# ------------------------------------------------------------------------------------------------------#
# 1- Criar uma lista vazia e imprimir ela:
# ------------------------------------------------------------------------------------------------------#

lista_vazia = []
print(lista_vazia)

# ------------------------------------------------------------------------------------------------------#
# 2 - Criar uma lista com 3 números e imprimir o 2 número: 
# ------------------------------------------------------------------------------------------------------#

lista_numeros = [1, 2, 5]
print(lista_numeros[1])

# ------------------------------------------------------------------------------------------------------#
# 3 - Criar uma lista com 4 nomes e imprimir o último nome (usar índice negativo): 
# ------------------------------------------------------------------------------------------------------#

lista_nomes = ['Leonardo', 'Edivane', 'Fred', 'Messi']
print(lista_nomes[-1])

# ------------------------------------------------------------------------------------------------------#
# 4 - Pegar a lista criada anteriormente e adicionar Gabriel no final e imprime a lista: 
# ------------------------------------------------------------------------------------------------------#

lista_nomes.append('Gabriel')
print(lista_nomes)

# ------------------------------------------------------------------------------------------------------#
# 5 - Pegar a lista criada anteriormente e adicionar o "Renan" na segunda posição e imprime a lista: 
# ------------------------------------------------------------------------------------------------------#

lista_nomes.insert(1, "Renan")
print(lista_nomes)

# ------------------------------------------------------------------------------------------------------#
# 6 - Pegar a lista criada anteriormente e remover o Gabriel (usar remove) e imprime a lista: 
# ------------------------------------------------------------------------------------------------------#

lista_nomes.remove("Gabriel")
print(lista_nomes)

# ------------------------------------------------------------------------------------------------------#
# 7 - Escrever um for que imprime uma Olá para cada nome da lista anterior. Exemplo: Olá, William / Olá Kaio: 
# ------------------------------------------------------------------------------------------------------#

for nome in lista_nomes:
    print(f"Olá, {nome}")

# ------------------------------------------------------------------------------------------------------#
# 8 - Remover o último elemento da lista anterior com o pop() e imprime o tamanho da lista antes e depois de remover: 
# ------------------------------------------------------------------------------------------------------#

print(len(lista_nomes))
lista_nomes.pop(1) #POSSO UTILIZAR TANTO VAZIO PARA EXCLUIR O ÚLTIMO, COMO COLOCAR QUAL POSIÇÃO DESEJO EXCLUIR. 
print(len(lista_nomes))

# ------------------------------------------------------------------------------------------------------#
# 9 - Faça um for para pegar uma lista de números interior e converter para float: 
# ------------------------------------------------------------------------------------------------------#

lista_numeros_inteiro = [1, 2, 3, 6, 5, 4, 8, 7]

for x in lista_numeros_inteiro:
    converter = float(x)
    print(converter)

# ------------------------------------------------------------------------------------------------------#
# 10 - Faça uma função que receba uma tupla como argumento. A tupla deve conter um nome na primeira posição, 
# e um sobrenome na segunda posioção: 
# ------------------------------------------------------------------------------------------------------#

def funcao_tupla(nome_completo: tuple) -> None: 
    nome = nome_completo[0]
    sobrenome = nome_completo[1]
    print(f"Meu nome é {sobrenome}, {nome}, {sobrenome}")

minha_primeira_tupla = ("Leonardo", "Gregório")
funcao_tupla(minha_primeira_tupla)

# ------------------------------------------------------------------------------------------------------#
# 11 - Faça uma função que recebe uma lista de nomes tudo minúsculo 
# e imprima os nomes com a primeira letra maiúscula: 
# ------------------------------------------------------------------------------------------------------#

def letras_maiusculas(letras: list[str]) -> None: 
    for nomes in letras: 
        maiusculas = nomes.capitalize()
        print(maiusculas)

letras_minusculas = ['leonardo', 'edivane', 'messi']

letras_maiusculas(letras_minusculas)

# ------------------------------------------------------------------------------------------------------#
# 12 - Faça uma função que receba uma lista de números e nomes como string e imprima somente os digitos. 
# ------------------------------------------------------------------------------------------------------#

def lista_numeros_nomes(lista: list[str]) -> None: 
    for x in lista:
        if x.isdigit():
            print(x)
        else: 
            print("Isso não é um número.")

lista_sortidas =['Leonardo', '2', '3', '10', 'Edivane', '15']

lista_numeros_nomes(lista_sortidas)

# ------------------------------------------------------------------------------------------------------#
# 13 - Faça uma função que recebe uma lista de frases (string) de atenção. Se a frase começar com 
# Perigo: ela é importante e deve ser imprimida na tela, senão não deve ser imprimida na tela:
# ------------------------------------------------------------------------------------------------------#

def alerta_perigo(alerta: list[str]) -> None: 
    for y in alerta:
        if y.startswith('Perigo'):
            print(y)

lista_alertas_perigos = ['Perigo: Não nadar no lado do hipopótamos', 
'Atenção: Não jogar lixo no chão', 
'Perigo: Leão a solta', 
'Perigo: Alienígenas estão atacando', 
'Atenção: Pare']

alerta_perigo(lista_alertas_perigos)

# ------------------------------------------------------------------------------------------------------#
# 14 - Fazer uma função que recebe uma lista de números float e retorna a soma desses números. 
# ------------------------------------------------------------------------------------------------------#

def somador(numeros: list[float]): 
    contador = 0
    for x in numeros: 
        contador = contador + x 
    return contador

numeros_para_somar = [1.5, 1.5, 4.0]

print(somador(numeros_para_somar))

# ------------------------------------------------------------------------------------------------------#
# 15 - Fazer uma função que recebe uma lista de números float e retorna a média desses números: 
# ------------------------------------------------------------------------------------------------------#

def media_da_sala(notas: list[float]):
    contador_media = 0
    for x in notas: 
        contador_media = contador_media + x 
    media = contador_media / len(notas)
    return media

notas = [4.0, 10.0, 5.0, 5.0]

print(media_da_sala(notas))




    

