programa {

  real notaI = 0.0
  real notaII = 0.0
  real media = 0.0

  funcao media_aritmetica(){
  media = (notaI+notaII)/2
  escreva("\n ")
  escreva("\n Esse é o seu resultado:")
  escreva("\n  Nota I: ", notaI)
  escreva("\n  Nota II: ", notaII)
  escreva("\n  Média de notas: ", media)
  escreva("\n")
  se(media >= 6.0){
  escreva("Você está aprovado.")
  }
  senao se(media == 5 ou media == 4){
  escreva("Você está em recuperação.")
  }
  senao se(media < 4){
  escreva("Você está reprovado.")
  }
  }

  funcao inserir_notas(){
  real _notaI
  real _notaII
  
  escreva("\n Nota I:")
  leia(_notaI)
  escreva("\n Nota II:")
  leia(_notaII)


  se( _notaI < 0 ou _notaI > 10 ou 
  _notaII < 0 ou _notaII > 10){
  escreva("\n Erro, insira os seus dados novamente:")
  escreva("\n ")
  inserir_notas()
  }
  senao{
  notaI = _notaI
  notaII = _notaII
  media_aritmetica()
  }
  }

  funcao inicio() {
  escreva("\n _____ Calculador de Notas _____")
  escreva("\n Insira seus dados:")
  escreva("\n ")
  inserir_notas()
  }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 467; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */