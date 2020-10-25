import os
from Commands.CommandLs import CommandLs


class CommandCd(object):
    def __init__(self, pathInfo, addition):
        self.pathInformation = pathInfo
        self.addition = addition
        self.commandLs = None
        # this array of type of commands Cd
        self.commands = [CdIntoFirstDir(self.pathInformation.getCurrentDir()),
                         CdIntoParentDir(self.pathInformation.getCurrentDir()),
                         CdIntoNewDir(self.pathInformation.getCurrentDir()),
                         CdIntoChildDir(self.pathInformation.getCurrentDir())]

    def Run(self):
        for varOfCommand in self.commands:  # TODO this cycle for check for which of the command addition is true and create new path
            result = varOfCommand.CheckAddition(self.addition)
            if result is None:  # if CheckAddition return None
                continue
            else:
                self.pathInformation.setCurrentDir(result)
                self.pathInformation.setCommandResult("Command is done")

                self.commandLs = CommandLs(self.pathInformation)  # TODO insert into pathInfo directories and files
                self.pathInformation = self.commandLs.Run()
                return self.pathInformation

        # if Command is not done
        self.pathInformation.setCommandResult("Command is not done")



        return self.pathInformation


class CdIntoFirstDir(object):
    def __init__(self, path):
        self.addition = '\\'
        self.path = path

    def CheckAddition(self, additionFromCd):
        if self.addition == additionFromCd:
            return self.CreatePathToFirstDir()
        return None

    def CreatePathToFirstDir(self):  # TODO replace current directory to new first directory
        indexOfFirst = self.path.find('\\')
        if indexOfFirst != -1:  # if any error in find
            newCurrentDir = self.path[0: indexOfFirst + 1]
            return newCurrentDir  # +1 to add \\
        return None


class CdIntoParentDir(object):
    def __init__(self, path):
        self.addition = '..'
        self.path = path

    def CheckAddition(self, additionFromCd):
        if self.addition == additionFromCd:
            return self.CreatePathToParentDir()
        return None

    def CreatePathToParentDir(self):  # TODO replace current directory to previous directory
        indexOfLast = self.path.rfind('\\', 0, len(self.path) - 2)
        newCurrentDir = self.path[0: indexOfLast + 1]  # +1 to add \\
        if newCurrentDir != "":
            return newCurrentDir
        return None


class CdIntoChildDir(object):
    def __init__(self, path):
        self.addition = None
        self.path = path

    def CheckAddition(self, additionFromCd):
        self.addition = additionFromCd
        if self.addition == additionFromCd:
            return self.CreatePathToNextDir(additionFromCd)
        return None

    def CreatePathToNextDir(self, NameOfChildDir):  # TODO add to path child directory
        newCurrentDir = self.path + NameOfChildDir + '\\'
        if os.path.exists(newCurrentDir) and not newCurrentDir.endswith('..\\'):
            return newCurrentDir
        return None


class CdIntoNewDir(object):
    def __init__(self, path):
        self.addition = None
        self.path = path

    def CheckAddition(self, additionFromCd):
        self.addition = additionFromCd
        if self.addition == additionFromCd:
            return self.CreatePathToNewDir(additionFromCd)
        return None

    def CreatePathToNewDir(self, path):  # TODO path = new path
        if path.endswith('\\'):  # if I:\\ then don't add \\
            newCurrentDir = path
        else:
            newCurrentDir = path + '\\'

        if os.path.exists(newCurrentDir) and not newCurrentDir =='..\\':
            return newCurrentDir
        return None



