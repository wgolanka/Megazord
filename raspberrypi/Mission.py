#TODO tutaj można dać operacje zebrania pomiarów
# i zapisania ich do pliku\
from raspberrypi.ToBase import ToBase


class Mission:

    @staticmethod
    def operation_for(command):
        to_base = ToBase()
        if 'ABORT' in command:
            to_base.send_statement('Mission aborted')
