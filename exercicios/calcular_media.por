programa {

  cadeia nome
  inteiro idade
  real notaI
  real notaII
  real notaIII
  real notaIV

  funcao mediaAritmetica(real notaI, real notaII, real notaIII, real notaIV){
  real resultado = (notaI+notaII+notaIII+notaIV)/4
  escreva("\n ")
  escreva("\n Esse é o seu resultado:")
  escreva("\n ")
  escreva("\n Nome do aluno: ", nome)
  escreva("\n Idade: ", idade)
  escreva("\n Nota I: ", notaI)
  escreva("\n Nota II: ", notaII)
  escreva("\n Nota III: ", notaIII)
  escreva("\n Nota IV: ", notaIV)
  escreva("\n Média de notas: ", resultado)
  }

  funcao inserirDados(){
  cadeia i_nome
  inteiro i_idade
  real i_notaI
  real i_notaII
  real i_notaIII
  real i_notaIV
  escreva("\n Nome:")
  leia(i_nome)
   escreva("\n Idade:")
  leia(i_idade)
   escreva("\n Nota I:")
  leia(i_notaI)
    escreva("\n Nota II:")
  leia(i_notaII)
    escreva("\n Nota III:")
  leia(i_notaIII)
    escreva("\n Nota IV:")
  leia(i_notaIV)

  se(i_idade <= 0 e i_idade >= 99 e
  i_notaI < 0 e i_notaI > 10 e 
  i_notaII < 0 e i_notaII > 10 e 
  i_notaIII < 0 e i_notaIII > 10 e 
  i_notaIV < 0 e i_notaIV > 10 ){
  escreva("\n Erro, insira os seus dados novamente:")
  escreva("\n ")
  inserirDados()
  }
  senao{
  nome = i_nome
  idade = i_idade
  notaI = i_notaI
  notaII = i_notaII
  notaIII = i_notaIII
  notaIV = i_notaIV

  mediaAritmetica(notaI, notaII, notaIII, notaIV)
  }
  }

  funcao inicio() {
  escreva("\n _____ Calculador de Notas _____")
  escreva("\n Insira seus dados:")
  escreva("\n ")
  inserirDados()
  }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1521; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */