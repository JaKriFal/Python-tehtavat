import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = float(huippunopeus)
        self.nopeus = 0.0
        self.matka = 0.0

    def __str__(self):
        return str("Rekisteritunnus: " + str(self.rekisteritunnus) + ", Huippunopeus: " + str(self.huippunopeus)
                   + ", Nopeus: " + str(self.nopeus) + ", Kuljettu matka: " + str(self.matka))

    def kiihdyta(self, acc):
        self.nopeus += acc
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, h):
        self.matka += self.nopeus * h

class Kilpailu:
    def __init__(self, nimi, pituus, autot):

        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for n in self.autot:
            n.kiihdyta(float(random.randint(-10, 15)))
            n.kulje(1.0)

    def tulosta_tilanne(self):
        for n in self.autot:
            print(f"{n.rekisteritunnus:6s}   {n.huippunopeus:6.1f}km/h   {n.nopeus:6.1f}km/h   {n.matka:6.1f}km")

    def kilpailu_ohi(self):
        for n in self.autot:
            if n.matka >= self.pituus:
                return True
        return False

