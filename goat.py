import random

"""
Patriks Jēkabsons
11.09.2024
Izveidot programmu, kas aprēķina pirkumu bez pvn un pašu pvn vērtību

"""

# def uzdevums1():


"""

Izveidot programmu, kur lietotājs secīgi var pabeigt 5 teikumus

"""

# def uzdevums2(teik1, teik2, teik3, teik4):
#     print("Mani sauc", teik1,", man patīk", teik2,", man ir", teik3,"gadi", ", es nodarbojos ar", teik4)

# uzdevums2(input("Mani sauc - "), input("Man patīk - "), input("Mans vecums - "), input("Es nodarbojos ar - "))
"""

Izveidot programmu, kas pārbauda vai lietotājam ir vairāk kā 18 gadi (tikai gadu).

"""

# def uzdevums3(dzGads, gads = 2024):
#     if gads - dzimsanas_gads == 18: 
#         print("Jums ir 18 gadi")
#     elif gads - dzimsanas_gads > 18:
#         print("Jums ir vairāk nekā 18 gadi")
#     else:
#         print("Jums nav 18 gadu")

# dzimsanas_gads = int(input("Kurā gadā jūs pidzimāt?"))
# uzdevums3(dzimsanas_gads)

"""

Izveidot programmu, kur 4 reizes var ievadīt kustības, tiek izvadīts virziens.

"""

# def uzdevums4(key):
#     if ievade == "w":
#         print("Uz priekšu")
#     elif ievade == "a":
#         print("Pa kreisi")
#     elif ievade == "d":
#         print("Pa labi")
#     elif ievade == "s":
#         print("Atpakaļ")
#     else:
#         print("Kļūda")

# ievade = input("Ievadi w, a, s vai d: ")
# uzdevums4(ievade)
    

"""

Izveidot programmu, kuru var atkārtot vairākas reizes

"""
# def uzdevums5(ievade):
#     while True:
#         user_input = input("Vai vēlies atkārtot šo programmu? y/n?")

#         if user_input == "n":
#             print("Programma beidzās")
#             break
#         elif user_input == "y":
#             print("Programma turpinās")
#         else:
#             print("Nepareiza ievade, lūdzu ierakstiet y vai n")

# user_input = input("Vai vēlies atkārtot šo programmu? y/n?")
# uzdevums5(user_input)
"""

Izveidot programmu, kur jāuzmin slēptais skaitlis (1-10)

"""

# def uzdevums6(random_skaitlis):
#     while True:

#         i = int(input("Ievadi savu minējumu: "))
#         if i < skaitlis:
#             print("Lielāks")
#         elif i > skaitlis:
#             print("Mazāks")
#         else:
#             print("Jūs uzminējāt")
#             break

# skaitlis = random.randint(1, 10)
# uzdevums6(skaitlis)

"""

Izveidot programmu, kur tiek izvadīti visi skaitļi, kas dalās ar ievadīto skaitli

"""

# def uzdevums7(ievaditais_skaitlis):
#     def atrast(cipars):
#         dalitaji = []
#         for i in range(1, cipars + 1):
#             if cipars % i == 0:
#                 dalitaji.append(i)
#         return dalitaji

#     dalitaji = atrast(skaitlis) 
#     print(f"Skaitlis {skaitlis} dalās ar: {dalitaji}")

# skaitlis = int(input("Ievadiet savu skaitli: "))
# uzdevums7(skaitlis)

"""

Izveidot programmu, kur lietotājs ievada vārdu un burtu.
Tiek izvadīts, cik norādīto burtu ir dotajā vārdā

"""
# def uzdevums8(word, letter):
#     atb = 0
#     for x in vards:
#         if x == burts:
#             atb+= 1
#     print(atb)

# vards = input("Ievadi vārdu: ")
# burts = input("Ievadi burtu: ")
# uzdevums8(vards, burts)

"""

9. uzd

"""

def uzdevums9(summers):
    summa = 0
    for x in range(1, 1000):
        if x % 3 == 0:
            summa += x
        elif x % 5 == 0:
            summa += x

            print(uzdevums9(summa))


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