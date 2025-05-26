import socket

def enviar_tarefa(ip, porta, id_tarefa):
    try:
        with socket.create_connection((ip, porta)) as sock:
            sock.sendall(f"TAREFA {id_tarefa}".encode())
            print(f"Tarefa {id_tarefa} enviada para {ip}:{porta}")
    except Exception as e:
        print(f"Erro ao enviar tarefa: {e}")

if __name__ == "__main__":
    while True:
        entrada = input("Digite o ID da tarefa (ou 'sair'): ")
        if entrada.lower() == "sair":
            break
        enviar_tarefa("127.0.0.1", 6000, entrada)