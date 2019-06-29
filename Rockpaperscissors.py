#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class CyclePlayer(Player):
    def __init__(self):
        self.ptr = 0

    def move(self):
        if(self.ptr > 2):
            self.ptr = 0
        x = moves[self.ptr]
        self.ptr += 1
        return x             


class ReflectPlayer(Player):

    def __init__(self):
        self.ptr = 0
                     
    def move(self):
        if(self.ptr == 0):
            self.ptr += 1
            return random.choice(moves)
    
        else: 
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = my_move       


class RandomPlayer(Player):
    
    def move(self):
        return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def move(self):
        while(True):
            x = input('Enter rock,paper or scissors:   ')
            if x in moves: 
                return x


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.player1 = 0
        self.p2.player2 = 0
    
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if(move1 == move2): 
            print("ITS A TIE")

        elif(beats(move1, move2)):
                self.p1.player1 += 1
        else:
                self.p2.player2 += 1
                
        self.p2.learn(move1, move2)

    def play_game(self):
        y = input("How many rounds do you want to play?") 
        while(not y.isnumeric()):
            print("your value is incorrect ")
            y = input("How many rounds do you want to play?") 
             
        print("Game start!")
        for round in range(int(y)):
            print(f"Round {round}:")
            self.play_round()
            if self.p1.player1 > self.p2.player2:
                print("Player 1 score is " + str(self.p1.player1) 
                      + " Player 2 score is " + str(self.p2.player2)
                      + " You won!")
            else:
                print("Player 1 score is " + str(self.p1.player1) 
                      + " Player 2 score is " + str(self.p2.player2) 
                      + " You lost!")
                print("Game over!")
if __name__ == '__main__':
    w = input("Enter your choice. RelectPlayer, CyclePlayer,RockPlayer or RandomPlayer?")
    if(w == "ReflectPlayer" or "reflect" or "Reflect"):
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game() 
    elif(w == "CyclePlayer" or "cycle" or "Cycle"):
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game() 
    elif(w == "RockPlayer" or "rock" or "Rock"):
        game = Game(HumanPlayer(), Player())
        game.play_game() 
    elif(w == "RandomPlayer" or "random" or "Random"):
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game() 
    elif(w == "quit"):
        SystemExit()
        