import sqlite3


def create():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT,title text ,author text,year integer ,isbn integer UNIQUE)")
    conn.commit()
    conn.close()

# create()


def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    except Exception:
        # Conditional: sqlite3.IntegrityError: UNIQUE constraint failed: book.isbn
        print("Record with ISBN no {0} Exists...".format(isbn))
    conn.commit()
    conn.close()
insert('Andre the Great', 'Hanna Alabi', 2001, 550551011)
insert('Da Vinci Code', 'Dan Brown', 2001, 34551012)


def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows


print(view())


def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    row = cur.fetchall()
    conn.close()
    return row

# to delete entries in ddb.
def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",str(id))
    conn.commit()
    conn.close()

# to update entries/columns in db
def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

# to do calculations with db entries and variables.
# using a random variable
add = 10
def addition(add, title):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    # BALANCE=BALANCE is basically a column in the db that i want to update. ie, add 10 to the initial value in d db.
    cur.execute('UPDATE book SET BALANCE=BALANCE - {} WHERE title=?'.format(add), (title,))
    conn.commit()
    conn.close()
    # you have to view entries in db to confirm changes.
    # can be applies for subtraction, multiplication and division.


# check for two columns in db
def usern_passw_check():
    global rows
    conn = sqlite3.connect('Banking.db')
    cur = conn.cursor()
    cur.execute('SELECT username, password FROM bank')
    rows = cur.fetchall()
    conn.close()
    return rows
print(usern_passw_check())