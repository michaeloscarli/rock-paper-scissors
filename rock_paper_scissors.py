'''
Created on Mar 9, 2014

@author: Oscar
'''

from game import game
import os

def print_options():
    '''
    Prints the options available to the user upon menu startup
    '''
    options = [str(x) + ". " + commands[x][0] for x in range(0, len(commands))]
    print '\n'.join(options)  
    
def exit_loop():
    '''    
    Exits the while loop by calling system's exit function
    '''
    print "Thank you for playing!"
    os._exit(1)    

if __name__ == '__main__':
    
    print "Welcome to Michael Li's game of Rock-Paper-Scissors - where everything's made up and the points don't matter!"
    name = raw_input("What is your name? ")
    game = game(name)
    
    commands = [["Start a new game.", game.start_new_game],
            ["Start a new round.", game.start_round],
            ["Print the current score.", game.print_scores],
            ["Print your win ratio.", game.print_ratio],
            ["Print the number of rounds that have been played.", game.print_rounds],
            ["Exit.", exit_loop]
            ]
    while (1):
        print_options()
        user_query = raw_input("What would you like to do? ")
        try:
            user_query = int(user_query)
            commands[user_query][1]()
        except:
            print ("Please enter a valid input.")
    
    
    
    