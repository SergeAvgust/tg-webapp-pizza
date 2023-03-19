import sqlite3

conn = sqlite3.connect('server.db')
c = conn.cursor()

c.execute("INSERT INTO chats (chat_id, user) VALUES (01, 'Tester');")
c.execute("INSERT INTO pizza (name, image, price) VALUES ('tpizza1', '1.png', 100);")
c.execute("INSERT INTO pizza (name, image, price) VALUES ('tpizza2', '2.png', 200);")
c.execute("INSERT INTO orders (chat_id, user, money) VALUES (01, 'Tester', 400);")
c.execute("INSERT INTO ordered_pizza (order_id, pizza_id, pizza_amount) VALUES (1, 1, 2);")
c.execute("INSERT INTO ordered_pizza (order_id, pizza_id, pizza_amount) VALUES (1, 2, 1);")
            

conn.commit()