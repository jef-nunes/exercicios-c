#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define QuantAlunos 2
#define QuantMaterias 2
#define QuantNotas 3
#define White "\033[38;2;254;254;254m"
#define BrightRed "\033[38;2;254;64;100m"
#define Red "\033[38;2;214;50;90m"
#define Green "\033[38;2;42;245;96m"
#define Blue "\033[38;2;56;205;254m"
#define Turquoise "\033[38;2;70;215;240m"
#define BlackBG "\033[48;2;1;1;1m"
#define DarkGreyBG "\033[48;2;44;48;48m"
#define DarkRedBG "\033[48;2;52;12;22m"
#define DarkGreenBG "\033[48;2;16;28;17m"
#define DarkBlueBG "\033[48;2;1;24;54m"
#define DarkTurquoiseBG "\033[48;2;15;56;70m"

typedef struct{
char nome[28];
float notas[QuantMaterias][QuantNotas];
} Aluno;

Aluno Vetor_Alunos[QuantAlunos];
int alunosRegistrados = 0;

void novoRegistro(){
if(alunosRegistrados < QuantAlunos){
int i = 0;
for(i; i<QuantAlunos; i++){
system("cls || clear");
printf("\n %s%sRegistro de Notas \n",DarkBlueBG,Blue);
printf("\n %s%sTotal de alunos registrados:%s %s%i \n",DarkGreyBG,White,DarkTurquoiseBG,Turquoise,alunosRegistrados);
printf("%s%s",DarkGreenBG,Green);
printf("\n Insira o nome do aluno: ");
scanf("%s",Vetor_Alunos[i].nome);
int j = 0;
int k = 0;
alunosRegistrados++;
	while(j<QuantMaterias){
	system("cls || clear");
	printf("\n %s%sRegistro de Notas \n",DarkBlueBG,Blue);
	printf("\n %s%sTotal de alunos registrados:%s %s%i \n",DarkGreyBG,White,DarkTurquoiseBG,Turquoise,alunosRegistrados);
	printf("%s%s",DarkGreenBG,Green);
	printf("\n Registrando notas do aluno %s \n",Vetor_Alunos[i].nome);
	switch(j){
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

void visualizarRegistros(){
int i = 0;
for(i;i<alunosRegistrados;i++){
}
}


int main(){
system("cls || clear");
printf("%s",Green);
novoRegistro();
// visualizarRegistros();
printf("%s%s",White,BlackBG);
return 0;
}
