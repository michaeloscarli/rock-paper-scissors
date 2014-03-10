'''
Created on Mar 10, 2014

@author: Oscar
'''
import Player
from Player import player
from computer import computer
import threading
import time
import MySQLdb as MS

class game(object):
    '''
    A game of rock paper scissors
    '''
    player = None
    computer = None
    rounds = 0
    


    def __init__(self,name):
        '''
        Constructor for a game of rock paper scissors
        Initializes Player and computer to None
        Initializes rounds to 0
        @param name: The user-given name for the Player
        '''
        self.player = player(name)
        self.computer = computer()
        self.rounds = 0
        
    def evaluate_winner(self):
        '''
        Evaluates a winner given a Player and a computer
        Increments the score of the winner
        @return: The object (Player or computer) that won the round
        '''
        if self.player.choice == "rock":
            if self.computer.choice == "rock":
                return None
            elif self.computer.choice == "paper":
                self.computer.increment_wins()
                return self.computer
            else: #computer.choice == "scissor"
                self.player.increment_wins()
                return self.player
        
        elif self.player.choice == "paper":
            if self.computer.choice == "paper":
                return None
            elif self.computer.choice == "scissor":
                self.computer.increment_wins()
                return self.computer
            else: #computer.choice == "rock"
                self.player.increment_wins()
                return self.player
            
        elif self.player.choice == "scissor":
            if self.computer.choice == "scissor":
                return None
            elif self.computer.choice == "rock":
                self.computer.increment_wins()
                return self.computer
            else: #computer.choice == "paper"
                self.player.increment_wins()
                return self.player
        else: #The player entered garbage or nothing
            print "You entered invalid input. Therefore the computer is the victor."
            return self.computer
        
    def print_rounds(self):
        '''
        prints the number of rounds that have been played
        '''
        print "You have played", str(self.rounds)+" rounds."
    
    def print_scores(self):
        '''
        prints the current scores of both the computer and Player
        '''
        print self.player.name + "'s score is:", self.player.wins
        print "The computer's score is:", self.computer.wins
        
    def print_ratio(self):
        '''
        Prints the current ratio of Player wins/rounds
        '''
        if self.rounds == 0:
            print "Your current win ratio is: 0"
        else:
            print "Your current win ratio is:", float(self.player.wins)/float(self.rounds)
        
    def reset_choices(self):
        '''
        Resets the choices of the player and the computer
        '''
        self.player.choice = ""
        self.computer.choice = ""
        
    def start_new_game(self):
        '''
        Starts a new game by assigning game to a newly constructed game object
        '''
        self.player.wins = 0
        self.computer.wins = 0
        self.rounds = 0
        print "New game created."
        
    def read_choice(self, choice):
        '''
        Reads in the user's input for choice
        Ran in parallel in a spawned thread
        @param choice: The array that the user input will be stored in
        '''
        choice.append(raw_input())
        
    def start_round(self):
        '''
        Starts a new round. Uses a thread to read input while main thread does countdown.
        '''
        self.reset_choices()
        print 'Ready for a new round? Type "rock", "paper", or "scissors" before the countdown ends to select your choice'
        raw_input("Press enter when you are ready to begin! ")
        print "Start!"
        choice = []
        t = threading.Thread(target=self.read_choice, args=(choice,))
        t.start()
        print "Rock..."
        time.sleep(1)
        print "Paper..."
        time.sleep(1)
        print "Scissor..."
        time.sleep(1)
        t.join()
        print "Shoot!"
        if len(choice)!=0:
            self.player.choice = choice[0]
        self.computer.generate_choice(self.player.choice)
        winner = self.evaluate_winner()
        print "You threw:", self.player.choice
        print "The computer threw:", self.computer.choice
        if type(winner) is player:
            print "The winner is", self.player.name + "!"
        elif type(winner) is computer:
            print "The winner is the computer!"
        else:
            print "It was a tie!"
        self.rounds+=1

    def save_result(self):
        db1 = MS.connect(host="localhost",user="user",passwd="password")
        cursor = db1.cursor()
        sql = 'CREATE DATABASE test1'
        cursor.execute(sql)
        sql = '''CREATE TABLE foo (
       bar VARCHAR(50) DEFAULT NULL
       ) ENGINE=MyISAM DEFAULT CHARSET=latin1
       '''
        cursor.execute(sql)