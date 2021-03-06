import shutil

from Commands.CommandCd import CommandCd


class CommandRMDIR(object):
    def __init__(self, pathInfo, addition):
        self.pathInformation = pathInfo
        self.addition = addition


    def Run(self):
        self.DeleteDirWithAllFiles()
        return self.pathInformation

    def DeleteDirWithAllFiles(self):
        try:
            if self.addition is None:  # if directory name is None, delete directory there we us
                shutil.rmtree(self.pathInformation.getCurrentDir())
                self.pathInformation.setCommandResult("Directory was delete")
                CommandCd(self.pathInformation, '..').Run()

            else:  # id directory name exists
                shutil.rmtree(self.pathInformation.getCurrentDir() + self.addition)
                self.pathInformation.setCommandResult("Directory was delete")

        except:  # if any errors
            self.pathInformation.setCommandResult("Directory wasn't delete")

