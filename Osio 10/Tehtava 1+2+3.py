

class Talo:

    def __init__(self, bot, top, n):
        self.bot = bot
        self.top = top
        self.hissit = []
        i = 1
        while i <= n:
            hissi = Hissi(bot, top)
            self.hissit.append(hissi)
            i += 1

    def printtaa_hissit(self):
        for n in self.hissit:
            print(str(n))

    def aja_hissia(self, n, kerros):
        self.hissit[n-1].siirry_kerrokseen(kerros)

    def palohalytys(self):
        for n in self.hissit:
            n.siirry_kerrokseen(self.bot)


class Hissi:
    def __init__(self, bot, top):
        self.top = top
        self.bottom = bot
        self.kerros = bot
    def __str__(self):
        return "Tämä on hissi kerroksessa " + str(self.kerros)
    def siirry_kerrokseen(self, kerros):
        while self.kerros > kerros:
            if self.kerros == self.bottom:
                break
            self.kerros_alas()
        while self.kerros < kerros:
            if self.kerros == self.top:
                break
            self.kerros_ylos()


    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros >= self.bottom:
            print(f"Kerros on nyt {self.kerros}")

    def kerros_ylos(self):
        self.kerros += 1
        if self.kerros <= self.top:
            print(f"Kerros on nyt {self.kerros}")


h = Hissi(1, 10)

h.siirry_kerrokseen(5)

talo = Talo(1, 10, 4)

talo.aja_hissia(1, 5)

talo.printtaa_hissit()

talo.palohalytys()

talo.printtaa_hissit()