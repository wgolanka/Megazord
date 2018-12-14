import datetime


class MissionData:
    timestamp = None
    sensorsData = map

    def __init__(self):
        self.timestamp = datetime.datetime.utcnow()
