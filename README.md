### Mastermind - Code Challenge

- Python 3.8

---

#### Code Requirements:

- Create a code of *n* pegs in a range of 4 to 20
- Compute hints based on the rules below
- Indicate when the input is invalid
- Indicate when the game has been won

---

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
