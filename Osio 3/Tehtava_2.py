print("Hyttiluokkavaihtoehdot ovat LUX, A, B, ja C.")
luokka = input("Anna hyttiluokka jonka kuvauksen haluat: ")

if luokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')

elif luokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')

elif luokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')

elif luokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')

else:
    print('Virheellinen hyttiluokka. Yritä uudelleen')
