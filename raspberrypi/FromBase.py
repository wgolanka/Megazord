import socket
from raspberrypi.Mission import Mission
from Command import Command

HOST = '127.0.0.1'
PORT = 62295

mission = Mission()

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:
    data = sock.recv(1024)

    command = data.decode()

    if Command.ABORT in command:
        print("Preparing to abort the mission")
        Mission.operation_for(command)  # TODO: this should break mission (maybe just make lentgh in seconds yo 0?
        command = 'no_command'  # not sure if this line is needed at all

    if Command.MOD_PARAMS in command:
        print("Preparing to modify params")
        Mission.operation_for(command)
        command = 'no_command'  # not sure if this line is needed at all

        # TODO one if is enough to handle the commands, unify
