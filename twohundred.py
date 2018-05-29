#James Nell 200 Dice Game

import random

def instructions(): #Gives user instructions at the start of the game
    print("Welcome to my dice game '200'!\nYou will play against A.I. For each round, you will have the chance to roll a die numerous times.")
    print("During each round, if you roll a die number of 1, the round will end and your score for that round will be 0.")
    print("The winner of the game will have a score of 100 or more. If the computer reaches 100 before you, you will have one more turn.")
    print("The computer will start first. It is now the computer's turn")

"""def roll():
Returns a random number in the range 1 to 6, inclusive. To do this, find the random module on https://docs.python.org/3/library/index.html and follow the link to find the randint method."""

def roll_(): #returns a Random number for each dice roll between 1 and 6
    x = random.randint(1,6)
    return x

"""def ask_yes_or_no(prompt):
Prints the prompt as a question to the user, for example, "Roll again? ". If the user responds with a string whose first character is 'y' or 'Y', the function returns True.
If the user responds with a string whose first character is 'n' or 'N', the function returns False.
Any other response will cause the question to be repeated until the user provides an acceptable response."""

def ask_yes_or_no(prompt): #Asks user whether they want to play or not and returns True or False respectively. Prompts user to enter ccorrect input if user enters incorrectly.
    prompt = input("Would you like to Roll Again? Enter 'Y' or 'y' to play another round, or N/n not to")
    while prompt != "Y" and prompt != "y" and prompt != "N" and prompt != "n": #For incorrect input
        print("That is not correct input. Please enter either Y/y or N/n:")
        prompt = input("Please try again: ")
    else:
        if prompt == "y" or prompt == "Y":
            return True
        elif prompt == 'N' or prompt == "n":
            return False

"""def human_move(computer_score, human_score):
Tells the user both her current score and the computer's score, and how far behind (or ahead) she is. Then repeatedly asks whether the user wants to roll again.
This continues until either:
- The user decides not to roll again. The function should return the total of the rolls made during this move.
- The user rolls a 1. The function should return 0."""


def human_move(computer_score, human_score): #Main move of the game. This is where human player is told their score and determines amount of rolls the human throws for each round.
 #list of all die rolls for this round if not 1
    if computer_score > human_score:
        print('Your current score is ',human_score, "and the computer's score is", computer_score, ".\nYou are", computer_score - human_score ,"points behind")
    elif computer_score == human_score:
        print('Your current score is ',human_score, "and the computer's score is", computer_score, ".\nYou are drawing")
    else:
        print('Your current score is ',human_score, "and the computer's score is", computer_score, ".\nYou are", human_score - computer_score, "points ahead" )
    print("First Roll")
    human_round_list = []
    y = 0
    prompt = 0
    while y == 0: #setting a condition for a loop, so that either rolling a 1 or player deciding not to roll again stops the hand. If player Chooses No to roll again or rolls 1 , y is set to 1 to end loop.
        x = roll_()
        print("You rolled", x)
        human_round_list.append(int(x))
        if 1 in human_round_list:
            y = 1
            human_round_list = []
            print("As you rolled 1, your score for this round is 0.")
        elif ask_yes_or_no(prompt) == False:
            y = 1
            print("Your score for this round is",sum(human_round_list),".")
    return sum(human_round_list)


"""def computer_move(computer_score, human_score):
The computer rolls some number of times, displays the result of each roll, and the function returns the result (either 0 or the total of the rolls).
The function may use its parameters in order to play more intelligently (for example, it may wish to gamble more agressively if it is behind)."""

def computer_move(computer_score, human_score): #This function is the computers round. The computer rolls for a certain number of times and the score is returned. If computer rolls 1, score of 0 is returned.
    computer_round_list = [] #List of die rolls for this round of the game. Local variable.
    if (human_score - computer_score) > 20:
        for i in range(random.randint(3,6)): #If computer is losing, computer rolls more aggressively. Computer will roll between 3 and 6 times each hand.
            computer_round_list.append(roll_())
            print("The Computer Rolled",computer_round_list[i],". The computer now has",computer_round_list, "for this hand.")
            if 1 in computer_round_list:
                print("The Computer rolled 1 ! Computer's score for this round is '0'.")
                computer_round_list = []
                break
            else:
                continue
    else:
        for i in range(random.randint(1,3)): #If computer is winning, computer rolls more carefully so as not to get roll of "1". Computer only rolls between 1 and 3 times each hand.
            computer_round_list.append(roll_())
            print("The Computer rolled",computer_round_list[i],". So far the computer has",computer_round_list, "for this hand.")
            if 1 in computer_round_list:
                print("As the Computer rolled 1 ! The Computer's score for this round is '0'.")
                computer_round_list = []
                break
            else:
                continue
    print("The total score for this hand is", sum(computer_round_list))
    return sum(computer_round_list)


"""def is_game_over(computer_score, human_score):
Returns True if either player has 100 or more, and the players are not tied, otherwise it returns False. (Call this only after the human's move.)"""

def is_game_over(computer_score, human_score): #Within in the main game, this function determines whether the game is finished and returns a true of false value respectively. Returns Flase for Ties also.
    if computer_score >= 100 or human_score >= 100:
        if computer_score == human_score:
            return False
        else:
            return True
    else:
        return False

"""def show_results(computer_score, human_score):
Tells whether the human won or lost, and by how much. (Call this when the game has ended.)
Every function should have a "doc comment" telling what it does. Also, begin the program with a comment giving your name and a *brief *description of the program."""

def show_results(computer_score, human_score): #Once the game is finished, (I.e. Once game_is_over is == True) this function shows the player their results and advices whether they won or not.
    if computer_score > human_score:
        print("Your score is",human_score,"and the computer's score is",computer_score,". \nYou have lost the Game")
    else:
        print("Your score is",human_score,"and the computer's score is",computer_score,". \nCongratulations, you have Won the game!")


def main(): #Main function for program Die roll game 200
    human_rounds = 0   #counter for number of game rounds
    computer_rounds = 0 #counter for number of game rounds for computer
    computer_score = 0 #Total score in the game for the computer. Resulting score of each hand is added to this tally.
    human_score = 0 #likewise, total score for human. Resulting score of each hand is added to this tally.
    instructions()
    while is_game_over(computer_score, human_score) == False:
        computer_score += computer_move(computer_score, human_score)
        computer_rounds += 1
        human_score += human_move(computer_score, human_score)
        human_rounds += 1
        is_game_over(computer_score, human_score)
    else:
        show_results(computer_score, human_score)

if __name__ == "__main__":
    main()
