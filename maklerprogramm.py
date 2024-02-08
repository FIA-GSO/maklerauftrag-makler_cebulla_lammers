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

# Erstelle eine Kopfzeile

print("################################################\n#              Marklerprogramm                 #\n#                                              #\n# - alle Angaben müssen in cm gemacht werden   #\n# - die ObjektID wird automatisch als nächste  #\n#      in der Datenbank freie angegeben        #\n#                                              #\n################################################\n\n")

# Erhalten der größten bisherigen ObjektID aus der Datenbank und speichern der nächsten Zahl als neue ObjektID 

conn = sqlite3.connect("Maklerdatenbank.db")
cursor = conn.cursor()
cursor.execute(f"SELECT MAX(ObjektID) FROM Objekte")
highestnumber = cursor.fetchone()
conn.close()

# Vergeben eines Objektnamens un der ObjektID

Objektname = input("Name des Objekts:")
ObjektID = highestnumber[0] + 1

# Erhalten der Information, wie viele Räume das Objakt hat

raumanzahl = int(input("Anzahl der Räume:"))
verbleibenderaeume = raumanzahl


# Berechne jeden der angegeben Anzahl von Räumen

while verbleibenderaeume > 0:
    raumid = raumid + 1
    print("\nRaum " + str(raumid))
    laengstewand = input("Angabe der längsten Wand (in cm):")
    angrenzendewand = input("90° angrenzende Wand (in cm):")
    raumflaeche = int(laengstewand) * int(angrenzendewand)
    raumflaeche = raumflaeche / 10000
    
    # addieren oder subtrahieren von weiteren Flächen eines Raumes
    
    weitere_flaeche = input("\nSoll eine weitere Fläche hinzugefügt werden? (y/n)")
    while weitere_flaeche == "y":
        flaechenart = input("Soll eine Fläche addiert oder subtrahiert werden? (+/-)")

        if flaechenart == "+":                      # Berechnung wenn etwas addiert werden soll
            wand1 = input("Erste Wand (in cm):")
            wand2 = input("Zweite Wand (in cm):")
            zusatzflaeche = int(wand1) * int(wand2)
            zusatzflaeche = zusatzflaeche / 10000
            raumflaeche = raumflaeche + zusatzflaeche
        
        if flaechenart == "-":                      # Berechnung wenn etwas subtrahiert werden soll
            wand1 = input("Erste Wand (in cm):")
            wand2 = input("Zweite Wand (in cm):")
            zusatzflaeche = int(wand1) * int(wand2)
            zusatzflaeche = zusatzflaeche / 10000
            raumflaeche = raumflaeche - zusatzflaeche
        
        weitere_flaeche = input("\nSoll eine weitere Fläche hinzugefügt werden? (y/n)")
    
    # ausgeben der Raumfläche und Addieren dieser auf die Gesamtfläche
    
    print("\n" + str(raumflaeche) + " m2 Raumfläche")
    gesamtflaeche = gesamtflaeche + raumflaeche

    # Speichern des jeweiligen Raumes in die Datenbank

    conn = sqlite3.connect("Maklerdatenbank.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO raeume (ObjektID, RaumID, Raumgroesse) VALUES ({ObjektID}, {raumid}, {raumflaeche})")
    conn.commit()
    conn.close()

    # Berechnen der noch verbleibenden Räume

    verbleibenderaeume = verbleibenderaeume - 1

# Speichern der Gesamtfläche und des Objektes in die Datenbank

conn = sqlite3.connect("Maklerdatenbank.db")
cursor = conn.cursor()
cursor.execute(f"INSERT INTO Objekte (ObjektID, ObjektName, Gesamtflaeche, Raumanzahl) VALUES ({ObjektID}, '{Objektname}', {gesamtflaeche}, {raumanzahl})")
conn.commit()
conn.close()

# Ausgeben der Informationen
print("\n\n\n-------- Daten --------")
print(f"Objekname: {Objektname}\nObjektID: {ObjektID}\nRaumanzahl: {raumanzahl}\nGesamtfläche: {gesamtflaeche}")
print("-----------------------\n\n\n")

input("Beliebige Taste zum beenden drücken")