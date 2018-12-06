import socket
from Command import Command

HOST = '127.0.0.1'
PORT = 61456
TO_PORT = 62295

mission_abort = 1

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:

    # --- TODO: make it a class and extract to method ---
    inputFromBase = input('Press 1 to abort mission\nPress 2 to change params\n')
    command = 0
    try:
        command = int(inputFromBase)
    except ValueError:
        print('Invalid number!')
    # ------

    if command == 1:
        sock.sendto(str.encode(Command.ABORT), (HOST, TO_PORT))
        print('\nSend command to abort mission!\n')
    if command == 2:
        sock.sendto(str.encode(Command.MOD_PARAMS), (HOST, TO_PORT))  # TODO add option to change params
        print('\nSend command to modify params!\n')
