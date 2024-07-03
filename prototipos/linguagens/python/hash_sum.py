from hashlib import sha256
from os import path, system as shell
from types import NoneType as void

app_title: str = "Utilidade de calculo SHA256\n"

class SumSHA256:
    @staticmethod
    def target_archive(archive: str) -> str:
        print("Calculando sum para o arquivo: {}".format(archive))
        archive_size: float = round(path.getsize(archive) / (1024 * 1024), 2)
        mb100 = 100 * 1024 * 1024
        sha256_hash = sha256()
        arc_data: bytes = b""
        parsed_arc_data: float = 0.0
        with open(archive, "rb") as f:
            while True:
                block = f.read(mb100)
                if not block:
                    break
                arc_data += block
                parsed_arc_data += 100.0
                shell("cls || clear")
                print(app_title)
                print("Calculando resultado de soma de hash para o arquivo: {}".format(archive))
                progress: int = int((parsed_arc_data / archive_size) * 100)
                progress = 100 if progress > 100 else progress
                print("{}{} completo".format(progress,"\%")) 
        sha256_hash.update(arc_data)
        return sha256_hash.hexdigest()

def calc_sha256_sum()->void:
    try:
        archive_path: str = input("Insira o caminho do arquivo: ").strip().replace("\"", "").replace("\'", "")
        result = SumSHA256.target_archive(archive_path)
        print(f"Resultado: {result}")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado")
    except PermissionError:
        print(f"Erro: Acesso negado para o arquivo")

def user_interface()->void:
    while 1:
        calc_sha256_sum()
        novo_calc = str(input("\n\nRealizar novo cálculo? (S/N): ")).lower()
        if novo_calc != "s":
            break

if __name__ == "__main__":
    shell("cls || clear")
    print(app_title)
    user_interface()
