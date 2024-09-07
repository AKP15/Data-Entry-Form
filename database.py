import sqlite3

def create_db():
    conn=sqlite3.connect('Students.db');#create database
    c=conn.cursor(); #create cursor
    c.execute('''CREATE TABLE IF NOT EXISTS Students (
                
                First_Name TEXT,
                Last_Name TEXT,
                Gender TEXT,
                Age INTEGER,
                Region TEXT,
                City TEXT,
                No INTEGER,
                Street Text,
                Town Text)''')
    conn.commit()
    conn.close()

def insert_students( FirstName ,
                LastName ,
                Gender ,
                Age ,
                Region ,
                City ,
                No ,
                Street,
                Town):
    conn=sqlite3.connect('Students.db')
    c=conn.cursor();
    insert_query=('''INSERT INTO Students(First_Name ,
                Last_Name ,
                Gender ,
                Age ,
                Region ,
                City ,
                No ,
                Street,
                Town) VALUES (?,?,?,?,?,?,?,?,?)''')
    insert_data=(FirstName ,
                LastName ,
                Gender ,
                Age ,
                Region ,
                City ,
                No ,
                Street,
                Town)

    c.execute(insert_query,insert_data)
    conn.commit()
    conn.close()