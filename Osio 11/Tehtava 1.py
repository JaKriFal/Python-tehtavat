
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, päätoimittaja: {self.paatoimittaja}")
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = int(sivumaara)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumaara}")

aa = Lehti("Aku Ankka", "Aki Hyyppä")

h6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aa.tulosta_tiedot()
h6.tulosta_tiedot()




