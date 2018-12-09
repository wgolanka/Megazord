# TODO tutaj można dać operacje zebrania pomiarów
# i zapisania ich do pliku\
import sched, time
import threading

from raspberrypi.ToBase import ToBase
from Command import Command


class Mission:
    LENGTH_IN_SECONDS = 40

    event_scheduler = sched.scheduler(time.time, time.sleep)

    @staticmethod
    def get_length():
        return Mission.LENGTH_IN_SECONDS

    @staticmethod
    def set_length(value):
        Mission.LENGTH_IN_SECONDS = value

    def operation_for(self, command):
        to_base = ToBase()

        if Command.START in command:
            print("Starting a mission")
            for x in range(0, 30):
                self.event_scheduler.enter(x,
                                           x,
                                           Mission.measure,
                                           [x])

            to_base.send_statement('Mission has launched!')
            self.event_scheduler.run()

        if Command.ABORT in command:
            # MissionConfig.IN_PROGRESS = False
            print("Is empty? ", self.event_scheduler.empty())

            for event in self.event_scheduler.queue:
                self.event_scheduler.cancel(event)

            to_base.send_statement('Mission aborted')
        if Command.MOD_PARAMS in command:
            Mission.set_length(10)
            to_base.send_statement("Mission length changed to " + str(Mission.get_length()))

    @staticmethod
    def measure(val):
        # print("Measuring and saving to file")
        if val % 10 == 0:
            to_base = ToBase()
            to_base.send_statement("Sending measurments: dasdad")
            print(val)
        # start_time = time.time()
        # elapsed_time = time.time() - start_time

        # print('BEFORE WHILE Mission length in seconds is ', Mission.get_length())
        # while elapsed_time < mission_length:
        #     print('\n\nStarting measurement\n')
        #     # time.sleep(3)
        #     elapsed_time = time.time() - start_time
        #     print('Time elapsed is ', elapsed_time)
        #     print('Mission length in seconds is ', mission_length)
        #     time.sleep(3)
        #     elapsed_time = time.time() - start_time
        # print('AFTER WHILE Mission length in seconds is ', Mission.get_length())

    # def init_mission(self):
    #     self.event_scheduler.enterabs(Mission.get_length(),
    #                                   0,
    #                                   self.measure,
    #                                   [12])

    # self.event_scheduler.run()
