import socket

HOST = '127.0.0.1'
PORT = 61456
TO_PORT = 62295

mission_abort = 1

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:

    inputFromBase = input('Press 1 to abort mission\nPress 2 to continue\n')
    command = 0
    try:
        command = int(inputFromBase)
    except ValueError:
        print('Invalid number!')

    if command == 1:
        sock.sendto(str.encode('ABORT'), (HOST, TO_PORT))
        print('\nSend command to abort mission!\n')
