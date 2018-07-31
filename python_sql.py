import pymysql
db = pymysql.connect("localhost", "root", "root", "northwind")
cursor = db.cursor()

sql = "select * from Shippers"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()
db.close()
