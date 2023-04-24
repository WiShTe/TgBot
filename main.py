import telebot
import pandas as pd
import random

bot = telebot.TeleBot('5732294625:AAHgq4u9sJSlLT9E1j4VL5kfWyLIKcO6jkI')
books_df = pd.read_csv('books.csv', sep=',', encoding="utf-8")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['recommend'])
def recommend(message):
    messs = f"Я порекомендую вам книгу '{get_random_book()}'"
    bot.send_message(message.chat.id, messs)

def get_random_book():
    random_book = books_df[['title', 'authors']].sample(1)
    return f"{random_book.iloc[0]['title']} by {random_book.iloc[0]['authors']}"


bot.polling(none_stop=True)
