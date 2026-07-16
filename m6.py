import json
with open("talabalar.json", 'r') as file:
    talabalar = json.load(file)

for talaba in talabalar:
    if talaba["baho"] > 85:
        print(talaba["ism"])