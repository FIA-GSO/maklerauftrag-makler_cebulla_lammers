############################################################
#                                                          #
#                                                          #
#           Maklerauftrag - Cebulla, Lammers               #
#                                                          #
#                                                          #
############################################################

import sqlite3

# Get highest number from the database and store it as "ObjektID" 

conn = sqlite3.connect("Maklerdatenbank.db")
cursor = conn.cursor()
cursor.execute(f"SELECT MAX(ObjektID) FROM Objekte")
highestnumber = cursor.fetchone()
conn.close()

Objektname = input("Name des Objekts:")
ObjektID = highestnumber[0] + 1
print("Objektname ist:" + Objektname)
print("ObjektID ist:" + ObjektID)

# get the number of rooms to calculate

raumanzahl = input("Anzahl der Räume:")

# calculate every room for the number of rooms to calculate

for i in raumanzahl:
    raumid = i
    laengstewand = input("Angabe der längsten Wand (in cm):")
    angrenzendewand = input("90° angrenzende Wand (in cm):")
    raumflaeche = int(laengstewand) * int(angrenzendewand)
    raumflaeche = raumflaeche / 10000
    print(raumflaeche + "m2")
    
