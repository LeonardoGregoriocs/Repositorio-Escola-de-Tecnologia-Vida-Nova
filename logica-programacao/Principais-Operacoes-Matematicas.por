programa {
	funcao inicio() {
		real entrada1, entrada2, soma, sub, mult, div
		cadeia nome, sobrenome
		
		escreva("Qual é seu nome: ")
		leia(nome)
		
		escreva("Qual é seu sobrenome: ")
		leia(sobrenome)
		
		limpa()
		
		escreva("Por favor, digite um número: ")
		leia(entrada1)

	    escreva("Por favor, digite outro número: ")
	    leia(entrada2)
	    
	    limpa()
	    
	    soma = entrada1 + entrada2
	    sub = entrada1 - entrada2
	    mult = entrada1 * entrada2
	    div = entrada1 / entrada2
	    
	    escreva("Olá ", nome, " ", sobrenome, "!\n")
	    
	    escreva("\nSeu primeiro número é: ", entrada1, "\n")
	    escreva("Seu segundo número é: ", entrada2, "\n")
	    
	    escreva("\nPrincipais operações matemáticas: \n")
	    
	    escreva("\nA soma é: ", soma)
	    escreva("\nA subtração é: ", sub)
	    escreva("\nA multiplicação é: ", mult)
	    escreva("\nA divisão é: ", div)
	    
	    escreva("\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 930; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */