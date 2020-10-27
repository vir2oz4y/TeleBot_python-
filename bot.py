import telebot
import requests
from BotMessage import BotMessage
from CommandController import CommandController
from DataToCommands import DataToCommands
from PathInformation import PathInformation

teleBot = telebot.TeleBot("1380437409:AAE5n24Rj9qzhSPzLPwYu2ApXymnS3F551U")
pathInfo = PathInformation()
pathInfo.setCurrentDir('I:\\')


@teleBot.message_handler(commands=['start'])
def send_welcome(message):
    teleBot.send_message(message.chat.id, BotMessage.StartMessage())


@teleBot.message_handler(commands=['help'])
def send_help(message):
    teleBot.send_message(message.chat.id, BotMessage.HelpMessage())


@teleBot.message_handler(content_types=['text'])
def messageWithCommand(message):
    global pathInfo
    pathInfo.setChatId(message.chat.id)
    dataMessage = DataToCommands(pathInfo, message.text)
    commandController = CommandController(dataMessage, teleBot)
    commandController.Start()
    pathInfo = commandController.GetNewPathInfo()
    textMessage = BotMessage.MessageFromAPI(pathInfo)
    teleBot.send_message(message.chat.id, textMessage)

@teleBot.message_handler(content_types=['document'])
def HandlerDocument(document):
    global pathInfo
    fileId = document.document.file_id
    fileName = document.document.file_name
    file_info = teleBot.get_file(fileId)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format('1380437409:AAE5n24Rj9qzhSPzLPwYu2ApXymnS3F551U', file_info.file_path))
    with open(pathInfo.getCurrentDir() + fileName,'a') as newFile:
        newFile.write(file.content.decode('utf-8'))



if __name__ == '__main__':
    teleBot.polling()

