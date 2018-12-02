import socket

HOST = '127.0.0.1'
PORT = 65433

mission_abort = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        inputFromBase = input('Press 1 to abort mission\nPress 2 to continue')
        command = 0
        try:
            command = int(inputFromBase)
        except ValueError:
            print('Invalid number!')

        if command == 1:
            s.sendall(b'ABORT')
            print('\nSend command to abort mission!\n')
