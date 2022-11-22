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

#timetable of paras
@bot.message_handler(commands=['т', 't'])
def start(message):
	print("/t\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
	bot.reply_to(message, "1 пара:	8.30-10.05\n2 пара:	10.20-11.55\n3 пара:	12.10-13.45\n4 пара:	14.30-16.05\n5 пара:	16.20-17.35")

#asdasd
#Команда SOS
@bot.message_handler(commands=['sos'])
def start(message):
	#print("/sos\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S"))

	if message.from_user.id == message.chat.id:
		text = message.from_user.first_name+" тебе виикликає!!!🤣 Проблема в користувача "+ tconv(message.date)
	else:
		text = message.from_user.first_name +" тебе виикликає!!!🤣 Проблема в чаті: "+ tconv(message.date)

	print("/sos\t"+ message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y")+ "\tID: " + str(message.from_user.id))
	bot.send_message(1051820337, text)

#Повідомлення від імені бота
@bot.message_handler(commands=['send'])
def start(message):
	if message.from_user.id == 1051820337:
		print("/send\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
		str1 = message.text
		str2 = str1.replace("/send", "")
		# id того кому пишемо
		bot.send_message(1004329909, str2)
	else:
		print("/send\t" + message.from_user.first_name + ", скористався адмінською командою. ID " + str(message.from_user.id))


bot.polling(none_stop=True)


