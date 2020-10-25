from Commands.CommandCd import CommandCd
from Commands.CommandLs import CommandLs
from Commands.CommandMKDIR import CommandMKDIR
from Commands.CommandRMDIR import CommandRMDIR


class CommandController(object):
    commands = {}

    def __init__(self, dataToCommand):
        self.command = dataToCommand.command
        self.addition = dataToCommand.addition
        self.pathInfo = dataToCommand.pathInfo
        self.IntoCommand()

    def IntoCommand(self):  # TODO create dict of command
        self.commands = {'cd': CommandCd(self.pathInfo, self.addition),
                         'ls': CommandLs(self.pathInfo),
                         'mkdir': CommandMKDIR(self.pathInfo, self.addition),
                         'rmdir': CommandRMDIR(self.pathInfo, self.addition)}

    def CheckCommand(self):  # TODO check what input command is exists
        if self.command in self.commands.keys():
            return True
        return False

    def Start(self):  # TODO get value from dict and RUN this
        if self.CheckCommand():
            self.pathInfo = self.commands.get(self.command).Run()
            self.pathInfo = self.commands.get('ls').Run()

    def GetNewPathInfo(self):
        return self.pathInfo
