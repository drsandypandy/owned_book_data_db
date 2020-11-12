import sqlite3


conn = sqlite3.connect('book_list.sqlite')

cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Book_Lib;
DROP TABLE IF EXISTS Author;

CREATE TABLE Books (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE
);

CREATE TABLE Location (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    location TEXT UNIQUE
);

CREATE TABLE Author (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Book_Lib (
    year  INTEGER NOT NULL,
    location_id  INTEGER,
    title_id  INTEGER,
    author_id  INTEGER,
    PRIMARY KEY (year, location_id, author_id, title_id)
);
''')
conn.commit()
# '''SELECT Location.location, Author.name, Books.title
# FROM Book_Lib JOIN Location JOIN Author JOIN Books
# ON Book_Lib.location_id = Location.id AND
# Book_Lib.author_id = Author.id AND Book_Lib.title_id =Books.id
# ORDER BY Author.name'''
conn.close()
print("All done.")
