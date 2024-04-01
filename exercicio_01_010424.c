#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define QuantAlunos 2
#define QuantMaterias 2
#define QuantNotas 3
#define Green "\033[38;2;42;245;96m"

typedef struct{
char nome[28];
float notas[QuantMaterias][QuantNotas];
} Aluno;

Aluno Vetor_Alunos[QuantAlunos];

void novoRegistro(){
static alunosRegistrados = 0;
if(alunosRegistrados < QuantAlunos){
	
int i = 0;
for(i; i<QuantAlunos; i++){
system("cls || clear");
printf("\n Novo registro \n");
printf("\n Insira o nome do aluno: ");
scanf("%s",Vetor_Alunos[i].nome);
int j = 0;
int k = 0;
	while(j<QuantMaterias){
	system("cls || clear");
	printf("\n Registrando notas do aluno %s \n",Vetor_Alunos[i].nome);
	switch (j)
	{
	case 0:
  	printf("\n Materia 01\n");
  	break;
	case 1:
  	printf("\n Materia 02\n");
  	break;
	default:
  	break;
	}
		for(k; k<QuantNotas; k++){
		printf("\n Nota %i: ",k+1);
		float scanNota;
		scanf("%f",&scanNota);
		Vetor_Alunos[i].notas[j][k] = scanNota;
		}
    k=0;
    j++;
   }
  }
 }
}


int main(){
system("cls || clear");
printf("%s",Green);
novoRegistro();
return 0;
}
