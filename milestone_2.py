<<<<<<< HEAD
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
=======
import random

# list of 5 favourite fruits

word_list = ["apple", "banana", "orange", "pineapple", "mango"]

print(word_list)

word = random.choice(word_list)
 
print(word)

guess = input("Enter a single letter: ")

if (len(guess) == 1) and (guess.isalpha() == 1):
    print("Good guess!")
else:
    print("Oops! Thats not a valid input.")
>>>>>>> 38bac94 (made changes to original)
