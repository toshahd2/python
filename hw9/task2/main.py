import telebot
import logging

def get_token():
    with open('token.txt', 'r') as file:
        return file.read()

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

app = telebot.TeleBot(get_token())

value1 = ''
value2 = ''

kboard = telebot.types.InlineKeyboardMarkup()
kboard.row(     telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<-', callback_data='<-'),
                telebot.types.InlineKeyboardButton('/', callback_data='/'),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'))

kboard.row(     telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'))

kboard.row(     telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'))

kboard.row(     telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'))

kboard.row(     telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='),
                telebot.types.InlineKeyboardButton(' ', callback_data='no'))

@app.message_handler(commands=['start'])
def send_welcome(message):
    app.send_message(message.from_user.id, 
    "Привет, " + message.from_user.first_name + "! Попробуй калькулятор, для этого запусти его из меню (снизу слева)!")

@app.message_handler(commands=['calc'])
def getMessage(message):
    global value1
    if value1 == '':
        app.send_message(message.from_user.id,
                         '0', reply_markup=kboard)
    else:
        app.send_message(message.from_user.id,
                         value1, reply_markup=kboard)

@app.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value1, value2
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value1 = ''
    elif data == '<-':
        if value1 != '':
            value1 = value1[:len(value1)-1]
    elif data == '=':
        value1 = str(eval(value1))
    else:
        value1 += data
    if value1 != value2:
        if value1 == '':
            app.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.id, text='0', reply_markup=kboard)
        else:
            app.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value1, reply_markup=kboard)
        value2 = value1

app.polling()