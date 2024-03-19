import sys
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    if not path_file.lower().endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return []

    with open(path_file, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


# Exemplo de uso:
# linhas = txt_importer('arquivo.txt')
# print(linhas)
