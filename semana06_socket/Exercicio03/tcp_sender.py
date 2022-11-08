import socket
import sys

TCP_IP = "127.0.0.1"  # ip
FILE_PORT = 5005  # Porta do arquivo
DATA_PORT = 5006  # Porta de dados
buf = 1024
file_name = sys.argv[1]


try:
    # Define tipo de entrada e saída
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))  # Conecta
    sock.send(file_name)  # Envia
    sock.close()

    print("Sending %s ..." % file_name)

    f = open(file_name, "rb")  # Acessa o arquivo
    # Define tipo de entrada e saída
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))  # Conecta
    data = f.read()  # Faz a leitura dos dados
    sock.send(data)  # Envia os dados

finally:
    sock.close()
    f.close()
