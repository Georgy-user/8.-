def add_everything_up(a, b):
    try:
        RS = a + b
        if type(RS) == float:
            RS = float("{0:.3f}".format(RS))
    except TypeError:
        RS = str(a) + str(b)
    return RS

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(f'{add_everything_up(123.456, 7)}')

