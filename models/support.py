from models.start import bot
from telebot import types
from models import db_session
from models.users import User

db_session.global_init('sqlite.db')


def answer_not(message):
    bot.send_message(message.chat.id, 'Я не знаю что даже ответить на' + ' <b><i>' + message.text + '</i></b> ' + '\n'
                                      'Напиши мне вопрос и ответ для него, чтобы я мог научиться так же говорить как '
                                      'и людишки\n'
                                      'Напиши вот так:\n'
                                      '\n'
                                      '<b>/Обучить "Тут вопрос"="тут ответ на этот вопрос"</b>',
                     parse_mode='html'
                     )


def back(message):

    sti = open('assets/4.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "Вы прекратили общение с ботом )", reply_markup=markup)


def Error(message):
    sti = open('assets/hi2.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "Ошибка, может вы ввели не правильную команду\n"
                     'Напиши вот так:\n'
                     '\n'
                     '<b>/Обущить "Тут вопрос"="тут ответ на этот вопрос"</b>',
                     parse_mode='html'
                     )


def start_hct(message):
    bot.send_message(message.chat.id,
                     " Чтобы начать общаться просто пиши и обучай этого бота :D",
                     reply_markup=markup
                     )
