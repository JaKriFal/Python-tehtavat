from flask import Flask, Response
import json
import mariadb

app = Flask(__name__)
@app.route('/lkhaku/<icao>')
def lkhaku(icao):
    try:
        yhteys = mariadb.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='pythontest',
            password='pythonpw',
            autocommit=True
        )
        sql = 'SELECT name, municipality FROM airport WHERE ident ="' + icao + '";'
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()


        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "ICAO": icao,
            "name": tulos[0][0],
            "municipality": tulos[0][1]

        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen argumentti"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

