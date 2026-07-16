import json

info =[
    {
        "ism": "Ali","baho": 90
    },

    {
        "ism": "Vali", "baho": 78
    },

    {
        "ism": "Zara","baho": 95
    },

    {
        "ism": "Kamol","baho": 82
    },

    {
        "ism": "Bek","baho": 91
    }
]

with open("talabalar.json", "w") as f:
    json.dump(info,f,indent=4)

print("Ma'lumotlar yozildi")