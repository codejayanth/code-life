import psycopg2
from datetime import datetime

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "1234",
                        port = 5432)


def Execute_SQL_Statement(data_one, data_two, typee):
    curr = conn.cursor()
    if typee == 'INSERT':
        timee = datetime.now()
        curr.execute('INSERT INTO Users VALUES (email, data_two);')
        conn.close()
    else:
        curr.execute('SELECT email, password FROM Users WHERE email = email AND password = password;')
        rows = curr.fetchall()
        print(rows)
        conn.close()

data = Execute_SQL_Statement('rama@gmail.com', '123456', 'INSERT')
print(data)
