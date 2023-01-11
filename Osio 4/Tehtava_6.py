import random

itr = int(input("Anna arvottavien pisteiden määrä: "))

N = 0
n = 0

while N < itr:                  #Koska 1/4 ympyrän suhde 1/4 neliöön on sama kuin koko ympyrän suhde koko neliöön, laskemme vain positiivisen neljänneksen tuloksen
    N += 1
    y = random.random()
    x = random.random()
    if (y**2 + x**2) < 1:
        n += 1



print(f"Piin likiarvoksi laskettiin {N} iteraation jälkeen {(4*n)/N:6.6f}")

