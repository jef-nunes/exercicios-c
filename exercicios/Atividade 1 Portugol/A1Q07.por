programa
{
	cadeia item_1 = "item_1"
	cadeia item_2 = "item_2"
	cadeia item_3 = "item_3"
	real valor_item_1 = 30.0
	real valor_item_2 = 99.0
	real valor_item_3 = 150.0

	cadeia item_selecionado = ""
	real valor_unidade = 0.0
	inteiro quantidade = 0
	real valor_total = 0.0
	
	funcao revisar(){
	escreva("Esse é o valor total da sua compra:\n")
	escreva("Item: ", item_selecionado, "\n")
	escreva("Valor Uni: ", valor_unidade, "\n")
	escreva("Quantidade: ", quantidade, "\n")
	escreva("Valor Total: ", valor_total, "\n")
	}
	
	funcao definir_valor_total(){
	valor_total = valor_unidade * quantidade
	se(quantidade <= 5){
	  valor_total = valor_total - (valor_total*0.2)
	}
	senao se(quantidade >5 e quantidade <= 10 ){
	  valor_total = valor_total - (valor_total*0.3)
	}
	senao se(quantidade > 10){
   	  valor_total = valor_total - (valor_total*0.5)
	}
	}
	
	funcao escolher_quantidade(){
	 inteiro _quantidade = 0
	 escreva("Agora digite a quantidade de itens:\n")
	 leia(_quantidade)
	 se(_quantidade > 0){
	 quantidade = _quantidade
	 definir_valor_total()
	 revisar()
	 } senao{
	 escreva("Erro - Quantidade inválida.\n")
	 escolher_quantidade() 
	 }
	}

	funcao definir_valor_unidade(){
	se(item_selecionado == item_1){
	valor_unidade = valor_item_1
	} senao se(item_selecionado == item_2){
	valor_unidade = valor_item_2
	} senao se(item_selecionado == item_3){
	valor_unidade = valor_item_3
	}
	}
	
	funcao escolher_item(){
	cadeia _item_selecionado = ""
	escreva("Digite o nome do item que deseja comprar:\n")
	leia(_item_selecionado)
	se(_item_selecionado == item_1 ou
	   _item_selecionado == item_2 ou
	   _item_selecionado == item_3){
	   item_selecionado = _item_selecionado
	   definir_valor_unidade()
	   escolher_quantidade()
	   } senao{
	   	escreva("Erro - item inválido")
	   	escolher_item()
	   }
	}
	
	funcao mostrar_items(){
	escreva("Esses são os items disponíveis:\n")
	escreva("Nome: ", item_1, " ", "Preço: ", valor_item_1, "\n")
	escreva("Nome: ", item_2, " ", "Preço: ", valor_item_2, "\n")
	escreva("Nome: ", item_3, " ", "Preço: ", valor_item_3, "\n")
	}

	
	funcao inicio()
	{
	mostrar_items()
	escolher_item()
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 860; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
