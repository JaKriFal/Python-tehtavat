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
        for a in self.autot:
            print(f"{a.rekisteritunnus:6s}   {a.huippunopeus:6.1f}km/h   {a.nopeus:6.1f}km/h   {a.matka:6.1f}km")

    def kilpailu_ohi(self):
        for n in self.autot:
            if n.matka >= self.pituus:
                return True
        return False


autot = []
n = 0

while n < 10:
    rekkari = "ABC-" + str(n + 1)
    hp = float(random.randint(100, 200))
    autot.append(Auto(rekkari, hp))
    n += 1

ralli = Kilpailu("Suuri romuralli", 8000, autot)

fflag = ralli.kilpailu_ohi()
i = 1

while not ralli.kilpailu_ohi():
    ralli.tunti_kuluu()
    if i%10 == 0:
        print(f"Kierros: {i}")
        ralli.tulosta_tilanne()
    i += 1


print(f"VOITTAJA! Kilpailu päättyi kierroksella {i}")
ralli.tulosta_tilanne()





