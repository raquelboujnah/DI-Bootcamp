# Steps
# Part I - game.py

#     game.py – this file/module should contain a class called Game. It should have 4 methods:
import random


class Game:
    def  get_user_item(self):
    #  – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.
        while True:
            user_input = input("Please select rock, paper, or scissors: ").lower()
            if user_input in ['rock', 'paper', 'scissors']:
                return user_input
            else:
                print("Invalid choice. Please select rock, paper, or scissors.")

    def get_computer_item(self):
    # Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).
        return random.choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, user_item, computer_item):

        # Determine the result of the game.
#             Parameters:
#                 user_item – the user’s chosen item (rock/paper/scissors)
#                 computer_item – the computer’s chosen (random) item (rock/paper/scissors)
#                 Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
        
        # If both selected the same item, it's a draw
        if user_item == computer_item:
            return 'draw'
    
        # Now check the cases where the user wins:
        elif (user_item == 'rock' and computer_item == 'scissors') or \
            (user_item == 'scissors' and computer_item == 'paper') or \
            (user_item == 'paper' and computer_item == 'rock'):
            return 'win'
    
        # If it's neither a draw nor a win, it must be a loss
        else:
            return 'loss'

    def play(self):
        #  the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
#             Get the user’s item (rock/paper/scissors) and remember it
        user_item = self.get_user_item()
#             Get a random item for the computer (rock/paper/scissors) and remember it
        computer_item = self.get_computer_item()
#             Determine the results of the game by comparing the user’s item and the computer’s item
        result = self.get_game_result(user_item, computer_item)
#                 Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == 'win':
            print("You win!")
        elif result == 'draw':
            print("It's a draw!")
        else:
            print("You lose!")

        return result
#                 Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
