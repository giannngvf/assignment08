# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

from random import randint
def display_program():
    print("Welcome to Lottery!")
    print("In this program, you will be asked to enter 3 numbers from 0-9 and if you are lucky enough to get your numbers matched with the lottery numbers, you become a winner!")

def lotto():
    count_user = 0; user_nums = []; count_lottery = 0 ; lottery_nums = []; num_of_right = 0
    while (len(user_nums)) < 3:
        count_user = int(input("Enter a number from 0-9: "))
        if count_user not in user_nums and 0 <= count_user <= 9:
            user_nums.append(count_user)
        else:
            print("Invalid number. Either you put the same number again or it is not a number from 0-9.")              
    while (len(lottery_nums)) < 3:
        count_lottery = randint(0, 9)
        if count_lottery not in lottery_nums:
            lottery_nums.append(count_lottery)
    for a in user_nums:
        for b in lottery_nums:
            if a == b:
                num_of_right += 1
    if num_of_right == 3:
        print("Winner!")
    else:
        print("You lose! You only guessed",num_of_right,"number(s) correctly. The lottery numbers are",lottery_nums)

def try_again():
    try_again = input("Try again? y/n: ")
    while try_again == "y" or try_again == "yes":
        display_program()
        lotto()
    while try_again == "n" or try_again == "no":
        print("OK. Goodbye!")
        break

display_program() #this will let the user know what is the program about.
lotto() #in this, the user will be asked 3 numbers from 0-9 and it will tell the user if he/she wins or loses. 
try_again() #this will ask the user if he/she wants to try it again.