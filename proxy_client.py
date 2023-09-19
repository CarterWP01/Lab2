import socket

BytesToRead = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHOST: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)
        chunk = s.recv(BytesToRead)
        result = b'' + chunk

        while(len(chunk)>0):
            chunk = s.recv(BytesToRead)
            result += chunk
        s.close()
        return result

print(get("127.0.0.1",8080))