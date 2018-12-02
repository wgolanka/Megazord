import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)

            command = repr(data)
            print("Command received: ", command)
            if 'ABORT' in command:
                print("Preparing to abort the mission")
                #TODO tutaj dodajemy wywołanie funkcji która zakończy
                # misje i wyslę komunikat o jej zakończeniu

            # TODO tutaj kolejne ify dla reszty komend,
            #  ale najpierw niech to wyżej zadziałą