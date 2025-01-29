# # Math Game

## Overview
`math_game.py` is a simple math quiz game that challenges users to solve addition problems. The user can choose a difficulty level (1-3), and the game will present 10 randomly generated addition problems based on the selected level. The user has three attempts to answer each question. If the user fails to provide the correct answer within the allowed attempts, the correct answer is revealed. The user's score is displayed at the end of the game.

## Features
- User can select a difficulty level (1-3).
- The game generates random addition problems based on the selected difficulty level.
- The user has three attempts to answer each question.
- Incorrect answers are marked with "EEE" and the correct answer is shown after three failed attempts.
- The program tracks the user's score and displays it after 10 questions.

## Example Usage
```
$ python math_game.py
Level (1-3): 2
23 + 45 = 68
EEE
45 + 23 = 68
You scored 8 out of 10!
```

## How to Run
1. Run the program by executing:
   ```
   python math_game.py
   ```
2. Select a difficulty level between 1 and 3.
3. Answer 10 randomly generated addition questions, with three attempts per question.
4. Your final score will be displayed after answering all questions.

## Notes
- The difficulty level determines the range of the numbers used in the addition problems:
  - Level 1: Numbers between 0 and 9.
  - Level 2: Numbers between 10 and 99.
  - Level 3: Numbers between 100 and 999.
- Invalid inputs (non-integer or out-of-range values) will prompt the user to enter a valid response.
