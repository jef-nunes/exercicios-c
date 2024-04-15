programa{

real preco_alcool = 3.79
real preco_gasolina = 6.59

caracter comb = "?"
real litros = 0

calc_valor_total(){

real _valor = 0.0

se(comb == "A"){
_valor = preco_alcool*litros
se(litros <= 25){
_valor = _valor*0.02
} senao se(litros > 25){
_valor = _valor*0.04
}
}

 senao se(comb == "G"){
_valor = preco_gasolina*litros
se(litros <= 25){
_valor = _valor*0.03
} senao se(litros > 25){
_valor = _valor*0.05
}
}

escreva("Total: R$",_valor)
}

quantos_litros(){
real _litros
escreva("Digite quantos litros você quer abastecer \n")
leia(_litros)
se(_litros > 0){
litros = _litros
calc_valor_total()
} senao{
escreva("Erro - escolha um valor positivo.")
quantos_litros()
}
}

funcao escolher_combustivel(){
caracter _comb
escreva("Escolha o seu combustível:\n")
escreva("digite A para álcool ou \n")
escreva("G para gasolina: \n")
leia(_comb)
se(_comb == "A" ou comb == "G"){
comb = _comb
quantos_litros()
} senao{
escreva("Erro - Opção inválida, tente novamente.")
escolher_combustivel()
}
}

funcao inicio(){
escolher_combustivel()
}
}
