import socket
import select

UDP_IP = "127.0.0.1"  # Endereço IP
IN_PORT = 5005  # Porta
timeout = 3  # Tempo de espera


# Define tipo de entrada e saída
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))  # Atribui uma porta e um IP

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("File name:", data)
        file_name = data.strip()

    f = open(file_name, 'wb')  # Acessa o arquivo

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)  # Escreve
        else:
            print("%s Finish!" % file_name)
            f.close()
            break
