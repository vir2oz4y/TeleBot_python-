import telebot
from BotMessage import BotMessage
from CommandController import CommandController
from DataToCommands import DataToCommands
from PathInformation import PathInformation

bot = telebot.TeleBot("1380437409:AAE5n24Rj9qzhSPzLPwYu2ApXymnS3F551U")
pathInfo = PathInformation()
pathInfo.setCurrentDir('I:\\')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, BotMessage.StartMessage())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, BotMessage.HelpMessage())


@bot.message_handler(content_types=['text'])
def messageWithCommand(message):
    global pathInfo
    dataMessage = DataToCommands(pathInfo, message.text)
    commandController = CommandController(dataMessage)
    commandController.Start()
    pathInfo = commandController.GetNewPathInfo()
    bot.send_message(message.chat.id, pathInfo)


if __name__ == '__main__':
    bot.polling()
