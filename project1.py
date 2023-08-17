
# dice number generator , generate random number between 1 to 6
import random

def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)

  return roll

value = roll()
print(value)


# ask user if they want to continue to roll, either toll again , or stop their turn
# if he/she decides to stop the turn, then add the dice result to the total score

# keep checking if either player has a score that is above 50
# if anyone totale score is more than 50, game end
