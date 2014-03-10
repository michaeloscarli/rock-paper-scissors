'''
Created on Mar 10, 2014

@author: Oscar
'''
import numpy

class computer(object):
    '''
    A computer class in the game rock_paper_scissors
    '''
    wins = 0
    choice = ""


    def __init__(self):
        '''
        Constructor for the computer
        Initializes wins to 0
        '''
        self.wins = 0
        self.choice = ""
        
    def generate_choice(self, player_choice):
        '''
        generates a choice for the computer depending on the user's choice
        @param player_choice: the user's choice for that round
        '''
        if player_choice == "rock":
            if numpy.random.rand()<.4:
                self.choice = "scissor"
            elif numpy.random.rand()<.5:
                self.choice = "paper"
            else:
                self.choice = "rock"
                
        elif player_choice == "paper":
            if numpy.random.rand()<.4:
                self.choice = "rock"
            elif numpy.random.rand()<.5:
                self.choice = "scissor"
            else:
                self.choice = "paper"
                
        else: #user input is "scissor" or nothing
            if numpy.random.rand()<.4:
                self.choice = "paper"
            elif numpy.random.rand()<.5:
                self.choice = "rock"
            else:
                self.choice = "scissor"
            
    def increment_wins(self):
        '''
        Increments the computer's wins
        '''
        self.wins+=1
        
        