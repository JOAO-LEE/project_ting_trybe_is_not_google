from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.data)

    def __str__(self):
        return f"{self.data}"

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.data.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if len(self.data) == 0 or index > len(self.data) - 1 or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
