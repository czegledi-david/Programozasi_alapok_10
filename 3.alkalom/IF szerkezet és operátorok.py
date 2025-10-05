"""
if feltetel:
    utasítások -> Ezt akkor futattja ha a feltetel igaz
else:
    utasítások  -> Ezt akkor futattja ha a feltetel hamis













    
"""

if 5 == 6:
    print("A két szám megegyezik")
else:
    print("A két szám nem egyezik")

x = 4
y = 9

#   0   0     1  :Hamis
if x>y and y == 9:
    print("Igaz")
else:
    print("Hamis")

#   1        1         0        1
#       1         (1)        0
if x<y and y == 9 or y >9 and y != 10:
    print("Igaz")
else:
    print("Hamis")

#        1    (1)           1
if 2 *2 == 4 and 12 % 2 ==0:
    print("Igaz")
else:
    print("Hamis")




#Írj egy programot ami bekér egy kort és ha 18 év alatti akkor írd ki
#hogy 18 év alatti, ha nem akkor azt, hogy 18 év feletti. Ha 18 éves
#Akkor azt írd ki, hogy a 18 éves vagy


x = int(input("Add meg a korod: "))
if x >18:
    print("18 év feletti vagy")
elif x < 18:
    print("18 év alatti vagy")
else:
    print("18 éves vagy")

"""

Készíts egy programot, amely megkérdezi a felhasználótól,
hogy jó napja van-e! A válasz kétféle lehet:
igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""

valasz = input("Milyen napod volt: ")
if valasz == "igen":
    print("Jó hogy jó napod volt")
elif valasz == "nem":
    print("Sajnálom, hogy rossz napod van")
else:
    print("Sajnálom, ezt a szót nem értem")



"""
Készíts egy programot, ami bekér egy számot a felhasználótól,
majd kiírja, hogy a megadott szám páros-e vagy páratlan!

"""

szam = int(input("Adjon meg egy számot:"))
if szam % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")







