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

summa = 0
for x in range(1, 1000):
    if x % 3 == 0:
      summa += x
    elif x % 5 == 0:
       summa += x

print(summa)


