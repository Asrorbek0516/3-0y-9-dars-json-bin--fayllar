import json

with open("mahsulotlar.json", 'r') as f:
    mahsulotlar = json.load(f)

# print(type(mahsulotlar))

max = mahsulotlar[0]
min = mahsulotlar[0]

for mahsulot in mahsulotlar:
    if mahsulot["narxi"] > max["narxi"]:
        max = mahsulot
    
    if mahsulot["narxi"] < min["narxi"]:
        min = mahsulot

print(f"Eng qimmati: {max['nomi']} - {max['narxi']} so'm")
print(f'Eng arzoni: {min["nomi"]} - {min["narxi"]} som')