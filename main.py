import telebot

# তোমার BotFather থেকে নেওয়া Token
bot = telebot.TeleBot("7592713558:AAHKKvq5tSgGz20xl5bDxCDyAz6kz5_jhAg")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো Mousumi! 😊\n\nআমি তোমার বট। বলো কীভাবে সাহায্য করতে পারি?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "তুমি লিখেছো: " + message.text)

bot.polling()
