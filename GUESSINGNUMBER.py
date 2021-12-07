# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number Display “Less than” if the inputed number is less than the random number Repeat asking the user until the random number has been guessed correctly.

from random import randint
def display_program():
    print("Welcome to Guess the Number!")
    print("In this prgram, you will guess a number from 0-100. It won't stop until you get it right! Don't worry, it will tell you whether the number you input is greater or less than the number you should guess. Enjoy!")
def num_guess():
    random_num = randint(0,100)
    user_num = int(input("Guess a number from 0-100: "))
    while user_num != random_num:
        if user_num < random_num:
            print("The number you entered is less than the number you are guessing. Guess higher!")
            user_num = int(input("Guess a number from 0-100: "))
        else:
            print("The number you entered is greater than the number you are guessing. Guess lower!")
            user_num = int(input("Guess a number from 0-100: "))
    print("Congratulations, you guessed it right!")

display_program() #this will let the user know what is the program about.
num_guess() #in this, user will be asked to input a number from 0-100. if the user didn't guess it right away, it will tell him if the number he/she should guess is lower or higher than the number he/she input.
