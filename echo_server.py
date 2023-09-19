import socket
from threading import Thread
BytesToRead = 4096
HOST = "127.0.0.1"
PORT = 8080

def handleConnection(conn,addr):
    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(BytesToRead)
            if not data:
                break
            print(data)
            conn.sendall(data)

def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()
        while True:
            conn,addr = s.accept()
            handleConnection(conn, addr)
        

def startThreadedServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        while True:
            conn,addr = s.accept()
            thread = Thread(target = handleConnection, args=(conn, addr))
            thread.run()

#startServer()
startThreadedServer()
