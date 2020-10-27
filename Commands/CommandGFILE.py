import telebot


class CommandGFILE(object):
    def __init__(self, bot, pathInfo, addition):
        self.pathInformation = pathInfo
        self.addition = addition
        self.telegramBot = bot

    def Run(self):
        try:
            self.SendDoc()
            self.pathInformation.setCommandResult("File upload")
        except ValueError:
            self.pathInformation.setCommandResult("File wasn't upload")

        return self.pathInformation

    def SendDoc(self):
        pathToFile = self.pathInformation.getCurrentDir() + self.addition
        document = open(pathToFile, 'rb')
        self.telegramBot.send_document(self.pathInformation.getChatId(),
                                       document,
                                       caption=self.addition)
