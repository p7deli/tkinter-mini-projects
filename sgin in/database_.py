import sqlite3
import bcrypt


def create_table():
    con_ = sqlite3.connect('db_.sqlite3')
    cursor_ = con_.cursor()
    cursor_.execute('''
        CREATE TABLE IF NOT EXISTS SignUp(
            id_ INTEGER PRIMARY KEY AUTOINCREMENT ,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(50),
            password VARCHAR(100))
        ''')
    
    con_.commit()
    con_.close()

def add_user(fname, lname, email, password):
    con_ = sqlite3.connect('db_.sqlite3')
    cursor_ = con_.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor_.execute('''
        INSERT INTO SignUp (first_name, last_name, email, password)
        VALUES (?, ?, ?, ?) 
    ''', (fname, lname, email, hashed_password))

    con_.commit()
    con_.close()

def check_user(email, password):

    conn_ = sqlite3.connect('db_.sqlite3')
    cursor_ = conn_.cursor()

    cursor_.execute('''
            SELECT * FROM SignUp WHERE email=?
    ''', (email,))

    result_ = cursor_.fetchone()
    try:
        if result_ and bcrypt.checkpw(password.encode('utf-8'), result_[4]):
            return True
        return False
    finally:
        conn_.close()


if __name__ == '__main__':
    # print(check_user('ali@gmail.com', 'Ali123456'))
    create_table()