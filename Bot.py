import telebot 
import datetime, time
#individual token
TOKEN = '1835690901:AAEwesdwqsht2mQhmn2Znp4ipSF7F9tN5no'
bot = telebot.TeleBot(TOKEN)
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертацsя датb в читабельний вид

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

bot.polling(none_stop=True)



