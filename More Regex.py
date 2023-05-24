#Tugsbileg Khaliunbat
#CIS 1051

import re

#.* matches anything except line breaks and zero or more preceding token
#.*? makes the quantifier * lazy meaning it will now match as few characters as possible

def Nakamoto():
    names = ['Satoshi Nakamoto',
             "Alice Nakamoto",
             "RoboCop Nakamoto",
             "satoshi Nakamoto",
             "Mr. Nakamoto",
             "Nakamoto",
             "Satoshi nakamoto"]
    namesRegex = re.compile(r"^[A-Z]\w+ Nakamoto")
    for item in names:
        if namesRegex.search(item) is not None:
            print(item)

def numbers():
    numbers = ['twenty',
               'twenty-one',
               'twenty-two',
               'thirty-five',
               'fifty',
               'ninety-nine']
    numbersRegex = re.compile(r"\w+-?\w+")
    for item in numbers:
        if numbersRegex.search(item) is not None:
            print(item)

def dollarValue():
    values = ['$100.00',
              '$10,000.00',
              '$1234',
              '$5000.00',
              '$',
              '100.00',
              '$1,000,000']
    valuesRegex = re.compile(r"\$\d+([.,]?\d*)*")
    for item in values:
        if valuesRegex.search(item) is not None:
            print(item)

Nakamoto()
numbers()
dollarValue()
            
            
