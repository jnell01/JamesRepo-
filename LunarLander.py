'''James Nell - Username = jnell01.
   Lunar Lander Game.'''


def strt(): #Starts - Initial Instructions and Countdown for user/player to begin game
    print("You are in a space ship rocketing towards the moon due to the moon's gravitational pull.\nYou will have to choose how much fuel to burn, to steady your speed, for each round of this game.")
    print("Get Ready")
    for i in range(1,4):
        print(i)
    print("START!")

def main(): #main game program that Calculates the variables for each round of the game and takes user input
    altcnt = 1000.0 #Starting Altitude above the moon (in meters)
    velcnt = 0  #Velocity at start.(meters per second)
    fuelcnt = 1000.0 #Fuel at start.
    turncnt = 1  #Game time
    fuelfin = 0 #Counter for player to leave session of the game.
    strt() #countdown function to start game

    def congrats(): #Local Function = Player message if successful at end of game in main()function.
        altcnt = 0 #Adjusting Altitutde to 0.
        print("Well Done! You have landed safely")
        print("You completed the game in", +turncnt, "rounds")
        print("Your altitude is", altcnt, ".")
        print("You landed on the moon with a velocity of", velcnt, "per meters second")
        print("You have", fuelcnt, "litres of fuel remaining")

    def unlucky(): #Local Function = Player message if unsuccessful game at end of game in main() function.
        crater = 5*velcnt
        print("You have Crashed!")
        print("You crashed into the Moon with a velocity of", velcnt, "meters per second")
        print("You have created a massive dent in the Moon!", +crater, "meters wide")

    while altcnt > 0:
        print("Round", turncnt)
        print("You are now", altcnt, "meters above the moon")
        if velcnt > 0:
            print("You have", fuelcnt, "litres of fuel remaining and you are travelling at", velcnt, "meters per second towards the moon")
        elif velcnt == 0:
            print("You have", fuelcnt, "litres of fuel remaining. Your velocity is 0. (Your are not currently moving away or towards the moon.)")
        elif velcnt < 0:
            print("You have", fuelcnt, "litres of fuel remaining and you are travelling at", velcnt, "meters per second away the moon")

        print("Please choose how much fuel to burn: ")
        correctinput = False #Creating Boolean variable for when user has not chosen a correct fuel input for this round.
        while not correctinput:
            try:
                fuel = int(input()) #chosen amount of fuel to burn for this round of the game
                if fuel < 0:
                    print("You cannot burn a negative amount of fuel. Please choose a positive integer")
                else:
                    correctinput = True
            except ValueError:
                print("Chosen Amount of fuel is not correct. You must choose a positive integer")

        turncnt += 1
        fuelcnt -= float(fuel)
        if fuel > fuelcnt:
            print("You have tried to burn more fuel than you have remaining. This will count as you burning all your remaining fuel")
            fuelcnt = 0
        else:
            velcnt += 1.6 - (0.15*float(fuel))
            altcnt -= velcnt
    else:
        if velcnt < 10 and velcnt >= 0 and altcnt <=0:
            congrats()
        elif fuelfin == 1:
            print("Leaving This Session of the Gme")
        else:
            unlucky()

#Starting the Lunar Lander Game
while True:
    main() #Main Game Program(Function)
    print("Would you like to play again? Please enter either Y/y for yes or N/n for No:")
    choose1 = input()
    while choose1 != "Y" and choose1 != "y" and choose1 and "N" and choose1 != "n": #For Incorrect User Input
        print("That is not the correct input. Please enter either Y/y or N/n")
        choose1 = input()
    else:
        if choose1 == "Y" or choose1 == "y": #For user to play again
            continue
        else:
            print("Thank you for playing. See you next time\nEnding Program")
            break
