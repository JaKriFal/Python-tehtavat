import mariadb

def haeLentokentta(ICAO):
    sql = 'SELECT name, municipality FROM airport WHERE ident ="' + ICAO + '";'
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

koodi = input("Anna lentokentän ICAO-koodi: ")
kentta = haeLentokentta(koodi)

for rivi in kentta:
    print(f"Lentokenttä on {rivi[0]} ja sen sijaintikunta on {rivi[1]}.")


