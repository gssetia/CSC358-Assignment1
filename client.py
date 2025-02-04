import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    #message = b'This is the message.  It will be repeated.'
    #print('sending {!r}'.format(message))
    #sock.sendall(message)
    # Look for the response
    #amount_received = 0
    #amount_expected = len(message)
    sock.sendall(b'Connect')
    data = sock.recv(1024)
    print(data.decode("utf-8"))

    while True:

        command = input(">")
        if 'LIST' in command:
            sock.sendall(b'LIST')

        elif 'PUSH' in command:
            sock.sendall(b'PUSH')
            filename = command.replace('PUSH', '')
            filename = filename.replace(' ', '')
            sock.sendall(filename.encode("utf-8"))

            file = open('client_data/'+filename, "r")
            data = file.read()

            sock.sendall(data.encode("utf-8"))
            file.close()

        elif 'DELETE' in command:
            sock.sendall(b'DELETE')
            filename = command.replace('DELETE', '')
            filename = filename.replace(' ', '')
            sock.sendall(filename.encode("utf-8"))

        elif command == 'EXIT':
            sock.sendall(b'EXIT')
            break

        data = sock.recv(1024)
        print(data.decode("utf-8"))


finally:
    print('Disconnected from the server!')
    sock.close()
