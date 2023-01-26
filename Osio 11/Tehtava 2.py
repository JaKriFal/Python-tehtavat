
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


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.kapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.kapasiteetti = float(tankki)


sa = Sahkoauto("ABC-15", 180, 52.5)

pa = Polttomoottoriauto("ACD-123", 165, 32.3)
pa.nopeus = 80
sa.nopeus = 70

pa.kulje(3)
sa.kulje(3)

print(f"Sähkoauto: {sa.matka}km")
print(f"Polttomoottoriauto: {pa.matka}km")
