<<<<<<< HEAD
import random

words = ['apple', 'banana', 'orange', 'strawberry', 'kiwi'] 
secret_word = random.choice(words)

def ask_for_input():
  guess = input("Guess a letter: ")
  return guess

def check_guess(guess):
  if guess in secret_word:
    print(f"Good guess! {guess} is in the word.") 
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

while True:
  guess = ask_for_input()
  check_guess(guess)
  
  if guess in secret_word:
=======
import random

words = ['apple', 'banana', 'orange', 'strawberry', 'kiwi'] 
secret_word = random.choice(words)

def ask_for_input():
  guess = input("Guess a letter: ")
  return guess

def check_guess(guess):
  if guess in secret_word:
    print(f"Good guess! {guess} is in the word.") 
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

while True:
  guess = ask_for_input()
  check_guess(guess)
  
  if guess in secret_word:
>>>>>>> 38bac94 (made changes to original)
    break