"""
    Coded by: Preocts
"""


def hintCheck(playerGuess: list, secretCode: list):
    hints = []
    if len(playerGuess) != len(secretCode):
        return "Missing Input"
    loc = 0
    while loc < len(playerGuess):
        if playerGuess[loc] == secretCode[loc]:
            playerGuess.pop(loc)
            secretCode.pop(loc)
            hints.append("black")
        else:
            loc += 1
    loc = 0
    while loc < len(playerGuess):
        if playerGuess[loc] in secretCode:
            found = playerGuess[loc]
            secretCode.pop(secretCode.index(found))
            hints.append("white")
        loc += 1
    if not(len(playerGuess)):
        return "You've guessed the code!"
    else:
        return hints


def main():
    """ Testing """

    secretCode = ["p", "g", "b", "y"]
    # playerGuess = ["p", "g", "b", "y"]
    # print(hintCheck(playerGuess.copy(), secretCode.copy()))
    # exit()
    # print(f"Secret Code: {secretCode}")
    guess = None
    while guess != "":
        guess = input("Enter your guess (blank to exit): ")
        print(f"Player Guess: {guess}")
        print(f"-\nHints: {hintCheck(guess.split(' '), secretCode.copy())}\n")


if __name__ == "__main__":
    exit(main())
