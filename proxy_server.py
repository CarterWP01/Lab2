import socket
from threading import Thread

BytesToRead = 4096
ProxyServerHost = "127.0.0.1"
ProxyServerPort = 8080

def sendRequest(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect((host, port))
        clientSocket.send(request)
        clientSocket.shutdown(socket.SHUT_WR)
        data = clientSocket.recv(BytesToRead)
        result = b'' + data
        while(len(data)>0):
            data = clientSocket.recv(BytesToRead)
            result += data
        return result
    
def handleConnection(conn, addr):
    with conn:
        print(f"connected by {addr}")
        request = b''
        while True:
            data = conn.recv(BytesToRead)
            if not data:
                break
            print(data)
            request += data
        response = sendRequest("www.google.com", 80, request)
        conn.sendall(response)

def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((ProxyServerHost, ProxyServerPort))
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        serverSocket.listen(2)
        conn, addr = serverSocket.accept()
        handleConnection(conn, addr)

def startThreadedServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((ProxyServerHost, ProxyServerPort))
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        serverSocket.listen(2)
        
        while True:
            conn, addr = serverSocket.accept()
            thread = Thread(target=handleConnection, args = (conn, addr))
            thread.run()

#startServer()
startThreadedServer()
