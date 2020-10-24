import json

class PathInformation(object):
    def __init__(self):
        self.__commandResult = False
        self.__currentDir = None
        self.__files = []
        self.__directories = []

    def __str__(self):
        jsonObject = {
            "CommandResult": self.__commandResult,
            "CurrentDirectory":self.__currentDir,
            "Files":self.__files,
            "Directories":self.__directories
        }
        return json.dumps(jsonObject)

    def setCommandResult(self,commandRes):
        self.__commandResult=commandRes

    def setCurrentDir(self,curDir):
        self.__currentDir = curDir

    def getCurrentDir(self):
        return self.__currentDir

    def setFiles(self,arrayFile):
        self.__files = arrayFile

    def setDirectories(self,arrayDirectories):
        self.__directories = arrayDirectories


