import json
from pprint import pprint

with open("talabalar.json", 'r') as fayl:
    talabalar = json.load(fayl)

pprint(talabalar)