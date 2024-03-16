from socket import *
import feistel

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
    #Cria um socket para tratar a conexao do cliente
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)

    decode = sentence.decode()
    deciphered_text = feistel.decipher(decode)

    capitalizedSentence = deciphered_text.upper()

    cipher_text = feistel.cipher(capitalizedSentence)

    connectionSocket.send(cipher_text.encode())
    connectionSocket.close()
