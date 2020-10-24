import os
import shutil

class CommandRMDIR(object):
    def __init__(self, pathInfo, addition):
        self.pathInformation = pathInfo
        self.addition = addition

    def Run(self):
        if self.addition == 'full':
            self.DeleteDirWithAllFiles()
        elif self.addition == 'dir':
            self.DeleteEmptyDit()
        else:
            self.pathInformation.setCommandResult("Invalid addition")

    def DeleteDirWithAllFiles(self):
        try:
            shutil.rmtree(self.pathInformation.getCurrentDir())
            self.pathInformation.setCommandResult("Directory was delete")

        except:
            self.pathInformation.setCommandResult("Directory wasn't delete")

    def DeleteEmptyDit(self):
        try:
            os.rmdir(self.pathInformation.getCurrentDir())
            self.pathInformation.setCommandResult("Directory was delete")
        except:
            self.pathInformation.setCommandResult("Directory wasn't delete")
