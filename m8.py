import json

with open("info.json", 'r') as f:
    data = json.load(f)

shahar = input("Kerakli shahar: ")

topildi = False

for kontakt in data:
    if kontakt["shahar"] == shahar:
        print(f"{kontakt['ism']} - {kontakt['telefon']}")
        topildi= True

if not topildi:
    print("Bu shaharda kontakt yuq")