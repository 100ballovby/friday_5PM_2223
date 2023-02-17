import json
import requests as r


url = "https://api.thedogapi.com/v1/breeds"
ans = r.get(url)


def make_file(filename, data):
    with open(filename, 'w') as file:
        file.write(json.dumps(data, indent=4))

def read_file(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())

make_file("dogs.json", ans.json())
dogs = read_file("dogs.json")

# универсальность заканчивается здесь
for dog in dogs:
    print(f"{dog['name']}\t |\t {dog['image']['url']}\t |\t {dog['life_span']}")

