#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>

void respostas(){
	
}

void perguntas(){
int index = 1;
char* nome;
int idade;
float salario;

while(index < 4){
switch(index){
	case 1:
	printf("\n Insira o seu nome: ");
	scanf("%s",&nome);
	index++;
		break;
		
		
	case 2:
	printf("\n Insira a sua idade: ");
	int test_idade;
	scanf("%i",&test_idade);
	if(test_idade>0 && test_idade <= 100){
	idade = test_idade;
	index++;
	} else{
	printf("\n Erro - Idade invalida");
	}
		break;
		
		
	case 3:
	printf("\n Insira o seu salario: ");
	float _salario;
	scanf("%f",&_salario);
	if(_salario>0){
	salario = _salario;
	index++;
	} else{
	printf("\n Erro - Salario invalido");
	}
		break;
		
	default:
		break;
}
}
printf("Nome: %s, Idade: %i, Salario: %f",nome,idade,salario);
}


int main(){
system("cls || clear");
perguntas();
return 0;
}
