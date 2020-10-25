class DataToCommands(object):
    def __init__(self, pathInfo, messageCommand):
        self.addition = None
        self.command = None
        self.CreateCommandFromMes(messageCommand)
        self.CreateAdditionFromMes(messageCommand)
        self.pathInfo = pathInfo

    def CreateCommandFromMes(self, message):
        try:
            self.command = message.split(' ')[0].lower().strip()
        except IndexError:
            pass

    def CreateAdditionFromMes(self, message):
        try:
            self.addition = message.split(' ')[1].lower().strip()
        except IndexError:
            pass
