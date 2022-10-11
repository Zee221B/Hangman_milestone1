# Hangman_milestone1
In this milestone I learned how to use basic Python commands to create varaibles for the game e.g 'if-else', import, input(), and print().

Code:
import random 
word_list = ("strawberries","pears","bananas","raspberries","dates")
print(word_list)
random.choice(word_list)
guess = input("Please eneter a single letter.")
if ((guess>= 'a' and guess<= 'z') or (guess>= 'A' and guess<= 'Z')):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

milestone_2.py: 
import random 
word = ["doctor"]
random_word = random.choice(word)


def check_guess(guess):
    
        # guess = str(input("Guess a number: ")).lower()
        if guess in random_word: 
            print(f"Good guess! {guess} is in the word")
            break
        else:
            print(f"Sorry, {guess}  is not in the word. Try again.")
            break
def ask_for_input():
    while True:
        guess = str(input("Guess a letter: ")).lower()
        if guess.isalpha() and len(guess) == 1:
            check_guess(guess)
            print(ask_for_input())
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
print(ask_for_input()) 