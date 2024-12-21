from interfaces_menus.interface import *
from player_related.player import Player
from player_related.weapons import Watergun


def main():

    # start player instance here so save works for the whole game
    player = Player()

    # pass player_related instance to the start screen
    start_screen(player)


if __name__ == '__main__':
    main()
