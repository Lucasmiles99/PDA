import socket
import threading

class ServidorNode(threading.Thread):
    def __init__(self, node):
        super().__init__()
        self.node = node

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.node.ip, self.node.port))
            server_socket.listen()
            print(f"[Node {self.node.node_id}] Servidor iniciado em {self.node.ip}:{self.node.port}")

            while True:
                conn, addr = server_socket.accept()
                threading.Thread(target=self.node.manipula_cliente, args=(conn,)).start()