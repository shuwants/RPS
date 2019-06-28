import random
moves = ['rock', 'paper', 'scissors']

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print("Sorry, I don't understand.")

def ask_input():
    rps = valid_input("Rock, paper, scissors? ('q' for quit)> ", ["rock", "paper", "scissors", "q"])
    if "q" in rps:
        print("Thanks for playing! See you next time.\n")
    else:
        print("play_game()")

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        return input("Rock, paper, scissors? > ").lower()


def beats(one, two):
    return((one == "rock" and two == "scissors") or (one == "scissors" and two == "paper") or
    (one == "paper" and two == "rock"))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0
        self.ties = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}\nOpponent played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) == True:
            print("** PLAYER 1 WINS **")
            self.p1.score += 1
            print(f"Score: Player 1 {self.p1.score}, Player 2 {self.p2.score}")
        elif beats(move2, move1) == True:
            print("** PLAYER 2 WINS **")
            self.p2.score += 1
            print(f"Score: Player 1 {self.p1.score}, Player 2 {self.p2.score}")
        else:
            print("** TIE **")
            print(f"Score: Player 1 {self.p1.score}, Player 2 {self.p2.score}")

    def play_game(self):
        print("Rock Paper Scissors, Let's go!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()

        print("Game over!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
