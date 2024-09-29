import random

"""
Patriks Jēkabsons
11.09.2024
Izveidot programmu, kas aprēķina pirkumu bez pvn un pašu pvn vērtību

"""


def uzdevums1(pvn, cikIztereja, bezPVN):
    print("Summa bez PVN:", bezPVN)
    bezPVN = cikIztereja * pvn
uzdevums1(0.79, float(input("Cik jūs naudu iztērējāt?")), )
"""

Izveidot programmu, kur lietotājs secīgi var pabeigt 5 teikumus

"""

# def uzdevums2(teik1, teik2, teik3, teik4):
#     print("Mani sauc", teik1,", man patīk", teik2,", man ir", teik3,"gadi", ", es nodarbojos ar", teik4)

# uzdevums2(input("Mani sauc - "), input("Man patīk - "), input("Mans vecums - "), input("Es nodarbojos ar - "))
"""

Izveidot programmu, kas pārbauda vai lietotājam ir vairāk kā 18 gadi (tikai gadu).

"""

def uzdevums3():
    gads = 2024
    dzGads = float(input("Jūsu dzimšanas gads: "))

    if gads - dzGads >= 18:
        print("Lietotājam ir 18 gadu")
    else:
        print("Lietotājam nav 18 gadu")

"""

Izveidot programmu, kur 4 reizes var ievadīt kustības, tiek izvadīts virziens.

"""

def uzdevums4():
    key = input("Ievadi w, a, s vai d: ")

    if key == "w":
        print("Uz priekšu")
    elif key == "a":
        print("Pa kreisi")
    elif key == "d":
        print("Pa labi")
    elif key == "s":
        print("Atpakaļ")
    else:
        print("Kļūda")

"""

Izveidot programmu, kuru var atkārtot vairākas reizes

"""
def uzdevums5():
    while True:
        user_input = input("Vai vēlies atkārtot šo programmu? y/n?")

        if user_input == "n":
            print("Programma beidzās")
            break
        elif user_input == "y":
            print("Programma turpinās")
        else:
            print("Nepareiza ievade, lūdzu ierakstiet y vai n")

"""

Izveidot programmu, kur jāuzmin slēptais skaitlis (1-10)

"""

def uzdevums6():
    skaitlis = random.randint(1, 10)

    while True:

        i = int(input("Ievadi savu minējumu: "))
        if i < skaitlis:
            print("Lielāks")
        elif i > skaitlis:
            print("Mazāks")
        else:
            print("Jūs uzminējāt")
            break

"""

Izveidot programmu, kur tiek izvadīti visi skaitļi, kas dalās ar ievadīto skaitli

"""

def uzdevums7():
    skaitlis = int(input("Ievadiet savu skaitli: "))

    def atrast(cipars):
        dalitaji = []
        for i in range(1, cipars + 1):
            if cipars % i == 0:
                dalitaji.append(i)
        return dalitaji

    dalitaji = atrast(skaitlis) 
    print(f"Skaitlis {skaitlis} dalās ar: {dalitaji}")


"""

Izveidot programmu, kur lietotājs ievada vārdu un burtu.
Tiek izvadīts, cik norādīto burtu ir dotajā vārdā

"""

# vards = input("Ievadi vārdu: ")
# burts = input("Ievadi burtu: ")

# atb = 0
# for x in vards:
#     if x == burts:
#         atb+= 1
# print(atb)

"""

9. uzd

"""

# summa = 0
# for x in range(1, 1000):
#     if x % 3 == 0:
#       summa += x
#     elif x % 5 == 0:
#        summa += x

# print(summa)


"""

10. uzd

"""

# sk1 = 0
# sk2 = 1
# summa = 0

# while sk2 <= 4000000:
#     if sk2 % 2 == 0:
#         summa += sk2
#     sk1, sk2 = sk2, sk1 + sk2

# print(summa)

"""

11. uzd

"""

# burti = "abcdefghijklmnopqrstuvwxyz"

# for burts1 in burti:
#     for burts2 in burti:
#         print(burts1 + burts2)

"""

12. uzd

"""

# skaitlis = int(input("Ievadi skaitli: "))
# print("2 ^", skaitlis)