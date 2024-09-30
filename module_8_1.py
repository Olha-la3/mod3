
def add_everything_up(a, b):
    try:
        if type(a) != type(b):
            return a + b
    except TypeError:
            return str(a) + str(b)
    else:
        return a + b




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))