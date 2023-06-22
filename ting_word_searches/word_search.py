# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    lower_cased_word = word.lower()

    word_occurrences_dict = {"palavra": "", "arquivo": "", "ocorrencias": ""}
    words_filtered = list()
    counter = 0
    encountered = list()
    for index in range(len(instance)):
        for j in instance.search(index)["linhas_do_arquivo"]:
            counter += 1
            if lower_cased_word in j.lower():
                encountered.append({"linha": counter})
        if encountered:
            word_occurrences_dict["palavra"] = lower_cased_word
            word_occurrences_dict["arquivo"] = instance.data[index][
                "nome_do_arquivo"
            ]
            word_occurrences_dict["ocorrencias"] = encountered
            words_filtered.append(word_occurrences_dict)
    return words_filtered


# fila = Queue()
# process("statics/nome_pedro.txt", fila)
# print(exists_word("Pedro", fila))


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
