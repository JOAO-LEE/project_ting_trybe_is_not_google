from ting_file_management.file_management import txt_importer
import sys


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
    if instance.is_empty():
        print("Não há elementos")
        return

    dequeued_file = instance.dequeue()
    print(f"Arquivo {dequeued_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position > len(instance) - 1 or instance.is_empty():
        print("Posição inválida", file=sys.stderr)
        return
    found_file = instance.search(position)
    print(found_file)
