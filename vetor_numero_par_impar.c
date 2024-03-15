#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>

 // Modelo
// \033[38;2;<r>;<g>;<b>m  

#define _YellowGreen "\033[38;2;200;250;75m"
#define _LimeDark "\033[38;2;65;245;100m"
#define _Magenta "\033[38;2;225;70;255m"
#define _Azure "\033[38;2;85;220;255m"
#define _Gold "\033[38;2;255;230;85m"

#define maxN 10
int Inteiros[maxN];

void inserir_numeros(){
int i=0;
int pares = 0;
int impares = 0;
for(i=0;i<maxN;i++){
int input = 0;
printf("\n %s Insira o %s %iº %s número: ",_LimeDark,_Gold,i+1,_LimeDark);
scanf("%i",&input);
if(input%2==0){
pares++;
} else{
impares++;
}
Inteiros[i]=input;
}
printf("\n Resultado: %s %i pares %s e %s %i impares%s.",_Azure,pares,_LimeDark,_Magenta,impares,_LimeDark);
fflush(stdin);
printf("\n\n\n[Digite algo para continuar]\n");
char* presskey;
scanf("%s",&presskey);
inserir_numeros();
}

int main(){
system("cls || clear");
setlocale(LC_ALL,"");
printf("%s \n_______________________\n|                     |\n|    Criar vetores    |\n|_____________________|\n", _YellowGreen);
inserir_numeros();
return 0;
}
