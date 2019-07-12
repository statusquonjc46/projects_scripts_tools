#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Simple password generator based on user input bit size.
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import random
import string

print('Welcome to the pyssword generator.')
userInput = input(
    'Please pick a character length for your password [8], [16], [32], [64], [128]:  ')

char = string.ascii_letters + string.digits + '!@#$%^&*()_-+='


def rgen():
    return ''.join(random.SystemRandom().choice(char) for _ in range(int(userInput)))


print(rgen())
