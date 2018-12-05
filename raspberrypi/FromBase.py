import socket
from raspberrypi.Mission import Mission

HOST = '127.0.0.1'
PORT = 62292

mission = Mission()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_connection:
    socket_connection.bind((HOST, PORT))
    socket_connection.listen()
    connection, address = socket_connection.accept()
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)

            command = data.decode()

            if 'ABORT' in command:
                print("Preparing to abort the mission")
                Mission.operation_for(command)
                command = 'no_command'
                #TODO tutaj dodajemy wywołanie funkcji która zakończy
                # misje i wyslę komunikat o jej zakończeniu

            # TODO tutaj kolejne ify dla reszty komend,
            #  ale najpierw niech to wyżej zadziałą