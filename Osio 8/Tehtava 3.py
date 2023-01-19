import mariadb
from geopy import distance

def koordinaattihaku(icao):
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident ="' + icao + '";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pythontest',
    password='pythonpw',
    autocommit=True
)


maat = []

maat.append(input("Anna ensimmäisen kentän ICAO-koodi: "))
maat.append(input("Anna toisen kentän ICAO-koodi: "))

koordinaatit = []

for n in maat:
    paikka = koordinaattihaku(n)
    koordinaatit.append(paikka[0])

dis = distance.distance(koordinaatit[0], koordinaatit[1])
print(f"Lentokenttien välinen etäisyys on {dis}.")








