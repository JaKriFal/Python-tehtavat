x = input("Anna luku: ")
if x == "":
    print("Toiminta lopetettu!")
else:
    min = int(x)
    max = int(x)


while x != "":
    if int(x) < min:
        min = int(x)
    elif int(x) > max:
        max = int(x)
    x = input("Anna luku: ")

print(f"Toiminta lopetettu! Pienin annettu luku oli {str(min):3} ja suurin annettu luku oli {str(max):3}.")


