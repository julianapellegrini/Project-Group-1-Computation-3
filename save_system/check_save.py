import os


# check if save file is not empty
def check_save_file():
    if os.path.getsize("save_system/gamesave.txt") > 0:
        return True
    else:
        return False
