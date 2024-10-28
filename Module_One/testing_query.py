import psycopg2

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "1234",
                        port = 5432)



curr = conn.cursor()
curr.execute('SELECT * FROM Users;')
rows = curr.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)