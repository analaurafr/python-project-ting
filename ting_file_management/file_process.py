import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    if not isinstance(file, list):
        return None

    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    if instance.__len__() > 0:
        for i in range(instance.__len__()):
            if instance.search(i)["nome_do_arquivo"] == path_file:
                return None

    instance.enqueue(dict_file)
    sys.stdout.write(str(dict_file))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    patch_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    sys.stdout.write(f"Arquivo {patch_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(str(file))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
