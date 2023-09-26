import random

# Create a list of fruits 
word_list = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

# Print the list  
print(word_list)

# Pick a random word
word = random.choice(word_list) 

# Print the random word
print(word)

# Take user input
guess = input('Enter a letter: ')

# Input validation
if len(guess) == 1 and guess.isalpha():
  print('Good guess!') 
else:
  print('Oops! That is not a valid input.')