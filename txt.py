

import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                 col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')

# tuple of names
persons_tuple = ('information.docx', 'Hello.txt', 'myImage.png',\
                 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# loop through each object in the tuple to find the names that end in y.
for x in persons_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()

            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES (?)", (x,))
            print(x)

conn.close()
