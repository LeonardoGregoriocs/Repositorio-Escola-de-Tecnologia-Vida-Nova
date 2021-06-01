programa
{
	inclua biblioteca Matematica --> Mat
	
	funcao inicio()
	{
	
		cadeia texto
		real km, litros, media, arredondar
		
		escreva("Digite a placa do veiculo: ")
		leia(texto)
		
		escreva("\nDigite o KM percorrido: ")
		leia(km)
		
		escreva("\nDigite a quatidade de litros: ")
		leia(litros)

		media = km / litros 
		arredondar = Mat.arredondar(media, 2)
		limpa()

		escreva("PLACA: ", texto)
		escreva("\n\nA média do veículo é: ", arredondar, " km por litro\n")
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 129; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */