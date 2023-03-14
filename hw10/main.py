import telebot

def get_token():
    with open('token.txt', 'r') as file:
        return file.read()

bot = telebot.TeleBot(get_token())

kboard = telebot.types.InlineKeyboardMarkup()
kboard.row(     telebot.types.InlineKeyboardButton('Рациональные', callback_data='rational'),
                telebot.types.InlineKeyboardButton('Комплексные', callback_data='complex'))
kboard.row(     telebot.types.InlineKeyboardButton('Посмотреть лог', callback_data='log'))
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
    "Привет, " + message.from_user.first_name + "! Это калькулятор рациональных и комплексных чисел!")
    bot.send_message(message.chat.id, 'Выберите инструмент:', reply_markup=kboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "rational":
        bot.answer_callback_query(call.id, "Рациональные")
    elif call.data == "complex":
        bot.answer_callback_query(call.id, "Комплексные")
    elif call.data == "log":
        bot.answer_callback_query(call.id, "Посмотреть лог")

bot.polling()