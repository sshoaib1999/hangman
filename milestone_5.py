import random
class Hangman:
    """
    A class to represent the Hangman game.

    Attributes:
    - word (str): The word to be guessed, picked randomly from word_list.
    - word_guessed (list): A list of the letters of the word with '_' for each letter not yet guessed.
    - num_letters (int): The number of unique letters in the word that have not been guessed yet.
    - num_lives (int): The number of lives the player has at the start of the game.
    - word_list (list): A list of words.
    - list_of_guesses (list): A list of the guesses that have already been tried.

    Methods:
    - __init__(self, word_list, num_lives=5): Initializes the attributes of the Hangman class.
    - check_guess(self, guess): Checks if the guessed letter is in the word.
    - ask_for_input(self): Asks the user to guess a letter and calls the check_guess method.

    """
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        """Checks if the guessed letter is in the word."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess  
            self.num_letters -= 1                  
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            if self.num_lives > 0:
                print(f"You have {self.num_lives} lives left.")
            else:
                print("You have run out of lives.")

    def ask_for_input(self):
        """Asks the user to guess a letter and calls the check_guess method."""
        while True:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()
        if game.num_lives == 0:
            print("You lost!")
            break
    if game.num_letters == 0:
        print("Congratulations. You won the game!")

# List of words to be used in the game
word_list = ["apple", "banana", "cherry"]

# Call the play_game function to play the game
play_game(word_list)


