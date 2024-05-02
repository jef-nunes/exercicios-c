from os import system
from typing import List
from dataclasses import dataclass as struct

@struct
class Pessoa:
    id_usuario: str
    nome: str
    idade: int
    altura: float
    peso: float
    imc: float

pessoas: List[Pessoa] = []

class Interface:
    Titulo:str = "=_____ SENAI _____="
    @staticmethod
    def reset():
        system("cls || clear")
        print(Interface.Titulo)
    @staticmethod
    def textColor(r,g,b):
        print("\033[38;2;{};{};{}m".format(r,g,b))

class Registros:
    contador: int = 1
    @staticmethod
    def visualizar():
        for elemento in pessoas:
            print("\n")
            print(" _________________________________________")
            print(" ID: {}".format(elemento.id_usuario))
            print(" Nome: {}".format(elemento.nome))
            print(" Idade: {}".format(elemento.idade))
            print(" Altura: {}".format(elemento.altura))
            print(" Peso: {}".format(elemento.peso))
            print(" IMC: {}".format(elemento.imc))
            print(" _________________________________________")
    @staticmethod
    def novo():
        while True:
            Interface.reset()
            print("quantidade de pessoas registradas {}".format(len(pessoas)))
            next = str(input("Realizar novo registro? Sim[S]/Não[N]"))
            if next.lower() == "s":
                Interface.reset()
                print("quantidade de pessoas registradas {}".format(len(pessoas)))
                print("\n ~> Novo registro iniciado")
                nome = str(input("Nome: "))
                idade = int(input("Idade: "))
                altura = float(input("Altura: "))
                peso = float(input("Peso: "))
                alturaQuad = altura*altura
                imc = peso / alturaQuad
                if Registros.contador < 10:
                    id_usuario =str("0{}".format(Registros.contador))
                else:
                    id_usuario = str(Registros.contador)
                p = Pessoa(id_usuario,nome,idade,altura,peso,imc)
                pessoas.append(p)
            else:
                break
        Registros.visualizar()

Interface.textColor(138,254,48)
Registros.novo()