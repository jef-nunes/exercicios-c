programa
{
	
	real valor_emprestimo = 0.0
	real renda_mensal = 0.0
	inteiro numero_de_prestacoes = 0
	real valor_prestacao = 0.0

	funcao inserir_numero_prestacoes(){
	real _n_prestacao
	escreva("Digite o número de prestações: \n")
        leia(_n_prestacao)
        se(_n_prestacao != 0 e (valor_emprestimo / _n_prestacao) <= (renda_mensal * 0.3){
        escreva("A sua solicitação de empréstimo foi aceita.")
        } senao{
         escreva("O numero de prestações inserido não foi aceito. Tente novamente: \n")
         inserir_numero_prestacoes()
         }
	}

	funcao inserir_valor_emprestimo(){
	real _emprestimo
	escreva("Digite o valor de empréstimo: \n")
	leia(_emprestimo)
	se(_emprestimo > 0 ou (_emprestimo * 10 > renda_mensal)){
	valor_emprestimo = _emprestimo
	inserir_numero_prestacoes()
	} senao{
	escreva("Erro - Insira uma quantia válida\n")
	escreva("o valor não deve exceder 10 vezes a sua renda mensal.\n")
	inserir_valor_emprestimo()
	}
	}

	funcao inserir_renda_mensal(){
	real _renda
	escreva("Digite a sua renda mensal \n")
	leia(_renda)
	renda_mensal = _renda
	inserir_valor_emprestimo()
	}
	
	funcao inicio()
	{
	escreva("Empréstimo \n \n")
	inserir_renda_mensal()
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 597; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
