programa{

funcao cardapio(){
inteiro item = 0
real custo = 0.0
real custo_A = 10.50
real custo_B = 12.50
real custo_C = 39.99
real custo_D = 29.99
real custo_E = 15.50
real custo_F = 10.50
real custo_G = 12.50
real custo_H = 19.99
escreva("(1) item_A")
escreva("\n")
escreva("(2) item_B")
escreva("\n")
escreva("(3) item_C")
escreva("\n")
escreva("(4) item_D")
escreva("\n")
escreva("(5) item_E")
escreva("\n")
escreva("(6) item_F")
escreva("\n")
escreva("(7) item_G")
escreva("\n")
escreva("(8) Faça o seu pedido: \n")

leia(item)

escolha(item){
caso 1:
custo = custo_A
pare
caso 2:
custo = custo_B
pare
caso 3:
custo = custo_C
pare
caso 4:
custo = custo_D
pare
caso 5:
custo = custo_E
pare
caso 6:
custo = custo_F
pare
caso 7:
custo = custo_G
pare
}

escreva("O valor do ", item, " é", " R$", custo) 
}


funcao inicio(){

escreva("Bem vindo \n")
escreva("opções do cardápio: \n")
cardapio()
}
	
}
