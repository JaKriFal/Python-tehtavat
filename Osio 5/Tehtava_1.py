import random


heitot = int(input("Anna nopanheittojen lukumäärä: "))

nopat = []

summa = 0

i = 0
while i < heitot:
    nopat.append(random.randint(1, 6))
    i += 1

for n in nopat:
    summa = summa + n

print("Noppien silmäluvut olivat :" + str(nopat))
print("Silmälukujen summa oli: " + str(summa))
