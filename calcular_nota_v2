#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>

float Notas[4];
#define quantNotas 4

void insere_notas(){
int i;
float media; 
for(i=0; i<quantNotas; i++){
printf("\n Insira o valor da %iª nota: ",i+1);
float input;
scanf("%f",&input);
Notas[i] = input;
media += input;
fflush(stdin);
}
media = media/quantNotas;
printf("\n Media de notas: %.2f",media);
}

int main(){
setlocale(LC_ALL,"");
insere_notas();
return 0;
}
