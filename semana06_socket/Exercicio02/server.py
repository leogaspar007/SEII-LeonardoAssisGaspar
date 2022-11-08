import socket
import threading

HEADER = 64
PORT = 5050  # Porta
SERVER = socket.gethostbyname(socket.gethostname())  # IP padrão
ADDR = (SERVER, PORT)  # Endereço
FORMAT = 'utf-8'  # Formato para utilizar na decodificação da mensagem
DISCONNECT_MESSAGE = "!DISCONNECT"

# Define tipo de entrada e saída do server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)  # Atribui uma porta e um IP ao server


def handle_client(conn, addr):  # Define a função que irá lidar com o client
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()  # Encerra a conexão com o client


def start():
    server.listen()
    print(f"[OUVINDO] Server está ouvindo em {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[INICIANDO] server está iniciando...")
start()
