# TODO klient wysyłający komunikaty/dane pomiarów do bazy
import socket


class ToBase:

    def send_statement(self, statement):
        HOST = '127.0.0.1'
        PORT = 65477

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(str.encode(statement))
            # print('\nSend command to abort mission!\n')
