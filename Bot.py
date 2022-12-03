import telebot 
import datetime, time
# commit with git bush
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
#-------------------------------РОЗКЛАД----------------------------------
#test1
#test1-1
#розклад для 1 підгрупи
@bot.message_handler(commands=['р11', 'p11'])
def start(message):
    print("/p11\t" + message.from_user.first_name + " " + datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
    bot.reply_to(message, "Підгрупа №1\nПонеділок\n\n1 пара:    -\n2 пара:  - / Сист. аналіз - Лекція\n3 пара:  Веб - Лекція\n4 пара:   -\n5 пара:  -")

@bot.message_handler(commands=['р12', 'p12'])
def start(message):
    print("/p12\t" + message.from_user.first_name + " " + datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
    bot.reply_to(message, "Підгрупа №1\nВівторок\n\n1 пара:    - / Програмування моб. систем - Лекція\n2 пара:  ООАП - Лекція / ШНМ - Лекція\n3 пара:   Мод. систем - Лекція\n4 пара:   -\n5 пара:  -")

@bot.message_handler(commands=['р13', 'p13'])
def start(message):
    print("/p13\t" + message.from_user.first_name + " " + datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
    bot.reply_to(message, "Підгрупа №1\nСереда\n\n1 пара:   ТПСПП\n2 пара:  Сист. аналіз\n3 пара:   ТПСПП - Лекція / Управління ІТ-проектами - Лекція\n4 пара:  Управління ІТ-проектами\n5 пара:    -")

@bot.message_handler(commands=['р14', 'p14'])
def start(message):
    print("/p14\t" + message.from_user.first_name + " " + datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
    bot.reply_to(message, "Підгрупа №1\nЧетвер\n\n1 пара:   Веб\n2 пара:    Моделювання систем\n3 пара: ШНМ\n4 пара:    -\n5 пара:  -")

@bot.message_handler(commands=['р15', 'p15'])
def start(message):
    print("/p15\t" + message.from_user.first_name + " " + datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
    bot.reply_to(message, "Підгрупа №1\nП'ятниця\n\n1 пара: -\n2 пара:  ООАП\n3 пара:   Програмування моб.с.\n4 пара:   -\n5 пара:  -")

#розклад для 2 підгрупи
#test2
@bot.message_handler(commands=['р21', 'p21'])
def start(message):
   print("/p21\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
   bot.reply_to(message, "Підгрупа №2\nПонеділок\n\n1 пара:    -\n2 пара:  - / Сист. аналіз - Лекція\n3 пара:  Веб - Лекція\n4 пара:   -\n5 пара:  -")

@bot.message_handler(commands=['р22', 'p22'])
def start(message):
   print("/p22\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
   bot.reply_to(message, "Підгрупа №2\nВівторок\n\n1 пара:    - / Програмування моб. систем - Лекція\n2 пара:  ООАП - Лекція / ШНМ - Лекція\n3 пара:   Мод. систем - Лекція\n4 пара:   -\n5 пара:  -")

@bot.message_handler(commands=['р23', 'p23'])
def start(message):
   print("/p23\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
   bot.reply_to(message, "Підгрупа №2\nСереда\n\n1 пара:    -\n2 пара:  Веб\n3 пара:    ТПСПП - Лекція / Управління ІТ-проектами - Лекція\n4 пара:  Системний аналіз\n5 пара:   ООАП")

@bot.message_handler(commands=['р24', 'p24'])
def start(message):
   print("/p24\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
   bot.reply_to(message, "Підгрупа №2\nЧетвер\n\n1 пара:    -\n2 пара:  ШНМ\n3 пара:    Моделювання систем\n4 пара: ТПСПП\n5 пара:  -")

@bot.message_handler(commands=['р25' , 'p25'])
def start(message):
   print("/p25\t" + message.from_user.first_name + " " +  datetime.datetime.today().strftime("%H:%M:%S %d.%m.%Y"))
   bot.reply_to(message, "Підгрупа №2\nП'ятниця\n\n1 пара:    -\n2 пара:    Програмування моб. систем\n3 пара:  Управління ІТ-проектами\n4 пара:    -\n5 пара:  -")
#-----------------------------РОЗКЛАД--------------------------------

#commit in Vlad_2_Branch
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