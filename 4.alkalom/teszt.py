##Írjunk egy programot ami kiírja a páros számok 1-től 20-ig
szam = 1
while szam <= 20:
    if szam % 2 == 0:
        print(szam)
    szam = szam +1
print("__________________________________________")

#Írj egy programot, ami kiírja a számokat 20-tól 1-ig
szam = 20
while szam >= 1:
    print(szam)
    szam = szam - 1
print("_______________________________________________________")
#Írj egy programot, ami kiírja a számokat 1-től 20-ig de csak
#a páratlanokat
szam = 1
while szam <= 20:
    if szam % 2 != 0:
        print(szam)
    szam = szam + 1


print("_______________________________________________________")
#Írj egy programot, ami bekér egy számot és annyiszor írja ki, hogy Hello!
x = int(input("Add meg hányszor fusson:"))

szamlalo = 1
while szamlalo <= x:
    print("hello")
    szamlalo = szamlalo + 1







