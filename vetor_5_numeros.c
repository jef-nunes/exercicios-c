#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <locale.h>

int V5[5];

void visualizar_V5(){
int indice = 0;
while(indice<=4){
printf("\n V5[%d] = %d",indice,V5[indice]);
indice++;
}
}

void constroi_V5(){
int i = 0;
for(i=0;i<5;i++){
system("cls || clear");
int input;
printf("Digite o valor do %dº elemento, indice[%d]: ",i+1,i);
scanf("%i",&input);
V5[i]=input;
}
visualizar_V5();
}

int main(){
setlocale( LC_ALL,"");
constroi_V5();
return 0;
}
