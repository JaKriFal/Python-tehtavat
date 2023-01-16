import mariadb


def haeLentokentta():
    sql = 'SELECT name, municipality FROM airport WHERE ident ="EFHK"'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    return


yhteys = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pythontest',
    password='pythonpw',
    autocommit=True
)

haeLentokentta()

