import socket

HEADER = 64
PORT = 5050  # Porta
FORMAT = 'utf-8'  # Formato para utilizar na decodificação da mensagem
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.100.36"  # IP do client
ADDR = (SERVER, PORT)  # Endereço

# Define tipo de entrada e saída do client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)  # Inicia a conexão


def send(msg):  # Define função para envio
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)
