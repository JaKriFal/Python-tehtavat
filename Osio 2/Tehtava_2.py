import math

sade_str: str = input("Anna ympyrän säde metreissä: ") #pyydän argumentin metreissä niin se on kiva ilmoittaa neliömetreinä

sade = float(sade_str)

pa = math.pi * sade**2

print("Ympyrän pinta-ala on " + str(round(pa,5)) + " neliömetriä.") #pyöristetään viiden numeron tarkkuuteen

