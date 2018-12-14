import socket
from Command import Command
from raspberrypi.Mission import Mission

HOST = '127.0.0.1'
PORT = 62295

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:
    data = sock.recv(1024)

    command = data.decode()

    if Command.ABORT in command:
        print("Preparing to abort the mission")
        Mission.operation_for(command)
        command = 'no_command'

    if Command.ALL_DATA in command:
        print("Preparing to send all collected data")
        Mission.operation_for(command)
        command = 'no_command'
