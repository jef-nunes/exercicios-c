from os import system
from dataclasses import dataclass
from typing import List
import hashlib

@dataclass
class User():
    username: str
    password: str

RegisteredUsers: List = []

def validateLogin(received_username,received_password) -> bool:
    x = ""
    for user in RegisteredUsers:
        if user.username == received_username:
            x = user
            break
    if x == "":
        return False
    h = hashlib.new('sha256')
    h.update(received_password.encode())
    hashed_received_password = h.hexdigest()
    if hashed_received_password == x.password:
        return True
    else:
        return False
    
def tryLogin():
    print("~ Login")
    u: str = str(input("Nome de usuario:\n"))
    p: str =  str(input("Senha:\n"))
    if validateLogin(u,p):
        print("Bem vindo!")
    else:
        print("Credenciais invalidas, tente novamente")
        tryLogin()

def registerUser():
  u: str = str(input("Escolha um nome de usuario:\n"))
  _p: str =  str(input("Escolha uma senha:\n"))
  h = hashlib.new('sha256')
  h.update(_p.encode())
  p = h.hexdigest()
  user = User(u,p)
  RegisteredUsers.append(user)
  print("Novo usuario registrado")
  print(user)
  print("\n\n\n")


# Testing
system("cls || clear")
registerUser()
tryLogin()
