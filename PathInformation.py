import json

class PathInformation(object):
    def __init__(self):
        self.__chatId = None
        self.__commandResult = False
        self.__currentDir = None
        self.__files = []
        self.__directories = []

    def PathJSON(self):
        jsonObject = {
            "CommandResult": self.__commandResult,
            "CurrentDirectory":self.__currentDir,
            "Files":self.__files,
            "Directories":self.__directories
        }
        return json.dumps(jsonObject)

    def getChatId(self):
        return self.__chatId

    def getCommandResult(self):
        return self.__commandResult

    def getCurrentDir(self):
        return self.__currentDir

    def getFiles(self):
        return self.__files

    def getDirs(self):
        return self.__directories

    def setChatId(self, chatId):
        self.__chatId = chatId

    def setCommandResult(self,commandRes):
        self.__commandResult=commandRes

    def setCurrentDir(self,curDir):
        self.__currentDir = curDir

    def setFiles(self,arrayFile):
        self.__files = arrayFile

    def setDirectories(self,arrayDirectories):
        self.__directories = arrayDirectories


