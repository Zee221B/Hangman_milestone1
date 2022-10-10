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
