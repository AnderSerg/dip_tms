import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="litecart",
    port=3307
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")
print(cursor.fetchall())
print("")
query = "SELECT customer_lastname FROM lc_orders ORDER BY customer_lastname DESC LIMIT 1"
cursor.execute(query)
print(cursor.fetchall())

db.close()
