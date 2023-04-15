import sys
from socket import *

# 커맨드라인에서 서버 이름과 포트 번호를 얻음
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

# 클라이언트 소켓 생성하고 서버에 연결
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentences = []
while True:
    line = input()
    if not line.strip():
        break
    line += "\r\n"
    sentences.append(line)
sentences.append("\r\n")
message = ''.join(sentences)

clientSocket.send(message.encode())

data = clientSocket.recv(2048)
print(data.decode(), end = "")
clientSocket.close()
