# HANGMAN PROJECT ATTEMPT 2 - Complete 

# For this project, I utilised object-oritented programming. I creatd he Hangman class and within that defined parameters within methods, including the magic 'init' method. I defined what happens when the user's guess is in the word, and how this affects the number of lives they have left, I also defined the input to check if the user guessed a valid single, alphabetical letter. For both of these instances I created the functions check_guess and ask_for_input. The conditions within these functions were in the form of 'if-else' statements and 'while' loops.

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

   


