import random

def random_str_generator(str_size=64):
    return ''.join(random.choice(
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ) for x in range(str_size))