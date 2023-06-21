import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return
    try:
        with open(f"{path_file}", "r") as file:
            stacked_text = file.read().split("\n")
            return stacked_text
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
