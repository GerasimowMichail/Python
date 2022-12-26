import sqlite3


def create_db():
    con = sqlite3.connect('pupils.db')
    cur = con.cursor()
    query = '''CREATE TABLE IF NOT EXISTS
    pupils(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    last_name TEXT,
    sholl TEXT,
    klass INTEGER,
    liter TEXT);
    '''
    cur.execute(query)
    con.commit()
    return con


def insert_employer(new_data: tuple, con):
    print(new_data)
    print(con)
    cur = con.cursor()
    cur.execute(
        'INSERT INTO pupils (name, last_name, sholl, klass, liter) VALUES(?,?,?,?,?)', new_data)
    con.commit()
    return 'Данные добавлены'


def print_all(con):
    cur = con.cursor()
    res_all = cur.execute('SELECT * FROM pupils;')
    res = res_all.fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str


def data_klass(con):
    cur = con.cursor()
    res = cur.execute('SELECT klass, liter FROM pupils').fetchall()
    out_int = 0
    for i in res:
        out_int += sum(i)
    return out_int


def select_last_name(con, last_name):
    cur = con.cursor()
    res = cur.execute(
        f'SELECT * FROM pupils WHERE last_name LIKE "{last_name.capitalize()}%";').fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str


def select_klass(con, klass):
    cur = con.cursor()
    res = cur.execute(
        f'SELECT * FROM pupils WHERE sholl LIKE "{klass.capitalize()}%";').fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str


def change_klas(con, id_str, zp_str):
    cur = con.cursor()
    cur.execute(f"UPDATE pupils SET klass = {zp_str} WHERE id = {id_str}")
    con.commit()
    return f'Изменили номер класса'
