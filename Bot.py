import telebot 
import datetime, time

#individual token
TOKEN = '1835690901:AAEwesdwqsht2mQhmn2Znp4ipSF7F9tN5no'
bot = telebot.TeleBot(TOKEN)
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертацsя датb в читабельний вид

#time to start paras
@bot.message_handler(commands=['ts'])
def start(message):	
	print("/ts\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
	tn = datetime.datetime.now()	
	ts1 = datetime.datetime.fromisoformat('2024-11-25 05:30:00')
	ts2 = datetime.datetime.fromisoformat('2024-11-25 07:20:00')
	ts3 = datetime.datetime.fromisoformat('2024-11-25 09:10:00')
	ts4 = datetime.datetime.fromisoformat('2024-11-25 11:30:00')
	ts5 = datetime.datetime.fromisoformat('2024-11-25 13:20:00')

	if datetime.datetime.now().time() > datetime.time(17,35,00):
		bot.reply_to(message, message.from_user.first_name + ", Пари взагалі то закінчились на сьогодні😂")		
	elif datetime.datetime.now().time() < datetime.time(8,30,00):
		g = (ts1 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(8,30,00) and datetime.datetime.now().time() < datetime.time(10,5,00):
		bot.reply_to(message, "Щось мені підказує, що пізно вже питатись коли пара розпочинається" )
	elif datetime.datetime.now().time() < datetime.time(10,20,00):
		g = (ts2 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(10,20,00) and datetime.datetime.now().time() < datetime.time(11,55,00):
		bot.reply_to(message, "Щось мені підказує, що пізно вже питатись коли пара розпочинається" )
	elif datetime.datetime.now().time() < datetime.time(12,10,00):
		g = (ts3 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(12,10,00) and datetime.datetime.now().time() < datetime.time(13,45,00):
		bot.reply_to(message, "Щось мені підказує, що пізно вже питатись коли пара розпочинається" )
	elif datetime.datetime.now().time() < datetime.time(14,30,00):
		g = (ts4 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(14,30,00) and datetime.datetime.now().time() < datetime.time(16,5,00):
		bot.reply_to(message, "Щось мені підказує, що пізно вже питатись коли пара розпочинається" )
	elif datetime.datetime.now().time() < datetime.time(16,20,00):
		g = (ts5 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(16,20,00) and datetime.datetime.now().time() < datetime.time(17,35,00):
		bot.reply_to(message, "Щось мені підказує, що пізно вже питатись коли пара розпочинається" )

#time to end paras
@bot.message_handler(commands=['te'])
def start(message):	
	print("/te\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
	tn = datetime.datetime.now()	
	ts1 = datetime.datetime.fromisoformat('2024-11-25 07:05:00')
	ts2 = datetime.datetime.fromisoformat('2024-11-25 08:55:00')
	ts3 = datetime.datetime.fromisoformat('2024-11-25 10:45:00')
	ts4 = datetime.datetime.fromisoformat('2024-11-25 13:05:00')
	ts5 = datetime.datetime.fromisoformat('2024-11-25 14:35:00')

	if datetime.datetime.now().time() > datetime.time(17,35,00):
		bot.reply_to(message, message.from_user.first_name + ", Пари взагалі то закінчились на сьогодні😂")		
	elif datetime.datetime.now().time() < datetime.time(10,5,00):
		g = (ts1 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(10,5,00) and datetime.datetime.now().time() < datetime.time(10,20,00):
		bot.reply_to(message, "Пара ще не розпочалась" )
	elif datetime.datetime.now().time() < datetime.time(11,55,00):
		g = (ts2 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(11,55,00) and datetime.datetime.now().time() < datetime.time(12,10,00):
		bot.reply_to(message, "Пара ще не розпочалась" )
	elif datetime.datetime.now().time() < datetime.time(13,45,00):
		g = (ts3 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(13,45,00) and datetime.datetime.now().time() < datetime.time(14,30,00):
		bot.reply_to(message, "Пара ще не розпочалась" )
	elif datetime.datetime.now().time() < datetime.time(16,5,00):
		g = (ts4 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )
	elif datetime.datetime.now().time() > datetime.time(16,5,00) and datetime.datetime.now().time() < datetime.time(16,20,00):
		bot.reply_to(message, "Пара ще не розпочалась" )
	elif datetime.datetime.now().time() > datetime.time(16,20,00) and datetime.datetime.now().time() < datetime.time(17,35,00):
		g = (ts5 - tn).total_seconds()
		bot.reply_to(message, datetime.datetime.fromtimestamp(g).strftime("%H:%M:%S") )



bot.polling(none_stop=True)


# 