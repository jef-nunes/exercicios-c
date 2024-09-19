#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// Mover para header
#ifndef Constantes
#define Constantes
#define Green "\033[38;2;0;250;110m"
#define Titulo "\n _________________________\n |                       |\n |         Notas         |\n |_______________________|\n"
// Quantidade de materias
#define QMaterias 3
// Quantidade de notas por materia
#define QNotas 2
#endif

	// Vetor de nomes de materia
 	char Nomes[QMaterias][20];
 	// Matriz de notas para cada materia
	float Notas[QMaterias][QNotas];

void visualizar_materias(){
system("cls || clear");
printf("\n Resultado: \n");
int i = 0;
 for(i;i<QMaterias;i++){
	printf("\n");
	printf("\n Materia: %s",Nomes[i]);
	int j = 0;
	while(j<QNotas){
	if(j==QNotas){
	break;
	}
	printf("\n Nota %i: %.1f",i+1,Notas[i][j]);
	j++;
   }
   
  }
printf("\n\n\n");
}

	
void inserir_materias(){
printf("\n Nova materia: ");
int i = 0;

 for(i;i<QMaterias;i++){
  float n1, n2, n3;
  printf("\n Insira o nome da materia: ");
  scanf("%s",Nomes[i]);
  fflush(stdin);
  printf("\n Insira agora cada nota: \n");
  int j = 0;
	while(j<QNotas){
	if(j==QNotas){
	break;
	}
	printf("\n Nota %i: ",j+1);
	scanf("%f",&Notas[i][j]);
	fflush(stdin);
	j++;
	}	
  }
visualizar_materias();
}

	int main(){
		printf("%s %s",Green,Titulo);
		inserir_materias();
		return 0;
	}
