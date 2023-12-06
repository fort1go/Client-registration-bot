import telebot
from datetime import datetime

bot = telebot.TeleBot('TOKEN')
data_users = {
    'User': ['Data{dd:mm}', 'time{hh:mm}', "Master"]}

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in data_users:
        pass
    else:
        bot.send_message(message.from_user.id, f'{message.from_user.username}, приветствуем вас в салоне красоты бубылда.\n'
                                               'Шаблон для записи: /create Data{dd:mm} time{hh:mm} Master\n'
                                               'Шаблон для проверки записи: /check\n'
                                               'Шаблон для удаления записи: /delete\n'
                                               'Мастера: Master, Джонни Депп, Бубылда')

@bot.message_handler(commands=['delete'])
def start(message):
    if message.from_user.id in data_users:
        data_users.pop(message.from_user.id)
        bot.send_message(message.from_user.id,
                         f'{message.from_user.username}, запись была удалена.')
    else:
        bot.send_message(message.from_user.id,
                         f'{message.from_user.username}, у вас нет записи.')

@bot.message_handler(commands=['check'])
def start(message):
    if message.from_user.id in data_users:
        bot.send_message(message.from_user.id,
                         f'{message.from_user.username}, у вас есть запись на {data_users[message.from_user.id][0]}'
                         f' в {data_users[message.from_user.id][1]} к мастеру {data_users[message.from_user.id][2]}')
    else:
        bot.send_message(message.from_user.id,
                         f'{message.from_user.username}, у вас нет записи.')

@bot.message_handler(content_types=['text'])
def create(message):
    if message.from_user.id not in data_users and '/create' in message.text:
        list = message.text.split(' ')[1::]
        if is_valid_date(list[0]) and is_valid_time(list[1]) and list[2] in ['Master', 'Джонни Депп', 'Бубылда']:
            data_users[message.from_user.id] = list
            bot.send_message(message.from_user.id,
                             f'{message.from_user.username}, у вас есть запись на {data_users[message.from_user.id][0]}'
                             f' в {data_users[message.from_user.id][1]} к мастеру {data_users[message.from_user.id][2]}')
        else:
            bot.send_message(message.from_user.id,
                             f'Неверный ввод.')
    else:
        pass


def is_valid_date(input_date):
    try:
        datetime.strptime(input_date, '%d.%m')
        return True
    except ValueError:

        return False

def is_valid_time(input_time):
    try:
        datetime.strptime(input_time, '%H:%M')
        return True
    except ValueError:
        return False

bot.polling(none_stop=True, interval=0)
