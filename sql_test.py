import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="litecart"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")
print(cursor.fetchall())

query = "SELECT * FROM lc_orders"
cursor.execute(query)
print(cursor.fetchall())

db.close()
