import threading
import time

class Tarefa(threading.Thread):
    def __init__(self, id_tarefa):
        super().__init__()
        self.id_tarefa = id_tarefa

    def run(self):
        print(f"Executando tarefa {self.id_tarefa} na thread {threading.get_ident()}")
        time.sleep(1)