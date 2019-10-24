#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Simple password generator based on user input bit size.
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.
import random

word_file = open('/Users/nicholascoletta/Desktop/git/projects_scripts_tools/python/40kwords.txt', 'r')
word_list = []

word_list = list(word_file)

password_list = []

for i in word_list:
    new = i.strip()
    newer = new.replace("'", '')
    password_list.append(newer)

num1 = random.randint(0, 25322)
num2 = random.randint(0, 25322)
num3 = random.randint(0, 25322)
num4 = random.randint(0, 25322)

word1 = password_list[num1]
word2 = password_list[num2]
word3 = password_list[num3]
word4 = password_list[num4]

entropy = word1 + word2 + word3 + word4
print(word1, word2, word3, word4)
print('----------------------------------------------')
print (entropy)
