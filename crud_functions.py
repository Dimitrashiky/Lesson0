import sqlite3

connection = sqlite3.connect("initiate_db.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCTS(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL)
''')

cursor.execute("DELETE FROM PRODUCTS")


for number in range(1,5):
    cursor.execute("INSERT INTO PRODUCTS (title, description, price) VALUES(?, ?, ?)", (f"Product{number}", f"Description{number}", f"{number * 100}"))


cursor.execute("SELECT * FROM PRODUCTS")

def get_all_products():
    return cursor.fetchall()





connection.commit()
#connection.close()