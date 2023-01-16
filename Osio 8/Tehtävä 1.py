import mysql.connector

def haeLentokentta(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident =" + icao +";"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='pythontest',
         password='pythonpw',
         autocommit=True
         )


