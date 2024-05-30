from dataclasses import dataclass
from os import system
from typing import List
from types import NoneType

static = staticmethod
void = NoneType

# _Nomes
# estrutura da lista de nomes
# dividido em feminino e masculino
@dataclass
class _Nomes:
    fem: List[str]
    masc: List[str]

# _Registro
# armazena as variaveis:
# 1. objeto nome contendo as listas de string
# para os nomes femininos e masculinos
# 2. lista de string de sobrenomes
class _Registro:
    nomes: _Nomes
    sobrenomes: List[str]
    _carregado: bool = False

    @static
    def carregar() -> void:
        if _Registro._carregado == False:
            _nomes_fem: List[str] = ["adriana", "alessandra", "alice", "amanda", "ana", "andrea", "andreia", "beatriz", "bianca", "bruna",\
                "camila", "carla", "cassia", "carolina", "clara", "claudia", "cristina", "daniela", "daiane", "eduarda",\
                "elaine", "eliane", "elisabete", "elisangela", "emilia", "erika", "fabiana", "fernanda", "flavia",\
                "gabriela", "gisele", "graziela", "helena", "ines", "isa", "isabel", "isabela", "iza", "jaqueline", "josefa",\
                "julia", "juliana", "karina", "karla", "karine", "kelly", "larissa", "lais", "leila", "leticia",\
                "luana", "lucia", "luciana", "luisa", "luzia", "margarida", "marcela", "marcia", "mariana", "mariane",\
                "marilia", "marisa", "marlene", "martha", "mayara", "michele", "natalia", "patricia", "priscila",\
                "rafaela", "raimunda", "raquel", "regiane", "regina", "renata", "roberta", "rosa", "rosangela", "roseli",\
                "roseli", "sabrina", "sandra", "sara", "silvana", "silvia", "solange", "sueli", "suzana", "tania",\
                "tatiane", "valeria", "valquiria", "vanessa", "vera", "viviane"]

            _nomes_masc: List[str] = [ "alan", "allan", "aldo", "amauri", "anderson", "andre", "antonio", "arthur",\
                "breno","bruno", "caio", "caua","carlos", "cesar", "cezar", "davi", "david", "daniel", "denilson", "diego", "diogo",\
                "eduardo","enzo", "eustaquio", "fabricio", "fausto", "felipe", "fernando", "francisco", "gabriel","geraldo",\
                "gabriel", "guilherme", "helio", "ivan", "ivanildo", "jair", "james",\
                "jeferson","jefferson","joao","john", "johnathan", "jonatan", "jonathan", "joaquim", "joel",\
                "jonas", "jorge", "julio", "lauro","lazaro", "leandro", "leandro", "leonardo", "leo",\
                "levi", "lucas", "lukas", "luiz", "luis","luan",\
                "marcelo", "marco", "marcos", "markos", "mario", "mateus", "matheus",\
                "miguel", "moises", "natan", "nathan", "nelson", "otavio", "paulo", "pedro",\
                "rafael", "raphael","raul", "renan", "renato", "renato", "ricardo", "roberto",\
                "robert","rodrigo", "samuel","silvio", "thiago", "tiago", "tulio", "vinicius",\
                "vitor","victor", "wagner","washington", "wiliam", "william", "yago","yuri"]

            _Registro.nomes = _Nomes(_nomes_fem,_nomes_masc)
            _Registro.sobrenomes = ["aguiar","almeida","alves","amaral",\
                "albuquerque","andrade","avila","araujo",\
                "bandeira","bahia","borges","brito",\
                "cabral","caldas","campos","camargo",\
                "cardoso","carvalho","carneiro","castro",\
                "cerqueira","correa","costa",\
                "dias","duarte","dutra","esteves",\
                "fagundes","fernandes","ferreira",\
                "fonseca","figueiredo","freire",\
                "gama","garcia","goes","gois","gomes","goncalves",\
                "guimaraes","guedes","lima","magalhaes","maciel","martins",\
                "mascarenhas","mata","medeiros","meireles","miranda",\
                "melo","morais","moraes","neves","nunes","oliveira",\
                "paz","penha","pinheiro","pereira","prado","prates",\
                "ramos","ramires","ramirez","resende","rezende","rodrigues",\
                "sa","silva","silveira","sousa","souza","santos",\
                "teixeira","teles","vaz","veloso","viegas","vieira"]
            _Registro.nomes.fem.sort()
            _Registro.nomes.masc.sort()
            _Registro.sobrenomes.sort()
            _Registro._carregado== True

# Editor
# acessar registro
class Editor:
    registro = _Registro()

    @static
    def visualizar_registro(flag:str)->void:
        if flag == "todos":
            #print("_________ Registro _________")
            print("\n» Listando todos os nomes e sobrenomes")

            # formatando os elementos de cada lista
            fmt_nomes_fem: str = ""
            fmt_nomes_masc: str = ""
            fmt_sobrenomes: str = ""
            
            j: int = 1
            while j <= 3:
                lista_x: List[str] = []
                if j == 1:
                    lista_x = Editor.registro.nomes.fem
                elif j == 2:
                     lista_x = Editor.registro.nomes.masc
                elif j == 3:
                     lista_x = Editor.registro.sobrenomes

                for k in range(0,len(lista_x)):
                     # formatando
                     e: str = "?"
                     e = lista_x[k]
                     if k < len(lista_x)-1:
                        e = "\"{}\",".format(e)
                     else:
                        e = "\"{}\"".format(e)
                    # 10 'nomes' por linha
                     if k > 1 and k % 10 == 0:
                         e += "\n"
                    # incrementar a string correspondente
                     if j == 1:
                        fmt_nomes_fem += e
                     elif j == 2:
                        fmt_nomes_masc += e
                     elif j == 3:
                        fmt_sobrenomes += e
                     else:
                        pass
                j += 1
            # escreve os elementos formatados
            print("\nNomes femininos({}{}{}):".format(\
                "\033[38;2;0;254;130m",\
                len(Editor.registro.nomes.fem),\
                "\033[38;2;0;180;250m"))
            print("\033[38;2;100;100;100m")
            print(fmt_nomes_fem)
            print("\033[38;2;0;180;250m")

            print("\nNomes masculinos({}{}{}):".format(\
                "\033[38;2;0;254;130m",\
                len(Editor.registro.nomes.masc),\
                "\033[38;2;0;180;250m"))
            print("\033[38;2;100;100;100m")
            print(fmt_nomes_masc)
            print("\033[38;2;0;180;250m")
            
            print("\nSobrenomes({}{}{}):".format(\
                "\033[38;2;0;254;130m",\
                len(Editor.registro.sobrenomes),\
                "\033[38;2;0;180;250m"))
            print("\033[38;2;100;100;100m")
            print(fmt_sobrenomes)
            print("\033[38;2;0;180;250m")
                    
def main()->void:
    # Testando
    # iniciar a logica estatica do registro
    Editor.registro.carregar()
    # visualizar as listas de nomes e sobrenomes
    Editor.visualizar_registro("todos")



if __name__ == "__main__":
    system("cls || clear")
    print("\033[38;2;0;180;250m")
    main()

