import random
moves = ['rock', 'paper', 'scissors']


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return option # correct option will be returned even with useless characters.
        print("Sorry, I don't understand.")


def ask_input():
    rps = valid_input("Rock, paper, scissors? > ", ["rock", "paper", "scissors"])
    return rps


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
        return ask_input()

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def move(self):
        if self.their_move == None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move

    # def __init__(self):
    #     super().__init__()
    #     self.my_move = None
    #
    # def learn(self, my_move, their_move):
    #     self.their_move = HumanPlayer.my_move
    #
    # def move(self):
    #     if self.my_move == None:
    #         self.my_move = RandomPlayer.move(self)
    #         self.learn(self, HumanPlayer.learn)
    #         return self.my_move
    #     else:
    #         self.my_move= self.their_move
    #         self.learn(self, HumanPlayer.their_move)
    #         return self.my_move

class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def move(self):
        if self.my_move == None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move

def beats(one, two):
    return((one == "rock" and two == "scissors") or (one == "scissors" and two == "paper") or
    (one == "paper" and two == "rock"))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}\nOpponent played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) == True:
            print("** PLAYER One WINS **")
            self.p1.score += 1
            print(f"Score: Player One {self.p1.score}, Player Two {self.p2.score}")
        elif beats(move2, move1) == True:
            print("** PLAYER Two WINS **")
            self.p2.score += 1
            print(f"Score: Player One {self.p1.score}, Player Two {self.p2.score}")
        else:
            print("** TIE **")
            print(f"Score: Player One {self.p1.score}, Player Two {self.p2.score}")

    def play_game(self):
        print("Rock Paper Scissors, Let's go!")
        for round in range(5):
            print(f"Round {round + 1}:")
            self.play_round()
        print(f"\nFinal Score: Player One {self.p1.score}, Player Two {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("Player One win! Congratulations!\nGame Over!")
        elif self.p2.score > self.p1.score:
            print("Player Two win! Congratulations!\nGame Over!")
        else:
            print("Wao! It's TIE! Let's play 5 more games to settle things down!")
            self.p1.score = 0
            self.p2.score = 0
            self.play_game()

if __name__ == "__main__":
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
