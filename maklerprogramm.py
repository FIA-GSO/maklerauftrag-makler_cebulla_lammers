############################################################
#                                                          #
#                                                          #
#           Maklerauftrag - Cebulla, Lammers               #
#                                                          #
#                                                          #
############################################################

import sqlite3
gesamtflaeche = 0
raumid = 0

# Get highest number from the database and store it as "ObjektID" 

conn = sqlite3.connect("Maklerdatenbank.db")
cursor = conn.cursor()
cursor.execute(f"SELECT MAX(ObjektID) FROM Objekte")
highestnumber = cursor.fetchone()
conn.close()

Objektname = input("Name des Objekts:")
ObjektID = highestnumber[0] + 1
print("Objektname: " + Objektname)
print("ObjektID ist: " + str(ObjektID))

# get the number of rooms to calculate

raumanzahl = int(input("Anzahl der Räume:"))
verbleibenderaeume = raumanzahl


# calculate every room for the number of rooms to calculate

while verbleibenderaeume > 0:
    raumid = raumid + 1
    print("\nRaum " + str(raumid))
    laengstewand = input("Angabe der längsten Wand (in cm):")
    angrenzendewand = input("90° angrenzende Wand (in cm):")
    raumflaeche = int(laengstewand) * int(angrenzendewand)
    raumflaeche = raumflaeche / 10000
    weitere_flaeche = input("Soll eine weitere Fläche hinzugefügt werden? (y/n)")
    while weitere_flaeche == "y":
        flaechenart = input("Soll eine Fläche addiert oder subtrahiert werden? (+/-)")
        if flaechenart == "+":
            wand1 = input("Erste Wand (in cm):")
            wand2 = input("Zweite Wand (in cm):")
            zusatzflaeche = int(wand1) * int(wand2)
            zusatzflaeche = zusatzflaeche / 10000
            raumflaeche = raumflaeche + zusatzflaeche
        if flaechenart == "-":
            wand1 = input("Erste Wand (in cm):")
            wand2 = input("Zweite Wand (in cm):")
            zusatzflaeche = int(wand1) * int(wand2)
            zusatzflaeche = zusatzflaeche / 10000
            raumflaeche = raumflaeche - zusatzflaeche
        weitere_flaeche = input("Soll eine weitere Fläche hinzugefügt werden? (y/n)")
    print(str(raumflaeche) + " m2 Raumfläche")
    gesamtflaeche = gesamtflaeche + raumflaeche

    conn = sqlite3.connect("Maklerdatenbank.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO raeume (ObjektID, RaumID, Raumgroesse) VALUES ({ObjektID}, {raumid}, {raumflaeche})")
    conn.commit()
    conn.close()

    verbleibenderaeume = verbleibenderaeume - 1


print("Gesamtfläche: " + str(gesamtflaeche))
conn = sqlite3.connect("Maklerdatenbank.db")
cursor = conn.cursor()
cursor.execute(f"INSERT INTO Objekte (ObjektID, ObjektName, Gesamtflaeche, Raumanzahl) VALUES ({ObjektID}, '{Objektname}', {gesamtflaeche}, {raumanzahl})")
conn.commit()
conn.close()