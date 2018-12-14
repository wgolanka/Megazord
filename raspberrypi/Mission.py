from raspberrypi.MissionConfiguration import MissionConfiguration
from raspberrypi.MissionData import MissionData
from raspberrypi.Sensor import Sensor
from raspberrypi.ToBase import ToBase
import time
from Command import Command
import glob


class Mission:

    @staticmethod
    def operation_for(command):
        to_base = ToBase()
        if Command.ABORT in command:
            to_base.send_statement('Mission aborted')
        if Command.ALL_DATA in command:
            to_base.send_statement("All data collected: ")
            Mission.send_all_data_collected(to_base)
            to_base.send_statement("Finished sending all collected data")

    def mission(self):
        start_time = time.time()
        elapsed_time = time.time() - start_time
        mission_config = MissionConfiguration()
        sample_num = 0
        to_base = ToBase()

        while elapsed_time < mission_config.LENGTH_IN_SECONDS:
            sample_num = sample_num + 1
            print(sample_num)
            mission_data = MissionData()
            sensors = Sensor(12, 36.3, 18.6, 14, False)  # TODO: need to be taken from arduino actual sensors
            mission_data.sensorsData = {'Timestamp': str(mission_data.timestamp), 'Time': sensors.time,
                                        'Temperature': sensors.temperature,
                                        'Pressure': sensors.pressure, 'Light': sensors.light}
            self.save_to_file(mission_data)
            if sensors.obstacle:
                to_base.send_statement("Mission : occurred obstacle, trying to avoid...")

            if sample_num % 10 == 0:
                print("Sending data do base")
                statement_to_base = "Sample nr." + str(sample_num) + \
                                    " : Mission data collected: " + str(mission_data.sensorsData)
                to_base.send_statement(statement_to_base)

            time.sleep(mission_config.FREQUENCY_IN_SECONDS)
            elapsed_time = time.time() - start_time
            print(elapsed_time)

        to_base.send_statement("Mission has been finished")

    def save_to_file(self, mission_data):
        file_name = str(mission_data.timestamp)
        file = open(file_name + ".txt", "w+")
        file.write(str(mission_data.sensorsData))
        file.close()

    @staticmethod
    def send_all_data_collected(to_base):
        for file in glob.glob("*.txt"):
            in_file = open(file)
            to_base.send_statement(''.join(in_file.readlines()))
            in_file.close()
