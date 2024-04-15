programa
{
	cadeia operador = ""
	inteiro a = 0
	inteiro b = 0

	funcao calcular(){
	inteiro _resultado = 0
	se(operador == "+" ou operador == "add"){
	_resultado = a+b
	}
	senao se(operador == "-" ou operador == "sub"){
	_resultado = a-b
	}
	senao se(operador == "*" ou operador == "mult"){
	_resultado = a*b
	}
	senao se(operador == "/" ou operador == "div"){
	_resultado = a/b
	}
	escreva("O valor de ", a, " ", operador, " ", b, " ", "é igual a ", _resultado)
	}

	funcao definir_b(){
	inteiro _b
	escreva("Digite o valor de B (inteiro): \n")
	escreva("\n")
	leia(_b)
	b = _b
	calcular()
	}

	funcao definir_a(){
	inteiro _a
	escreva("Digite o valor de A (inteiro): \n")
	escreva("\n")
	leia(_a)
	a = _a
	definir_b()
	}
	
	funcao definir_operador(){
	cadeia _operador
	escreva("Digite a operação desejada: \n")
	escreva("\n")
	escreva(" Adição: digite '+' ou 'add' \n")
	escreva(" Subtração: digite '-' ou 'sub' \n")
	escreva(" Multiplicação: digite '*' ou 'mult' \n")
	escreva(" Subtração: digite '/' ou 'div' \n")
	leia(_operador)
	se(_operador == "+" ou
	   _operador == "add" ou
	   _operador == "-" ou
	   _operador == "sub" ou
	   _operador == "*" ou
	   _operador == "mult" ou
	   _operador == "/" ou
	   _operador == "div"){
	   operador = _operador
	   definir_a()
	   } senao{
	   	escreva("Operador inválido \n")
	   	definir_operador()
	   }
	}
	
	funcao inicio()
	{
		escreva("Calculadora \n")
		definir_operador()
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 577; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */