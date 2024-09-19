#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

// Strings
#define _Green "\033[38;2;42;245;96m"
#define _Red "\033[38;2;245;42;62m"
#define _Blue "\033[38;2;20;212;255m"
#define _Yellow "\033[38;2;255;230;85m"
#define _Cyan "\033[38;2;0;255;240m]"
#define Titulo "\n ______________\n |            |\n |  Vetores   |\n |____________|\n"
// Numeros
#define V1Length 6

int V1[V1Length];

void insere_numeros(){
int i = 0;
bool next = false;

for(i=0;i<V1Length;i++){
next = false;

while(next==false){
fflush(stdin);
int input;
printf("\n Insira o %iº número: ",i+1);
scanf("%i",&input);
if(input>0 && input%2==0){
V1[i] = input;
next = true;
} else{
 printf("\n Erro - Número inválido \n");
 }
}
}

printf("\n Ordem inversa: \n");
int j;
for(j=V1Length-1; j>=0; j--){
int X = V1[j];
printf("\n Indice %i: %i",j,X);
}
}

int main(){
 setlocale(LC_ALL,"");
 system("cls || clear");
 printf("%s %s",_Blue,Titulo);
 insere_numeros();
 return 0;
}
