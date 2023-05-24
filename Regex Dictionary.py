#Tugsbileg Khaliunbat
#CIS 1051

import re

text = open("words.txt","r")
def catOrDog():
    wordRegex = re.compile(r'cat|dog')
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            #print(line)
            count+=1
    print(count)
#catOrDog()

def fourLetterWords():
    wordRegex = re.compile(r"\b\w{4}\b")
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            #print(line)
            count+=1
    print(count)
#fourLetterWords()

def hun():
    wordRegex = re.compile(r'hun')
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            #print(line)
            count+=1
    print(count)
#hun()

def ingORion():
    wordRegexIng = re.compile(r"ing\b")
    wordRegexIon = re.compile(r"ion\b")
    countIng = 0
    countIon = 0
    for line in text:
        if wordRegexIng.search(line) is not None:
            #print(line)
            countIng+=1
        if wordRegexIon.search(line) is not None:
            #print(line)
            countIon+=1
    print("ing:",countIng,"ion:",countIon)
#ingORion()

def QandU():
    wordRegex = re.compile(r'[Qq][^u]')
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            print(line)
            count+=1
    print(count)
QandU()

def noVowels():
    wordRegex = re.compile(r'[aeiouAEIOU]')
    count = 0
    for line in text:
        if wordRegex.search(line) is None:
            #print(line)
            count+=1
    print(count)

#noVowels()

def onlyVowels():
    wordRegex = re.compile(r'[^aeiouAEIOU]')
    count = 0
    for line in text:
        if wordRegex.search(line) is None:
            print(line)
            count+=1
    print(count)
#onlyVowels()

def nt():
    wordRegex = re.compile(r"n't\b")
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            print(line)
            count+=1
    print(count)

#nt()

def twoVowels():
    wordRegex = re.compile(r"[aeoiuAEIOU]{2}")
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            #print(line)
            count+=1
    print(count)
#twoVowels()

def atLeastTwoVowels():
    wordRegex = re.compile(r"[aeoiuAEIOU](\w+)?[aeoiuAEIOU]")
    count = 0
    for line in text:
        if wordRegex.search(line) is not None:
            #print(line)
            count+=1
    print(count)
#atLeastTwoVowels()
