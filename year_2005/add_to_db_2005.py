import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('D:/py4e/Book-Project/book_list.sqlite')
    print('Connected to Database')
except Error:
    print('Error Connecting to Database')

cur = conn.cursor()


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = '2005_Output.txt'
year=fname.split('_')
year=int(year[0])

div=input('Data divisable by: ')
div = int(div)


count=0
fhand=open(fname)
for line in fhand:
    line = line.rstrip()
    line = line.split('@')
    location =line[0]
    name = line[1]
    name = name.strip()
    title = line[-1]
    title = title.strip()
    count=count+1

#    print(count, [year, location, name, title])

    cur.execute('''INSERT OR IGNORE INTO Books (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Books WHERE title = ? ', (title, ))
    title_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Author (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM Author WHERE name = ? ', (name, ))
    author_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Location (location)
        VALUES ( ? )''', ( location, ) )
    cur.execute('SELECT id FROM Location WHERE location = ? ', (location, ))
    location_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Book_Lib
        (year, location_id, author_id, title_id) VALUES (?, ?, ?, ? )''',
        (year, location_id, author_id, title_id ) )

    if count%div==0:
        conn.commit()
#'''SELECT Location.location, Author.name, Books.title
#FROM Book_Lib JOIN Location JOIN Author JOIN Books
#ON Book_Lib.location_id = Location.id AND
#Book_Lib.author_id = Author.id AND Book_Lib.title_id =Books.id
#ORDER BY Author.name'''
conn.close()
print("All done.")
