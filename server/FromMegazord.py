import socket

HOST = '127.0.0.1'
PORT = 61341

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:
    data = sock.recv(1024)

    statement = repr(data)

    if 'Mission' in statement:
        print('\n' + statement + '\n')
        statement = 'no_statement'
    elif 'data' or 'Timestamp' in statement:
        print(statement)
        statement = 'no_statement'
