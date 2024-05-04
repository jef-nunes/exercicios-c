programa
{
	
	funcao calcular(){
		
	escreva("Insira os valores inteiros de A e B: \n")
	inteiro A
	inteiro B
	inteiro C
	
	escreva("A: ")
	leia(A)
	escreva("\n")
	
	escreva("B: ")
	leia(B)
	escreva("\n")
	se(A==B){
	C = A+B
	escreva("A + B = ", C)
	} senao{
	C = A*B
	escreva("A * B = ", C)
	}
	}
	
	funcao inicio()
	{
	calcular()
	escreva("\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 350; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
