
vuodenajat = "kevät", "kesä", "syksy", "talvi"


kuu = int(input("Anna kuukauden järjestysnumero:" ))

if 0 < kuu < 3 or kuu == 12:
    print(vuodenajat[3])
elif 2 < kuu < 6:
    print(vuodenajat[0])
elif 5 < kuu < 9:
    print(vuodenajat[1])
elif 8 < kuu < 12:
    print(vuodenajat[2])
