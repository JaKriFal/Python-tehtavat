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


# T1 tulostukset

auto1 = Auto("ABC-123", 142)
print(auto1)

# T2 tulostukset

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.kiihdyta(-200)

print(auto1)

# AUTOKILPAILU

autot = []
n = 0

while n < 10:
    rekkari = "ABC-" + str(n + 1)
    hp = float(random.randint(100, 200))
    autot.append(Auto(rekkari, hp))
    n += 1

kilpatunnit = 0.0
lippu = True

while lippu:
    kilpatunnit += 1
    for n in autot:
        n.kiihdyta(float(random.randint(-10, 15)))
        n.kulje(1.0)
    for n in autot:
        if n.matka >= 1000:
            lippu = False

vrekkari = ""
vmatka = 0.0

for n in autot:
    if n.matka >= vmatka:
        vmatka = n.matka
        vrekkari = n.rekisteritunnus

print("Tunnus    " + "Huippunopeus    " + "Nopeus    " + "Kuljettu matka")

for n in autot:
    print(f"{n.rekisteritunnus:6s}   {n.huippunopeus:6.1f}km/h   {n.nopeus:6.1f}km/h   {n.matka:6.1f}km")

print(f"Voittaja: {vrekkari:6s} ")
