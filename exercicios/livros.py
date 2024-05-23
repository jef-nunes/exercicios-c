from os import system as shell, getcwd
from types import NoneType
from typing import Dict, List, Union
from dataclasses import dataclass

# paths
path_catalogo = "catalogo.txt"

# classe de objeto contendo informações de um livro
@dataclass
class Livro:
    nome: str
    autor: str 
    categoria: str
    preco: float

# tipos adicionais
void = NoneType
union_float_str = Union[float,str]
array_float_str = List[union_float_str]

class Livraria:
    # vetor para guardar objetos 'Livro'
    catalogo: List[Livro] = []

    # adicionando um livro
    @staticmethod
    def adicionar_livro(nome: str,autor: str,categoria: str,preco: float)->void:
        local_variables = locals()
        for v in local_variables:
            if v == None:
                print("Erro - A variável {} possui valor nulo".format(v))
                return
        livro = Livro(nome,autor,categoria,preco)
        Livraria.catalogo.append(livro)

class Database:
    @staticmethod
    def atualizar_catalogo()->void:
        open(path_catalogo, 'w').close()
        with open(path_catalogo, "w") as arquivo:
            texto: str = ""
            for livro in Livraria.catalogo:
                texto += "\n{}".format(str(livro))
            arquivo.write(texto)

    @staticmethod
    def visualizar_catalogo()->void:
        with open(path_catalogo) as arquivo:
            print(arquivo.read())

#_____________________________________________________________________________
def testing():
    matriz_adicionar_livros: List[array_float_str] = [\
        ["ABC","autor1","categoria1",99.9],\
        ["DEF","autor2","categoria2",99.9],\
        ["GHI","autor3","categoria3",99.9]]
    for x in matriz_adicionar_livros:
        Livraria.adicionar_livro(x[0],x[1],x[2],x[3])
    #for livro in Livraria.catalogo:
    #    print(livro)
    Database.atualizar_catalogo()
    Database.visualizar_catalogo()


shell("cls || clear")
print("\033[38;2;30;255;0m") 
cwd = getcwd()
shell("cd {}".format(cwd))
shell("echo > {}".format(path_catalogo))
testing()