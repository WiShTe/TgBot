import telebot
import pandas as pd
import os
import random

bot = telebot.TeleBot('5732294625:AAHgq4u9sJSlLT9E1j4VL5kfWyLIKcO6jkI')
books_df = pd.read_csv('books.csv', sep=',', encoding="utf-8")
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("/help", "/recommend")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет {message.from_user.first_name} {message.from_user.last_name}, я помогу тебе выбрать книгу'
    bot.send_message(message.chat.id, mess, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    mess = f'/help - помощь \n' \
           f'/start - приветствие\n' \
           f'/recommend - рекомендует случайную книгу\n'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['recommend'])
def recommend(message):
    messs = f"Я порекомендую вам книгу '{get_random_book()}'"
    bot.send_message(message.chat.id, messs)


def get_random_book():
    random_book = books_df[['title', 'authors']].sample(1)
    return f"{random_book.iloc[0]['title']} by {random_book.iloc[0]['authors']}"


@bot.message_handler(content_types=['text'])
def func(message):
    def send_random_toad_pic():
        files = os.listdir('./toads')
        random_file = random.choice(files)
        bot.send_photo(message.chat.id, photo=open(f'toads/{random_file}', 'rb'))

    if "лягушки" in message.text or "отправь" in message.text or "давай" in message.text:
        send_random_toad_pic()

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован, я могу порекомендовать тебе "
                                               "книгу, или отправить крутое фото лягушки")


bot.polling(none_stop=True)
