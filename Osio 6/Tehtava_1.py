import random


def heitto():
    x = random.randint(1, 6)
    return x

n = 0
x = 0

while x != 6:
    n += 1
    x = heitto()
    print(f"Heiton {n} silmäluku oli {x}.")


print(f"Heittojen kokonaismäärä oli {n}.")




