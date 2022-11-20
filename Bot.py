import telebot 
import datetime, time

#individual token
TOKEN = '1835690901:AAEwesdwqsht2mQhmn2Znp4ipSF7F9tN5no'
bot = telebot.TeleBot(TOKEN)
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертацsя датb в читабельний вид



bot.polling(none_stop=True)


# 