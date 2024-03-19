import os
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_data = txt_importer(path_file)
    file_name = os.path.basename(path_file)

    # Verifica se o arquivo já foi processado anteriormente
    if file_metadata(instance, file_name):
        print(
            f"Arquivo {file_name} já foi processado anteriormente. Ignorando."
        )
        return

    metadata = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(file_data),
        "linhas_do_arquivo": file_data,
    }

    # Adiciona os metadados do arquivo à fila
    instance.enqueue(metadata)

    # Mostra os dados processados via stdout
    print(metadata)


def remove(instance):
    try:
        # Remove o primeiro arquivo processado da fila
        removed_file = instance.dequeue()
        print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso"
        )
    except IndexError:
        print("Não há elementos")


# Exemplo de uso:
# remove(minha_fila)


def file_metadata(instance, position):
    try:
        # Busca as informações do arquivo na posição especificada na fila
        metadata = instance.search(position)

        # Mostra as informações do arquivo via stdout
        print(metadata)
    except IndexError:
        print("Posição inválida", file=sys.stderr)


# Exemplo de uso:
# file_metadata(minha_fila, 0)
