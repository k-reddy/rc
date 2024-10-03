import helpers
import character
from board import Board
import os
from game_loop import GameLoop


def main():
    # set up terminal
    if os.getenv("TERM") is None:
        os.environ["TERM"] = "xterm"

    # get some user input before starting the game
    player_name = input("What's your character's name? ")
    # default to happy :D
    player_name = "Happy" if player_name == "" else player_name
    helpers.clear_terminal()
    want_help = input("Hit enter to start or type help for instructions ")
    helpers.clear_terminal()
    if want_help == "help":
        helpers.give_help()
    monsters = []
    names = ["Tree Man", "Evil Blob", "Living Skeleton"]
    for i in range(3):
        monster = character.Monster(names[i], 10)
        monsters.append(monster)
    player = character.Player(player_name, 10)
    board = Board(10, monsters, player)
    game = GameLoop(board)
    game.start()


if __name__ == "__main__":
    main()
