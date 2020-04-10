### Mastermind - Code Challenge

**Requirements**
- [Python 3.8.1](https://www.python.org/)
- [Colorama v0.4.3](https://pypi.org/project/colorama/)
- [Flask v1.1.2](https://flask.palletsprojects.com/en/1.1.x/installation/#installation)

---

#### Code Requirements:

- Compute hints based on the rules below
- Validate input
- Draw a game board
- Use color to indicate code pieces
- Indicate when the game has been won

**Added Challenges**

- Playable game from Flask generated webpage (template)
- All game logic run in python
- Information passed via API
- Javascript can only manipulate HTML DOM

---

##### Files:

masterMind.py
- Stand-alone playable console game

flask_masterMind.py
- Stands up a default configured dev Flask
- Game can be played at 127.0.0.1:5000/masteregg

---

##### Basic Concept of the Game:

The computer picks a hidden code that consists of 4 numbers in the range of 0 to 5. You have 10 changes to guess the code. With each guess the computer will tell you how many times you put the correct number in the correct place and how many times you put a number in the code in the incorrect place.

The game is won if you guess the code.


##### Truncated rules
Each guess is made by placing a row of code pegs on the decoding board. Once placed, the codemaker provides feedback by placing from zero to four key pegs in the small holes of the row with the guess. A colored or black key peg is placed for each code peg from the guess which is correct in both color and position.

|       | 1 | 2 | 3 | 4 | Hints   |
|-------|---|---|---|---|---------|
| Code  | Y | Y | G | B |         |
| Guess | B | O | G | P | W,B     |

#### Hints

- Peg #1 is Blue. There is a blue in the code, but it is not in position #1. This earns a white hint peg.
- Peg #2 is Orange. There is no orange in the code, so no hint peg gets put down.
- Peg #3 is Green. There is a green in the code, and it is in position #3. This - earns a red (or black) hint peg.
- Peg #4 is Purple. There is no purple in the code, so no hint peg gets put down.

Code Pegs:
- Red, Blue, Yellow, Green, White, Black

Hint Pegs:
- Black, White

---

**The magic 22 lines**

This is the code that started the entire project and carries the heart of the game logic through from beginning to end. The rules of a game can seem so small in logical form. Then you have to build a GUI around them.

```python
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
```

---

**The Console Game:**

A chance to play around with ascii escape codes to move the print cursor around on the screen and create color. Reminded me, heavily, of the days I used to program in qBasic with locates and colors galore.

Input for the console game became numbers which were then translated to color on the game board. This was easier than translating "blue blue white red" each time and made for easier play.

**The HTML Game:**

Found in the /templates folder are the three base renditions of the HTML that I planned out for the game board. You can literally see what a few hours of w3school.com will do for your understanding of HTML layout.

The javascript was the smallest amount of code, yet the longest to write. At least coming out of this little project I feel more confident in my skills, though I'm not going to start web-design anytime soon.

**Why an API?**

Why not just program the entire game in Javascript? The thought hit me at least three times through this as well. The goal, the hope, of this challenge was to mentally picture how setting up an API works and how to use it inside of a dynamic webpage design. I consider the mission a success.

---

### Open ended To-Do

No project is without its "if only I had time to do:"
- On screen instructions, tips, and help
- Selectable code size from 1 to n
  - The code is already dynamic enough, just needs tweaks to the CSS
- The Class for the game itself is scalable, maybe cookies to save games?
- Logging, DocStrings, type suggestions, oh my....
