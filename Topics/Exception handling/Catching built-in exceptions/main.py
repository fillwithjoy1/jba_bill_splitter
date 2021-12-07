def exception_check(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print('The Error!')
    else:
        print(a / b)