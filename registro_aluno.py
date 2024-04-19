from os import system
from dataclasses import dataclass as structure
from typing import List

@structure
class Materia():
  nome: str = "?"
  nota1: float = 0.0
  nota2: float = 0.0
  nota3: float = 0.0
  
class Aluno():
  identificador: str
  nome: str
  materias: List[Materia]
  def __init__(self, _nome: str):
        print("New ~Aluno object created")
        self.id = "0"+str(registros)
        self.nome = _nome
        self.materias = [Materia("Logica",0.0,0.0,0.0),Materia("Fisica",0.0,0.0,0.0)]

registros: int = 0
vetorAlunos: List[Aluno]

def novoRegistro():
   print("Novo registro iniciado:\n")
   print("» Nome:")
   _nome = str(input(""))
   if len(_nome) > 0:
    aluno = Aluno(_nome)
    print("O registro do aluno foi concluido")
    print(aluno.id)
    print(aluno.nome)
   else:
    print("Insira algum nome")

novoRegistro()
