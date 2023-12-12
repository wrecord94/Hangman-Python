from replit import clear
import random
from hangman_words import *
from hangman_art import *

# Sets the difficulty via the number of lives
LIVES = 6


# Define our class
class HangmanGame:
    def __init__(self):
        # Sets the random word using the word_list in the files.
        self.chosen_word = random.choice(word_list)
        # Pulls out the length of this chosen word
        self.word_length = len(self.chosen_word)
        # Set end of game monitoring variable to False
        self.end_of_game = False
        # Sets the difficulty via the number of lives
        self.lives = LIVES
        self.display = ["_" for _ in range(self.word_length)]
        self.guessed_list = []

    # Function to print out the current word left to guess and the relevant art stage
    def display_current_state(self):
        print(f"{' '.join(self.display)}")
        print(stages[self.lives])

    # Method to handle making a guess
    def check_guess(self, guess):
        # Clear screen as text based game.
        clear()
        # Check if letter already guessed
        if guess in self.guessed_list:
            print(f"You've already guessed: {guess}.")
            return

        # Set and reset variable to check for correct letter to False
        correct_guess = False
        # Loops through word and checks if in our word
        for position in range(self.word_length):
            letter = self.chosen_word[position]
            # If correct..
            if letter == guess:
                # Update the display with the letter
                self.display[position] = letter
                # Set correct guess to True
                correct_guess = True
        # If incorrect..
        if not correct_guess:
            # provide feedback to user
            print(f"The letter {guess} is not in the word - sorry!")
            # They lose a life
            self.lives -= 1
            # Check for end of the game via a loss
            if self.lives == 0:
                self.end_of_game = True
                print("You lose.")
        # Add our guess to the guessed list
        self.guessed_list.append(guess)
        # Display hangman art and word left to guess
        self.display_current_state()
        # Check for win
        if "_" not in self.display:
            self.end_of_game = True
            print("You win.")


def main():
    # Instantiate object from our Class
    hangman_game = HangmanGame()
    # Print out our logo
    print(logo)
    # *** HINT for testing
    print(f'Pssst, the solution is {hangman_game.chosen_word}.')
    # While loop to keep running through game logic whilst game is yet to end.
    while not hangman_game.end_of_game:
        guess = input("Guess a letter: ").lower()
        hangman_game.check_guess(guess)


# Good practice for separating reusable code.
if __name__ == "__main__":
    main()
