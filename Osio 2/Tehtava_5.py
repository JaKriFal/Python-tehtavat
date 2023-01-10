import math

Lei = float(input("Anna leiviskät: "))

Nau = float(input("Anna naulat: "))

Luo = float(input("Anna luodit: "))

g = Luo*13.3 + Nau*32*13.3 + Lei*20*32*13.3

kg = int(math.trunc(g/1000))

g = g - kg*1000

print(f'Massa nykymittojen mukaan: {kg:3.0f} kilogrammaa ja {g:6.3f} grammaa.')

