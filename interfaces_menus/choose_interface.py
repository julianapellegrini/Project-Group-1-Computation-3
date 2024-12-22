from save_system.check_save import check_save_file


# function to choose the interface based on the save file
def choose_interface(player, interface_w_save, interface_no_save):
    
    """
    Chooses the interface based on the presence of a save file.

    Parameters:
    -----------
    player : object
        The player object.
    interface_w_save : function
        The function to call if a save file is present.
    interface_no_save : function
        The function to call if no save file is present.
    """

    if check_save_file():
        interface_w_save(player)
    else:
        interface_no_save(player)
