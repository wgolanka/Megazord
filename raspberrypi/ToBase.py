# TODO klient wysyłający komunikaty/dane pomiarów do bazy
import socket


class ToBase:

    def send_statement(self, statement):
        HOST = '127.0.0.1'
        PORT = 65477
        TO_PORT = 61341
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)

        sock.bind((HOST, PORT))
        sock.sendto(str.encode(statement), (HOST, TO_PORT))
