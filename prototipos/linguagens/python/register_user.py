from os import system
from hashlib import sha256
import random
import string
from dataclasses import dataclass
from typing import List

@dataclass
class EncryptedString:
    original: str
    salting: str
    sha256: str

@dataclass
class Account:
    username: EncryptedString
    password: EncryptedString
    ID: str

class Database:
    serverLogs: List[str] = []
    accounts: List[Account] = []

    @staticmethod
    def genAccountId() -> str:
        x = len(Database.accounts)
        return f"{x:04d}"

    @staticmethod
    def registerAccount(username: str, password: str):
        salting_1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        salting_2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        un_encrypted = sha256(f"{username}{salting_1}".encode()).hexdigest()
        pw_encrypted = sha256(f"{password}{salting_2}".encode()).hexdigest()
        username_object = EncryptedString(username, salting_1, un_encrypted)
        password_object = EncryptedString(password, salting_2, pw_encrypted)
        account = Account(username_object, password_object, Database.genAccountId())
        Database.accounts.append(account)
        Database.serverLogs.append(" New account registered:\n ID: {}\n username: {}\n password: {}".format(
        account.ID,account.username.sha256,account.password.sha256))

class Validate:
    @staticmethod
    def entryUsername(received_username: str) -> bool:
        Database.serverLogs.append(
            " Verifying if username exists: \n {}".format(
            sha256(received_username.encode()).hexdigest()))
        for account in Database.accounts:
            u = sha256(f"{received_username}{account.username.salting}".encode()).hexdigest()
            if account.username.sha256 == u:
                return True
        Database.serverLogs.append(" Username not found:\n {}".format(
            sha256(received_username.encode()).hexdigest()))
        return False

    @staticmethod
    def entryPassword(received_username: str, received_password: str) -> bool:
        Database.serverLogs.append(
            " Trying username and password combination:\n {}\n {}".format(
                sha256(received_username.encode()).hexdigest(),sha256(received_password.encode()).hexdigest()))
        for account in Database.accounts:
            u = sha256(f"{received_username}{account.username.salting}".encode()).hexdigest()
            p = sha256(f"{received_password}{account.password.salting}".encode()).hexdigest()
            if account.username.sha256 == u:
                if account.password.sha256 == p:
                    Database.serverLogs.append(
                        " Login success for credentials:\n {}\n {}".format(p, u))
                    return True
        Database.serverLogs.append(
            " Login attempt failed for credentials:\n {}\n {}".format(
                sha256(received_username.encode()).hexdigest(),sha256(received_password.encode()).hexdigest()))
        return False

    @staticmethod
    def login(username: str, password: str):
        if Validate.entryUsername(username):
            if Validate.entryPassword(username, password):
                return True
        return False

def testing1():
    print("\033[38;2;220;254;100m")
    Database.registerAccount("admin", "x1A2ABC_1Z123abc")
    Database.registerAccount("bulbassauro", "AZ2_M1Xabc_7890")
    Database.registerAccount("charizard", "_AMZ1A_10JAS91")
    Database.registerAccount("squirtle","A120Z_K1_ZM")
    print(" ~> Registrando uma nova conta")
    username = input("  Crie um nome de usuário: ")
    password = input("  Crie uma senha: ")
    print("  ...  ")
    Database.registerAccount(username, password)
    print("{}\n {}".format(" A sua conta foi registrada com sucesso!",
          "Para acessar a sua conta insira o seu [nome de usuário] e [senha]."))
    print("\n ~> Login")
    enter_username: str = str(input("  Insira o seu nome de usuário: "))
    enter_password: str = str(input("  Insira a sua senha: "))
    while not Validate.login(enter_username, enter_password):
        print("  Erro - credenciais inválidas, tente novamente")
        enter_username = input("  Nome de usuário: ")
        enter_password = input("  Senha: ")
    if Validate.login(enter_username,enter_password):
        print("\n Bem vindo!")
        print("\033[38;2;100;254;0m")
        print("\n\n ~> Server logs:")
        for log in Database.serverLogs:
            print("\n"+log)

def main():
    system("cls || clear")
    testing1()


if __name__ == "__main__":
    main()
else:
    print("Error")
