import os


# check if save file is not empty
def check_save_file():

    """
    Checks if the save file is not empty.

    Returns:
    --------
    bool
        True if the save file is not empty, False otherwise.
    """
    
    if os.path.getsize("save_system/gamesave.txt") > 0:
        return True
    else:
        return False
