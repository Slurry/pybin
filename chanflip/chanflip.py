#!/usr/bin/python3.1

import sqlite3
conn = sqlite3.connect('/home/jayson/streams/streamtest.db')
cursor = conn.cursor()
# data requests
query_ht={}
query_ht['listgenre']="[line for line in cursor.execute('select * from genres;')]"

# menu design
genremaint = {'1) Add Genre':'addgenre',\
                  '2) Modify Genre':'modgenre',\
                  '3) List Genres':'listgenre',\
                  '99) back':'back'}

search = {'1) Any Search':'anysearch',\
              '2) Genre Search':'genresearch',\
              '3) Name Search':'namesearch',\
              '99) back':'back'}

maintenance = {'1) Stream Maintenance':'streammaint', \
                   '2) Genre Maintenance':genremaint,\
                   '3) Validation Maintenance':'valmaint',\
                   '99) back':'back'}


watch = {'1) Flip':'flipsearch',\
             '2) Search':search,\
             '3) Pick':'picksearch',\
             '99) back':'back'}

menu={'1) Watch':watch, '2) Maintenance':maintenance}


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
result=eval(query_ht[request])
result.append(request)
print(result)





