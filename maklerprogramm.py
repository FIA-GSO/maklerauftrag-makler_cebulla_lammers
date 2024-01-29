import sqlite3

conn = sqlite3.connect("Maklerdatenbank.db")
cursor = conn.cursor()
highestnumber = cursor.execute(f"SELECT MAX(ObjektID) FROM Objekte")
conn.close()

print(highestnumber)