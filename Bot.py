import telebot 
import datetime, time

#individual token
TOKEN = '1835690901:AAEwesdwqsht2mQhmn2Znp4ipSF7F9tN5no'
bot = telebot.TeleBot(TOKEN)
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертацsя датb в читабельний вид

#help comand
@bot.message_handler(commands=['help'])
def start(message):
	print("/help\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
	bot.reply_to(message, "Hi! Мене звати SkyNet і моя місія допомоти тобі.\n/pXY -	X номер підгрупи Y порядковий номер тижня.\n /t - Розклад.\n /te - Час до кінця пари.\n /ts - Час до початку пари.\n /w - парний чи непарний тиждень\n /sos Call the creator of the bot, Vlad")



bot.polling(none_stop=True)


