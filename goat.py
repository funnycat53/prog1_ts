"""
Patriks Jēkabsons
11.09.2024
Izveidot programmu, kas aprēķina pirkumu bez pvn un pašu pvn vērtību

"""

import random

# pvn = 0.79
# cikIztereja = float(input("Cik jūs naudu iztērējāt?"))
# bezPVN = cikIztereja * pvn

# print("Summa bez PVN:", bezPVN)


"""

Izveidot programmu, kur lietotājs secīgi var pabeigt 5 teikumus

"""

# Teik1 = input("Mani sauc - ")
# Teik2 = input("Man patīk - ")
# Teik3 = input("Mans vecums - ")
# Teik4 = input("Es nodarbojos ar - ")
# Teik5 = input("Mana mīļakā krāsa ir - ")
# print("Mani sauc", Teik1, "Man patīk", Teik2, "Man ir", Teik3, "gadi", "Es nodarbojos ar", Teik4, "Mana mīļākā krāsa ir", Teik5)

"""

Izveidot programmu, kas pārbauda vai lietotājam ir vairāk kā 18 gadi (tikai gadu).

"""

# gads = 2024
# dzGads = float(input("Jūsu dzimšanas gads: "))

# if gads - dzGads >= 18:
#     print("Lietotājam ir 18 gadu")
# else:
#     print("Lietotājam nav 18 gadu")

"""

Izveidot programmu, kur 4 reizes var ievadīt kustības, tiek izvadīts virziens.

"""

# key = input("Ievadi w, a, s vai d: ")

# if key == "w":
#     print("Uz priekšu")
# elif key == "a":
#     print("Pa kreisi")
# elif key == "d":
#     print("Pa labi")
# elif key == "s":
#     print("Atpakaļ")
# else:
#     print("Kļūda")

"""

Izveidot programmu, kuru var atkārtot vairākas reizes

"""

# while True:
#     user_input = input("Vai vēlies atkārtot šo programmu? y/n?")

#     if user_input == "n":
#         print("Programma beidzās")
#         break
#     elif user_input == "y":
#         print("Programma turpinās")
#     else:
#         print("Nepareiza ievade, lūdzu ierakstiet y vai n")

"""

Izveidot programmu, kur jāuzmin slēptais skaitlis (1-10)

"""

# skaitlis = random.randint(1, 10)

# while True:
#     print(skaitlis)

#     i = int(input("Ievadi savu minējumu: "))
#     if i < skaitlis:
#         print("Lielāks")
#     elif i > skaitlis:
#         print("Mazāks")
#     else:
#         print("Jūs uzminējāt")
#         break

"""

Izveidot programmu, kur tiek izvadīti visi skaitļi, kas dalās ar ievadīto skaitli

"""

# skaitlis = int(input("Ievadiet savu skaitli: "))

# def atrast(cipars):
#     dalitaji = []
#     for i in range(1, cipars + 1):
#         if cipars % i == 0:
#             dalitaji.append(i)
#     return dalitaji

# dalitaji = atrast(skaitlis) 
# print(f"Skaitlis {skaitlis} dalās ar: {dalitaji}")
