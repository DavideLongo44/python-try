def berechne_ggt(a, b):
    while b != 0:
        a, b = b, a % b
    return a

zahl1 = int(input("Geben Sie die erste Zahl ein: "))
zahl2 = int(input("Geben Sie die zweite Zahl ein: "))

ggt = berechne_ggt(zahl1, zahl2)

print("Der größte gemeinsame Teiler von", zahl1, "und", zahl2, "ist", ggt)