from interfaces_menus.interface import *
from player_related.player import Player


def main():
    # loading music file
    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")
    pygame.mixer.music.set_volume(0.3)

    # start player_related instance here so save works for the whole game
    player = Player()

    # playing the music infinitely
    pygame.mixer.music.play(loops=-1)
    # pass player_related instance to the start screen
    start_screen(player)


if __name__ == '__main__':
    main()
