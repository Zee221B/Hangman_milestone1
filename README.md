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

milestone_3.py

I created a hangman class, and defined it with the init method and self attributes.
Code:
import random

from milestone_2 import ask_for_input


def check_guess(guess):
    print(check_guess(guess))

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word)* ["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list  = word_list
        self.list_of_guesses = []
    
    def check_guess(self,guess):
            if guess.lower() in self.word: 
                print(f"Good guess! {guess} is in the word")
                for char in range(len(self.word)):
                    print(char)
                    if self.word[char] == guess:
                        self.word_guessed[char] = guess
                        break
                    print(self.word_guessed)
                count +=1
            else:
                self.num_lives -=1
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left.") 
            self.list_of_guesses.append(guess)
                
                
    def ask_for_input(self):
        while True:
            guess = str(input("Guess a letter: ")).lower()
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
    def __add__(self, guess, list_of_guesses):
            self.guess = guess + list_of_guesses
            return self.guess + self.list_of_guesses

my_game = Hangman(word_list = ["doctor", "hello", "apple", "people"])
my_game.ask_for_input()