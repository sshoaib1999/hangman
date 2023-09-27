import random

class Hangman:

    def __init__(self, word_list, num_lives=6):
        self.word = random.choice(word_list) 
        self.word_guessed = ["_"] * len(self.word)  
        self.num_letters = len(set(self.word)) 
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Update word_guessed
            index = 0
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[index] = letter
                index += 1

    def ask_for_input(self):
        
        while self.num_lives > 0 and "_" in self.word_guessed:
            print(f"You have {self.num_lives} lives left")
            print(" ".join(self.word_guessed))
            
            guess = input("Guess a letter: ")
            
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                
            else:
                self.check_guess(guess)
                
                if guess not in self.word:
                    self.num_lives -= 1
                
                self.list_of_guesses.append(guess)
        
        if "_" not in self.word_guessed:
            print(f"You win! The word was {self.word}")
        else:
            print(f"You lost! The word was {self.word}")

word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
game = Hangman(word_list, num_lives=6)
game.ask_for_input()