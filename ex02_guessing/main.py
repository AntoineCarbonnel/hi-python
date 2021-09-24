import sys
import random


def guessing_number(number_min, number_max):
    rand = random.randint(int(number_min), int(number_max))
    guess = int(input("Now guess the number kiddo: "))
    while rand != guess:
        if guess < rand:
            print("C'est plus +++++")
        elif guess > rand:
            print("C'est moins nullos -----")

        guess = int(input("Now guess the number kiddo: "))

    print("T'as REUSSIS GG uWu")


guessing_number(sys.argv[1], sys.argv[2])
