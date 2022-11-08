import socket
import time
import sys

UDP_IP = "127.0.0.1"  # Endereço IP
UDP_PORT = 5005  # Porta
buf = 1024
file_name = sys.argv[1]


# Define tipo de entrada e saída
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print("Sending %s ..." % file_name)

f = open(file_name, "r")  # Acessa o arquivo
data = f.read(buf)  # Lê o arquivo
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02)  # Delay

sock.close()
f.close()
