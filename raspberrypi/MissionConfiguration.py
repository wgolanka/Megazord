class MissionConfig:
    LENGTH_IN_SECONDS = [40]
    FREQUENCY_IN_SECONDS = 20
    IN_PROGRESS = True

    # def get_length(self):
    #     return type(self).LENGTH_IN_SECONDS
    #
    # def set_length(self, val):
    #     type(self).length = val
    #
    # def get_frequency(self):
    #     return type(self).FREQUENCY_IN_SECONDS
    #
    # def set_frequency(self, val):
    #     type(self)._i = val
    #
    # def get_progress(self):
    #     return type(self).IN_PROGRESS
    #
    # def set_progress(self, val):
    #     type(self)._i = val
    #
    # length = property(get_length, set_length)

    @staticmethod
    def getlength():
        return MissionConfig.LENGTH_IN_SECONDS
