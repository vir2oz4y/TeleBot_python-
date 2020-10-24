import telebot
from BotMessage import BotMessage

bot = telebot.TeleBot("1380437409:AAE5n24Rj9qzhSPzLPwYu2ApXymnS3F551U")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, BotMessage.StartMessage())

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, BotMessage.HelpMessage())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling()

