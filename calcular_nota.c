#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>

float nota_I = -1;
float nota_II = -1;
float resultado;

    void calcular_media(){
    char* enter;
    resultado = (nota_I + nota_II) / 2;
    if(resultado >= 7){
    printf("Aprovado");
    } else{
    printf("Reprovado");
    }
    printf(" \n \n \n [Digite algo para realizar outro calculo. Para encerrar este programa digite 'Ctrl+C']\n \n");
    fflush(stdin);
    scanf("%s",&enter);
    if(enter=="12321321321321312321312312321312"){
    printf("Erro");
    }else{
    prologo();
    }
    }

    void insere_nota(){
    printf("Nota I: ");
    printf("\n");
    scanf("%f",&nota_I);
    printf("Nota II: ");
    printf("\n");
    scanf("%f",&nota_II);
    if(nota_I > -1 && 
        nota_II > -1 && 
         nota_I <= 10 && 
          nota_II <= 10){
    calcular_media();
    } else if(nota_I < 0 || nota_II < 0){
    printf("Erro - Valor negativo. Insira as suas notas novamente: \n");
    insere_nota();
    }
    if(nota_I > 10 || nota_II > 10){
    printf("Erro - Alguma das notas inseridas ultrapassa o limite (10). Insira as suas notas novamente: \n");
    insere_nota();
    }
    }

    void prologo(){
    system("cls || clear");
    printf("\n Calculadora de Media \n");
    printf("A seguir insira as suas notas: \n");
    insere_nota();
    }

    void main(){
    prologo();
    }
