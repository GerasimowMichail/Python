import sqlite3

def create_db():
    con = sqlite3.connect('number_phone.db')
    cur = con.cursor()
    query = '''CREATE TABLE IF NOT EXISTS
    number_phone(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    last_name TEXT,    
    phone INTEGER    
    '''
    cur.execute(query)
    con.commit()
    return con

def insert_employer(new_data: tuple, con):
    print(new_data)
    print(con)
    cur = con.cursor()
    cur.execute(
        'INSERT INTO number_phone (name, last_name, phone) VALUES(?,?,?)', new_data)
    con.commit()
    return 'Данные добавлены'

def print_all(con):
    cur = con.cursor()
    res_all = cur.execute('SELECT * FROM number_phone;')
    res = res_all.fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str

def select_last_name(con, last_name):
    cur = con.cursor()
    res = cur.execute(
        f'SELECT * FROM number_phone WHERE last_name LIKE "{last_name.capitalize()}%";').fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str

def change_number(con, id_str, number_str):
    cur = con.cursor()
    cur.execute(f"UPDATE number_phone SET phone = {number_str} WHERE id = {id_str}")
    con.commit()
    return f'Изменили заработную плату'