##Python program to implement Rock-Paper-Scissor game

#importing required module for generating random values
import numpy
import random

##Printing the instructions to play the game
print('Winning rules of the game ROCK PAPER SCISSORs:\n')
print('Rock vs paper -> Paper wins\n')
print('Paper vs Scissor -> Scissor wins\n')
print('Rock vs Scissors -> Rock wins\n')

while True:
    print("Enter your choice\n 0-Rock \n 1-Paper \n 2-Scisssors\n")

    #Take user input
    user_choice=int(input("Enter your choice: "))

    #looping until user enters a valid input
    while user_choice>2 or user_choice<0: 
        user_choice=int(input('Enter a valid input choice:'))

    #Initialize the value of user_choice variable corresponding to the choice value
    if user_choice==0:
        choice_name='Rock'
    elif user_choice==1:
        choice_name='Paper'
    else:
        choice_name='Scissor'

    #Print User choice
    print("User choice is:",choice_name)
    print("Now its Computer's Turn...")

    comp_choice=random.randint(1,3)

    #Initialize  value of comp_choice_name variable corresponding to the choice value

    if comp_choice==0:
        comp_choice_name="Rock"
    elif comp_choice==1:
        comp_choice_name="Paper"
    else:
        comp_choice_name="Scissor"

    print("Computer choice is:",comp_choice_name)

    #Determine the winner
    if(user_choice == comp_choice):
        print("Its a draw")
    elif user_choice==0 and comp_choice==2:
        print("You Win")
    elif comp_choice > user_choice:
        print("You Lose")
    elif user_choice==2 and comp_choice==0:
        print("You Lose")
    elif user_choice >comp_choice:
        print("You Win")

    print("Do you want to play again? (Y/N)")
    ans=input().lower()
    if ans=='n':
        break

print("Thanks for Playing")
            