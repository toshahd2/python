from datetime import datetime as dt
from pathlib import Path

p = Path('./hw10c/')
log_file = p / 'log.txt'

def get_log(log_mode, a, b, func, c):
    dtime = dt.now()
    with open(log_file, 'a', encoding='utf-8') as file:
        file.write('Время:{}; операция: {}; решение: {} {} {} = {}\n'
                     .format(dtime, log_mode, a, func, b, c))