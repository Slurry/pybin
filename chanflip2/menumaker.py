#!/usr/bin/python3.1


english_only = {'1) By Genre':'watchbygenreenglish',
                '2) By Random':'watchrandomenglish',
                '3) By Flip':'fliprandomenglish',
                '99) Back':'back'}

all_languages = {'1) By Random':'watchrandomall',
                 '2) By Flip':'fliprandomall',
                 '99) Back':'back'}

watch = {'1) English Stations':english_only,
         '2) All Stations':all_languages,
         '99) Back':'back'}

stream_maintenance = {'1) Add Stream':'addstream',
                      '2) Modify Stream':'modifystream',
                      '99) Back':'back'}

content_maintenance = {'1) Add Content Info':'addcontentinfo',
                       '2) Update Content Info':'updatecontentinfo',
                       '3) Next Non-Content Stream':'next_noncontent',
                       '99) Back':'back'}

genre_maintenance = {'1) Add Genre':'addgenre',
                     '99) Back':'back'}

maintenance = {'1) Stream Maintenance':stream_maintenance,
               '2) Content Maintenance':content_maintenance,
               '3) Genre Maintenance':genre_maintenance,
               '99) Back':'back'}

menu = {'1) Watch':watch,'2) Maintenance':maintenance}

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
        

request = show_menu()        

command_string = request + '()'
command = command_string



def next_noncontent():
    print('made it to next_noncontent')


eval(command)
