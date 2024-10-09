import random

"""
Patriks Jēkabsons
11.09.2024
Izveidot programmu, kas aprēķina pirkumu bez pvn un pašu pvn vērtību

"""

def uzdevums1(cena):
    

uzdevums1(float(input("Cik jūs samaksājāt? ")))

"""

Izveidot programmu, kur lietotājs secīgi var pabeigt 5 teikumus

"""

def uzdevums2(teik1, teik2, teik3, teik4):
    print("Mani sauc", teik1,", man patīk", teik2,", man ir", teik3,"gadi", ", es nodarbojos ar", teik4)

# uzdevums2(input("Mani sauc - "), input("Man patīk - "), input("Mans vecums - "), input("Es nodarbojos ar - "))
"""

Izveidot programmu, kas pārbauda vai lietotājam ir vairāk kā 18 gadi (tikai gadu).

"""

def uzdevums3(dzimsanas_gads, gads = 2024):
    if gads - dzimsanas_gads == 18: 
        print("Jums ir 18 gadi")
    elif gads - dzimsanas_gads > 18:
        print("Jums ir vairāk nekā 18 gadi")
    else:
        print("Jums nav 18 gadu")

# uzdevums3(int(input("Kurā gadā jūs pidzimāt?")))

"""

Izveidot programmu, kur 4 reizes var ievadīt kustības, tiek izvadīts virziens.

"""

def uzdevums4(ievade):
    if ievade == "w":
        print("Uz priekšu")
    elif ievade == "a":
        print("Pa kreisi")
    elif ievade == "d":
        print("Pa labi")
    elif ievade == "s":
        print("Atpakaļ")
    else:
        print("Kļūda")

# uzdevums4(input("Ievadi w, a, s vai d: "))
    

"""

Izveidot programmu, kuru var atkārtot vairākas reizes

"""
def uzdevums5(ievade):
    while True:
        user_input = input("Vai vēlies atkārtot šo programmu? y/n?")

        if user_input == "n":
            print("Programma beidzās")
            break
        elif user_input == "y":
            print("Programma turpinās")
        else:
            print("Nepareiza ievade, lūdzu ierakstiet y vai n")

# uzdevums5(input("Vai vēlies atkārtot šo programmu? y/n?"))
"""

Izveidot programmu, kur jāuzmin slēptais skaitlis (1-10)

"""

def uzdevums6(skaitlis):
    while True:

        i = int(input("Ievadi savu minējumu: "))
        if i < skaitlis:
            print("Lielāks")
        elif i > skaitlis:
            print("Mazāks")
        else:
            print("Jūs uzminējāt")
            break

skaitlis = random.randint(1, 10)
# uzdevums6(skaitlis)

"""

Izveidot programmu, kur tiek izvadīti visi skaitļi, kas dalās ar ievadīto skaitli

"""

def uzdevums7(skaitlis):
    def atrast(cipars):
        dalitaji = []
        for i in range(1, cipars + 1):
            if cipars % i == 0:
                dalitaji.append(i)
        return dalitaji

    dalitaji = atrast(skaitlis) 
    print(f"Skaitlis {skaitlis} dalās ar: {dalitaji}")

# uzdevums7(int(input("Ievadiet savu skaitli: ")))

"""

Izveidot programmu, kur lietotājs ievada vārdu un burtu.
Tiek izvadīts, cik norādīto burtu ir dotajā vārdā

"""
def uzdevums8(vards, burts):
    atb = 0
    for x in vards:
        if x == burts:
            atb+= 1
    print(atb)

# uzdevums8(input("Ievadi vārdu: "), input("Ievadi burtu: "))

"""

9. uzd

"""


def uzdevums9(max):
    summa = 0
    for x in range(1, max):
        if x % 3 == 0:
            summa += x
        elif x % 5 == 0:
            summa += x
    print(summa) 

# uzdevums9(1000)

"""

10. uzd

"""
def uzdevums10(maks):
    sk1 = 0
    sk2 = 1
    summa = 0

    while sk2 <= maks:
        if sk2 % 2 == 0:
            summa += sk2
        sk1, sk2 = sk2, sk1 + sk2
    print(summa) 

# uzdevums10(4000000)

"""

11. uzd

"""

def uzdevums11():
    burti = "abcdefghijklmnopqrstuvwxyz"

    for burts1 in burti:
        for burts2 in burti:
            print(burts1 + burts2)

# uzdevums11()

"""

12. uzd

"""

def uzdevums12():
    skaitlis = int(input("Ievadi skaitli: "))
    print("2 ^", skaitlis)

# uzdevums12()

"""

14. uzd

"""

def uzdevums14(sk1, sk2, sk3):
    if sk1 > sk2 and sk1 > sk3:
        print("Pirmais ir vislielākais")
    elif sk2 > sk1 and sk2 > sk3:
        print("Otrais ir vislielākais")
    elif sk3 > sk1 and sk3 > sk2:
        print("Trešais ir vislielākais")
# uzdevums14(1, 2, 3)

"""

15. uzd

"""

def uzdevums15(skaitlis):
    baze = 0
    while baze <= skaitlis:
        rezultats = baze ** 2
        print(rezultats)
        baze += 1

# uzdevums15(4)

