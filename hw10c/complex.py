def calculation_c(a, b, func):
    if func == '+':
        calc = complex(a) + complex(b)
    elif func == '-':
        calc = complex(a) - complex(b)
    elif func == '*':
        calc = complex(a) * complex(b)
    elif func == '/':
        calc = complex(a) / complex(b)
    return calc