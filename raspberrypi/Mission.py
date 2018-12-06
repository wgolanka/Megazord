# TODO tutaj można dać operacje zebrania pomiarów
# i zapisania ich do pliku\
import time

from raspberrypi.MissionConfiguration import MissionConfig
from raspberrypi.ToBase import ToBase
from Command import Command


class Mission:

    @staticmethod
    def operation_for(command):
        to_base = ToBase()
        if Command.ABORT in command:
            to_base.send_statement('Mission aborted')
        if Command.MOD_PARAMS in command:
            MissionConfig.LENGTH_IN_SECONDS = 240  # TODO: doesn't work, need to figure out how to change params in a fly
            to_base.send_statement("Mission length changed to " + str(MissionConfig.LENGTH_IN_SECONDS))

    def init_mission(self):
        start_time = time.time()
        elapsed_time = time.time() - start_time

        while elapsed_time < MissionConfig.LENGTH_IN_SECONDS:
            print('\n\nStarting measurement\n')
            time.sleep(5)
            elapsed_time = time.time() - start_time
            print('Time elapsed is ', elapsed_time)
            print('Mission length in seconds is ', MissionConfig.LENGTH_IN_SECONDS)
            time.sleep(5)
            elapsed_time = time.time() - start_time
