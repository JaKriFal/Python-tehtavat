import random


def heitto(arg):
    x = random.randint(1, arg)
    return x

n = 0
x = 0

arg = int(input("Anna nopan tahkojen määrä kokonaislukuna: "))

while x != arg:
    n += 1
    x = heitto(arg)
    print(f"Heiton {n} silmäluku oli {x}.")


print(f"Heittojen kokonaismäärä oli {n}.")