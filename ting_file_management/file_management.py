def is_valid_txt_file(path_file):
    return path_file.endswith(".txt")


def txt_importer(path_file):
    if not is_valid_txt_file(path_file):
        print("Formato inválido - Arquivo deve ter extensão .txt")
        return []

    try:
        with open(path_file, "r") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado")
        return []
    except IOError:
        print("Erro ao ler o arquivo")
        return []


# Exemplo de uso:
# linhas = txt_importer('arquivo.txt')
# print(linhas)
