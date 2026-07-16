import json

mahsulotlar = []

while True:
    nomi = input("Nomi: ").strip()

    if not nomi:
        print("Kiritilmadi")
        break

    narxi = int(input("narxi: "))
    
    mahsulotlar.append(
        {
            "nomi": nomi,
            "narxi": narxi
        }
    )

with open("mahsulotlar.json", 'w') as file:
    json.dump(mahsulotlar,file,indent=4)

print("Muvaffaqiyatli yozildi")