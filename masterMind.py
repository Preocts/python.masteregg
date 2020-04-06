"""
    Coded by: Preocts
"""

from colorama import init as coloramaInit
from colorama import Fore
import random
import os

coloramaInit(autoreset=True)
random.seed()


def loc(x: int, y: int) -> str:
    return f"\033[{y};{x}f"


def color(n: int) -> list:
    colorList = [f"{Fore.RED}", f"{Fore.GREEN}", f"{Fore.YELLOW}",
                 f"{Fore.MAGENTA}", f"{Fore.CYAN}", f"{Fore.WHITE}"]
    colorNames = ["Red", "Green", "Yellow", "Magenta", "Cyan", "White"]
    return [colorList[n], colorNames[n]]


def clearBoard():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def gameBoard(pGuess: list, hints: list, round: list, start: bool = False):
    print("{}{: ^25}".format(loc(1, 1), 'Mastermind'))
    print("|{:-^23}|".format(''))
    for row in range(0, 11):
        if not(start) and row < len(pGuess):
            for p in range(0, 4):
                print(f"{Fore.WHITE}|{color(pGuess[row][p])[0]}"
                      f" ▓{pGuess[row][p]}▓ ", end="")
            print("| ", end="")
            if row == len(pGuess) - 1:
                for p in range(0, hints[0]):
                    print("X", end="")
                for p in range(0, hints[1]):
                    print("O", end="")
            print("")
        else:
            print("|     |     |     |     |")
        print("|{:-^23}|".format(''))

    if round[0] > round[1]:
        round[0] = round[1]
    print(f"{Fore.YELLOW}{loc(45,1)}Round {round[0]} of {round[1]}     ")
    if hints[0] == 1:
        print(f"{Fore.YELLOW}{loc(45,3)}You have {Fore.WHITE}{hints[0]} "
              f"{Fore.YELLOW}piece correctly placed.     ")
    else:
        print(f"{Fore.YELLOW}{loc(45,3)}You have {Fore.WHITE}{hints[0]} "
              f"{Fore.YELLOW}pieces correctly placed.     ")
    if hints[1] == 1:
        print(f"{Fore.YELLOW}{loc(45,4)}You have {Fore.WHITE}{hints[1]} "
              f"{Fore.YELLOW}correct color placed incorrectly.     ")
    else:
        print(f"{Fore.YELLOW}{loc(45,4)}You have {Fore.WHITE}{hints[1]} "
              f"{Fore.YELLOW}correct colors placed incorrectly.     ")
    print("{}{: ^15}".format(loc(45, 6), "Choices"))
    print("{}{:-^15}".format(loc(45, 7), ""))
    for n in range(0, 6):
        print(f"{loc(45, 8 + n)}{color(n)[0]}{n} | for {color(n)[1]}")

    print("{}{: ^15}".format(loc(65, 6), "Hint Key"))
    print("{}{:-^15}".format(loc(65, 7), ""))
    print("{}{: <15}".format(loc(65, 8), "X : Correctly placed piece"))
    print("{}{: <15}".format(loc(65, 9), "O : Correct color, incorrect place"))

    print(f"{loc(45, 20)}Enter a guess with the numbers of the choices above.")
    print(f"{loc(45, 21)}Example: 1 3 5 0")
    print(f"{loc(45, 22)}This would be 'Green, Magenta, White, Red'")
    print(f"{loc(45, 23)}Enter 'exit' to Exit")
    return


def getGuess() -> list:
    guess = None
    print("{}{: <40}".format(loc(1, 28), ''))
    guess = input(f"{loc(1, 28)}What is your guess? ").split(' ')
    if guess == "exit":
        print(f"{loc(1,29)}")
        print("See ya space cowboy!")
        exit()
    results = []
    if len(guess) != 4:
        return False
    for g in guess:
        try:
            if int(g) > 5 or int(g) < 0:
                raise ValueError
            results.append(int(g))
        except ValueError:
            return False
    return results


def checkWin(hints: list) -> list:
    print("{}{: <40}".format(loc(1, 26), ''))
    if hints[0] <= 2:
        print(f"{loc(1,26)}Good attempt! Try again")
    else:
        print(f"{loc(1,26)}You're doing well! Keep going")

    if hints[1] == 4:
        print("{}{: <40}".format(loc(1, 26), ''))
        print(f"{loc(1,26)}Well, that's a thing!")

    if hints[0] == 4:
        print("{}{: <40}".format(loc(1, 26), ''))
        print(f"{loc(1,26)}Victory is yours!")
        print(f"{loc(1,29)}")
        return True
    else:
        return False


def hintCheck(playerGuess: list, secretCode: list):
    hints = [0, 0]
    if len(playerGuess) != len(secretCode):
        return hints
    loc = 0
    while loc < len(playerGuess):
        if playerGuess[loc] == secretCode[loc]:
            playerGuess.pop(loc)
            secretCode.pop(loc)
            hints[0] += 1
        else:
            loc += 1
    loc = 0
    while loc < len(playerGuess):
        if playerGuess[loc] in secretCode:
            found = playerGuess[loc]
            secretCode.pop(secretCode.index(found))
            hints[1] += 1
        loc += 1
    return hints


def main():
    secretCode = []
    rounds = [0, 10]
    playerGuess = []
    allGuesses = []

    for i in range(0, 4):
        secretCode.append(random.randint(0, 5))

    clearBoard()
    gameBoard(allGuesses, [0, 0], [0, 10], True)

    while True:
        playerGuess = False
        while not(playerGuess):
            playerGuess = getGuess()
        allGuesses.append(playerGuess)
        rounds[0] += 1
        gameBoard(allGuesses.copy(),
                  hintCheck(playerGuess.copy(), secretCode.copy()),
                  rounds.copy())
        if checkWin(hintCheck(playerGuess.copy(), secretCode.copy())):
            exit()
        if rounds[0] > rounds[1]:
            print(f"{loc(1,29)}")
            print("Better luck next time!")
            exit()


if __name__ == "__main__":
    exit(main())
