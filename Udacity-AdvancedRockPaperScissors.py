#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.score = 0
        self.name = None
        self.last_move = None
        self.choice_index = random.randint(0, len(moves)) - 1

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        player_choice = my_move
        # print("Test: " + player_choice)

    def add_to_score(self):
        self.score += 1

    def set_name(self):
        self.name = "Player"

    def set_last_move(self, last_move):
        self.last_move = last_move


class RandomPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        return choice

    def set_name(self):
        self.name = "Random Player"


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Enter Rock, Paper, or Scissors: ").lower()
            print("You chose: " + choice)
            if ((choice == "rock") or (choice == "paper") or
                    (choice == "scissors")):
                return choice
            else:
                print("\nInvalid Entry. Please try again.\n")

    def set_name(self):
        self.name = "Human Player"


class ReflectPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        if game.p1.name == "Reflect Player":
            if game.p2.last_move is None:
                # print("No move remembered, Choose Randomly: " + choice)
                return choice
            else:
                choice = game.p2.last_move
                # print("Last move remembered, choosing: " + choice)
                return choice
        elif game.p2.name == "Reflect Player":
            if game.p1.last_move is None:
                # print("No move remembered, Choose Randomly: " + choice)
                return choice
            else:
                choice = game.p1.last_move
                # print("Last move remembered, choosing: " + choice)
                return choice
        else:
            return choice

    def set_name(self):
        self.name = "Reflect Player"


class CyclePlayer(Player):
    def move(self):
        if self.last_move == moves[self.choice_index]:
            self.choice_index += 1
            if self.choice_index > len(moves) - 1:
                self.choice_index = 0
            choice = moves[self.choice_index]
            self.set_last_move(choice)
            return choice
        else:
            # print("Test: Not Checking Moves")
            choice = moves[self.choice_index]
            self.set_last_move(choice)
            return choice

    def set_name(self):
        self.name = "Cycle Player"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.set_name()
        self.p2.set_name()
        self.rounds = 4

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.set_last_move(move1)
        self.p2.set_last_move(move2)
        print(f"\n{game.p1.name} Uses: {move1}\n{game.p2.name} Uses: {move2}")
        if move1 != move2:
            if beats(move1, move2):
                print(f"\n{game.p1.name} Wins!\n")
                self.p1.add_to_score()
            else:
                print(f"\n{game.p2.name} Wins!\n")
                self.p2.add_to_score()
        else:
            print("\nTie Game!\n")
        print(f"{self.p1.name} Score: {self.p1.score}")
        print(f"{self.p2.name} score: {self.p2.score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, self.rounds):
            print(f"Round {round}:")
            self.play_round()
        print(f"Final Score...")
        print(f"{self.p1.name} Score: {self.p1.score}")
        print(f"{self.p2.name} score: {self.p2.score}\n")
        if self.p1.score > self.p2.score:
            print(f"{self.p1.name} Wins the Series!!")
        elif self.p2.score > self.p1.score:
            print(f"{self.p2.name} Wins the Series!!")
        else:
            print("Series is tied. No Winner...")
        print("\nGame over!")


if __name__ == '__main__':
    # game = Game(Player(), Player())
    game = Game(RandomPlayer(), ReflectPlayer())
    game.play_game()
