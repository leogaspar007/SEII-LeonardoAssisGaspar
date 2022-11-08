import socket

TCP_IP = "127.0.0.1"  # Endereço IP
FILE_PORT = 5005  # Porta do arquivo
DATA_PORT = 5006  # Porta de dados
timeout = 3  # Tempo de espera
buf = 1024


# Define tipo de entrada e saída
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT))  # Atribui uma porta e um IP
sock_f.listen(1)  # Escuta

# Define tipo de entrada e saída
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))  # Atribui uma porta e um IP
sock_d.listen(1)  # Escuta


while True:
    conn, addr = sock_f.accept()
    data = conn.recv(buf)
    if data:
        print("File name:", data)
        file_name = data.strip()

    f = open(file_name, 'wb')

    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data)

    print("%s Finish!" % file_name)
    f.close()
