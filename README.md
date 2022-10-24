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



CYLINDER PRACTICAL
from cgitb import small
import math

class Cylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = None 

    def get_surface_area(self):
        surface_area_value = 3.14*self.radius*self.height + 2*3.14*(self.radius ** 2) 
        return(surface_area_value)

    def get_volume(self):
        volume_value = 3.14*self.radius**2*self.height
        return(volume_value)
      

small_cylinder = Cylinder(5, 10)
big_cylinder = Cylinder(10, 8)

print(small_cylinder.surface_area)
print(small_cylinder.get_volume())
#print(small_cylinder.get_surface_area())
#print(big_cylinder.height)

CAR PRACTICAL
from unittest import TestLoader


class Car:
    def __init__(self, model, year=2022):
        self.model = model
        self.year = year
        self.miles_driven = 0
        
    def info(self):
        print(f"The car {self.model} was made in {self.year}.")
    
    def drive(self):
            print("Vroom!")

    def update_miles_driven(self, additional_miles):
        self.miles_driven = additional_miles
        print("You have driven " + str(self.miles_driven) + " miles so far!")
    
    def increment_miles_driven(self, additional_miles):
        # add miles driven by 1
        self.miles_driven += additional_miles
        print("You have driven " + str(self.miles_driven) + " miles so far!")

my_car = Car("Tesla")

my_car.info()

my_car.drive()

my_car.update_miles_driven(0)
my_car.increment_miles_driven(1)

MAGIC METHODS
class Vector:
    def __init__(self, three, nine, ten):
        self.three = three
        self.nine = nine
        self.ten = ten
    
    def __repr__(self):
        return repr()

HANGMAN PROJECT ATTEMPT 2 - Complete 

For this project, I utilised object-oritented programming. I creatd he Hangman class and within that defined parameters within methods, including the magic 'init' method. I defined what happens when the user's guess is in the word, and how this affects the number of lives they have left, I also defined the input to check if the user guessed a valid single, alphabetical letter. For both of these instances I created the functions check_guess and ask_for_input. The conditions within these functions were in the form of 'if-else' statements and 'while' loops.

import random


# define the list possible words and choose random word from list


# word = random.choice(word_list)
# print(word)


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word)* ["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [] 
        
    
    # method to check if guess is in the word
    def check_guess(self, guess):
        #print(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word. ")
            for index,char in enumerate(self.word):
                    # print(index,char)
                    if guess == char:
                        self.word_guessed[index] = guess
                        #break
            print(self.word_guessed)
            self.num_letters -= 1   
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                print("Oh no! You lost! ")
            if self.num_lives != 0 and self.num_letters == 0:
                print(f"Congratulations, you have won Hangman! :D ")
           

        self.list_of_guesses.append(guess)
        

    # ask the user for input and check if it is a valid guess

    def ask_for_input(self):
        while True:
            guess = str(input("Guess a letter: ")).lower()
            if not guess.isalpha() or len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character. ")
            elif guess in self.list_of_guesses:
                print("You already tried that letter! ")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

           

word_list = ["strawberry", "kiwi", "banana", "dates", "pear"]
form_input = Hangman(word_list)
form_input.ask_for_input()

   



