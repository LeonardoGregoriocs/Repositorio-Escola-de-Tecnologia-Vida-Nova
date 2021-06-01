programa
{
    
	funcao inicio()
	{
		inteiro candidato_a = 0, candidato_b = 0
		
		inteiro brancos = 0, nulos = 0, total_votos = 0
		
		real porcentagem_candidato_a, porcentagem_candidato_b
		
		real porcentagem_brancos, porcentagem_nulos
		
		inteiro voto
		
		faca
		{
			limpa()
			escreva("Escolha seu candidato ou tecle zero para encerrar\n\n")
			
			escreva("  1 -> Candidato A\n")
			escreva("  2 -> Candidato B\n")
			escreva("  3 -> Branco\n")
			
			escreva("\nQualquer número diferente de 0, 1, 2 e 3 anulará o seu voto\n")
			escreva("Digite seu voto: ")
			
			leia(voto)
			limpa()

			escolha (voto)
			{
				caso 0:
					escreva ("Votação encerrada!\n")
				pare
				
				caso 1: 
			 		candidato_a = candidato_a + 1 // Soma um voto para o candidato A
			 	pare
			 	
			 	caso 2: 
			 		candidato_b = candidato_b + 1 // Soma um voto para o candidado B
			 	pare
			 	
			 	caso 3: 
			 		brancos = brancos + 1 // Soma um voto em branco
			 	pare
			 	
			 	caso contrario:
			 		nulos = nulos + 1 // Opção inválida. Soma um voto nulo
			}			 
		}
		enquanto(voto != 0)
		
		total_votos = candidato_a + candidato_b + brancos + nulos
		porcentagem_candidato_a = (candidato_a) * 100 / total_votos
		porcentagem_candidato_b = (candidato_b) * 100 / total_votos
		porcentagem_brancos = (brancos * 100) / total_votos
		porcentagem_nulos = (nulos * 100) / total_votos
	
		        escreva("\nTotal de votos: ", total_votos, "\n")
		        escreva("\nPorcetagem Candidato A: ", porcentagem_candidato_a, " %")
		        escreva("\nPorcetagem Candidato B: ", porcentagem_candidato_b, " %")
		        escreva("\nPorcetagem de votos em branco: ", porcentagem_brancos, " %")
		        escreva("\nPorcetagem de Votos Nulos: ", porcentagem_nulos, " %\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1192; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */