import random

choices = ['paper', 'rock', 'scissors']


def rps():
    return choices[random.randint(0, 2)]


def checkResult(userChoice, computerChoice):
    if userChoice == "paper":
        return computerChoice == "rock"

    if userChoice == "rock":
        return computerChoice == "scissors"

    if userChoice == "scissors":
        return computerChoice == "paper"


def userMakeChoice():
    userChoice = input()

    if userChoice not in choices:
        print("Plz make a real choice rock, paper or scissors\n")
        userChoice = userMakeChoice()

    return userChoice


def gameLoop():
    print("Welcome to Rock, Paper, Scissors game: \nComputer have made choice your turn !\n")

    userChoice = userMakeChoice()
    computerChoice = rps()

    while not checkResult(userChoice, computerChoice):
        print("Try again looser " + str(userChoice) + " loose on the " + str(computerChoice))
        userChoice = userMakeChoice()
        computerChoice = rps()

    print("GG u RULES " + str(userChoice) + " win on the " + str(computerChoice))


gameLoop()
