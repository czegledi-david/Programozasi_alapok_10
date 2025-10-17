#1. Feladat
nev = input("Mi a neved: ")
print(f"Szia {nev}! Üdv a programban!")

#2. feladat
szam = int(input("Adjon meg egy számot: "))
if szam > 0:
    print("A szám pozitív")
elif szam < 0:
    print("A szám negatív")
else:
    print("A szám nulla")

#3. feladat
szam2 = int(input("Adjon meg egy számot: "))
i = 1
while i <=szam2:
    print(i)
    i = i + 1
#4. feladat
szam3 = int(input("Adjon meg egy számot: "))
if szam3 % 2 == 0:
    print("A megadott szám páros")
else:
    print("A megadott szám páratlan")

#5. feladat
egyik = int(input("Adjon meg egy számot: "))
masik = int(input("Adjon meg egy másik számot: "))

if egyik > 0 and masik >0:
    print("Mindakettő pozitív")




