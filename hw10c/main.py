import telebot
from pathlib import Path
import log
from rational import *
from complex import *

p = Path('./hw10c/')
log_file = p / 'log.txt'


def get_token():
    with open('tok.txt', 'r') as file:
        return file.read()

calc = telebot.TeleBot(get_token())

mode = ''
a = ''
b = ''
c = ''
func = ''
log_mode = ''

menu_buttons = telebot.types.ReplyKeyboardMarkup()
menu_buttons.row('Рациональные', 'Комплексные')

func_buttons = telebot.types.ReplyKeyboardMarkup()
func_buttons.row('+', '-', '*', "/")

markup = telebot.types.ReplyKeyboardRemove()

end_buttons = telebot.types.ReplyKeyboardMarkup()
end_buttons.row('Показать лог', 'Новый расчет')

@calc.message_handler(commands=['start'])
def start(message):
    calc.send_message(message.from_user.id,
    "Привет, " + message.from_user.first_name + "! Это калькулятор рациональных и комплексных чисел!")
    calc.send_message(message.chat.id, 'Выберите инструмент:', reply_markup=menu_buttons)

@calc.message_handler(content_types=['text'])
def send_text(message):
    global mode
    global log_mode
    if message.text.strip() == 'Рациональные':
        calc.send_message(message.chat.id, 'Запущен калькулятор рациональных чисел.\n\nПеременные вводятся без пробелов, через слеш, в формате числитель/знаменатель')
        mode = 'rational'
        log_mode = 'Рациональные'
    elif message.text.strip() == 'Комплексные':
        calc.send_message(message.chat.id, 'Запущен калькулятор комплексных чисел.\n\nПеременные вводятся без пробелов, мнимая обозначается j')
        mode = 'complex'
        log_mode = 'Комплексные'
    calc.send_message(message.chat.id, 'Введите первое значение, переменная A = ', reply_markup=markup)
    calc.register_next_step_handler(message, get_variable_a)

def get_variable_a(message):
    global a
    a = message.text
    calc.send_message(message.chat.id, 'Введите второе значение, переменная B = ', reply_markup=markup)
    calc.register_next_step_handler(message, get_variable_b)

def get_variable_b(message):
    global b
    b = message.text
    calc.send_message(message.chat.id, '"A ? B" Выберите действие:', reply_markup=func_buttons)
    calc.register_next_step_handler(message, result)

def result(message):
    global func
    func = message.text
    global c
    if mode == 'rational':
        c = calculation_r(a, b, func)
        calc.send_message(message.chat.id, c, reply_markup=markup)
    elif mode == 'complex':
        c = calculation_c(a, b, func)
        calc.send_message(message.chat.id, c, reply_markup=markup)
    log.get_log(log_mode, a, b, func, c)
    calc.send_message(message.chat.id, 'Выберите действие:', reply_markup=end_buttons)
    calc.register_next_step_handler(message, end_menu)

def end_menu(message):
    if message.text.strip() == 'Показать лог':
        calc.send_message(message.chat.id, 'Выводим лог:', reply_markup=markup)
        with open(log_file, 'r') as f:
            log_text = f.read()
        calc.send_message(message.chat.id, log_text)
    elif message.text.strip() == 'Новый расчет':
        calc.send_message(message.chat.id, 'Начинаем заново!')
        calc.register_next_step_handler(message, start)

calc.polling()