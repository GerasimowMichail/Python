from view import *
from models import *

from view import *
from models import *


def menu():
    con = create_db()
    while True:
        user_choice = inp_menu()
        if user_choice == '1':
            add_w = add_number()
            data_add = insert_employer(add_w, con)
            print_data(data_add)
        elif user_choice == '2':
            p_all = print_all(con)
            print_data(p_all)
        elif user_choice == '3':
            find_n = find_number()
            slm = select_last_name(con, find_n)
            print_data(slm)
        # elif user_choice == '4':
        #     find_pos = find_position()
        #     sel_pos = select_position(con, find_pos)
        #     print_data(sel_pos)
        # elif user_choice == '5':
        #     p_all = print_all(con)
        #     print_data(p_all)
        #     change_zp = change_number()
        #     ch_sal = change_sal(con, *change_zp)
        #     print_data(ch_sal)
        # elif user_choice == '6':
        #     d_zp = data_zp(con)
        #     print_data(d_zp)
        elif user_choice == '0':
            print('До свидания')
            break
        else:
            print('Вы что-то напутали с вводом')


# with open('file.txt', 'w', encoding='utf-8') as file:
# file.write(res_from_print_all)