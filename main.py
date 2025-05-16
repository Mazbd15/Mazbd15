import telebot

TOKEN = '7703344167:AAEzldfaPel398R71gMKcb9E1qVinK7uIe4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! كيف يمكنني مساعدتك؟")

bot.polling()
