from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f"{self.data}"

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        # if self.is_empty():
        #     return None
        return self.data.pop(0)

    def search(self, index):
        if len(self.data) == 0 or index > len(self.data) - 1 or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]

    def is_empty(self):
        if not len(self.data):
            return True
        return False
