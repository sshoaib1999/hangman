import random

# list of 5 favourite fruits

word_list = ["apple", "banana", "orange", "pineapple", "mango"]

print(word_list)

word = random.choice(word_list)
 
print(word)

def check_guess(guess):
  guess.lower
  if guess in word:
    print(f"Good guess! {guess} is in the word.")
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
  while True:

    guess = input("Enter a single letter: ")

    if (len(guess) == 1) and (guess.isalpha() == 1):
      print("Good guess!")
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")
  check_guess(guess)

ask_for_input()


