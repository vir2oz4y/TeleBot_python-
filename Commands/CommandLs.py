import os

class CommandLs(object):
    def __init__(self, pathInfo):
        self.pathInformation = pathInfo

    def Run(self):  # return new PathInformation
        try:  # TODO try get all files and dir
            self.__AddFilesAndDirIntoPathInfo()
            self.pathInformation.setCommandResult("Command is done")
        except ValueError:
            self.pathInformation.setCommandResult("Command is not done")

        return self.pathInformation

    def __GetAllInDirectories(self):
        allInDirectory = os.listdir(
            path=self.pathInformation.getCurrentDir()
        )  # TODO get all files and directories in current path
        return allInDirectory

    def __AddFilesAndDirIntoPathInfo(self):
        files = []
        directories = []
        for file in self.__GetAllInDirectories():  # TODO Проходим по всем элементам и находим директории и файлы
            filePath = self.pathInformation.getCurrentDir() + file
            if self.__IsDirectory(filePath):
                directories.append(file)
            if self.__IsFile(filePath):
                files.append(file)
        self.pathInformation.setFiles(files)  # TODO add files into PathInformation
        self.pathInformation.setDirectories(directories)  # TODO add directories into PathInformation

    def __IsDirectory(self, fileName):
        if os.path.isdir(fileName):
            return True
        else:
            return False

    def __IsFile(self, fileName):
        if os.path.isfile(fileName):
            return True
        else:
            return False
