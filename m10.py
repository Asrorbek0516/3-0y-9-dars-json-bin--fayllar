import json

file_a = open("a.json", 'r')
file_b = open("b.json", 'r')

data_a = json.load(file_a)
data_b = json.load(file_b)

file_a.close()
file_b.close()

for talaba in data_a:
    print(f"{talaba['ism']} - {talaba['baho']}")

for talaba in data_b:
    if not talaba["ism"] in [t["ism"] for t in data_a]:
        print(f"{talaba['ism']} - {talaba['baho']}")