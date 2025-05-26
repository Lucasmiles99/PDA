from servico.servidor_node import ServidorNode
import socket

class Node:
    def __init__(self, node_id, ip, port, next_ip, next_port):
        self.node_id = node_id
        self.ip = ip
        self.port = port
        self.next_ip = next_ip
        self.next_port = next_port

    def iniciar(self):
        servidor = ServidorNode(self)
        servidor.start()
        print(f"[Node {self.node_id}] Iniciado com próximo nó em {self.next_ip}:{self.next_port}")
        self.enviar_mensagem_eleicao()

    def manipula_cliente(self, conn):
        with conn:
            msg = conn.recv(1024).decode()
            print(f"[Node {self.node_id}] Mensagem recebida: {msg}")
            # Lógica de eleição ou de tarefa

    def enviar_mensagem_eleicao(self):
        try:
            with socket.create_connection((self.next_ip, self.next_port), timeout=2) as sock:
                msg = f"ELEICAO {self.node_id}"
                sock.sendall(msg.encode())
                print(f"[Node {self.node_id}] Enviando: {msg}")
        except Exception as e:
            print(f"[Node {self.node_id}] Erro ao enviar mensagem para o próximo nó: {e}")