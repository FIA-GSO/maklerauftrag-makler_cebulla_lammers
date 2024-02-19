import sqlite3
gesamtflaeche = 0
<<<<<<< HEAD
raumid = 0

# -------- Erstellen eine Kopfzeile --------
=======
# Get highest number from the database and store it as "ObjektID" 
>>>>>>> 5d724ef43b4b31e0851e8498ed3f1e17eb89c46c

print("""
        ################################################\n
        #              Marklerprogramm                 #\n
        #                                              #\n
        # - alle Angaben müssen in cm gemacht werden   #\n
        # - die ObjektID wird automatisch als nächste  #\n
        #      in der Datenbank freie angegeben        #\n
        #                                              #\n
        ################################################\n\n
      """)




# -------- Vorbereitung für die Berechnungen --------


conn = sqlite3.connect("Maklerdatenbank.db")        # Erhalten der größten bisherigen ObjektID aus der Datenbank und speichern der nächsten Zahl als neue ObjektID
cursor = conn.cursor()
cursor.execute(f"SELECT MAX(ObjektID) FROM Objekte")
highestnumber = cursor.fetchone()
conn.close()


Objektname = input("Name des Objekts:")     # Vergeben eines Objektnamens un der ObjektID
ObjektID = highestnumber[0] + 1
<<<<<<< HEAD
=======
print("Objektname: " + Objektname)
print("ObjektID ist: " + str(ObjektID))
>>>>>>> 5d724ef43b4b31e0851e8498ed3f1e17eb89c46c


raumanzahl = int(input("Anzahl der Räume:"))        # Erhalten der Information, wie viele Räume das Objakt hat
verbleibenderaeume = raumanzahl




# -------- Berechnen der benötigten Werte --------


while verbleibenderaeume > 0:       # Berechne jeden der angegeben Anzahl von Räumen
    raumid = raumid + 1
    print("\nRaum " + str(raumid))
    laengstewand = input("Angabe der längsten Wand (in cm):")
    angrenzendewand = input("90° angrenzende Wand (in cm):")
    raumflaeche = int(laengstewand) * int(angrenzendewand)
    raumflaeche = raumflaeche / 10000
<<<<<<< HEAD
    

    weitere_flaeche = input("\nSoll eine weitere Fläche hinzugefügt werden? (y/n)")     # addieren oder subtrahieren von weiteren Flächen eines Raumes
    while weitere_flaeche == "y":
        flaechenart = input("Soll eine Fläche addiert oder subtrahiert werden? (+/-)")

        if flaechenart == "+":                      # Berechnung wenn etwas addiert werden soll
=======
    weitere_flaeche = input("Soll eine weitere Fläche hinzugefügt werden? (y/n)")
    while weitere_flaeche == "y":
        flaechenart = input("Soll eine Fläche addiert oder subtrahiert werden? (+/-)")
        if flaechenart == "+":
>>>>>>> 5d724ef43b4b31e0851e8498ed3f1e17eb89c46c
            wand1 = input("Erste Wand (in cm):")
            wand2 = input("Zweite Wand (in cm):")
            zusatzflaeche = int(wand1) * int(wand2)
            zusatzflaeche = zusatzflaeche / 10000
            raumflaeche = raumflaeche + zusatzflaeche
<<<<<<< HEAD
        
        if flaechenart == "-":                      # Berechnung wenn etwas subtrahiert werden soll
=======
        if flaechenart == "-":
>>>>>>> 5d724ef43b4b31e0851e8498ed3f1e17eb89c46c
            wand1 = input("Erste Wand (in cm):")
            wand2 = input("Zweite Wand (in cm):")
            zusatzflaeche = int(wand1) * int(wand2)
            zusatzflaeche = zusatzflaeche / 10000
            raumflaeche = raumflaeche - zusatzflaeche
<<<<<<< HEAD
        
        weitere_flaeche = input("\nSoll eine weitere Fläche hinzugefügt werden? (y/n)")
    
    
    print("\n" + str(raumflaeche) + " m2 Raumfläche")       # ausgeben der Raumfläche und Addieren dieser auf die Gesamtfläche
    gesamtflaeche = gesamtflaeche + raumflaeche


    conn = sqlite3.connect("Maklerdatenbank.db")        # Speichern des jeweiligen Raumes in die Datenbank
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO raeume (ObjektID, RaumID, Raumgroesse) VALUES ({ObjektID}, {raumid}, {raumflaeche})")
    conn.commit()
    conn.close()


    verbleibenderaeume = verbleibenderaeume - 1     # Berechnen der noch verbleibenden Räume




# -------- Informationsausgabe und Speichern von Informationen --------


conn = sqlite3.connect("Maklerdatenbank.db")        # Speichern der Gesamtfläche und des Objektes in die Datenbank
cursor = conn.cursor()
cursor.execute(f"INSERT INTO Objekte (ObjektID, ObjektName, Gesamtflaeche, Raumanzahl) VALUES ({ObjektID}, '{Objektname}', {gesamtflaeche}, {raumanzahl})")
conn.commit()
conn.close()


print("\n\n\n-------- Daten --------")      # Ausgeben der Informationen
print(f"Objekname: {Objektname}\nObjektID: {ObjektID}\nRaumanzahl: {raumanzahl}\nGesamtfläche: {gesamtflaeche}")
print("-----------------------\n\n\n")

input("Beliebige Taste zum beenden drücken")
=======
        weitere_flaeche = input("Soll eine weitere Fläche hinzugefügt werden? (y/n)")
    print(raumflaeche + "m2")
    gesamtflaeche = gesamtflaeche + raumflaeche
    
    conn = sqlite3.connect("Maklerdatenbank.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX(ObjektID) FROM Objekte")
    conn.close()
>>>>>>> 5d724ef43b4b31e0851e8498ed3f1e17eb89c46c
