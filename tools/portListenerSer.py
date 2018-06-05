import socket
import sys

host = ''
port = 80
#Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print('Starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(10)

while True:
    print('Waiting for a connection.')
    connection, client_address = sock.accept()
    try:
        print ('Connection from: ', client_address)
        while True:
            data = connection.recv(16)
            print ('Received data: "%s"' % data)
            if data:
                print ('Data sent back to client')
                #connection.sendall(data)
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
