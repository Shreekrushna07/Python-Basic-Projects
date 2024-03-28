---

# Hangman Game

This is a simple Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player must guess letters in the word. The player starts with 6 lives, losing one for each incorrect guess. The game ends when the player guesses the word correctly or runs out of lives.

## How to Play

1. Run the `hangman.py` script in a Python environment.
2. You will see the Hangman ASCII art and a series of underscores representing the letters in the word.
3. Guess a letter by typing it in and pressing Enter.
4. If the letter is in the word, it will be revealed in its correct position(s). If not, you lose a life.
5. Keep guessing letters until you either guess the word correctly or lose all your lives.

## Files

- `hangman.py`: Contains the main game logic.
- `HangmanArt.py`: Contains ASCII art for the Hangman stages.
- `HangmanWords.py`: Contains a list of words for the game to choose from.

## Requirements

- Python 3.x
- replit (for clearing the console)

## Installation

1. Clone the repository:

   ```bash
   git clone git clone https://github.com/Shreekrushna07/hangman.git
   ```

2. Run the game:

   ```bash
   python hangman.py
   ```

---
