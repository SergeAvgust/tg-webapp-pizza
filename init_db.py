import sqlite3

conn = sqlite3.connect('server.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS chats (
                chat_id INTEGER, 
                user TEXT
        );''')
c.execute('''
        CREATE TABLE IF NOT EXISTS pizza (
                id INTEGER PRIMARY KEY, 
                name TEXT, 
                image TEXT, 
                price INTEGER
        );''')
c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY, 
                chat_id INTEGER REFERENCES chats(chat_id),
                user TEXT REFERENCES chats(user),
                money INTEGER
        );''')
c.execute('''
        CREATE TABLE IF NOT EXISTS ordered_pizza (
                order_id INTEGER REFERENCES orders(id),
                pizza_id INTEGER REFERENCES pizza(id),
                pizza_amount INTEGER
        );''')
conn.commit() 

