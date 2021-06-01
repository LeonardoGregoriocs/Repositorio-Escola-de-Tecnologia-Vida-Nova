programa{ 
	
	funcao inicio()
	{
		const real PRECO_PARAFUSO = 1.50
		const real PRECO_ARRUELAS = 2.00
		const real PRECO_PORCA = 2.50

		cadeia nome
		inteiro quantidade_parafusos, quantidade_arruelas, quantidade_porcas
		real total_parafusos, total_arruelas, total_porcas, total_pagar

		escreva("Digite seu nome: ")
		leia(nome)

		escreva("\nDigite a quantidade de parafusos que deseja comprar: ")
		leia(quantidade_parafusos)

		escreva("\nDigite a quantidade de arruelas que deseja comprar: ")
		leia(quantidade_arruelas)

		escreva("\nDigite a quantidade de porcas que deseja comprar: ")
		leia(quantidade_porcas)

		total_parafusos = PRECO_PARAFUSO * quantidade_parafusos
		total_arruelas = PRECO_ARRUELAS * quantidade_arruelas
		total_porcas = PRECO_PORCA * quantidade_porcas

		total_pagar= total_parafusos + total_arruelas + total_porcas

		limpa ()

		escreva("\nCliente: ", nome, "\n")
		escreva("===========================\n")
		escreva("Parafusos: ", quantidade_parafusos, " /// Valor: R$ ", total_parafusos, "\n")
		escreva("Arruelas: ", quantidade_arruelas, " /// Valor: R$ ", total_arruelas, "\n")
		escreva("Porcas: ", quantidade_porcas, " /// Valor: R$ ", total_porcas, "\n")
		escreva("===========================\n")
		escreva("Total a pagar: R$ ", total_pagar, "\n")
		
		
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 9; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */