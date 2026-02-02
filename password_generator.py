from random import *
from pyperclip import *
class PGenerator:
    @staticmethod
    def p_generate():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

        n_letters = randint(8, 10)
        n_numbers = randint(2, 4)
        n_symbols = randint(2, 4)

        password_l = [choice(letters) for _ in range(n_letters)]
        password_n = [choice(numbers) for _ in range(n_numbers)]
        password_s = [choice(symbols) for _ in range(n_symbols)]

        password_list = password_l + password_s + password_n

        shuffle(password_list)
        password = "".join(password_list)
        copy(password)
        return password
