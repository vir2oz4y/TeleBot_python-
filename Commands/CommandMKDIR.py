import os

class CommandMKDIR(object):
    def __init__(self, pathInfo, addition):
        self.pathInformation = pathInfo
        self.addition = addition

    def Run(self):  # TODO create new directory in path + addition(new directory name)
        pathToNewDir = self.pathInformation.getCurrentDir() + self.addition
        try:
            os.mkdir(pathToNewDir)
            self.pathInformation.setCommandResult("Directory created")
        except OSError:
            self.pathInformation.setCommandResult("Directory is already exists")

        return self.pathInformation




