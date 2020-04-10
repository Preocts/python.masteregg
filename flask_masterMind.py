"""
    Coded by Preocts
"""

# from flask import Flask, jsonify, render_template, request
from flask import Flask, render_template, request
import json
import random
random.seed()


class gameData:

    def __init__(self):
        self.gameData = {}
        self.autoInc = 1

    def newGame(self):
        """ Create a new game """
        secretCode = []
        for i in range(0, 4):
            secretCode.append(random.randint(0, 5))

        self.gameData[str(self.autoInc)] = {
            "secretCode": secretCode,
            "maxRounds": 12,
            "curRound": 1,
            "gameState": 0,
            "playerMoves": [],
            "cpuHints": [],
            "gameID": str(self.autoInc)
        }
        self.autoInc += 1
        return self.gameData[str(self.autoInc - 1)]

    def getGame(self, id):
        """ return existing game """
        if id in self.gameData:
            return self.gameData[id]
        else:
            return False

    def addRound(self, id, playerGuess):
        """ used to progress the game """
        if not(id in self.gameData):
            return False
        hints = self.hintCheck(playerGuess.copy(),
                               self.gameData[id]["secretCode"].copy())
        if not(hints):
            return False
        self.gameData[id]["playerMoves"].append(playerGuess)
        self.gameData[id]["cpuHints"].append(hints)
        self.gameData[id]["curRound"] += 1
        # If the current round exceeds max rounds then game over
        if self.gameData[id]["curRound"] > self.gameData[id]["maxRounds"]:
            self.gameData[id]["gameState"] = 2
        # if hints doesn't have 0 to 2 then the game is won
        if not((0 in hints) or (2 in hints)):
            self.gameData[id]["gameState"] = 1
        return self.gameData[id]

    def hintCheck(self, playerGuess: list, secretCode: list):
        """ Core of the game, returns the hint pegs """
        hints = []
        gameSize = len(playerGuess)
        if len(playerGuess) != len(secretCode):
            return False
        loc = 0
        # Find all the correctly placed guesses
        while loc < len(playerGuess):
            if playerGuess[loc] == secretCode[loc]:
                playerGuess.pop(loc)
                secretCode.pop(loc)
                hints.append(1)
            else:
                loc += 1
        loc = 0
        # Find any incorrectly placed, but correct answers
        while loc < len(playerGuess):
            if playerGuess[loc] in secretCode:
                found = playerGuess[loc]
                secretCode.pop(secretCode.index(found))
                hints.append(2)
            loc += 1
        # Fill remaining list with 0's
        while len(hints) < gameSize:
            hints.append(0)
        return hints


app = Flask(__name__)
masterMind = gameData()


@app.route('/checkMove', methods=['POST'])
def checkMove():
    if request.method == 'POST':
        myData = request.get_json()
        print(myData)
        print(json.dumps(myData))

        gameData = masterMind.addRound(myData["gameID"],
                                       myData["playerGuess"])
        # print(gameData)
    return json.dumps(gameData)


@app.route('/masteregg')
def playGame():
    gameData = masterMind.newGame()
    return render_template("mastermind_base.html",
                           templateData=json.dumps(gameData))


@app.route('/testgame')
def testGame():
    templateData = {}
    playerGuesses = [[0, 1, 2, 3], [4, 5, 1, 2], [4, 5, 2, 3]]
    cpuHints = [[2, 2, 0, 0], [1, 1, 2, 2], [1, 1, 1, 0]]
    templateData["playerMoves"] = playerGuesses.copy()
    templateData["cpuHints"] = cpuHints.copy()
    templateData["maxRounds"] = "12"
    templateData["curRound"] = "4"
    templateData["gameState"] = 0
    templateData["secretCode"] = [4, 5, 2, 1]

    return render_template("mastermind_base.html",
                           templateData=json.dumps(templateData))


if __name__ == '__main__':

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
