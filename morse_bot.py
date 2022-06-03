'''Morse Trasnlater'''
import telebot 
from telebot import types 


bot = telebot.TeleBot('5243596495:AAEgyjbhX9xd5GcEnKpfmyubp9HjeCVUzcI')

def exception(message):
    bot.send_message(message.chat.id, "Я могу переводить только <b>русские</b> слова. Отправь текст на <b>русском</b>",parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, {message.from_user.first_name}, отправь мне любой текст, и я переведу его на язык МОРЗЕ"
    bot.send_message(message.chat.id, mess)

@bot.message_handler(content_types=['text'])
def translate(message):
    morze = {
    'А' : '.-' ,'Б' : '-..' ,'В': '.--' ,'Г': '--.' ,'Д': '-..' ,'Е': '.' ,'Ж': '...-' ,'З': '--..' ,'И': '..' ,'Й': '.---' ,'К': '-.-' ,
    'Л': '.-..' ,'М': '--' ,'Н': '-.' ,'О': '---' ,'П': '.--.' ,'Р': '.-.' ,'С': '...' ,'Т': '-' ,'У': '..-' ,'Ф': '..-.' ,
    'Х': '....' ,'Ц': '-.-.' ,'Ч': '---.' ,'Ш': '----' ,'Щ': '--.-' ,'Ъ': '.--.-.' ,'Ы': '-.--' ,'Ь': '-..-' ,
    'Э': '...-...' ,'Ю': '..--' ,'Я': '.-.-', ' ' : ' '
    }
    
    try:
        result = ''
        textmes = message.text
        mess = textmes.upper()
        
        for i in range(len(mess)):
            b = list(mess)
            result += f'| {morze[b[i]]} |'
            
        bot.send_message(message.chat.id, result)
        
    except KeyError:
        exception(message) 

bot.polling(none_stop = True)