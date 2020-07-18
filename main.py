from models.start import bot, mat
from telebot import types
from models.support import answer_not, back, Error, start_hct
from models import db_session
from models.users import User
from random import choice

db_session.global_init('sqlite.db')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, я мини ИИ, можешь поговорить со мной, или обучить для развития!")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Привет, я мини ИИ, можешь поговорить со мной, или обучить для развития!")


@bot.message_handler(commands=['bd'])
def db(message):
    try:
        session = db_session.create_session()
        iduser = message.from_user.id
        user_all = session.query(User).all()

        for all in user_all:
            if iduser == 943101770 or iduser == 1218845111:
                bot.send_message(message.chat.id,
                                 "Слово: " + str(all.question) + '\n' + " Ответ: " + str(all.answer))
            else:
                bot.send_message(message.chat.id,
                                 'Вы не имеете доступ к этой команде')
    except BaseException:
        print('error/db/1_try')
        bot.send_message(message.chat.id,
                         'Ошибка, на входе в базу данных')

@bot.message_handler(commands=['Обучить'])
def training(message):
    message.text = message.text.replace('/Обучить ', '')
    try:
        msg = message.text.split('=')
        answer = msg[1].lower()
        question = msg[0].lower().lstrip()
        #for i in mat:
        #    if question or answer == i:
        #        bot.send_message(message.chat.id, 'Пиши без мата, друг )')
        #        break
        session = db_session.create_session()
        user_all = session.query(User).all()
        for all in user_all:
            try:
                if session.query(User).filter(User.question == question).first():
                    if session.query(User).filter(User.answer != answer).first():
                        if all.question == question:
                            all.answer += '|' + answer
                            session.commit()
                            break
                    else:
                        bot.send_message(message.chat.id, 'Такой ответ уже есть на' + all.question + ' этот вопрос')
                        break
                else:
                    user = User(
                        question=question,
                        answer=answer,
                    )
                    session.add(user)
                    session.commit()
                    break

            except SQLAlchemyError:
                bot.send_message(message.chat.id, 'Ошибка')
                back(message)
                print('error/training/2_try')

    except BaseException:
        Error(message)
        print('error/training/1_try')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':

        session = db_session.create_session()

        user_all = session.query(User).all()

        for all in user_all:
            try:

                if all.question == message.text.lower():
                    msg = all.answer.split('|')
                    if len(msg) == 1:
                        bot.send_message(message.chat.id, all.answer)
                    else:
                        bot.send_message(message.chat.id, choice(msg))
                    break

            except RuntimeError:
                bot.send_message(message.chat.id, 'Ошибка')
                back(message)
                print('error/text/1_try')

        else:
            for i in mat:
                if message.text.lower() == i:
                    bot.send_message(message.chat.id, 'Пиши без мата, друг )')
                    start_ht_com(message)
                    break
            else:
                answer_not(message)


bot.polling(none_stop=True)
