import socket
from raspberrypi.Mission import Mission
from Command import Command
import sched, time

HOST = '127.0.0.1'
PORT = 62295

mission = Mission()

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

# event_scheduler = sched.scheduler(time.time, time.sleep)

while True:
    data = sock.recv(1024)

    command = data.decode()

    mission_event = "it will be event"

    if Command.START in command:
        mission.operation_for(command)
        print("dooooone")
        command = 'no_command'  # not sure if this line is needed at all

    if Command.ABORT in command:
        print("Preparing to abort the mission")
        mission.operation_for(command)  # TODO: this should break mission
        command = 'no_command'  # not sure if this line is needed at all

    if Command.MOD_PARAMS in command:
        print("Preparing to modify params")
        mission.operation_for(command, mission_event)
        command = 'no_command'  # not sure if this line is needed at all

        # TODO one if is enough to handle the commands, unify

    # def init_mission(self):
    #     self.event_scheduler.enterabs(Mission.get_length(),
    #                                   0,
    #                                   self.measure,
    #                                   [12])
