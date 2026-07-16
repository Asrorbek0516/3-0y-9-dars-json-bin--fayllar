import json

info = {
    "ism": "Ali", 
    "yosh": 20, 
    "baho": 88
}

with open("data.json", 'w') as f:
    json.dump(info,f)

print("yozildi")