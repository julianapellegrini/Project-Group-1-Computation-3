from save_system.check_save import check_save_file


def choose_interface(player, interface_w_save, interface_no_save):
    if check_save_file():
        interface_w_save(player)
    else:
        interface_no_save(player)
