programa
{	
	real valor_amarelo = 30.0
	real valor_azul = 20.0
	real valor_verde = 10.0
	real valor_vermelho = 40.0

	cadeia cor_selecionada = ""
	real valor_selecionado = 0.0

	funcao visualizar_valor(){
	cadeia nome_cor = ""
	se(cor_selecionada == "Amarelo" ou
	cor_selecionada == "amarelo"){
	 valor_selecionado = valor_amarelo
	 nome_cor = "amarelo"
	} 
	senao se(cor_selecionada == "Azul" ou
	cor_selecionada == "azul"){
	 valor_selecionado = valor_azul
	 nome_cor = "azul"
	} 
	senao se(cor_selecionada == "Verde" ou
	cor_selecionada == "verde"){
	 valor_selecionado = valor_verde
	 nome_cor = "verde"
	} 
	senao se(cor_selecionada == "Vermelho" ou
	cor_selecionada == "vermelho"){
	 valor_selecionado = valor_vermelho
	 nome_cor = "vermelho"
	}
	escreva("O valor do CD de cor ", nome_cor, " é: R$", valor_selecionado)
	}
	
	funcao escolher_cor(){
	cadeia _cor
	escreva("\n")
	escreva("Cores disponíveis: Amarelo, Azul, Verde, Vermelho \n")
	escreva("Digite qual a cor desejada: \n")
	leia(_cor)
	se(_cor == "Amarelo" ou
	   _cor == "amarelo" ou
	   _cor == "Azul" ou
	   _cor == "azul" ou
	   _cor == "Verde" ou
	   _cor == "verde" ou
	   _cor == "Vermelho" ou
	   _cor == "vermelho"){
	   	cor_selecionada = _cor
	   	visualizar_valor()
	   }
	   senao{
	   escreva("Erro - Cor inválida \n")
	   escolher_cor()
	   }
	}
	
	funcao inicio()
	{
	escolher_cor()
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 228; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */