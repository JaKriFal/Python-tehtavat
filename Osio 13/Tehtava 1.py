from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/onko_alkuluku/<luku>')
def onko_alkuluku(luku):
    try:
        luku = int(luku)
        itr = luku - 1

        flag = True

        while itr > 1:
            if luku % itr == 0:
                flag = False

            itr -= 1
        vastaus = ""
        if flag:
            vastaus = "On alkuluku"
        else:
            vastaus = "Ei ole alkuluku"

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku": luku,
            "alkuluku": vastaus
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