from interface import *


def main():
    # loading music file
    pygame.mixer.music.load("audio/nocturne-of-ice.mp3")
    pygame.mixer.music.set_volume(0.3)

    # playing the music infinitely
    pygame.mixer.music.play(loops=-1)
    start_screen()


if __name__ == '__main__':
    main()
