import sqlite3

class Database:


    # __init__ is called when you create an object. the rest become functions on that class
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS comics (id INTEGER PRIMARY KEY, title text, publisher text, issue integer, print integer, month string, year integer)")
        self.conn.commit()
        # conn.close()

    def insert(self, title, publisher, issue, print, month, year):
        # conn=sqlite3.connect("books.db")
        # cur=conn.cursor()
        self.cur.execute("INSERT INTO comics VALUES (NULL,?,?,?,?,?,?)", (title,publisher,issue,print,month,year))
        self.conn.commit()
        # self.conn.close()

    def view(self):
        # conn = sqlite3.connect("books.db")
        # cur=conn.cursor()
        self.cur.execute("SELECT * FROM comics")
        rows = self.cur.fetchall()
        # don't have to commit because we're reading, but not writing/adding to database
        # self.conn.close()
        # rows is returned as a Python list
        return rows

    def search(self, title="",publisher="",issue="",print="",month="",year=""):
        # conn = sqlite3.connect("books.db")
        # cur=conn.cursor()
        self.cur.execute("SELECT * FROM comics WHERE title=? OR publisher=? OR issue=? OR print=? OR month=? OR year=?", (title,publisher,issue,print,month,year))
        rows=self.cur.fetchall()
        # self.conn.close()
        return rows

    def delete(self, id):
        # conn = sqlite3.connect("books.db")
        # cur=conn.cursor()
        self.cur.execute("DELETE FROM comics WHERE id=?", (id,))
        self.conn.commit()
        # self.conn.close()

    def update(self,id,title,publisher,issue,print,month,year):
        # conn = sqlite3.connect("books.db")
        # cur=conn.cursor()
        self.cur.execute("UPDATE comics SET title=?, publisher=?, issue=?, print=?, month=?, year=? WHERE id=?", (title,publisher,issue,print,month,year,id))
        self.conn.commit()
        # self.conn.close()


    def __del__(self):
        self.conn.close()   