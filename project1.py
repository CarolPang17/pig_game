# ---- dice number generator , generate random number between 1 to 6 ----

import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# ---- ask user how many player ----

while True:
    #ask how many players is in the game)
    players = input("Enter the number of players (2-4): ")
    # check if a integer number of players were inputted
    if players.isdigit():
        #convert the input from a string into an integer
        players = int(players)
        #check if user inputted a vaild number that is greater or equal to 2 and less or equal to 4
        if 2 <= players <= 4:
            #if user did input a vaild number that is greater or equal to 2 and less or equal to 4, we can break out of the loop
            break
            #if user did not input a vaild number, then it going to keep asking for a vaild number that between 2- 4
        else:
            print("Must be between 2 - 4 players")
    #if user did not input a integer number
    else:
        print("Invalid, try again")

# --- set up the initial game

#set the maximum score to 50
max_score = 50
#set all player initial score to 0
player_scores = [0 for _ in range(players)]

#ask user if they want to continue to roll, either toll again , or stop their turn
#if he/she decides to stop the turn, then add the dice result to the total score

# keep checking if either player has a score that is above 50
# if anyone totale score is more than 50, game end
