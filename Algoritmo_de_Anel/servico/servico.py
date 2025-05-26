import sys
from .node import Node

def main():
    if len(sys.argv) != 6:
        print("Uso: python servico.py <nodeId> <ip> <porta> <nextIp> <nextPorta>")
        return

    node_id = int(sys.argv[1])
    ip = sys.argv[2]
    porta = int(sys.argv[3])
    next_ip = sys.argv[4]
    next_porta = int(sys.argv[5])

    node = Node(node_id, ip, porta, next_ip, next_porta)
    node.iniciar()

if __name__ == "__main__":
    main()