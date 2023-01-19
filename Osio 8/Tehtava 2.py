import mariadb

def get_types(koodi):
    sql = 'SELECT type FROM airport WHERE iso_country ="' + koodi + '";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def typecounter(tyypit):

    tyyppiset = set()
    tyyppilista = []

    for n in tyypit:
        tyyppilista.append(n[0])
        tyyppiset.add(n[0])

    print("Maakoodin lentokenttien tyypit ja määrät ovat:")

    for n in tyyppiset:
        print(f"{n}:{tyyppilista.count(n)}")


yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pythontest',
    password='pythonpw',
    autocommit=True
)

tyypit = get_types(input("Anna maakoodi: "))

typecounter(tyypit)







