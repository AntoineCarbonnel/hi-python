import random
import numpy as np
from words import english_words as dic


def findLetter(guess, word, letter, start=0):
    occurences = np.where(np.array(word) == letter)
    for i in occurences:
        guess[occurences] = letter
    return guess


def loop(word, guess, life):
    while word != guess and life > 0:
        letter = input("guess a letter \n")
        if letter in word:
            guess = findLetter(guess, word, letter)
            print(''.join(guess))

        else:
            life = life - 1
            print("u have " + str(life) + " chance left")

    if life > 0:
        print("u win cunt")


def gameLoop():
    choosenWord = list(dic[random.randint(0, len(dic))])
    guess = ''

    life = int(input("Choose the number of try u want to have \n"))

    for i in choosenWord:
        guess += '_'

    print(guess)

    loop(choosenWord, list(guess), life)

    input("try again")


gameLoop()
