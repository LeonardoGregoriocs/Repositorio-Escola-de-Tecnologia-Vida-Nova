		programa
		{
			
			funcao inicio()
			{
				real valor_real, valor_dolar, conversao, dolar_hoje
		
				escreva("Escreva o valor do dólar hoje: \nPor favor, utilizar ponto para casas decimais: ")
				leia(dolar_hoje)
				limpa()
				
				escreva("QUAL CONVERSÃO DESEJA REALIZAR: \n\n 1-> Dolár para Real: \n\n 2-> Real para Dolár: \n\n Digite aqui: ")
				leia(conversao)
				limpa()

				se(conversao == 1){
					escreva("Digite o valor a ser convertido: $")
					leia(valor_dolar)

					valor_real = valor_dolar * dolar_hoje
					escreva("\nValor convertido: R$", valor_real,"\n\n")
					
				}senao se (conversao == 2){
					escreva("Digite o valor a ser convertido: R$")
					leia(valor_real)
							
			  		valor_dolar = valor_real / dolar_hoje
			  		escreva("\n\nValor convertido $", valor_dolar, "\n\n")	
					
					
				}senao 
					escreva("ERRO, digite um valor válido!")
			
	}
		}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 193; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */