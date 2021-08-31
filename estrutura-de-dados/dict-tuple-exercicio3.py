# ------------------------------------------------------------------------------------------------------#
# 2 - Criar um dicíonario vazio e imprimi-lo:
# ------------------------------------------------------------------------------------------------------#

meu_dicionario = {}
print(meu_dicionario)

# ------------------------------------------------------------------------------------------------------#
# 3 - Criar um dicíonario que irá conter dados de uma pessoa. Com: nome, idade, e-mail, cpf.
# ------------------------------------------------------------------------------------------------------#
 
dados_pessoais = {'Nome': 'Leonardo', 'Idade': 24, 'email': 'leonardo@hotmail.com', 'cpf': 41021021082}
print(dados_pessoais)

# ------------------------------------------------------------------------------------------------------#
# 3 - Pegar esse dicionario criado no exercicio 3 e crie uma função que receba um dicionario e imprima o nome
# da pessoa e o e-mail.
# ------------------------------------------------------------------------------------------------------#

def impressao_nome_email(dados: dict) -> None:
    print(dados)
