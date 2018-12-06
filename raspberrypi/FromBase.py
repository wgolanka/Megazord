import socket
from raspberrypi.Mission import Mission

HOST = '127.0.0.1'
PORT = 62295

mission = Mission()

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:
    data = sock.recv(1024)

    command = data.decode()

    if 'ABORT' in command:
        print("Preparing to abort the mission")
        Mission.operation_for(command)
        command = 'no_command'

        # TODO tutaj dodajemy wywołanie funkcji która zakończy
        # misje i wyslę komunikat o jej zakończeniu

    # TODO tutaj kolejne ify dla reszty komend
