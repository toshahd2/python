from fractions import Fraction

def calculation_r(a, b, func):
    a_list = a.split(sep='/')
    b_list = b.split(sep='/')
    if func == '+':
        calc = Fraction(int(a_list[0]), int(a_list[1])) + Fraction(int(b_list[0]), int(b_list[1]))
    elif func == '-':
        calc = Fraction(int(a_list[0]), int(a_list[1])) - Fraction(int(b_list[0]), int(b_list[1]))
    elif func == '*':
        calc = Fraction(int(a_list[0]), int(a_list[1])) * Fraction(int(b_list[0]), int(b_list[1]))
    elif func == '/':
        calc = Fraction(int(a_list[0]), int(a_list[1])) / Fraction(int(b_list[0]), int(b_list[1]))
    return calc