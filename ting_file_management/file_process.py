from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        file = instance.search(index)
        if path_file == file["nome_do_arquivo"]:
            return

    file_rows = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_rows),
        "linhas_do_arquivo": file_rows,
    }

    instance.enqueue(new_dict)

    print(new_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
