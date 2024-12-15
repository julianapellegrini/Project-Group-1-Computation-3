from interfaces_menus.interface import *
from player_related.player import Player


def main():


    # start player_related instance here so save works for the whole game
    player = Player()


    # pass player_related instance to the start screen
    start_screen(player)


if __name__ == '__main__':
    main()
