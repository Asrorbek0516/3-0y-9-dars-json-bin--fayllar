import json

with open("talabalar.json", 'r') as file:
    talabalar = json.load(file)

yuqori_ball = talabalar[0]
past_ball = talabalar[0]

for talaba in talabalar:
    if talaba["baho"] > yuqori_ball["baho"]:
        yuqori_ball = talaba
    if talaba["baho"] < past_ball["baho"]:
        past_ball = talaba

jami = 0
for talaba in talabalar:
    jami += talaba["baho"]

print(f"o'rtachasi: {jami/len(talabalar)}")
print(f"Eng yuqori baho: {yuqori_ball['ism']} - {yuqori_ball['baho']}")
print(f"Eng past baho: {past_ball['ism']} - {past_ball['baho']}")