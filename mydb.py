import mysql.connector

dataBase = mysql.connector.connect(

host = 'localhost',
user = 'root',
passwd = 'password456'



)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE olderco")

print("All Done!")