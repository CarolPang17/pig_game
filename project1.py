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

# --- set game's term

#game will keep going if player's scores is less then maximum score
while max(player_scores) < max_score:

    #go over each player one by one
    for player_idx in range(players):
        print("\nPlayer number ", player_idx + 1, " turn has just started\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        #set initial score for this turn
        current_score = 0

        while True:
            #ask play if he/she want to continue to roll
            should_roll = input("would you like to toll (y)? ")
            # if the input is capital, .lower() convert it to lowercase, if lowercase then keep lowercase
            if should_roll.lower() != "y":
                #if put not equal to y , means n or something else, then break, this turn will stop
                break
            #otherwise if input == "y", it will not "break" the loop, then roll again
            value = roll()

            #if the dice number is 1 , player loss score of this turn, trun end
            if value == 1:
                print("you rolled a 1! Turn done!")
                #make this turn score to be 0
                current_score = 0
                #trun end
                break
            #if player get any number other then 1, player's score in this turn goes up with the dice number
            else:
                current_score += value
                print("you rolled a:", value)

            print("Your score is:", current_score)

        #add the score in this turn to the total score of the player
        player_scores[player_idx] += current_score
        print("your total score is:", player_scores[player_idx])

# re-set the maximum score to the player's highest score
max_score = max(player_scores)

# print out the winner
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:",
      max_score)
