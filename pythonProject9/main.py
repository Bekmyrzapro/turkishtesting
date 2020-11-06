import telebot
from telebot import types

bot = telebot.TeleBot("1325280140:AAEOHn_YQLqm611f_0oZgtDJA9aSoU-ErKc",
                      parse_mode=None)


@bot.message_handler(commands=['start', 'back'])
def send_echo(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    button = types.KeyboardButton("Start learning the language")
    button2 = types.KeyboardButton("Test your knowledge of Turkish")
    markup.add(button, button2)
    bot.send_message(message.chat.id, "Welcome to the courses of"
                     " Turkish!\n\nThis bot can perform 2 functions:\n",
                     reply_markup=markup)
    bot.send_message(message.chat.id, "𝟏)Determine your knowledge of Turkish")
    bot.send_message(message.chat.id, "𝟐)It can help you to learn Turkish.")
    bot.send_message(message.chat.id,
                     "So let's start, choose the buttons!:",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def learn(message):
    if message.text == 'Start learning the language':
        markup = types.ReplyKeyboardMarkup(True, row_width=3)
        button3 = types.KeyboardButton("Temel")
        button4 = types.KeyboardButton("Orta")
        button5 = types.KeyboardButton("Yüksek")
        button6 = types.KeyboardButton("/back")
        markup.add(button3, button4, button5, button6)
        bot.send_message(message.from_user.id,
                         'Choose your lvl',
                         reply_markup=markup)
        bot.register_next_step_handler(message, learn2)
    elif message.text == 'Test your knowledge of Turkish':
        markup = types.ReplyKeyboardMarkup(True, row_width=1)
        btn7 = types.KeyboardButton("test")
        btn8 = types.KeyboardButton("/back")
        markup.add(btn7, btn8)
        bot.send_message(message.from_user.id,
                         'Choose the button start',
                         reply_markup=markup)
        bot.register_next_step_handler(message, test)


@bot.message_handler(content_types=['text'])
def learn2(message):
    if message.text == 'Temel':
        bot.send_message(message.from_user.id,
                         'https://lingust.ru/t%C3%BCrk'
                         '%C3%A7e/t%C3%BCrk%C3%A7e-dersleri')
        bot.register_next_step_handler(message, learn3)


@bot.message_handler(content_types=['text'])
def learn3(message):
    if message.text == 'Orta':
        bot.send_message(message.from_user.id,
                         "https://www.lingo-play.com/ru/"
                         "%D1%83%D1%87%D0%B8%D1%82%D1%8C-"
                         "%D1%82%D1%83%D1%80%D0%B5%D1%86%D"
                         "0%BA%D0%B8%D0%B9-%D1%8F%D0%B7%D1"
                         "%8B%D0%BA-%D0%BE%D0%BD%D0%BB%D0%"
                         "B0%D0%B9%D0%BD/")
        bot.register_next_step_handler(message, learn4)


@bot.message_handler(content_types=['text'])
def learn4(message):
    if message.text == 'Yüksek':
        bot.send_message(message.from_user.id,
                         'http://www.de-fa.ru/dersonline.htm')


@bot.message_handler(content_types=['text'])
def test(message):
    if message.text == 'test':
        bot.send_message(message.from_user.id,
                         'https://languagelifeschool.com'
                         '/quiz/test-na-znanie-turetskogo-yazyka/')


bot.polling(none_stop=True)
