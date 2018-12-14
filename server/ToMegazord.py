import socket
from Command import Command


class BaseToMegazord:
    HOST = '127.0.0.1'
    PORT = 61456
    TO_PORT = 62295

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    def send_command(self, sock, command, log_message):
        sock.sendto(str.encode(command), (self.HOST, self.TO_PORT))
        print('\nSend command to !', log_message)

    def start_communication(self):

        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)

        sock.bind((self.HOST, self.PORT))

        while True:

            input_from_base = input('Press 1 to abort mission'
                                    '\nPress 2 to get all data'
                                    '\nPress 3 to continue\n')
            command = 0
            try:
                command = int(input_from_base)
            except ValueError:
                print('Invalid number!')

            if command == 1:
                self.send_command(sock, Command.ABORT, 'abort mission')  # TODO: not supported
            if command == 2:
                self.send_command(sock, Command.ALL_DATA, 'get all data')
            else:
                continue
