import socket

BytesToRead = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHOST: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BytesToRead)
    while(len(result)>0):
        print(result)
        result = s.recv(BytesToRead)
    s.close()


#get("www.google.com",80)
get("127.0.0.1", 8080)