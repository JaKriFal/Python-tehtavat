x = input("Anna luku: ")
if x == "":
    print("Toiminta lopetettu!")
else:
    min = float(x)
    max = float(x)


while x != "":
    if float(x) < min:
        min = float(x)
    elif float(x) > max:
        max = float(x)
    x = input("Anna luku: ")

print(f"Toiminta lopetettu! Pienin annettu luku oli {str(min):3} ja suurin annettu luku oli {str(max):3}.")


