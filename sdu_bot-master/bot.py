import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n Я - <b>{1.first_name}</b>, бот созданный для того чтобы помогать студентам СДУ.".format(message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(commands=['get_info', 'info'])
def get_info(message):
    markup = types.InlineKeyboardMarkup()
    option_1 = types.InlineKeyboardButton("Faculties", callback_data = 'faculties')
    option_2 = types.InlineKeyboardButton("Other", callback_data = 'others')
    markup.add(option_1, option_2)
    bot.send_message(message.chat.id, "Choose between two", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'faculties')
def callback_faculties(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    option_1 = types.KeyboardButton("Engenieer")
    option_2 = types.KeyboardButton("Law")
    option_3 = types.KeyboardButton("Medical")
    markup.add(option_1, option_2, option_3)
    bot.send_message(call.message.chat.id,'Choose your faculty', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'others')
def callback_others(call):
    pass




@bot.message_handler(content_types=['text'])
def m_bot(message):
    # bot.send_message(message.chat.id, message.text)
    if message.text == 'Engenieer':
        bot.send_message(message.chat.id, "Your faculty is Engineer")
    elif message.text == 'Law':
        bot.send_message(message.chat.id, "Your faculty is Law")
    elif message.text == 'Medical':
        bot.send_message(message.chat.id, "Your faculty is Medical")


bot.polling(none_stop=True)
