programa{
	
inteiro produto_escolhido = 0
real quantidade = 0.0
logico desconto = falso
real val_produto_1 = 2.50/1000
real val_produto_1_desc = 2.20/1000
real val_produto_2 = 1.80/1000
real val_produto_2_desc = 1.50/1000


funcao calcular_total(){
real resultado = 0.0
real valor_base = 0.0
se(produto_escolhido == 1){
valor_base = val_produto_1
se(desconto){
valor_base = val_produto_1_desc
}
}
senao se(produto_escolhido == 2){
valor_base = val_produto_2
se(desconto){
valor_base = val_produto_2_desc
}
}

resultado = valor_base * quantidade

se(resultado > 25.0 ou quantidade > 8000){
resultado = (resultado - (resultado*(10/100)))
}

escreva("\n O valor total da sua compra é: ", resultado)
}

funcao escolher_quantidade(){
real _quantidade
escreva("Digite a quantidade (em gramas):\n")
leia(_quantidade)
se(_quantidade > 0.0){
quantidade = _quantidade
calcular_total()
} senao{
escreva("O valor inserido é inválido.\n")
escolher_quantidade()
}
}


funcao escolher_fruta(){
inteiro Fruta
escreva(" Digite 1 para comprar Morangos \n")
escreva(" ou digite 2 para comprar Maçãs.\n")
leia(Fruta)
se(Fruta == 1 ou Fruta == 2){
produto_escolhido = Fruta
escolher_quantidade()
} senao{
escreva("Erro - escolha uma opção válida.")
escolher_fruta()
}
}

funcao inicio(){
escreva("Morango R$ 2,50 por Kg (acima de 5kg R$ 2,20 por Kg)\n")
escreva("Maçã R$ 1,80 por Kg (acima de 5kg R$ 1,50 por Kg)\n")
escreva("Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra \n")
escreva("ultrapassar R$ 25,00,receberá ainda um desconto de 10% sobre este total.\n")
escreva("\n")
escreva("Qual fruta você deseja comprar?\n")
escolher_fruta()
}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1126; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
