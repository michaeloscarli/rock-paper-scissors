'''
Created on Mar 10, 2014

@author: Oscar
'''

class player(object):
    '''
    A player class in the game rock_paper_scissors
    '''
    wins = 0
    name = ""
    choice = ""
    


    def __init__(self, name):
        '''
        Constructor for the player object 
        Initializes wins to 0
        @param name: The player's name for the game session
        '''
        self.wins = 0
        self.name = name
        self.choice = ""
        
    def increment_wins(self):
        '''
        increases the player wins by 1
        '''
        self.wins+=1
        