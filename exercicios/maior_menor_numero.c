#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>

#define maxN 5

float Numeros[maxN];

void insere_numeros(){
int i = 0;
float menorN = 99999;
float maiorN = -99999;

for(i=0; i<maxN; i++){
float input;
printf("\n Insira o %iº numero: ", i+1);
scanf("%f",&input);
Numeros[i] = input;
if(input<menorN){
menorN = input;
}
if(input>maiorN){
maiorN = input;
}
fflush(stdin);
}

printf("\n O menor número é: %.2f \n O maior número é: %.2f",menorN,maiorN);
}

int main(){
setlocale(LC_ALL,"");
insere_numeros();
return 0;
}
