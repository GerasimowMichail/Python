from view import *
from models import *


def menu():
    con = create_db()
    while True:
        user_choice = inp_menu()
        if user_choice == '1':
            add_s = add_student()
            data_add = insert_employer(add_s, con)
            print_data(data_add)
        elif user_choice == '2':
            p_all = print_all(con)
            print_data(p_all)
        elif user_choice == '3':
            find_s = find_student()
            slm = select_last_name(con, find_s)
            print_data(slm)
        elif user_choice == '4':
            find_sl = find_shool()
            sel_pos = select_klass(con, find_sl)
            print_data(sel_pos)
        elif user_choice == '5':
            p_all = print_all(con)
            print_data(p_all)
            change_kl = change_klass()
            ch_kl = change_klas(con, *change_kl)
            print_data(ch_kl)
      
        elif user_choice == '0':
            print('До свидания')
            break
        else:
            print('Вы что-то напутали с вводом')
