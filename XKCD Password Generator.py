#Tugsbileg KHaliunbat
#CIS 1051
import re
import random
text = open("words.txt","r")
text = list(text)
'''
def newPassword():
    lowerCaseRegex = re.compile(r"^[a-z]+\b")
    fourCharRegex = re.compile(r'\w{4,}')
    newPassword = ''
    passwordWords = []
    for line in text:
        if lowerCaseRegex.search(line) is not None:
            if fourCharRegex.search(line) is not None:
                passwordWords.append(line)
    for _ in range(4):
        word = random.choice(passwordWords)
        newPassword+=word[:-2]
    print(newPassword)
newPassword()
'''
def newPassword():
    lowerCaseRegex = re.compile(r"^[a-z]+\b")
    fourCharRegex = re.compile(r'\w{4,}')
    newPassword = []
    while len(newPassword) != 4:
        word = random.choice(text)
        if lowerCaseRegex.search(word) is not None:
            if fourCharRegex.search(word) is not None:
                newPassword.append(word[:-2])
    print(' '.join(newPassword))

newPassword()

