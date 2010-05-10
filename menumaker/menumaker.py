#!/usr/bin/python3.1

""" MenuMaker
Written by Jayson Williame 
2010/03/05
MenuMaker presents the user with a simple customized menu. It will
return a specified value if no submenu is configured.
"""
# Replace the following lines with your menu
helpmenu = {'1)Help':'help', '2)About MenuMaker':'about','99)Back':'back'}
editmenu = {'1)Undo':'undo', '2)Cut':'cut',\
                '4)Copy':'copy','5)Paste':'paste','99)Back':'back'}
filemenu = {'1)New':'newitem', '2)Open':'openitem',\
                '3)Save':'saveitem', '4)Exit':'exit','99)Back':'back'}
menu = {'1)File':filemenu, '2)Edit':editmenu,\
            '4)Help':helpmenu}


def show_menu():
    menupath=[menu]
    exitflag = False
    index = 0
    title = 'Menu'
    while not exitflag:
        index = len(menupath) - 1
        menu_level = menupath[index]
        menu_list = sorted(menu_level)
        print('----', title, '------')
        for i in menu_list:
            print(i)
        print('----------')
        menu_choice = input('Choice -> ')
        # Get key that matches menu_choice
        try:
            menu_item = [key for key in menu_level if menu_choice in key][0]
            title = str(menu_item).strip('123456789) ')
        except:
            # if input causes an error setup to return to main menu
            menupath=[menu, watch]
            menu_level = watch
            menu_choice = 'back'
            menu_item = [key for key in menu_level if menu_choice in key][0]
        # if menu_item is a dict, there is another level of menus
        if type(menu_level[menu_item]) == dict:
            menupath.append(menu_level[menu_item])
        elif menu_level[menu_item] == 'back':
            menupath.pop()
        else:
                      return menu_level[menu_item]
        # ADD back to menu items to move back through menus
        

        
show_menu()
