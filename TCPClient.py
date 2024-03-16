from socket import *
import feistel

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
#Conecta ao servidor
clientSocket.connect((serverName,serverPort))
#Recebe mensagem do usuario e envia ao servidor
message = input('Digite uma frase: ')

cipher_text = feistel.cipher(message)
clientSocket.send(cipher_text.encode())

#Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)

decode = modifiedMessage.decode()
deciphered_text = feistel.decipher(decode)

print("Retorno do Servidor:", deciphered_text)
clientSocket.close()
