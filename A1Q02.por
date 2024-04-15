programa
{

cadeia info_1 = ""
cadeia info_2 = ""
inteiro info_3 = -1

funcao parte_3(){
 inteiro get_info_3
 escreva("\n Digite a quantos anos (completos) você está casada: \n")
 leia(get_info_3)
 se(get_info_3+0 == get_info_3){
 info_3 = get_info_3
 retorne
 } senao{
 escreva("\n Porfavor insira um valor inteiro (ex: 1,2,3...)")
 parte_3()
 }
}

funcao parte_2(){
inteiro get_info_2
escreva("Informe o seu estado civil: \n")
escreva("1: Solteira \n")
escreva("2: Casada \n")
escreva("3: Outro \n")
leia(get_info_2)
se(get_info_2 == 1){
info_2 = "Solteira"
retorne
} senao se(get_info_2 == 2){
 info_2 = "Casada"
 parte_3()
 }
 senao se(get_info_2 == 3){
 info_2 = "Outro"
 retorne
 }
   senao{
   escreva("Insira uma opção válida. \n")
   parte_2()
   }
}

funcao parte_1(){
caracter get_info_1
escreva("Digite a opção correspondente ao seu sexo \n")
escreva("F: Feminino \n")
escreva("M: Masculino \n")
leia(get_info_1)
se(get_info_1 == 'M'){
info_1 = "Masculino"
retorne 
} senao se(get_info_1 == 'F'){
info_1 = "Feminino"
parte_2()
}
senao{
escreva("Insira uma opção válida. \n")
parte_1()
}
}

funcao inicio(){
parte_1()
escreva("\n")
escreva("Tudo certo. Os seus dados foram salvos: \n")
se(info_1 != ""){
escreva("Sexo: ", info_1, "\n")
}
se(info_2 != "" e info_3 != -1){
escreva("Estado civil: ", info_2, " à ", info_3, " anos.")
 } senao se(info_2 != "" e info_3 == -1){
 escreva("Estado civil: ", info_2)
 }
 senao{
 escreva(" ")
 }
 escreva("\n")
}


}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1144; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */